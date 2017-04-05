from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import StrictButton

from captcha.fields import ReCaptchaField

from ombudsman.models import ApiKeyGrant

class ApiKeyGrantForm(ModelForm):
    captcha =  ReCaptchaField(attrs={
                    'theme' : 'clean',
                })
    def __init__(self, *args, **kwargs):
        super(ApiKeyGrantForm, self).__init__(*args, **kwargs)
        self.fields['captcha'].label = False
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            Field('email'),
            Field('app_url'),
            Field('captcha')
        )
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_tag = True
        self.helper.form_method = 'post'
        self.helper.form_action = ''

    class Meta:
        model = ApiKeyGrant
        fields = ['name', 'email', 'app_url']
