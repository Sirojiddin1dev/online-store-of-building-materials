from account.models import *


class Products(models.Model):
    image = models.ImageField(upload_to='product_photo/')
    title = models.CharField(max_length=55)
    price = models.IntegerField(default=0)
    product_info = models.TextField(null=True, blank=True)
    Category =(
        ("Fasad", "Fasad"),
        ('Tiokliya', 'Tiokliya'),
        ('Qoliplik', 'Qoliplik'),
    )
    category = models.CharField(max_length=100, choices=Category)
    is_banner = models.BooleanField(default=False)
    banner_title = models.CharField(max_length=100, null=True, blank=True)
    banner_text = models.CharField(max_length=255, null=True, blank=True)
    shop_collections = models.BooleanField(default=False)
    featured_product = models.BooleanField(default=False)
    is_advert = models.BooleanField(default=False)
    advert_text = models.CharField(max_length=50, null=True, blank=True)
    new_product = models.BooleanField(default=True)
    product_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    product = models.ManyToManyField(Products)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Basket(models.Model):
    product = models.ManyToManyField(Products)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Checkout(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message="Telefon raqamingizni to'g'ri ko'rsating.",
            code="Telefon raqam xato"
        )
    ])
    message = models.TextField()

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
