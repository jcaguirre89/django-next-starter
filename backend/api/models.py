from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class MyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_name_set')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    field_1 = models.PositiveSmallIntegerField(blank=True, null=True, default=5)
    field_2 = models.CharField(max_length=200, blank=True)
    field_3 = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering=('created',)
        get_latest_by = ('created', )

    def __str__(self):
        username = getattr(self.user, self.user.USERNAME_FIELD)
        return f'Model entry for {username}'

    @property
    def some_property(self):
        """ Some example property calculated from the fields """
        return self.field_1 * 5

