from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import CanonicalSource

from .models import CanonicalUpdate

from .models import RDBMSInstance

from .models import UpdateJob



class CanonicalSourceInline(admin.TabularInline):
    model = CanonicalSource


class CanonicalUpdateInline(admin.TabularInline):
    model = CanonicalUpdate


class RDBMSInstanceInline(admin.TabularInline):
    model = RDBMSInstance
 

class UpdateJobInline(admin.TabularInline):
    model = UpdateJob


class CanonicalSourceAdmin(admin.ModelAdmin):
    inlines = [
    ]


class CanonicalUpdateAdmin(admin.ModelAdmin):
    inlines = [
    ]


class RDBMSInstanceAdmin(SimpleHistoryAdmin):
    inlines = [
    ]


class UpdateJobAdmin(SimpleHistoryAdmin):
    inlines = [
    ]



admin.site.register(CanonicalSource, CanonicalSourceAdmin)

admin.site.register(CanonicalUpdate, CanonicalUpdateAdmin)

admin.site.register(RDBMSInstance, RDBMSInstanceAdmin)

admin.site.register(UpdateJob, UpdateJobAdmin)

