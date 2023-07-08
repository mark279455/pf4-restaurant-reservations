from django.views.generic import TemplateView
import os
import random
import glob


class Index(TemplateView):
    template_name = 'home/index.html'


def randomhomepageimage(dirname):
    valid_fileanme = "restaurant"
    valid_extension = '.webp'

    files = glob.glob(dirname+'/'+valid_fileanme+'?'+valid_extension)
    return dirname + "/" + random.choice(files)
