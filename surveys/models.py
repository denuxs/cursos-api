from django.db import models
from courses.models import Course

class Survey(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="questions", null=True
    )

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


QUESTION_TYPE = [
    ("simple", "Simple"),
    ("multiple", "Multiple"),
]


class Question(models.Model):
    question = models.CharField(max_length=140)
    question_type = models.CharField(max_length=140, choices=QUESTION_TYPE)
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="questions"
    )

    def __str__(self):
        return self.question

    # class Meta:
    #     ordering = ["-id"]


class Answer(models.Model):
    answer = models.CharField(max_length=140)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return self.answer

    # class Meta:
    #     ordering = ["-id"]
