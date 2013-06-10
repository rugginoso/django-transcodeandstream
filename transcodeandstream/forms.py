from django import forms


class MoveForm(forms.Form):
    path = forms.CharField(required=False)


class RenameForm(forms.Form):
    name = forms.CharField()


class DeleteForm(forms.Form):
	pass
