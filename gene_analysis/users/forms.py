from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput
from django import forms


class LoginForm(AuthenticationForm):
    def init(self, *args, **kwargs):
        super(LoginForm, self).init(*args, **kwargs)

        self.fields['username'].widget = forms.widgets.TextInput(attrs={
            'placeholder': 'Your Email address'
        })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
            'placeholder': 'Your password'
        })


class UserRegisterForm(forms.Form):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    username = forms.CharField(widget=TextInput(
        attrs={
            'required': True,
            'placeholder': 'Your Username'
        }
    ))
    email = forms.EmailField(widget=TextInput(
        attrs={
            'required': True,
            'placeholder': 'Your Email Address'
        }
    ))
    first_name = forms.CharField(widget=TextInput(
        attrs={
            'required': True,
            'placeholder': 'Your First Name'
        }
    ))
    last_name = forms.CharField(widget=TextInput(
        attrs={
            'required': True,
            'placeholder': 'Your Last Name'
        }
    ))
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={
                                    'required': True,
                                    'placeholder': 'Your password'
                                }))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(attrs={
                                    'required': True,
                                    'placeholder': 'Password confirmation'
                                }),
                                help_text="Enter the same password as above, for verification.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        try:
            password_validation.validate_password(password2)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password2
