from django.contrib import admin
from escola.models import Aluno, Curso


# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento',)
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo','descricao','nivel',)
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)
    list_per_page = 10

admin.site.register(Aluno,Alunos)
admin.site.register(Curso,Cursos)
