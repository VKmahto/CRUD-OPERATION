# from django.shortcuts import render,redirect
# from .models import brand_add


# def base(request):
#     return render(request, 'app/base.html', {})

# def brand(request):
#     if request.method == 'POST':
#         print('Data Added')

#         brand_name = request.POST.get('brand_name')
#         brand_date = request.POST.get('brand_date')
#         brand_status = request.POST.get('brand_status')
#         print(brand_name)

#         brand = brand_add()
#         brand_name=brand_name
#         brand_date=brand_date
#         brand_status=brand_status
#         brand.save()

#         return redirect('base')  # Redirect to the base view after saving data

#     return render(request, 'app/brand_add.html', {})
from django.shortcuts import render, redirect
from .models import brand_add, supplier


def base(request):
    brands=brand_add.objects.all()
    return render(request, 'app/base.html' ,{'brands':brands})

def brand(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name')
        brand_date = request.POST.get('brand_date')
        brand_status = request.POST.get('brand_status')

        brand = brand_add(brand_name=brand_name, datetime=brand_date, status=brand_status)
        brand.save()

        return redirect('base.html')  # Redirect to the base view after saving data

    return render(request, 'app/brand_add.html', {})

def fetch_data(request):
    brands = brand_add.objects.all()  # Fetch all records from the brand_add table
    return render(request, 'app/brand_data.html', {'brands': brands})


#for suppllier table

def basesupplier(request):
    suppliers=supplier.objects.all()
    return render(request,'app/basesupplier.html',{'supplier':suppliers})

def add_supplier(request):
    if request.method =="POST":
        supplier_name=request.POST.get('supplier_name')
        mobile_no=request.POST.get('mobile_no')
        address=request.POST.get('address')
        datetime=request.POST.get('datetime')
        status=request.POST.get('status')
        supp=supplier(supplier_name=supplier_name,mobile_no=mobile_no,address=address,datetime=datetime,status=status)
        supp.save()
        return redirect('basesupplier.html')
    return render(request,'app/insertsupplier.html',{} )