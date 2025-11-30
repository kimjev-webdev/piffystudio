from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("manage/products/", views.products_list, name="products_list"),
    path("manage/products/add/", views.add_product, name="add_product"),
    path("manage/products/<int:product_id>/edit/", views.product_edit, name="product_edit"),

    path("manage/products/<int:product_id>/upload-image/", views.upload_product_image, name="upload_product_image"),
    path("manage/products/delete-image/<int:image_id>/", views.delete_product_image, name="delete_product_image"),

    path("manage/variants/add/<int:product_id>/", views.add_variant, name="add_variant"),
    path("manage/variants/edit/<int:variant_id>/", views.edit_variant, name="edit_variant"),
    path("manage/variants/delete/<int:variant_id>/", views.delete_variant, name="delete_variant"),

    # NEW — Step 1 endpoint
    path("manage/products/update-image-order/", views.update_image_order, name="update_image_order"),
]
