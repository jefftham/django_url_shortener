from django import forms
from .models import Url_table


class UrlForm(forms.Form):
    full = forms.URLField(label='Full URL', required=True, widget=forms.TextInput(attrs={'placeholder': 'http://yourUrl.com'}))
    short = forms.CharField(max_length=8, label='Customize URL', required=False, )

    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['full'].widget.attrs.update({'class': 'form-control'})
        self.fields['short'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        super(UrlForm, self).clean()
        if '' != self.cleaned_data['short']:
            # short url is not empty
            qs = Url_table.objects.filter(short__iexact=self.cleaned_data['short'])
            if qs.exists():
                # if the full url is not same in db
                print(qs[0].full)
                if qs[0].full != self.cleaned_data['full']:
                    raise forms.ValidationError("short code is not unique!")

        return self.cleaned_data

