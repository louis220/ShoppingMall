from django import forms
from .models import Product

class RegisterForm(forms.Form):


    title = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        }, label="상품명", max_length=64)

    price = forms.IntegerField(
        error_messages={
            'required': '가격을 입력해주세요.'
        }, label="가격")

    discount = forms.IntegerField(
        error_messages={
            'required': "할인율을 입력해주세요."
        }, label="할인율")

    description = forms.CharField(widget=forms.Textarea,
        error_messages={
            'required': "제품설명을 입력해주세요."
        }, label="설명")



    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        price = cleaned_data.get('price')
        discount = cleaned_data.get('discount')
        description = cleaned_data.get('description')
        if Product.objects.filter(title=title).exists():
            self.add_error('title', '이미 존재하는 상품 입니다.')