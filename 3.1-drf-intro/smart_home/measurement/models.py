from django.db import models

class Sensor(models.Model):
    name = models.Charfield(max_lenght=50, verbose_name = 'датчик')
    description = models.CharField(max_length=80, verbose_name='описание')


    class Meta:
        ordering = ['-id']

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата')

    class Meta:
        ordering = ['-created_at']





