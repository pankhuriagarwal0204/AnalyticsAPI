import base
from archives import models

all = models.Morcha.objects.all()
for i in all:
   print i.name