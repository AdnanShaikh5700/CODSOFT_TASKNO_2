from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ['id', 'name', 'email', 'phone', 'address', 'company', 'created_at', 'updated_at']


  def validate_name(self,value):
    if not value.strip():
      raise
    serializers.ValidationError("Name Cannot Be Empty")
    return value.strip()


  def validate_phone_no(self, value):
    cleaned = value.replace("+","").replace("-","").replace(" ","")
    if not cleaned.isdigit():
      raise
    serializers.ValidationError("Phone Number Must Contain Only Valid Digits.")

    if len(cleaned) < 10:
      raise
    serializers.ValidationError("Phone Number Must Contain At Least 10 Digits.")
    return value


  def validate(self,data):
    email = data.get('email', getattr(self.instance,'email', None))
    phone = data.get('phone', getattr(self.instance,'phone', None))

    queryset = Contact.objects.filter(email=email, phone=phone)

    if self.instance:
      queryset = queryset.exclude(id=self.instance.id)

    if queryset.exists():
      raise
    serializers.ValidationError("A Contact With This Email And Phone Number Already Exists.")
    
    return data  