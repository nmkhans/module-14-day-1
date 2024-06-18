from django.db import models

# Create your models here.
class User(models.Model):
  id = models.AutoField(primary_key=True)
  # id = models.BigAutoField(primary_key=True) same as auto field but for 64 bit large integer number

  roll = models.IntegerField()
  agree = models.BooleanField()
  name = models.CharField(max_length=255)
  date = models.DateField()
  event_time = models.DateTimeField()
  email = models.EmailField()


  #? teacher = models.ForeignKey(anotherModel, on_delete = models.CASCADE)
  #: this Foreign key field is used to establish one to many rellationship with another model of database

  #? book = models.ManyToManyField(anotherModel)
  #: this field is used to create many to many relation with another database model

  #? id_card = models.OneToOneField(anotherModel, on_delete=models.CASCADE)
  #: this field is used to create one to one relation with another database model

  message = models.TextField()