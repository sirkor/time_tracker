from django.contrib import admin
from django.core.urlresolvers import reverse
from time_tracker.models import Activities
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class ActivitiesAdmin(admin.ModelAdmin):
    list_filter = ['activities_type']
    search_fields = ['activities_name']
admin.site.register(Activities, ActivitiesAdmin)

admin.site.unregister(User)


class UserActivitiesInline(admin.StackedInline):
    model = Activities
    fields = ('activity_link',)
    readonly_fields = fields

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def activity_link(self, obj):
        return u'<a href="{0}">{1}</a>'.format(reverse('admin:time_tracker_activities_change', args=(obj.pk,)),
                                               obj.activities_name)

    activity_link.allow_tags = True
    activity_link.short_description = Activities._meta.get_field('activities_name').verbose_name.title()
    activity_link.admin_order_field = 'activities_name'


@admin.register(User)
class UserProfileAdmin(UserAdmin):
    inlines = [ UserActivitiesInline ]