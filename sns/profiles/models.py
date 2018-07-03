from django.db import models
from users.models import User
from djeet.models import Djeet


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    likes = models.ManyToManyField(Djeet, related_name="liked_by", symmetrical=False)

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

