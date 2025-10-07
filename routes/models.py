from django.db import models


class AirportRoute(models.Model):
    airport_code = models.CharField(max_length=10, unique=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    duration = models.FloatField()
    next_node = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="previous_node",
    )

    def __str__(self):
        return f"{self.airport_code} (Pos: {self.position})"
