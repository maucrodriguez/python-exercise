from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class CommaSeparatedNumbersField(forms.Field):
    default_error_messages = {
        "invalid": "Enter comma separated numbers only.",
    }

    def __init__(self, *args, **kwargs):
        super(CommaSeparatedNumbersField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return []

        try:
            return [int(item.strip()) for item in value.split(",") if item.strip()]
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages["invalid"])

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value


class SevenPairsForm(forms.Form):
    values = CommaSeparatedNumbersField(label="Comma separated numbers")

