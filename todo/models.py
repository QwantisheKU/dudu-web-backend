from django.db import models
from users.models import UserModel

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(
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
    is_done = models.BooleanField(null=True, blank=True)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        null=False
    )

    def __str__(self):
        return self.title

