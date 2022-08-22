from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(VeryGoodModel)
admin.site.register(GoodModel)
admin.site.register(AverageModel)
admin.site.register(BadModel)
admin.site.register(VeryBadModel)