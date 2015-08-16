from django.test import TestCase

from .models import Customer, Contact
# Create your tests here.

class ContactTests(TestCase):
  def setUp(self):
    Customer.objects.create(name='Sample Customer')
    self.company = Customer.objects.get(name='Sample Customer')

  def test_name(self):
    """
    last name should be last
    """
    Contact.objects.create(first_name='Bob', last_name='Sample', company=self.company)
    retrieved_contact = Contact.objects.get(first_name='Bob', last_name='Sample')
    self.assertEqual(retrieved_contact.last_name, 'Sample')


