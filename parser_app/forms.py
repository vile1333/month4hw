from django import forms
from . import models,parser_litres

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('litres', 'litres'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type'
        ]
    def parser_data(self):
        if self.data['media_type'] == 'litres':
            litres_file = parser_litres.parsing()
            for i in litres_file:
                models.LitresModel.objects.create(**i)