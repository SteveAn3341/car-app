from django import forms
from .models import Brand
from .models import Car

class BrandForm(forms.ModelForm):
     class Meta:
        model = Brand
        fields = ['name', 'img_url']


class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra', False)
        super(CarForm, self).__init__(*args, **kwargs)

        if extra:
            self.fields['year'] = forms.IntegerField(required=True)
            self.fields['color'] = forms.CharField(max_length=100, required=True)
            self.fields['model'] = forms.CharField(max_length=100, required=True)
            self.fields['brand_name'] = forms.ModelChoiceField(queryset=Brand.objects.all(), required=True)

    class Meta:
        model = Car
        fields = ['name', 'img_url']
        


        