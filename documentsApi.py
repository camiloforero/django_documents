# -*- coding: utf-8 -*-
import os
import subprocess
import webodt
from . import models
from django.template import Context

class ODTTemplate():
    def __init__(self, templateName):
        """
            Creates a template converter which will generate ODT documents when passed a dictionary, among other things
            templateName: The name of the template, it will be used to load it from the database
        """
        self.template = webodt.ODFTemplate(templateName)

    def render(self, context, odt=False):
        document = self.template.render(Context(context), delete_on_close=False)
        if odt:
            return document
        else:
            oldenviron = os.environ['HOME']
            os.environ['HOME'] = "/tmp"
            returncode = subprocess.call(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", "/tmp", document.name])
            print "PDF generation return code: %s " % str(returncode)
            filename, file_extension = os.path.splitext(document.name)
            pdf = open(filename + ".pdf")
            os.environ['HOME'] = oldenviron
            return pdf
        
    def renderODT(self, context):
        document = self.template.render(Context(context), delete_on_close=False)
        return document
