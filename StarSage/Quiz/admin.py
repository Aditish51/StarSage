from django.contrib import admin
from .models import basic_mcq, basic_tf, basic_fbl

admin.site.register(basic_mcq)
admin.site.register(basic_tf)
admin.site.register(basic_fbl)