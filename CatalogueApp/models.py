from django.db import models
from django.urls import reverse


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='Название')
    width = models.IntegerField(verbose_name='Ширина', null=True)
    height = models.IntegerField(verbose_name='Высота', null=True)
    depth = models.IntegerField(verbose_name='Глубина', null=True)
    countertop_material = models.CharField(max_length=50, verbose_name='Материал столешницы', null=True)
    disposition = models.CharField(max_length=50, verbose_name='Расположение', null=True)
    execution_material = models.CharField(max_length=50, verbose_name='Материал исполнения', null=True)
    purpose = models.CharField(max_length=50, verbose_name='Назначение', null=True)
    date_added = models.DateTimeField(null=True)
    photo_file_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, blank=True, verbose_name='Описание', null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, allow_unicode=True,
                            verbose_name='URL', null=True)

    def __str__(self):
        return self.title

    # 1. такой подход более предпочтительный в случае, когда есть связанные посты по
    # каким-либо индексам
    # 2. СОГЛАСНО КОНВЕНЦИИ, модули джанго используют этот метод в своей работе,
    # если он определен в модели (админка обращается для построения ссылок на модели)
    # 3. переходит по данной юрле, когда через форму добавляем новую запись
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    class Meta:
        ordering = ['id']
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'
        # имеет важное значение для пагинации - в консоли будет алерт об этом
