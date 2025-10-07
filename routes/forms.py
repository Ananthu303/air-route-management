from django import forms
from .models import AirportRoute


class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ["airport_code", "duration"]
        widgets = {
            "airport_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "duration": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class SearchForm(forms.Form):
    start_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Start Airport Code"}
        ),
    )
    n = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Nth Node"}
        ),
    )
    direction = forms.ChoiceField(
        choices=[("left", "Left"), ("right", "Right")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )


class ShortestPathForm(forms.Form):
    start_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Start Airport Code"}
        ),
    )
    end_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "End Airport Code"}
        ),
    )
