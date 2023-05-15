from django import forms
from django.forms import ModelForm
from .models import *

class PumpForm(ModelForm):
    class Meta:
        model = Pump
        exclude = ['province', 'subprovince']
        
    def save(self, *args, **kwags):
        print("\n\n", kwags, "\n\n")

        province = kwags.pop('province')        
        subprovince = kwags.pop('subprovince')
        print("sss", subprovince)

        pro = Province.objects.filter(title=province).first()        
        subpro = SubProvince.objects.filter(title=subprovince).first()
        
        print("a", province, "b", subpro)

        instance = self.Meta.model(**kwags)
        instance.province = pro
        instance.subprovince = subpro
        instance.save()

        return instance

         
        
        
class UserForm(forms.ModelForm):
    password2 = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','email','phone','password','password2')
   
        
    # def save(self, *args, **kwags):
    #     province = kwags.get('province')        
    #     subprovince = kwags.get('subprovince')

    #     pro = Province.objects.filter(title=province).first()        
    #     subpro = SubProvince.objects.filter(title=subprovince).first()

    #     instance = self.Meta.model(**kwags)
    #     instance.province = pro
    #     instance.subprovince = subpro
        
    #     instance.save()

    #     return instance