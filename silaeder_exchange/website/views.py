from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser, User_with_skill
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
# Create your views here.
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
            person.first_name = request.POST.get("name")
            person.last_name = request.POST.get("last_name")
            person.age = request.POST.get("age")
            person.username = request.POST.get("username")
            person.save()
            return HttpResponseRedirect("/main/pr")
        else:
            return render(request, "edit_profile.html", {"person": person})
    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
