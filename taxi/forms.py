import re
from django import forms
from django.contrib.auth import get_user_model
from taxi.models import Car, Driver


class DriverCreationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "license_number",
        )
        widgets = {
            "password": forms.PasswordInput(),
        }

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of 8 characters."
            )
        if (
            not license_number[:3].isupper()
            or not license_number[:3].isalpha()
        ):
            raise forms.ValidationError(
                "First 3 characters must be uppercase letters."
            )
        if not license_number[3:].isdigit():
            raise forms.ValidationError("Last 5 characters must be digits.")
        return license_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of 8 characters."
            )
        if (
            not license_number[:3].isupper()
            or not license_number[:3].isalpha()
        ):
            raise forms.ValidationError(
                "First 3 characters must be uppercase letters."
            )
        if not license_number[3:].isdigit():
            raise forms.ValidationError("Last 5 characters must be digits.")
        return license_number


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"


from django.contrib.auth.forms import UserCreationForm
from django import forms
from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "license_number",
        )

    def clean_license_number(self) -> str:
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of 8 characters."
            )
        if (
            not license_number[:3].isupper()
            or not license_number[:3].isalpha()
        ):
            raise forms.ValidationError(
                "First 3 characters must be uppercase letters."
            )
        if not license_number[3:].isdigit():
            raise forms.ValidationError("Last 5 characters must be digits.")
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self) -> str:
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of 8 characters."
            )
        if (
            not license_number[:3].isupper()
            or not license_number[:3].isalpha()
        ):
            raise forms.ValidationError(
                "First 3 characters must be uppercase letters."
            )
        if not license_number[3:].isdigit():
            raise forms.ValidationError("Last 5 characters must be digits.")
        return license_number
