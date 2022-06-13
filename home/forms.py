from django import forms
from .models import Todo


class NewTodoForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField()


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title' ,'body' ,'created')

