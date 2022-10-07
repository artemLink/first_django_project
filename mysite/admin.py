from django.contrib import admin
from .models import users
from .models import count


admin.site.register(users)
admin.site.register(count)
