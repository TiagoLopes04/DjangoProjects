from django.db import models
from django.contrib.auth import get_user_model

class Chassi(models.Model):
    numero = models.CharField('Chassi',max_length=16,help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome',max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome

class Carro(models.Model):
    """
    # OneToOneField
    Cada carro só se pode relacionar com 1 chassi
    Cada chassi só se pode relacionar com 1 carro
    Relacionamento 1 para 1

    # ForeignKey
    Cada carro tem 1 montadora
    Cada Montadora pode ter varios carros
    Relacionamento 1 para muitos

    # ManyToManyField
    1 carro pode ser conduzido por vários motoristas
    1 motorista por conduzir vários carros
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo',max_length=30,help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preço',max_digits=8,decimal_places=2) #valor max=99999999.99


    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'