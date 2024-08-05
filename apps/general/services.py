from django.db.models import TextField
from django.forms import CharField


def normalize_text(obj):
    for field in obj._meta.get_fields():
        if isinstance(field, (CharField, TextField)):
            obj_field = getattr(obj, field.name)
            if isinstance(obj_field, str) and obj_field is not None:
                setattr(obj, field.name, ' '.join(obj_field.split()))
