from django.shortcuts import render
from .forms import ReservationForm
# Create your views here.

def home_page(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            # Обработка данных формы
            pass
    else:
        form = ReservationForm()
    return render(request, 'index.html', {'form': form})