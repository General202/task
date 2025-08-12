from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Треба зробити'),
        ('in_progress', 'В процесі'),
        ('complited', 'Готово!'),
    ]
    PRIORITY_CHOISCES = [
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    ]
    title = models.CharField(max_length=100, verbose_name='Назва завдання:')
    description = models.TextField(null=True, blank=True, verbose_name='Опис завдання:')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус завдання:')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOISCES, default='medium', verbose_name='Пріоритет завдання:')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Термін виконання завдання:')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення завдання:')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created', verbose_name='Створено користувачем:')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено:')

    def __str__(self):
        return f"{self.title}"
    


