# test.py file within the air_pollution_data application
from django.test import TestCase,Client
from django.urls import reverse
from main.models.products import Products
from main.models.customer import Customer 
from main.models.orders import Order 
from main.models.category import Category 


class ViewsTestCase(TestCase):
    # Setup is called before each test case runs.
    # Setting up any objects that will be tested.
    def setUp(self):
           self.client = Client()
            
    def tearDown(self) -> None:
        pass
    @classmethod
    def setUpTestData(cls):
        # creat test data
        for i in range(30):  # creat enough data to test
            product = Products.objects.create(product_id=f"{i:05}", name=f"Product {i}")
            customer = Customer.objects.create(customer_id=f"{i}", name=f"Customer{i}")
            
   
    # checks if the region_detail view page returns a 200 status code and if the 'region' is present in the response context
    def test_products_view_invalid_id(self):
        response = self.client.get('products', args=['999'])
        self.assertEqual(response.status_code, 404)

    # test home view
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue('cards' in response.context)
        
        
    # test checkout view
    def test_checkout_view(self):
        response = self.client.get('/check-out/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
       
    