from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Exercice(models.Model):
    name = models.CharField(max_length=255, default="exercice")
    description = models.TextField(default="description")
    
    def __str__(self):
        return self.name

class Session(models.Model):
    session_name = models.CharField(max_length=255, default="myNewSession")
    creation_date = models.DateTimeField(default=timezone.now())
    exercices = models.ManyToManyField(Exercice, through='SessionExercice')
    
    def __str__(self):
        return f"Session created at {self.creation_date}"

class SessionExercice(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(100)])
    
    def __str__(self):
        return f"{self.session} - {self.exercice} ({self.repetitions} reps)"


#class Exercice(models.Model):
#    exercice_name = models.CharField(max_length=210)
#    creation_date = models.DateTimeField("date of creation")
#
#    def __str__(self):
#        return self.exercice_name
#
#class Session(models.Model):
#    session_name = models.CharField(max_length=210)
#    exercices    = models.Fo
#    position     = models.IntegerField()
#    exercice     = models.ForeignKey(Exercice, on_delete=models.CASCADE)
#    reps         = models.IntegerField()
#
#    def __str__(self):
#        return self.session_name