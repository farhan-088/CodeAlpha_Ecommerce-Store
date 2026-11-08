from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CheckoutForm, RegistrationForm
from .models import Product, Order, OrderItem


def home(request):
    products = Product.objects.filter(is_active=True, stock__gt=0)
    search = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    if search:
        products = products.filter(name__icontains=search)
    if category:
        products = products.filter(category__iexact=category)
    categories = Product.objects.filter(is_active=True).exclude(category="").values_list("category", flat=True).distinct()
    return render(request, "store/home.html", {"products": products, "categories": categories, "search": search, "selected_category": category})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/product_detail.html", {"product": product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_active=True)
    cart = request.session.get("cart", {})
    key = str(product_id)
    current_qty = int(cart.get(key, 0))
    if current_qty < product.stock:
        cart[key] = current_qty + 1
        request.session["cart"] = cart
        messages.success(request, f"{product.name} added to your cart.")
    else:
        messages.warning(request, "Requested quantity is not available in stock.")
    return redirect("cart")


def cart_view(request):
    cart = request.session.get("cart", {})
    items = []
    total = Decimal("0.00")
    for product_id, quantity in cart.items():
        product = Product.objects.filter(pk=product_id, is_active=True).first()
        if product:
            quantity = int(quantity)
            subtotal = product.price * quantity
            total += subtotal
            items.append({"product": product, "quantity": quantity, "subtotal": subtotal})
    return render(request, "store/cart.html", {"items": items, "total": total})


def update_cart(request, product_id):
    if request.method != "POST":
        return redirect("cart")
    product = get_object_or_404(Product, pk=product_id, is_active=True)
    try:
        quantity = int(request.POST.get("quantity", "1"))
    except ValueError:
        quantity = 1
    cart = request.session.get("cart", {})
    if quantity <= 0:
        cart.pop(str(product_id), None)
    elif quantity <= product.stock:
        cart[str(product_id)] = quantity
    else:
        messages.warning(request, f"Only {product.stock} item(s) available.")
    request.session["cart"] = cart
    return redirect("cart")


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    cart.pop(str(product_id), None)
    request.session["cart"] = cart
    return redirect("cart")


@login_required
def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.info(request, "Your cart is empty.")
        return redirect("home")

    initial = {"full_name": request.user.get_full_name(), "email": request.user.email}
    form = CheckoutForm(request.POST or None, initial=initial)

    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            products_and_quantities = []
            total = Decimal("0.00")
            for product_id, quantity in cart.items():
                product = Product.objects.select_for_update().filter(pk=product_id, is_active=True).first()
                quantity = int(quantity)
                if not product or quantity < 1 or quantity > product.stock:
                    messages.error(request, "One or more products are no longer available in the requested quantity.")
                    return redirect("cart")
                products_and_quantities.append((product, quantity))
                total += product.price * quantity

            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data["full_name"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                total=total,
            )
            for product, quantity in products_and_quantities:
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    product_name=product.name,
                    quantity=quantity,
                    unit_price=product.price,
                )
                product.stock -= quantity
                product.save(update_fields=["stock"])

        request.session["cart"] = {}
        messages.success(request, f"Order #{order.pk} has been placed. This demo does not process payments.")
        return redirect("order_history")

    return render(request, "store/checkout.html", {"form": form})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items")
    return render(request, "store/order_history.html", {"orders": orders})


def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account has been created.")
        return redirect("home")
    return render(request, "registration/register.html", {"form": form})
