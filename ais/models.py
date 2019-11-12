from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Task(models.Model):
    TYPE_CHOICES = (
        (0, u'Обычная задача'),
        (1, u'Срочная задача'),
        (2, u'Важная задача!'),
        (3, u'Другое'),
    )
    STATUS_CHOICES = (
        (0, u'Не Активно'),
        (1, u'Активно'),
        (2, u'В прогрессе'),
        (3, u'Завершено'),
        (4, u'Просрочено'),
    )
    task_date = models.DateField(verbose_name='Дата', auto_now_add=True)
    type = models.PositiveIntegerField(choices=TYPE_CHOICES, verbose_name='Тип задачи', default=0)
    task = models.CharField(max_length=200, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст', blank=True)
    file = models.FileField(upload_to='task_files', blank=True)
    status = models.PositiveIntegerField(verbose_name='Статус', choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class TaskFiles(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задача', on_delete=models.CASCADE)
    file = models.FileField(verbose_name='Файл', upload_to='task_files')

    class Meta:
        verbose_name = 'Файлы'
        verbose_name_plural = 'Файлы'


class Advantage(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задача', on_delete=models.CASCADE)
    username = models.CharField(verbose_name='Имя', max_length=255, default='user')
    name = models.CharField(verbose_name='Название', max_length=255)
    about = models.TextField(verbose_name='Про достижение',)
    start_date = models.DateField(verbose_name='Начала времени',default=timezone.now)
    end_date = models.DateField(verbose_name='Конец времени',default=timezone.now)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижение'


class Feedback(models.Model):
    advantage = models.ForeignKey(Advantage, verbose_name='Достижение', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Юзер', on_delete=models.DO_NOTHING)
    username = models.CharField(verbose_name='Имя пользователя', max_length=255)
    feedback = models.TextField(verbose_name='Отзыв',)
    created_at = models.DateField(verbose_name='Создан', default=timezone.now)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
