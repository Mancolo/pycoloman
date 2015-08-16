"""
CRM Models.
"""
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType



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
  kind = models.ForeignKey('CustomerKind', blank=True, null=True)
  number = models.CharField(max_length=20, blank=True)
  notes = models.TextField(blank=True)
  start_date = models.DateField(blank=True, null=True)
  closed_date = models.DateField(blank=True, null=True)
  last_modified = models.DateTimeField(auto_now=True)
  history = HistoricalRecords() 

  def __str__(self):
    return self.name

class CustomerKind(models.Model):
  """
  Table for categorizing customers, can only belong to one category at a time.

  label   The name of the customer kind (or type)
  desc    Longer description, optional
  """
  label = models.CharField(max_length=20, blank=False)
  desc = models.CharField(max_length=100, blank=True)
  history = HistoricalRecords() 

  def __str__(self):
    return self.label

class Contact(models.Model):
  """
  A human being that is employed by a customer and can have access to colo resources.
  """
  first_name = models.CharField(max_length=20)
  middle_name = models.CharField(max_length=20, blank=True)
  last_name = models.CharField(max_length=20)
  company = models.ForeignKey(Customer)
  role = models.CharField(max_length=10, blank=True)
  phone = models.CharField(max_length=25, blank=True)
  phone_second = models.CharField(max_length=25, blank=True)
  email = models.EmailField(blank=True)
  access_phone = models.BooleanField(default=False)
  access_phys = models.BooleanField(default=False)
  notes = models.TextField(blank=True)
  last_modified = models.DateTimeField(auto_now=True)
  history = HistoricalRecords()

  def __str__(self):
    return '%s %s' % (self.first_name, self.last_name)

class Site(models.Model):
  """
  A discrete datacenter location. 
  """
  name = models.CharField(max_length=100)

class Room(models.Model):
  """
  A discrete usually access controlled area of floorspace in the datacenter.
  """
  name = models.CharField(max_length=100)
  rack_pos = generic.GenericRelation('RackPosition')

  def __str__(self):
    return '%s' % self.name

class Cage(models.Model):
  """
  A sepearate area of a room under another layer of access control.
  """
  name = models.CharField(max_length=100)
  room = models.OneToOneField('Room')
  rack_pos = generic.GenericRelation('RackPosition')

  def __str__(self):
    return '%s' % self.name

class Rack(models.Model):
  """
  A physically installed rack frame.
  """
  label = models.CharField(max_length=100,blank=True)
  u_height = models.IntegerField(default=42)

  def __str__(self):
    return '%s' % self.label


class RackPosition(models.Model):
  """
  A mapped space on a datacenter floor that can hold a rack.
  """
  rack = models.OneToOneField('Rack', blank=True, null=True)
  pos_x = models.IntegerField(blank=True)
  pos_y = models.IntegerField(blank=True)
  content_type = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  content_object = generic.GenericForeignKey("content_type", "object_id")

  class Meta:
    unique_together = ('content_type', 'object_id')

  def __str__(self):
    return '%s:(%d,%d)' % (self.content_object.name, self.pos_x, self.pos_y)
