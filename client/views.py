import re
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.http import HttpResponse
from client.forms import LogMessageForm
from client.models import LogMessage
from django.views.generic import ListView

# def home(request):
#     return HttpResponse("Hello, Django!")

# def hello_there(request, name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)

def hello_there(request, name):
    return render(
        request,
        'client/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# def home(request):
#     return render(request, "client/home.html")

def about(request):
    return render(request, "client/about.html")

def contact(request):
    return render(request, "client/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "client/log_message.html", {"form": form})
    
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context