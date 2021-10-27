from django.contrib import admin
from .models import Vendas, Produto, Vendedor

admin.site.register(Vendas)
admin.site.register(Produto)
admin.site.register(Vendedor)

