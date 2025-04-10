from django.db import models

#from django.contrib.auth.models import User
#1 FORMA SO FUNFA SE USAR O DEFAULT
#class Post(models.Model):
#   autor =models.ForeignKey(User,verbose_name='Autor',on_delete=models.CASCADE)
#   titulo = models.CharField('Titulo',max_length=100)
#   texto = models.CharField('Tecto',max_length=400)
#   def __str__(self):
#       return self.titulo

#from django.conf import settings
#2 FORMA
#class Post(models.Model):
#   autor =models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Autor',on_delete=models.CASCADE)
#   titulo = models.CharField('Titulo',max_length=100)
#   texto = models.CharField('Tecto',max_length=400)
#   def __str__(self):
#       return self.titulo

#3 forma e mais indicada
from django.contrib.auth import get_user_model
class Post(models.Model):
   autor =models.ForeignKey(get_user_model(),verbose_name='Autor',on_delete=models.CASCADE)
   titulo = models.CharField('Titulo',max_length=100)
   texto = models.CharField('Tecto',max_length=400)
   def __str__(self):
       return self.titulo
