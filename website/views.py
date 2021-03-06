# -*- coding: utf-8 -*
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
from django.views.generic.detail import DetailView


def main(request):
    applications = Application.objects.all()
    all_users = CustomUser.objects.filter(can_see=True)
    users = []
    if request.method == "POST":
        keyword = request.POST['find']
        for i in all_users:
            if keyword in i.skills_know:
                users.append(i)
            elif keyword in i.skills_wont:
                users.append(i)
            elif keyword in i.about_me:
                users.append(i)
    else:
        users = all_users
    return render(request, 'new_design/main_d.html', {"users": users})


def is_not_none_warning(request, model_field, text_name_in_ht, warning):
    field = request.POST.get(text_name_in_ht)
    print(field, list(field))
    if field is not str():
        print("!!")
        model_field = field
    else:
        warning += 1
    print(warning, "###")
    return model_field, warning


@login_required(login_url="/login")
def cob(request):
    # print(request.META["HTTP_REFERER"])
    bad_ap = []
    user = CustomUser.objects.get(id=request.user.id)
    applications = Application.objects.filter(user_creator=request.user.id)
    warning = 0

    if request.method == "POST":
        print("#################################")
        application = Application()
        application.user_creator = user
        application.about_me, warning = is_not_none_warning(request, application.about_me, "about_me", warning)
        application.wont, warning = is_not_none_warning(request, application.wont, "wont", warning)
        application.know, warning = is_not_none_warning(request, application.know, "know", warning)
        application.contacts, warning = is_not_none_warning(request, application.contacts, "contacts", warning)
        # print(warning)
        if warning == 0:
            application.save()
        else:
            bad_ap = application
        # print(warning, "!!!")
    if warning == 0:
        fin_warning = False
    else:
        fin_warning = True
    user_skills_wont = User_with_skill.objects.filter(User_main=user, wont_know=False)
    user_skills_know = User_with_skill.objects.filter(User_main=user, wont_know=True)
    fields = [f"{user.first_name} {user.last_name}", user.age, user.contact]
    return render(request, 'new_design/profile.html', {"user": user, "fields": fields, "skills_wont": user_skills_wont,
                                            "skills_know": user_skills_know, "applications": applications,
                                            "warning": fin_warning, "bad_ap": bad_ap, "MEDIA_URL": '/media/'})


def check_is_not_none(request, model_field, text_name_in_ht):
    field = request.POST.get(text_name_in_ht)
    if field is not str():
        model_field = field
    return model_field


@login_required(login_url="/login")
def edit_profile(request):
    try:
        person = CustomUser.objects.get(id=request.user.id)
        if request.method == "POST":
            # print("##########################")
            # print(request.POST)
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
            if contact is not None:
                person.contact = contact
            skills_wont = request.POST.get("skills_wont")
            if skills_wont is not None:
                person.skills_wont = skills_wont
            skills_know = request.POST.get("skills_know")
            if skills_know is not None:
                person.skills_know = skills_know
            about_me = request.POST.get("about_me")
            if about_me is not None:
                person.about_me = about_me
            short_description = request.POST.get("short_description")
            if short_description is not None:
                person.short_description = short_description
            pict = request.POST.get("pict")
            print(pict)
            if pict is not None:
                print("!!!!!")
                person.user_ava = pict
            # print("!!!!!!!!!!!!!!", name, last_name, skills_know, skills_wont, '3333333333333')
            person.save()
            return HttpResponseRedirect("/pr")
        else:
            return render(request, "en_templates/en_edit_profile_new.html",
                          {"user": CustomUser.objects.get(id=request.user.id)})
    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'new_design/signup.html'


class ApplicationView(DetailView):
    model = Application
    template_name = "application_detail.html"


def edit_application(request, pk):
    id_ap = request.path.split('/')[-2]
    # print(id_ap)
    template_name = "application_detail.html"
    application = Application.objects.get(id=id_ap)
    # print(application)
    if request.method == 'POST':
        application.about_me = check_is_not_none(request, application.about_me, "about_me")
        application.wont = check_is_not_none(request, application.wont, "wont")
        application.know = check_is_not_none(request, application.know, "know")
        application.contacts = check_is_not_none(request, application.contacts, "contacts")
        application.save()
        return HttpResponseRedirect("/pr")
    return render(request, "application_detail.html", {"application": application})
    # return redirect("home")


from django.views.generic.edit import DeleteView

# Relative import of GeeksModel
from .models import Application

from django.urls import path


def delit_application(request, pk):
    print(request.path.split('/'))
    id_ap = request.path.split('/')[1]
    try:
        application = Application.objects.get(id=id_ap)
        print(id_ap, request.user.id, application.user_creator.id)
        if application.user_creator.id == request.user.id:
            application.delete()
        return HttpResponseRedirect("/pr")
    except Application.DoesNotExist:
        return HttpResponseRedirect("/pr")


def activate(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.user.is_authenticated:
        if user.can_see:
            user.can_see = False
        else:
            user.can_see = True
        user.save()
    return HttpResponseRedirect("/pr")


class ApplicationDeleteView(DeleteView):
    model = Application
    success_url = "/pr"


def show_all_inf(request, pk):
    print(pk, "#####", request.user.id )
    print(request)
    try:
        user = CustomUser.objects.get(id=pk)
        if user.can_see:
            print(user.id, user.about_me)
            print(user.skills_wont)
            return render(request, "en_templates/en_detail_application.html", {"application": user})
        else:
            return HttpResponseRedirect("/")
    except CustomUser.DoesNotExist:
        return HttpResponseRedirect("/")
    print(user, user.id)

def responding(request, pk):
    user = CustomUser.objects.get(id=pk)
    user.responding += 1
    user.save()
    return HttpResponseRedirect("/")

