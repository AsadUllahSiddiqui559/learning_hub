from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from core.models import User, Teacher, Class, Student


# Custom UserAdmin to handle password hashing
class UserAdmin(DefaultUserAdmin):
    # Ensure passwords are hashed when saving users via the admin
    def save_model(self, request, obj, form, change):
        if not change:  # Creating a new user
            obj.set_password(obj.password)  # Hash the password
        elif 'password' in form.changed_data:  # Updating an existing user's password
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)

# Register models with the admin
admin.site.register(User, UserAdmin)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)