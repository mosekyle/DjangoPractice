from django import forms

from application.models import Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'admission': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your admission number'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your course'}),
            'image' : forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'title' : 'Upload image here'})
        }



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter course description', 'rows': 4}),
            'credits': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter credits'}),

        }
