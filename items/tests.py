from decimal import Decimal
from django.test import TestCase
from .models import Item

# Create your tests here.
class ItemsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for i in range(10):
            Item.objects.create(name=f"Product {i+1}", description=f"Desc Prod {i+1}", price = Decimal(i*1000))

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def testObjects(self):
        items = Item.objects.all()
        self.assertEqual(len(items), 10)