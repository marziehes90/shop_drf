import factory
from product.models import Category,Brand,Product

class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model=Category

    name=factory.sequence(lambda x: f"category_{x}")


class BrandFactory(factory.django.DjangoModelFactory):

    class Meta:
        model=Brand
        
    name=factory.sequence(lambda z: f"brand_{z}")

class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model=Product
        
    name=factory.sequence(lambda v: f"product_{v}")
    # name="product_test"
    # descirption="description_test"
    description=factory.sequence(lambda v: f"description_{v}")

    is_digital=False
    brand=factory.SubFactory(BrandFactory)
    category=factory.SubFactory(CategoryFactory)
    