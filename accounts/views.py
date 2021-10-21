from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.forms import UserRegForm, RegistrationForm
from accounts.models import Course


def home(request):
    return render(request, 'accounts/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    form = UserRegForm()

    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)


def register(request):
    if request.is_ajax():
        semester_no = request.POST.get('semester_no', None)
        courses = Course.objects.filter(semester_no=semester_no)
        courses_list = []
        for course in courses:
            courses_list.append({
                'course_no': course.course_no,
                'course_title': course.course_title,
                'credit': course.credit,
            })
        return JsonResponse({'courses_list': courses_list})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.student = request.user.student
            registration.save()
            return redirect(reverse_lazy('registration_list'))
    
    args = {'form': RegistrationForm()}
    return render(request, 'accounts/registration.html', args)
    


def registration_list(request):
    return render(request, 'accounts/registration_list.html', {})
