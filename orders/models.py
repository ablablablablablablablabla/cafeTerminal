from django.db import models
import json

class Order(models.Model):
    table_number = models.IntegerField()
    items = models.JSONField(encoder=json.JSONEncoder, decoder=json.JSONDecoder)  # Список блюд с ценами
    status = models.CharField(max_length=20, default="В ожидании")

    def calculate_total_price(self):
        return sum(item['price'] for item in self.items)

    @property
    def total_price(self):
        return self.calculate_total_price()

    def save(self, *args, **kwargs):
        # Автоматически исправляем кодировку при сохранении
        if self.items and any(r'\u' in str(item['name']) for item in self.items):
            # Декодируем экранированные последовательности
            self.items = json.loads(json.dumps(self.items).encode('utf-8').decode('unicode_escape'))
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Заказ #{self.id} (Стол: {self.table_number})"