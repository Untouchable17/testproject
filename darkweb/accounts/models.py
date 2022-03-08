from django.db import models


class Blog(models.Model):
    """ Модель блога """

    title = models.CharField(max_length=255, verbose_name="Пост")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title} - {self.created}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
