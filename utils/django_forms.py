from django.core.exceptions import ValidationError
import re

def senhaForte(password):
    expressao = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not expressao.match(password):
        raise ValidationError((
            'A senha deve ter ao menos uma letra maiúscula',
            'ao menos uma letra minúscula e um número. Também é necessário'
            'que tenha ao menos 8 caracteres...'
        ),
        code='Invalid')