from django.db import models
from users.models import UserModel

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)
    user_id = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        null=False
    )

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    deadline = models.DateTimeField(null=True)
    PRIORITIES = [
        (1, "Низкий"),
        (2, "Средний"),
        (3, "Высокий"),
    ]
    priority = models.IntegerField(choices=PRIORITIES, null=True)
    is_done = models.BooleanField(null=False)
    tag_id = models.OneToOneField(
        Tag,
        on_delete=models.SET_NULL,
        null=True
    )
    user_id = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        null=False
    )

    def __str__(self):
        return self.title

