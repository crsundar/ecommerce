from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=7, decimal_places=2)
	sale_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def get_price(self):
		return self.price


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	activr = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.product.title