from django.shortcuts import render, redirect, get_object_or_404
from .models import Devices
from django.contrib import messages
from .forms import DevicesForm
from django.http import JsonResponse
from django.db.models import Q

# Views homepage.
def homepage(request):
    return render(request, "homepage/index.html")

# Views about
def about(request):
    return render(request, "homepage/about.html")

# Views rent
def rent(request):
    return render(request, "homepage/rent.html")

# READ Device
def device_index(request):
    query = request.GET.get('q')
    devices = Devices.objects.all()
    if query:
        devices = Devices.objects.filter(
            Q(noDevice__icontains=query) |
            Q(namaDevice__icontains=query) |
            Q(fasilitas__icontains=query) |
            Q(bonus__icontains=query) |
            Q(tanggalMasuk__icontains=query)
        )
    else:
        devices = Devices.objects.all()
    return render(request, 'device/index.html', {'devices': devices, 'query':query})

# Create Device
def device_create(request):
    if request.method == 'POST':
        form = DevicesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Devices berhasil ditambahkan!')
            return redirect('device_index') 
    else:
        form = DevicesForm()

    return render(request, 'device/create.html', {'form': form})

# UPDATE Device
def device_update(request, device_id):
    device = get_object_or_404(Devices, id=device_id)
    if request.method == 'POST':
        form = DevicesForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Device Berhasil Diubah!')
            return redirect('device_index')
    else:
        form = DevicesForm(instance=device)
    return render(request, 'device/update.html', {'form': form, 'device': device})

# DELETE Device
def device_delete(request, device_id):
    device = get_object_or_404(Devices, id=device_id)
    device.delete()
    messages.success(request, 'Data Device berhasil dihapus')
    return JsonResponse({'success': True})



