"""Models for the period tracker app."""
from django.db import models
from django.contrib.auth.models import User

# Models.


class Cycle(models.Model):
    """Cycle model for a user."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Period(models.Model):
    """Period model for a user."""

    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Ovulation(models.Model):
    """Ovulation model for a user."""

    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    date = models.DateField()


class Pregnancy(models.Model):
    """Pregnancy model for a user."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)


class NutritionEntry(models.Model):
    """Daily nutrition entry for a user."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    nutrients = models.JSONField


class FitnessEntry(models.Model):
    """Daily fitness entry for a user."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    # steps = models.PositiveIntegerField()
    # calories = models.PositiveIntegerField()
    # distance = models.PositiveIntegerField()
    active_minutes = models.PositiveIntegerField()
    activity_type = models.CharField(max_length=100)


class SexEducation(models.Model):
    """Daily sec education entry for a user."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


class PeriodEducation(models.Model):
    """Daily period education entry for a user."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


class PregnancyEducation(models.Model):
    """Daily pregnancy education entry for a pregnant user."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


class OvulationEducation(models.Model):
    """Daily ovulation education entry for ovulating user."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
