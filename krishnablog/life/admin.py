from django.contrib import admin

# Register your models here.
from .models import Life
from .models import Task

class StepInline(admin.StackedInline):
    # also we can use tabular form
    model = Task

class LifeAdmin(admin.ModelAdmin):
    inlines = [StepInline,]


admin.site.register(Life, LifeAdmin)
admin.site.register(Task)
