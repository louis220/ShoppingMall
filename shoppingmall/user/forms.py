from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):


    id = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        }, label="아이디", max_length=64)

    username = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        }, label="이름", max_length=64)

    password = forms.CharField(
        error_messages={
            'required': "비밀번호를 입력해주세요."
        }, label="비밀번호",
        widget=forms.PasswordInput
    )
    re_password = forms.CharField(
        error_messages={
            'required': "비밀번호를 입력해주세요."
        }, widget=forms.PasswordInput, label="비밀번호 확인"
    )
    email = forms.EmailField(required=False,
         label="이메일", max_length=64)






    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get('id')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if User.objects.filter(id=id).exists():
            self.add_error('id', '이미 존재하는 아이디 입니다.')

        if password and re_password:
            if password != re_password:
                self.add_error('re_password', '비밀번호가 일치하지 않습니다.')


class LoginForm(forms.Form):
    id = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        }, label="아이디", max_length=64)

    password = forms.CharField(
        error_messages={
            'required': "비밀번호를 입력해주세요."
        }, label="비밀번호",
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get('id')
        password = cleaned_data.get('password')

        if id and password:
            try:
                user = User.objects.get(id=id)
            except User.DoesNotExist:
                self.add_error('id', '존재하지 않는 아이디입니다.')
                return
            if not check_password(password, user.password):
                self.add_error('password', '패스워드가 일치하지 않습니다.')