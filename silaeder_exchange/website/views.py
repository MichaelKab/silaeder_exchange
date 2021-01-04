from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser, User_with_skill
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

def main(request):
    html = "<html><body> <p>Main page<p> <a href='http://127.0.0.1:8000/accounts/login'>Log in</a></body></html>"
    return HttpResponse(html)

@login_required
def cob(request):
    print(request.user)
    print(request.user.username, request.user.password)
    print("###", request.GET)
    print(request.user.id, "!!!!!!!!!")
    user = CustomUser.objects.get(id=request.user.id)
    user_skills_wont = User_with_skill.objects.filter(User_main=user, wont_know=False)
    user_skills_know = User_with_skill.objects.filter(User_main=user, wont_know=True)
    #username = request.GET['username']
    #assword = request.GET['password']
    #print(username, password)
    #fr = request.POST["first_name"]
    return render(request, 'base.html', {"user": user, "skills_wont":user_skills_wont, "skills_know":user_skills_know})#, context={"username":username,"password":password, "fr":fr })

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