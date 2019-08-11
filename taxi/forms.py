from django import forms
from taxi.models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('number_for_invite', 'user_number_for_invite', 'name', 'surname', 'lastname', 'phone')
