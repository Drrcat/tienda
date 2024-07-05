from django import forms
from django.forms import ModelForm, Form, Textarea, FileInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Perfil





# *********************************************************************************************************#
#                                                                                                          #
# INSTRUCCIONES PARA EL ALUMNO, PUEDES SEGUIR EL VIDEO TUTORIAL, COMPLETAR EL CODIGO E INCORPORAR EL TUYO: #
#                                                                                                          #
# https://drive.google.com/drive/folders/1ObwMnpKmCXVbq3SMwJKlSRE0PCn0buk8?usp=drive_link                  #
#                                                                                                          #
# *********************************************************************************************************#

# PARA LA PAGINA MANTENEDOR DE PRODUCTOS:
# Crea ProductoForm como una clase que hereda de ModelForm
# asocialo con el modelo Producto
# muestra todos los campos
# crea 2 widgets para:
#   - la descripción del producto como TextArea
#   - el botón de cargar imagen como FileInput y 
#     escóndelo para reemplazarlo por otro acorde 
#     con tu diseño gráfico
# renombra las siguientes etiquetas para que ocupen menos
# espacio en la página: 'Nombre', 'Subscriptor(%)' y 'Oferta(%)'

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'imagen': forms.FileInput(attrs={'style': 'display:none;'}),
        }
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'descuento_subscriptor': 'Subscriptor (%)',
            'descuento_oferta': 'Oferta (%)',
        }
class BodegaForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    nombre_producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label='Nombre del Producto')
    cantidad = forms.IntegerField(label='Cantidad')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_producto'].queryset = Producto.objects.all()

    class Meta:
        fields = '__all__'

class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Cuenta")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
        }

class RegistroPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'direccion', 'subscrito', 'imagen']
        exclude = ['tipo_usuario']
        widgets = {
            'direccion': Textarea(),
            'imagen': FileInput(),
        }

class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': 'E-mail',
        }

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['tipo_usuario', 'rut', 'direccion', 'subscrito', 'imagen']
        widgets = {
            'direccion': forms.Textarea(),
            'imagen': forms.FileInput(),
        }







