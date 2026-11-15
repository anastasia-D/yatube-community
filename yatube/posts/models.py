from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

SHORTENED_NAME = 20


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True, verbose_name='ссылка')
    description = models.TextField(verbose_name='описание')

    def __str__(self) -> str:
        return (
            self.title[:SHORTENED_NAME] + '...'
            if len(self.title) > SHORTENED_NAME
            else self.title
        )


class Post(models.Model):
    text = models.TextField(verbose_name='текст поста')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='группа',
    )

    class Meta:
        ordering = ('-pub_date',)
        default_related_name = 'posts'

    def __str__(self) -> str:
        return (
            self.text[:SHORTENED_NAME] + '...'
            if len(self.text) > SHORTENED_NAME
            else self.text
        )
