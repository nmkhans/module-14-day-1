from django import forms
import datetime
class PracticeForm(forms.Form):
  #? char, email, number, decimal, date, boolean fields
  name = forms.CharField()

  address = forms.CharField(widget = forms.Textarea())
  comment = forms.CharField(widget = forms.Textarea(attrs = {
    'rows': 3,
  }))

  email = forms.EmailField()

  phone = forms.IntegerField()

  agree = forms.BooleanField(label='agree with terms and condirion')

  date = forms.DateField(initial= datetime.date.today)
  birth_date = forms.DateField(widget = forms.NumberInput(attrs = {'type': 'date'}))

  value = forms.DecimalField(required =  False)

  message = forms.CharField(max_length=10)

  first_name = forms.CharField(initial='jhon doe')

  #? select, radio, checkbox field

  #: select field
  food_choices = [
    ('burger', 'Burger'),
    ('pizza', 'Pizza'),
    ('pasta', 'Pasta')
  ]

  food = forms.ChoiceField(choices=food_choices)

  #: radio field

  color_choice = [
    ('blue', 'Blue'),
    ('red', "Red"),
    ('green', 'Green')
  ]

  color = forms.ChoiceField(widget=forms.RadioSelect(), choices=color_choice)

  #: multiple choice field

  subject_choice = [
    ('bangla', "Bangla"),
    ('english', 'English'),
    ('science', 'Science'),
    ('math', 'Math')
  ]

  subject = forms.MultipleChoiceField(choices=subject_choice)

  #: multiple choice with check box
  language_choice = [
    ('javascript', 'Javascript'),
    ('python','Python'),
    ('c', 'C'),
    ('cpp', 'Cpp')
  ]

  language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=language_choice)