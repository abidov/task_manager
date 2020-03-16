from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=255, null=False)
    date_of_creation = models.DateField(null=True, blank=True)
    task = models.ManyToManyField('Task', related_name='tags', blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})

class Task(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    date_of_creation = models.DateField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='tasks', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})