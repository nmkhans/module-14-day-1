from django.shortcuts import render
from .forms import PracticeForm

# Create your views here.
def home(req):
  form = PracticeForm()
  return render(req, 'forms_practice/index.html', {'form': form})