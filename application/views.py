from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django_daraja.mpesa.core import MpesaClient
from .serializer import (StudentSerializer, CourseSerializer)
from django.contrib import messages
from .models import Student, Course
from .forms import StudentForm, CourseForm




# Index page
def index(request):
    return render(request, 'index.html')


# About page - combines student and course management



# Contact page - handles student form submission
def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors in the student form.')
    else:
        form = StudentForm()

    return render(request, 'contact.html', {'form': form})


# Edit student details
def edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('about')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit.html', {'form': form, 'student': student})


# Delete student
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    try:
        student.delete()
        messages.success(request, 'Student deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting student: {e}')
    return redirect('about')


# API for students
@api_view(['GET', 'POST'])
def studentsapi(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API for courses
@api_view(['GET', 'POST'])
def coursesapi(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Mpesa API Integration
def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0703684505'
    amount = 1
    account_reference = 'eMobilis'
    transaction_cost = 'Payment for Web Dev'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = client.stk_push(phone_number, amount, account_reference, transaction_cost, callback_url)
    return HttpResponse(response)


# def about(request):
#     data = Student.objects.all()
#     return render(request, 'about.html', {'students': students})


#
# def about(request):
#     students = Student.objects.all()
#     courses = Course.objects.all()
#     course_form = CourseForm()  # Assuming you're using forms
#     return render(request, 'about.html', {
#         'students': students,
#         'courses': courses,
#         'course_form': course_form,
#     })
#



def about(request):
    # Handle Course Form Submission
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid():
            course_form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('about')  # Redirect to refresh the page and clear the form
        else:
            messages.error(request, 'Please correct the errors in the course form.')
    else:
        course_form = CourseForm()

    # Fetch all Students and Courses to display on the About page
    students = Student.objects.all()
    courses = Course.objects.all()

    context = {
        'students': students,
        'courses': courses,
        'course_form': course_form,  # Include the course form in the context
    }

    return render(request, 'about.html', context)


def edit_course(request, id):
        course = get_object_or_404(Course, id=id)
        if request.method == 'POST':
            form = CourseForm(request.POST, instance=course)
            if form.is_valid():
                form.save()
                messages.success(request, 'Course updated successfully!')
                return redirect('about')
            else:
                messages.error(request, 'Please correct the errors in the course form.')
        else:
            form = CourseForm(instance=course)

        return render(request, 'change.html', {'form': form, 'course': course})


def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    try:
        course.delete()
        messages.success(request, 'Course deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting course: {e}')
    return redirect('about')