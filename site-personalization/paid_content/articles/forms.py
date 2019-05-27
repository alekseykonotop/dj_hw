from django import forms

# Надо проверить - возможно этот класс вообще не нужен
class SubscribeProfileForm(forms.ModelForm):

    class Meta(object):
        model = Profile
        exclude = ('id', )