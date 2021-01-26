from django.contrib import admin
from .models import *
admin.site.register(CustomUser)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Category_with_skill)
admin.site.register(User_with_skill)
# Register your models_b here.
