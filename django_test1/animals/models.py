from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

class AnimalModel(models.Model):
    class Meta:
        db_table = 'animals'
    name = models.CharField(max_length=20, validators=[RegexValidator('^([a-zA-Z]{1,20})$', 'only a-z A-Z')])
    ANIMAL_TYPES = [
        (1, 'dog'),
        (2, 'cat'),
        (3, 'bird')
    ]
    animal_types = models.IntegerField(choices=ANIMAL_TYPES)
    user = models.ForeignKey(User, related_name='animals', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
