from django import forms


class MoveForm(forms.Form):
    path = forms.CharField()


class RenameForm(forms.Form):
    name = forms.CharField()
