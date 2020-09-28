from django.contrib import admin

from apps.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):

    list_display = ('name','slug_name', 'rides_offered', 'rides_taken', 'verified', 'is_public', 'is_limited', 'members_limit')
    list_filter = ('is_public', 'is_limited')
    search_fields = ('slug_name', 'name')