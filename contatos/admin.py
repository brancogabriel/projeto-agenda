from django.contrib import admin
from . models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email','data_criacao', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome', 'email')
    list_per_page = 50
    search_fields = ('nome', 'sobrenome', 'email')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
