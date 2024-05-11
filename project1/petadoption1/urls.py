from django.urls import path, include  
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup, name="signup"),
    path("marketplace", views.marketplace, name="marketplace"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("logout", views.logout_view, name="logout"),
    path("pet_page/<int:pet_id>", views.pet_page, name="pet_page"),
    path("category_disp/<int:category_id>", views.category_disp, name="category_disp"),
    path("pet_page/<int:pet_id>/newcomment", views.newcomment, name="newcomment"),  # Use a distinct path for newcomment
]
