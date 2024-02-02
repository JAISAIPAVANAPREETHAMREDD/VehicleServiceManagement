from django import forms
from .models import Vehicle, Service

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'year')

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service_date', 'description')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service_date', 'description', 'expense')


class VehicleSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search')



from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'contact_number')

from django import forms
class VehicleSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service_date', 'description', 'expense', 'reminder_date')
