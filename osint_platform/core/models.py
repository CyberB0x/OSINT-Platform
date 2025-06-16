from django.db import models

class OSINTQuery(models.Model):
    query_type = models.CharField(max_length=50)
    input_data = models.CharField(max_length=255)
    result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.query_type} | {self.input_data}"
