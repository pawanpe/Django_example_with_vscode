from django.urls import path
from . import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name = "hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there_view, name="hello_there_view"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]