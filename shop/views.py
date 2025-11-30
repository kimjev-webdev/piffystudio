import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, ProductImage, Variant, Category
from .forms import ProductForm, VariantForm, CategoryForm


# PRODUCT LIST
def products_list(request):
    products = Product.objects.all()
    return render(request, "shop/manage/products_list.html", {"products": products})


# ADD PRODUCT
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect("shop:product_edit", product.id)
    else:
        form = ProductForm()

    return render(request, "shop/manage/product_form.html", {"form": form, "product": None})


# EDIT PRODUCT
def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.images.all()
    variants = product.variants.all()

    if request.method == "POST" and "save_product" in request.POST:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("shop:product_edit", product.id)
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "shop/manage/product_form.html",
        {"form": form, "product": product, "images": images, "variants": variants},
    )


# UPLOAD IMAGES
def upload_product_image(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST" and request.FILES.getlist("images"):
        for file in request.FILES.getlist("images"):
            ProductImage.objects.create(product=product, image=file)

    return redirect("shop:product_edit", product.id)


# DELETE IMAGE
def delete_product_image(request, image_id):
    image = get_object_or_404(ProductImage, id=image_id)
    product_id = image.product.id
    image.delete()
    return redirect("shop:product_edit", product_id)


# ADD VARIANT
def add_variant(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = VariantForm(request.POST)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.product = product
            variant.save()
            return redirect("shop:product_edit", product.id)
    else:
        form = VariantForm()

    return render(request, "shop/manage/variant_form.html", {"form": form, "product": product})


# EDIT VARIANT
def edit_variant(request, variant_id):
    variant = get_object_or_404(Variant, id=variant_id)
    product = variant.product

    if request.method == "POST":
        form = VariantForm(request.POST, instance=variant)
        if form.is_valid():
            form.save()
            return redirect("shop:product_edit", product.id)
    else:
        form = VariantForm(instance=variant)

    return render(request, "shop/manage/variant_form.html", {"form": form, "product": product})


# DELETE VARIANT
def delete_variant(request, variant_id):
    variant = get_object_or_404(Variant, id=variant_id)
    product_id = variant.product.id
    variant.delete()
    return redirect("shop:product_edit", product_id)


# ============================================
# NEW: UPDATE IMAGE ORDER (AJAX ENDPOINT)
# ============================================

def update_image_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order_list = data.get("order", [])

        for item in order_list:
            img_id = item.get("id")
            pos = item.get("position")
            ProductImage.objects.filter(id=img_id).update(position=pos)

        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "invalid request"}, status=400)
