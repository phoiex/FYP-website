from django.contrib import admin

# Register your models here.

from .models import CustomerInfo, TodoItem, CopilotResponse

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(CustomerInfo)
admin.site.register(CopilotResponse)