from django.shortcuts import render,redirect
from .forms import VehicleForm, ServiceForm,VehicleSearchForm,UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Vehicle,Service,UserProfile
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.db.models import Sum
from django.shortcuts import get_object_or_404

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('vehicle_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'services/add_vehicle.html', {'form': form})

def add_service(request, vehicle_id):
    vehicle = vehicle.objects.get(pk=vehicle_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.vehicle = vehicle
            service.save()
            return redirect('service_list', vehicle_id=vehicle_id)
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form, 'vehicle': vehicle})


def dashboard(request):
    user_vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, 'services/dashboard.html', {'user_vehicles': user_vehicles})


def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('dashboard')
    else:
        form = VehicleForm()
    return render(request, 'services/add_vehicle.html', {'form': form})




def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'services/edit_vehicle.html', {'form': form, 'vehicle': vehicle})


def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('dashboard')
    return render(request, 'services/delete_vehicle.html', {'vehicle': vehicle})


def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, vehicle__user=request.user)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list', vehicle_id=service.vehicle.id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/edit_service.html', {'form': form, 'service': service})


def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, vehicle__user=request.user)
    if request.method == 'POST':
        vehicle_id = service.vehicle.id
        service.delete()
        return redirect('service_list', vehicle_id=vehicle_id)
    return render(request, 'services/delete_service.html', {'service': service})


def generate_report(request):
    services = Service.objects.filter(vehicle__user=request.user)
    template_path = 'services/report_template.html'
    context = {'services': services}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="service_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, vehicle__user=request.user)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list', vehicle_id=service.vehicle.id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/edit_service.html', {'form': form, 'service': service})


def generate_report(request):
    user_vehicles = Vehicle.objects.filter(user=request.user)
    template_path = 'services/report_template.html'
    context = {'user_vehicles': user_vehicles}
    
    for vehicle in user_vehicles:
        total_expense = Service.objects.filter(vehicle=vehicle).aggregate(Sum('expense'))['expense__sum']
        vehicle.total_expense = total_expense
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="service_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def dashboard(request):
    user_vehicles = Vehicle.objects.filter(user=request.user)
    search_form = VehicleSearchForm(request.GET or None)
    
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    profile_form = UserProfileForm(request.POST or None, instance=user_profile)
    
    if request.method == 'POST' and profile_form.is_valid():
        profile_form.save()
        return redirect('dashboard')
    
    if request.GET and search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        user_vehicles = user_vehicles.filter(make__icontains=search_query) | user_vehicles.filter(model__icontains=search_query)
    
    context = {
        'user_vehicles': user_vehicles,
        'search_form': search_form,
        'profile_form': profile_form,
    }
    
    return render(request, 'services/dashboard.html', context)

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, vehicle__user=request.user)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list', vehicle_id=service.vehicle.id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/edit_service.html', {'form': form, 'service': service})
