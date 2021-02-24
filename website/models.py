from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.IntegerField(default=13)
    skills_wont = models.CharField(max_length=20000, default="-")
    skills_know = models.CharField(max_length=20000, default="-")
    about_me = models.CharField(max_length=10000, default="-")
    city = models.CharField(max_length=100, default="-")
    contact = models.CharField(max_length=100, default="0000000")

class Skill(models.Model):
    name_skill = models.CharField(max_length=100, default="дизайн")

    def __str__(self):
        return self.name_skill


class Category(models.Model):
    name_category = models.CharField(max_length=60)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Родитель",
                               related_name='child')

    def __str__(self):
        return "Название:{} Родитель:{}".format(self.name_category, self.parent)


class Category_with_skill(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_in_category = models.ManyToManyField(Skill, blank=True)


    def __str__(self):
        return "Категория:{} Навык:{}".format(self.main_category.name_category, self.skill_in_category)


class User_with_skill(models.Model):
    User_main = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill_string = models.CharField(max_length=60)
    # skill_main = models.ForeignKey(Skill, on_delete=models.CASCADE)
    wont_know = models.BooleanField("Умеешь/хочешь научиться")  # True - know ; False - wont
    def __str__(self):
        return "ID:{} Навык:{} {}".format(self.User_main.id, self.skill_main, self.wont_know)


class Application(models.Model):
    user_creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=1000)
    wont = models.CharField(max_length=1000)
    know = models.CharField(max_length=1000)
    contacts = models.CharField(max_length=1000)
    def __str__(self):
        return "ID:{} Навык:{} {}".format(self.user_creator.id, self.wont, self.know)
