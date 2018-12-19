from django.db import models

class BaseModel(models.Model):
  id = models.UUIDField(primary_key=True)
  date_changed = models.DateTimeField(auto_now=True)

  class Meta:
        abstract = True


class Quiz(BaseModel):
  owner = models.TextField(max_length=50)
  

class QuizPoint(BaseModel):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_points')
  question = models.CharField(max_length=200)
  right_answere = models.TextField(max_length=30)
  wrong_alternative_1 = models.TextField(max_length=30)
  wrong_alternative_2 = models.TextField(max_length=30)
  wrong_alternative_3 = models.TextField(max_length=30)
  position = models.DecimalField(max_digits=9, decimal_places=6)
  author = models.TextField()
