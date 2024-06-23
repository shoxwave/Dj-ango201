from django.urls import path

from . import views

app_name ="profiles"

urlpatterns = [
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
    path("profiles/edit/", views.ProfileUpdateView.as_view(), name='edit_profile'),
]