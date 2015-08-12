from django.test import TestCase

from .models import Customer, Contact
# Create your tests here.

class ContactTests(TestCase):
  def setUp(self):
    Customer.objects.create(name='Sample Customer')

  def test_name(self):
    """
    last name should be last
    """
    company = Customer.objects.get(name='Sample Customer')
    new_contact = Contact(first_name='Bob', last_name='Sample', company=company)
    self.assertEqual(new_contact.last_name, 'Sample')


