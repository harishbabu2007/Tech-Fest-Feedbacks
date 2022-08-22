from django.db import models

# Create your models here.
class VeryGoodModel(models.Model):
  yes = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return f'{self.yes}'


class GoodModel(models.Model):
  yes = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return f'{self.yes}'


class AverageModel(models.Model):
  yes = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return f'{self.yes}'

class BadModel(models.Model):
  yes = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return f'{self.yes}'

class VeryBadModel(models.Model):
  yes = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return f'{self.yes}'

