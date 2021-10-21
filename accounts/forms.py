from django.contrib.auth.forms import UserCreationForm
from django import forms


from accounts.models import Student, Registration, SEMESTER_NO


class UserRegForm(UserCreationForm):
    first_name = forms.CharField(label='First name',)
    last_name = forms.CharField(label='Last name')
    roll_no = forms.CharField(label='Roll No.')
    registration_no = forms.CharField(label='Reg No.', widget=forms.NumberInput())
    session = forms.CharField(label='Session')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')

    def save(self, commit=True):
        user = super().save(commit)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            Student.objects.create(**{
            'user': user,
            'roll_no': self.cleaned_data['roll_no'],
            'registration_no': self.cleaned_data['registration_no'],
            'session': self.cleaned_data['session'],
            })


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('semester_no',)
        


    
