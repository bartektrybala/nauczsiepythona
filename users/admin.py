from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'education', 'profile_image', 'points')

    def get_queryset(self, request):
        return Profile.objects.filter(user_id=request.user.id)

    def has_change_permission(self, request, obj):
        """
            Enable own profile for requested user
        """
        if obj.user_id == request.user.id:
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj):
        if obj.user_id == request.user.id:
            return True
        return super().has_change_permission(request, obj)

