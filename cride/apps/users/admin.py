# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from apps.users.models import User, Profile


#Esta clase es diferente por el modelo de usuario es CUSTOM
class CustomUserAdmin(UserAdmin):

    list_display = ('email','username', 'first_name', 'last_name', 'is_staff', 'is_client',  'is_verified')
    list_filter = ('is_staff', 'is_client', 'is_verified', 'created', 'modified')


# Este decorador funciona igual que admin.site.register
@admin.register(Profile)
class Profile(admin.ModelAdmin):

    list_display = ('user','reputation','rides_taken','rides_offered')
    search_fields = ('user__username', 'user__email', 'user__first_name','user__last_name')
    list_filter = ('reputation',)



admin.site.register(User, CustomUserAdmin)

# cambiar nombre del sitio
admin.site.site_header = "Cride"
admin.site.site_title = "Cride"
admin.site.index_title = "Panel"
