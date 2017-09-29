from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.isAdmin)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    image = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=10000)
    price = models.FloatField(null=False)
    stock = models.IntegerField(default=0, null=False)
    category = models.CharField(max_length=50, null=False)
    timesBought = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.name + ' - ' + str(self.price) + ' - ' + self.category


class PurchaseHistory(models.Model):
    id = models.AutoField(primary_key=True)
    idUser = models.ForeignKey('User')
    totalPrice = models.FloatField(null=False)
    date = models.DateField(null=False)
    ostentacaoCount = models.IntegerField(default=0, null=False)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return str(self.id) + '; User: ' + str(self.idUser) + '; Total price: ' + str(self.totalPrice) + '; Date: ' + str(self.date)