from cProfile import label
import imp
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django import forms

class TodoForm(forms.Form):
    todo = forms.CharField(label="Task",max_length=200)