from django import forms
from .models import Periodista


class PeriodistaForm(forms.ModelForm):
    class Meta:
        model = Periodista
        fields = ['codigo', 'nombre', 'rango', 'imagen']
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'rango': 'Rango',
            'imagen': 'Imagen'
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese codigo..',
                    'id': 'codigo',
                    'class': 'form-control mb-3',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre..',
                    'id': 'nombre',
                    'class': 'form-control mb-3',
                }
            ),
            'rango': forms.Select(
                attrs={
                    'placeholder': 'Ingrese su rango..',
                    'id': 'rango',
                    'class': 'form-control mb-3',
                }, choices=[
                    ("alto", "Alto"),
                    ("medio", "Medio"),
                    ("bajo", "Bajo"),
                ]
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control mb-3',
                    'id': 'imagen',
                }
            )
        }


class PeriodistaForm2(forms.ModelForm):
    class Meta:
        model = Periodista
        fields = ['codigo', 'nombre', 'rango', 'imagen']
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'rango': 'Rango',
            'imagen': 'Imagen'
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese codigo..',
                    'id': 'codigo',
                    'class': 'form-control mb-3',
                    'readonly': True,

                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre..',
                    'id': 'nombre',
                    'class': 'form-control mb-3',
                }
            ),
            'rango': forms.Select(
                attrs={
                    'placeholder': 'Ingrese su rango..',
                    'id': 'rango',
                    'class': 'form-control mb-3',
                }, choices=[
                    ("alto", "Alto"),
                    ("medio", "Medio"),
                    ("bajo", "Bajo"),
                ]
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control mb-3',
                    'id': 'imagen',
                }
            )
        }
