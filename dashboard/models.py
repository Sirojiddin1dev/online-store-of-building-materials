from account.models import *

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Products(models.Model):
    image = models.ImageField(upload_to='product_photo/')
    title = models.CharField(max_length=55)
    price = models.IntegerField(default=0)
    product_info = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to='Category', default=1, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    featured_product = models.BooleanField(default=False)
    is_advert = models.BooleanField(default=False)
    advert_text = models.CharField(max_length=50, null=True, blank=True)
    new_product = models.BooleanField(default=True)
    product_create = models.DateField(auto_now_add=True)
    view = models.IntegerField(default = 0)

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Basket(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Checkout(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message="Telefon raqamingizni to'g'ri ko'rsating.",
            code="Telefon raqam xato"
        )
    ])
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TotalSum(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.TextField()
    sub_total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.total_expenses}"
