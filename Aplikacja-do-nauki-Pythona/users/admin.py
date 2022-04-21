from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    template = "admin/profile_inline.html"
    max_num = 1
    can_delete = False
    readonly_fields = ('points',)
    fields = ('education', 'profile_image', 'points')

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return Profile.objects.filter(user_id=request.user.id)

    def has_change_permission(self, request, obj=None):
        """
            Enable own profile for requested user
        """
        if obj and obj.id == request.user.id:
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.id == request.user.id:
            return True
        return super().has_delete_permission(request, obj)


admin.site.unregister(User)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )
    inlines = (ProfileInline, )


    def get_queryset(self, request):
        print(request.user.id)

        if request.user.is_superuser:
            return super().get_queryset(request)
        return User.objects.filter(id=request.user.id)

    def has_change_permission(self, request, obj=None):
        """
            Enable own profile for requested user
        """
        if obj and obj.id == request.user.id:
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.id == request.user.id:
            return True
        return super().has_delete_permission(request, obj)
