from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()



    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            
    context = {"form": form}
    return render(request,"todo/register.html", context)


