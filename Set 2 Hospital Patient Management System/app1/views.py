from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm

def patient_list(request):
 patients = Patient.objects.all()
 return render(request, 'patient_list.html', {'patients': patients})

def patient_create(request):
 form = PatientForm(request.POST or None)
 if form.is_valid():
    form.save()
    return redirect('patient_list')
 return render(request, 'patient_form.html', {'form': form})

def patient_update(request, id):
 patient = get_object_or_404(Patient, id=id)
 form = PatientForm(request.POST or None, instance=patient)
 if form.is_valid():
    form.save()
    return redirect('patient_list')
 return render(request, 'patient_form.html', {'form': form}) 

def patient_delete(request, id):
 patient = get_object_or_404(Patient, id=id)
 patient.delete()
 return redirect('patient_list')
