from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doctor, Patient, MedicalRecord

# def doctor_patients(request):
#     doctor_id = request.GET.get('doctor_id')
#     doctor = get_object_or_404(Doctor, id=doctor_id)
#     patients = doctor.patients.all()
#     medical_records = MedicalRecord.objects.filter(patient__in=patients)
#     context = {'doctor': doctor, 'patients': patients, 'medical_records': medical_records}
#     return render(request, 'doctor_patients.html', context)






class DoctorList(ListView):
    model = Doctor
    template_name = 'myapp/doctor_list.html'
    context_object_name = 'doctors'

class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'myapp/doctor_detail.html'
    context_object_name = 'doctor'

class DoctorCreate(CreateView):
    model = Doctor
    template_name = 'myapp/doctor_form.html'
    fields = ['user', 'specialty', 'medical_license_number', 'patients']

class DoctorUpdate(UpdateView):
    model = Doctor
    template_name = 'myapp/doctor_form.html'
    fields = ['user', 'specialty', 'medical_license_number', 'patients']

class DoctorDelete(DeleteView):
    model = Doctor
    template_name = 'myapp/doctor_confirm_delete.html'
    success_url = reverse_lazy('myapp:doctor_list')

class PatientList(ListView):
    model = Patient
    template_name = 'myapp/patient_list.html'
    context_object_name = 'patients'

class PatientDetail(DetailView):
    model = Patient
    template_name = 'myapp/patient_detail.html'
    context_object_name = 'patient'

class PatientCreate(CreateView):
    model = Patient
    template_name = 'myapp/patient_form.html'
    fields = ['user', 'birth_date', 'address', 'height', 'weight', 'blood_pressure', 'allergies', 'conditions', 'medications']

class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'myapp/patient_form.html'
    fields = ['user', 'birth_date', 'address', 'height', 'weight', 'blood_pressure', 'allergies', 'conditions', 'medications']

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'myapp/patient_confirm_delete.html'
    success_url = reverse_lazy('myapp:patient_list')

class MedicalRecordCreate(CreateView):
    model = MedicalRecord
    template_name = 'myapp/medical_record_form.html'
    fields = ['patient', 'date', 'diagnosis', 'notes', 'prescription']

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.kwargs['patient_pk']
        return initial

class MedicalRecordUpdate(UpdateView):
    model = MedicalRecord
    template_name = 'myapp/medical_record_form.html'
    fields = ['patient', 'date', 'diagnosis', 'notes', 'prescription']

class MedicalRecordDelete(DeleteView):
    model = MedicalRecord
    template_name = 'myapp/medical_record_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('myapp:patient_detail', kwargs={'pk': self.object.patient.pk})
