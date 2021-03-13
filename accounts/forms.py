from django.contrib.auth.models import User
from django import forms


# 모델이 있고 그에 대한 자료를 입력받고 싶을 때 사용
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    # Meta 클래스를 이용해 기존에 있는 모델의 입력 폼을 쉽게 만들 수 있음
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # 특별한 유효성 검사나 조작을 하고 싶을 때 만들어서 사용
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password not matched!')
        return cd['password2']
