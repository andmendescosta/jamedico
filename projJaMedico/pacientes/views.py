from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm


def pacientes_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente.html', {'pacientes': pacientes})


def pacientes_new(request):
    form = PacienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(pacientes_list)
    return render(request, 'pacientes_form.html', {'form': form})


def pacientes_update(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect(pacientes_list)
    return render(request, 'pacientes_form.html', {'form': form})


def pacientes_delete(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)

    if request.method == 'POST':
        paciente.delete()
        return redirect(pacientes_list)

    return render(request, 'paciente_delete_confirm.html', {'paciente': paciente})
