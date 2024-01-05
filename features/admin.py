from django.contrib import admin
from features.models import *
# Register your models here.
admin.site.register(InboxDetails)
admin.site.register(SentDetails)
admin.site.register(BinDetails)
admin.site.register(JunkDetails)