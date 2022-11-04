from django.contrib import admin
from .models import Resto, Owner, item, Comments
# Register your models here.

admin.site.register(Resto)
admin.site.register(Owner)
admin.site.register(item)
admin.site.register(Comments)