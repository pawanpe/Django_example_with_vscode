from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from datetime import datetime
from hello.models import LogMessage
from hello.forms import LogMessageForm

# Create your views here.

def home(request):
    return render(request, "hello/home.html")

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def hello_there_view(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'title': 'Hello, Django',
            'name': name,
            'date': datetime.now(),
        }
    )


def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    if request.method == "POST":
        form = LogMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        form = LogMessageForm()
        return render(request, "hello/log_message.html", {"form": form})
