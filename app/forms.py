# from django import forms
# from .models import brand_add
# from django.core.validators import MinValueValidator, MaxValueValidator

# class Brand(forms.ModelForm):
#     class Meta:
#         model = brand_add 
#         fields = ['brand_name','datetime','status']

 
# class MyForm(forms.ModelForm):
#     def clean_brand(self):
#         brand_name=self.cleaned_data['brand_name']

#         if len(brand_name)<1:
#             raise forms.ValidationError()
#         return brand_name
