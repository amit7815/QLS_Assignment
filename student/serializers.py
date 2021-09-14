from rest_framework import serializers
from .models import Student,Address

class AddressSerializer(serializers.Serializer):
    address_id = serializers.IntegerField(source = "id",read_only=True)
    city = serializers.CharField(max_length=50)
    landmark = serializers.CharField(max_length = 50)
    postal_address = serializers.CharField(max_length = 225)


class StudentSerializer(serializers.Serializer):
    student_id = serializers.IntegerField(source = 'id',read_only =True)
    student_name = serializers.CharField(max_length= 50)
    standard = serializers.IntegerField()
    address = AddressSerializer()

    def create(self,validated_data):
        address_dict = validated_data.get('address')
        address = Address.objects.create(**address_dict)
        validated_data['address'] = address
        return Student.objects.create(**validated_data)


