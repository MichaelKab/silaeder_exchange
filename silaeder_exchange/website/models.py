from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models_b here.
class CustomUser(AbstractUser):
    age = models.IntegerField(default=13)
    gender = models.CharField(choices=[("М", "М"), ("Ж", "Ж")], max_length=2)
    gender_work = models.CharField(choices=[("М", "М"), ("Ж", "Ж"), ("Неважно", "Неважно")], max_length=8)


class Skill(models.Model):
    name_skill = models.CharField(max_length=100)


class Category(models.Model):
    name_category = models.CharField(max_length=60)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Родитель",
                               related_name='child')


class Category_with_skill(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_in_category = models.ManyToManyField(Skill, blank=True)


class User_with_skill(models.Model):
    User_main = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill_wont_know = models.BooleanField(Skill)  # True - know ; False - wont
