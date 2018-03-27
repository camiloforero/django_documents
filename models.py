# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def upload_prefix(instance, name):
    return u"odtTemplates/%s.odt" % (instance.file_name, )

class ODTTemplate(models.Model):
    """
        This represents a template, which should contain the actual file and a name so this can be easily retrieved in the API
    """
    name = models.CharField("Nombre", max_length=32, unique=True, db_index=True, help_text="Un nombre único para este documento que sirva para identificarlo y diferenciarlo de los demás")
    file_name = models.SlugField(max_length=32, default="default", help_text="El nombre que va a tener el archivo cuando se guarde")
    generated_file_name = models.CharField("Nombre autogenerado", max_length=32, default="default", help_text="El nombre final que va a tener el documento cuando se envíe por correo o se suba a PODIO. Admite sintaxis de templates de Django para valores dinámicos")
    templateFile = models.FileField(upload_to=upload_prefix, help_text=u"Acá va el archivo de formato ODT que será utilizado para generar el PDF. Si quieres saber más revisa el booklet que se encuentra en esta dirección: LINK")
    def __str__(self):
        return self.name

# Create your models here.
