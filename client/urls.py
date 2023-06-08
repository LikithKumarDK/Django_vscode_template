from django.urls import path, include
from client import views
from client.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="client/home.html",
)

urlpatterns = [
    path("hello/<name>", views.hello_there, name="Likith Kumar D K"),
    # path("", views.home, name="home"),
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]