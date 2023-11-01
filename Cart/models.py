from django.db import models

class Cart(models.Model):
    user_id = models.ForeignKey("Accounts.User", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Accounts.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product_id