from django import forms
from multiselectfield import MultiSelectFormField
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }

        )
    )


class EnquiryForm(forms.Form):
    Name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    Email=forms.EmailField(
        label="Enter Your Emil",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
    Mobile=forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    Gender_Choices=(
        ('F','Female'),
        ('M','Male')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect,choices=Gender_Choices
    )
    COURSES_CHOICES = (
        ('PY', "Python"),
        ('DJ', "Django"),
        ('RA', "Rest-Api"),
        ('FL', "Flask"),
        ('UI', "Ui")
    )
    courses=MultiSelectFormField(choices=COURSES_CHOICES)

    # SHIFTS_CHOICES = (
    #     ('Morinung', 'Morning Shift'),
    #     ('AfterNoon', 'AfternoonShift'),
    #     ('Evening', 'Evening Shift'),
    #     ('Night', 'Night Shift')
    # )
    # shifts=MultiSelectFormField(choices=SHIFTS_CHOICES)


