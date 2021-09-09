from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    bank_id=models.IntegerField()
    balance=models.IntegerField()


class After(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    sender=models.CharField(max_length=256)
    receiver=models.CharField(max_length=256)
    amount=models.IntegerField()

    def __str__(self):
        return self.sender