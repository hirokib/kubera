from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer = models.ForeignKey(Customer)
    trans_date = models.DateTimeField('Purchase Time')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Balance(models.Model):
    customer = models.ForeignKey(Customer)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.customer.name+": "+str(self.balance)