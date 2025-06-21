from django.db import models


class NotificateBefore(models.IntegerChoices):
    FIVE_MIN = 1, '5 min'
    TEN_MIN = 2, '10 min'
    HIGH = 3, 'Высокий'

class TelegramUser(models.Model):
    user_id = models.TextField()
    username = models.TextField()

    def __str__(self):
        return f"{self.user_id}:{self.username}"

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user_id", "username"], name="unique_user_id_username")]


class Project(models.Model):
    name = models.CharField()
    owner = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, related_name="owned_projects"
    )
    members = models.ManyToManyField(TelegramUser, related_name="projects", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    user = models.ForeignKey(
        TelegramUser, on_delete=models.SET_NULL, null=True, related_name="tags",
    )
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "name"], name="unique_user_id_name")]


class Task(models.Model):
    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )
    compleated_by_user = models.ForeignKey(
        TelegramUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="compleated_by_me"
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True,
    )
    name = models.CharField(max_length=256)
    notificate_before = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    is_important = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} {self.name}"
