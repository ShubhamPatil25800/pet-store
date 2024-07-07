from django.contrib import admin
from .models import Orders,OrderItem

class OrderItemInline(admin.TabularInline):
    model=OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemInline]


admin.site.register(Orders,OrderAdmin)

admin.site.register(OrderItem)
