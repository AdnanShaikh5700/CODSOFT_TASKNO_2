from django.db import models

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=15)
  address = models.TextField(blank=True)
  company = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  class Meta:
    constraints = [models.UniqueConstraint(fields=['email', 'phone'], name='unique_email_phone')]
    ordering = ['-created_at']


  def __str__(self):
    return self.name