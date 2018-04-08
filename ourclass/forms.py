#encoding:utf-8

from django import forms

class SearchForm(forms.Form):
    nameform= forms.CharField(widget=forms.TextInput,error_messages={'user_name':'用户名不能为空'})