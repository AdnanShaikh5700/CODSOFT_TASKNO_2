from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from .models import Contact
from .serializer import ContactSerializer

# Create your views here.

class ContactPagination(PageNumberPagination):
  page_size = 10
  page_size_query_param = 'page_size'
  max_page_size = 100

class ContactListCreateView(generics.ListCreateAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  pagination_class = ContactPagination

  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['name', 'email', 'phone']
  ordering_fields = ['name', 'email', 'company', 'created_at']
  ordering = ['-created_at']


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer 
