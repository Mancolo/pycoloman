"""
CRM Models.
"""
from django.db import models

from simple_history.models import HistoricalRecords

class Customer(models.Model):
  """A single customer, usually meaning a company/business."""
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=50, blank=True)
  city = models.CharField(max_length=50, blank=True)
  state = models.CharField(max_length=2, blank=True)
  zipcode = models.CharField(max_length=10, blank=True)
  phone = models.CharField(max_length=25, blank=True)
  active = models.BooleanField(default=True)
  locked = models.BooleanField(default=False)
  kind = models.ForeignKey('CustomerKind')
  number = models.CharField(max_length=20, blank=True)
  notes = models.TextField(blank=True)
  start_date = models.DateField(blank=True, null=True)
  closed_date = models.DateField(blank=True, null=True)
  last_modified = models.DateTimeField(auto_now=True)
  history = HistoricalRecords() 

class CustomerKind(models.Model):
  """
  Table for categorizing customers, can only belong to one category at a time.

  label   The name of the customer kind (or type)
  desc    Longer description, optional
  """
  label = models.CharField(max_length=20, blank=False)
  desc = models.CharField(max_length=100, blank=True)
  history = HistoricalRecords() 

class Contact(models.Model):
  first_name = models.CharField(max_length=20)
  middle_name = models.CharField(max_length=20, blank=True)
  last_name = models.CharField(max_length=20)
  company = models.ForeignKey(Customer)
  role = models.CharField(max_length=10)
  phone = models.CharField(max_length=25, blank=True)
  phone_second = models.CharField(max_length=25, blank=True)
  email = models.EmailField(blank=True)
  access_phone = models.BooleanField(default=False)
  access_phys = models.BooleanField(default=False)
  notes = models.TextField(blank=True)
  last_modified = models.DateTimeField(auto_now=True)
  history = HistoricalRecords()
