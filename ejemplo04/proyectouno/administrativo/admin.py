from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Estudiante, Modulo, Matricula
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Se crea la clase heredada de ModelResource
# con el objetivo hacer exclude  para la importación
class EstudianteResource(resources.ModelResource):
    class Meta:
        model = Estudiante
        exclude = ('modulos', )

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EstudianteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # se vincula con la clase EstudianteResource
    resource_class = EstudianteResource
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante')
    search_fields = ('nombre', 'cedula')
    exclude = ("modulos",) # se excluye de la interfaz del admin

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Estudiante, EstudianteAdmin)

admin.site.register(Modulo)

# admin.site.register(Matricula)
class MatriculaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('estudiante', 'modulo', 'comentario')
    search_fields = ('estudiante__nombre', 'modulo__nombre')

admin.site.register(Matricula, MatriculaAdmin)
