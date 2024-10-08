import pytest
pytestmark=pytest.mark.django_db

class TestCategoryModel:

    def test_str_method(self,category_factory):
        new_object=category_factory(name="category_test")
        assert new_object.__str__()=="category_test"

class TestBrandModel:

    def test_str_method(self,brand_factory):
        new_object=brand_factory(name="brand_test")
        assert new_object.__str__()=="brand_test"

class TestProductModel:

    def test_str_method(self,product_factory):
        new_object=product_factory(name="product_test")
        assert new_object.__str__()=="product_test"