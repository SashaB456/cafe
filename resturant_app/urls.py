from django.urls import path
import resturant_app.views as views
urlpatterns = [
    path("get-reviews/", views.get_posts, name="get-reviews"),
    path("register/", views.register, name="register"),
    path("create-review/", views.create_post, name="create-review"),
]