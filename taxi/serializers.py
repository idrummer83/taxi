from rest_framework import serializers
from taxi.models import Driver


class TaxidriverList(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name')


class Taxidriver(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
