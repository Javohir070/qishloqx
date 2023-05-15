from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Province,Pump,SubProvince
from .forms import PumpForm
from django.http import JsonResponse,HttpResponse,HttpResponseBadRequest
from django.views import View
from django.views.generic.list import ListView
from django.db.models import Q
from django.db.models import Sum



def create_pump(request):
    form = PumpForm()
    if request.method == 'POST':
        forms = PumpForm(request.POST,request.FILES)
        post = request.POST
        data = {
            "province": post.get("province", ""),
            "image": post.get("image", ""),
            "subprovince": post.get("subprovince", ""),
            "name": post.get("name", ""),
            "info": post.get("info", ""),
            # "umumiy_mal": post.get("umumiy_mal", ""),
            # "oy_mal": post.get("oy_mal", ""),
            # "kun_mal": post.get("kun_mal", ""),
            # "soat_mal": post.get("soat_mal", ""),

        }
        if forms.is_valid():
            forms.save(**data)
            return redirect('index')
        else:
            print(forms.errors)
    ctx = {
        'form':form
    }
    return render(request,'malumotbir.html',ctx)


def index(request):
   
    return render(request,'index.html')

def userbr(request):
   
    return render(request,'userbr.html')
def hisobotlar(request):

    return render(request,'hisobotlar.html')


def semantik(request):
    qs = Province.objects.all()
    return render(request,'semantic.html',{'qs':qs})


def get_province(request):
    qs_val = list(Province.objects.values())
    return JsonResponse({'data':qs_val})


def get__subprovince(request,*args, **kwargs):
    selected_subprovince = kwargs.get('subprovince')
    obj_models = list(SubProvince.objects.filter(sub_name=selected_subprovince).values())
    return JsonResponse({'data':obj_models})

class GetProvince(View):
    def get(self,request,*args, **kwargs):
        print(request.GET)
        province = SubProvince.objects.values('province').distinct()        
        ctx = {
            'province':province,
        }
        return render(request,'malumotbir.html',ctx)


class GetSubprovince(View):
    def get(self,request,province,*args, **kwargs):
        if request.is_ajax():
            province = SubProvince.objects.filter(province=province).values('id','title')
            return JsonResponse({'data':list(province)})
        return HttpResponse('hgdhscvhvdsw')
        
        
def users(request):
    print(request.GET.get('q'))
    if request.GET.get("q",None): 
        word=request.GET.get('q')   
        pumps = Pump.objects.filter(Q(name__icontains=word))
    else:
        pumps = Pump.objects.all()
        
    return render(request,'user.html',{'pumps':pumps})


def getsubprovince(request,pk):
    subprovince = SubProvince.objects.filter(pk=pk)
    print('ishladi')
    return JsonResponse({'data':list(subprovince)})





def district_list(request):
    if request.is_ajax():
        province_id = request.GET.get('province_id')
        districts = Province.objects.filter(province_id=province_id)
        list_data = [{'id': district.pk, 'name': district.title} for district in districts]
        return JsonResponse(list_data, safe=False)
    else:
        return HttpResponseBadRequest()








def pump_edit(request,pk):
    pump = Pump.objects.get(pk=pk)
    print("sdcsdvdfvbfvkvdkv",pump)
    form = PumpForm(instance=pump)
    if request.method == 'POST':
        forms = PumpForm(request.POST,request.FILES ,instance=pump)
        post = request.POST
        data = {
            "province": post.get("province", ""),
            "subprovince": post.get("subprovince", ""),
            "name": post.get("name", ""),
            "info": post.get("info", ""),
            "budget":post.get("budget",""),
            "image": post.get("image", ""),
            "phone": post.get("phone", ""),

            
        }
        if forms.is_valid():
            forms.save(**data)
            return redirect('index')
        else:
            print(forms.errors)
    ctx = {
        'form':form
    }
    return render(request,'malumotbir.html',ctx)



def pump_delete(request,pk):
    news = Pump.objects.get(pk=pk)
    
    ctx = {
        'pump':news
    }
    return render(request,'delete.html',ctx)
        
def pump_del(request,pk):
    pump = Pump.objects.get(pk=pk)
    pump.delete()
    return redirect('users')
    
    
def loud(request):
    return render(request,'auth/logout.html')



def tuman(request):
    if request.method == 'POST':
        subpro = request.POST['subprovince']
        tuman = SubProvince.objects.get(title=subpro)
        
    tuman = SubProvince.objects.all()
    ctx = {
        'tuman':tuman
    }
    return render(request,'tuman.html',ctx)






class NewsList(ListView):
    model = Pump
    context_object_name = 'pump'
    template_name = 'user.html'
    extra_context = {
        'title':'maqolalar royhati '
    }

    
class SearchResult(NewsList):
    def get_queryset(self):
        print(self.request.GET,'ghhgfhgfjg')
        word = self.request.GET.get("q")        
        news = Pump.objects.filter(Q(name__icontains=word))
        print(news)
        return news


def manitoringvil(request):
    if request.method =='POST':
        vil=request.POST.get('province')
        info = Pump.objects.filter(province__title=vil)
        ctx = {
           'info':info
        }
        if info:
            return render(request,'manitoringvil.html',ctx)
    return render(request,'manitoringvil.html')




def manitoringtuman(request):
    if request.method =='POST':
        subp=request.POST.get('subprovince')
        info = Pump.objects.filter(subprovince__title=subp)
        # umumiysumma = 0
        # oysumma = 0
        # kunsumma = 0
        # soatsumma = 0
        #
        # for i in info:
        #     umumiysumma += i.yil_mal
        #     oysumma += i.oy_mal
        #     kunsumma += i.kun_mal
        #     soatsumma += i.soat_mal
        ctx = {
           'info':info,
           # 'umumiysumma': yilsumma,
           # 'oysumma': oysumma,
           # 'kunsumma': kunsumma,
           # 'soatsumma': soatsumma
        }
        if info:
            return render(request,'manitoringtuman.html',ctx)
        if not info:
              return render(request,'manitoringtuman.html',{'error':True})
         

            
    return render(request,'manitoringtuman.html')


