from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CookieStand


class CookieStandModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='12345')
        test_user.save()

        CookieStand.objects.create(
            location='Test Location',
            owner=test_user,
            description='Test Description',
            hourly_sales=10,
            minimum_customers_per_hour=5,
            maximum_customers_per_hour=50,
            average_cookie_per_sale=2.5
        )

    def test_location_field_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_owner_field_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')

    def test_description_field_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_hourly_sales_field_label(self):
        cookie_stand = CookieStand.objects.get(id=1)
        field_label = cookie_stand._meta.get_field('hourly_sales').verbose_name
        self.assertEquals(field_label, 'hourly sales')

    def test_absolute_url(self):
        cookie_stand = CookieStand.objects.get(id=1)
        expected_url = reverse('cookiestand_detail', args=[str(cookie_stand.id)])
        self.assertEquals(cookie_stand.get_absolute_url(), expected_url)
