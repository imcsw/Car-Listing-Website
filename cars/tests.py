from django.test import TestCase
from django.urls import reverse

from .models import Cars

# Create your tests here.
class CarsModelTests(TestCase):
    def test_no_cars(self):
        response = self.client.get(reverse('cars:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['carList'], [])

    def get_queryset(self):
        return Cars.object.order_by('dateAdded')[:3]