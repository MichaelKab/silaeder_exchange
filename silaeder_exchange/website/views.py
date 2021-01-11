from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser, User_with_skill, Application
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

def main(request):
    applications = Application.objects.all()
    print(applications)
    return render(request, 'main.html', {"applications": applications})

@login_required
def cob(request):
    user = CustomUser.objects.get(id=request.user.id)
    applications = Application.objects.filter(user_creator=request.user.id)
    if request.method == "POST":
        print("#################################")
        application = Application()
        application.user_creator = user
        application.about_me = request.POST.get("about_me")
        application.wont = request.POST.get("wont")
        application.know = request.POST.get("know")
        application.contacts = request.POST.get("contacts")
        application.title = request.POST.get("title")
        application.save()
    user_skills_wont = User_with_skill.objects.filter(User_main=user, wont_know=False)
    user_skills_know = User_with_skill.objects.filter(User_main=user, wont_know=True)
    return render(request, 'base.html', {"user": user, "skills_wont": user_skills_wont,
                                         "skills_know": user_skills_know, "applications": applications})

@login_required
def edit_profile(request):
    try:
        person = CustomUser.objects.get(id=request.user.id)
        if request.method == "POST":
            print(request.POST)
            name = request.POST.get("name")
            if name is not None:
                person.first_name = name
            last_name = request.POST.get("last_name")
            if last_name is not None:
                person.last_name = last_name
            age = request.POST.get("age")
            if age is not None:
                person.age = age
            username = request.POST.get("username")
            if username is not None:
                person.username = username
            contact = request.POST.get("contact")
            if username is not None:
                person.contact = contact
            city = request.POST.get("city")
            if username is not None:
                person.city = city
            person.save()
            return HttpResponseRedirect("/main/pr")
        else:
            return render(request, "edit_profile.html", {"person": person})
    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'