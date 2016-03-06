# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def upload_prefix(instance, name):
    return u"odtTemplates/%s.odt" % (instance.name, )

class ODTTemplate(models.Model):
    """
        This represents a template, which should contain the actual file and a name so this can be easily retrieved in the API
    """
    name = models.CharField(max_length=16, unique=True, db_index=True)
    templateFile = models.FileField(upload_to=upload_prefix, help_text=u"Acá va el archivo de formato ODT que será utilizado para generar el PDF. Si quieres saber más revisa el booklet que se encuentra en esta dirección: LINK")
    def __str__(self):
        return self.name

# Create your models here.
