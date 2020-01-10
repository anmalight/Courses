from django import forms

sex_choices = (
    ('M', 'male'),
    ('F', 'female'),
    ('O', 'other'),
)

eng_lvl = (
    ('A1', 'No knowledge of English'),
    ('A2', 'Elementary level of English'),
    ('B1', 'Low intermediate level of English'),
    ('B2', 'High intermediate level of English'),
    ('C1', 'Advanced level of English'),
    ('C2', 'Proficient in English'),
)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=5)
    your_sex = forms.ChoiceField(choices=sex_choices)
    your_age = forms.IntegerField(min_value=0)
    your_eng_lvl = forms.ChoiceField(choices=eng_lvl)


class LoginForm(forms.Form):
    username = forms.CharField(label='uname')
    password = forms.CharField(label='pass')