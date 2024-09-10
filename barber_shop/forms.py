from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'mobile', 'time', 'branches', 'date', 'number_of_people', 'comment']
        widgets = {
            'time': forms.TimeInput(format='%H:%M'),
            'date': forms.DateInput(format='%d.%m.%Y'),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
