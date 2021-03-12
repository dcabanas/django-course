from django.contrib import admin
from .models import Todo

# This class is super important if we want to at least
# see (not edit) in the admin page some properties of our
# models that we cannot edit
class TodoAdmin(admin.ModelAdmin):
    # these must match the name of the models properties
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Todo, TodoAdmin)