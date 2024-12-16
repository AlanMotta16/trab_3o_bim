from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'respondido', 'data_recebimento')
    list_filter = ('respondido',)
    search_fields = ('nome', 'email')
    readonly_fields = ('data_recebimento',)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.respondido:
            return self.readonly_fields + ('resposta',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if obj.resposta and not obj.respondido:
            obj.respondido = True
            obj.data_resposta = now()
        super().save_model(request, obj, form, change)


admin.site.register(Contact, ContactAdmin)