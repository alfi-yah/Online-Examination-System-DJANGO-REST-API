from django.db import models

# Create your models here.

class QuestionDb(models.Model):
	question = models.CharField(max_length=100)
	option_a = models.CharField(max_length=100)
	option_b = models.CharField(max_length=100)
	option_c = models.CharField(max_length=100)
	option_d = models.CharField(max_length=100)
	correct_answer = models.CharField(max_length=100)

class AnswerSubmissionDb(models.Model):
	student_name = models.CharField(max_length=100)
	# question = models.IntegerField()
	question = models.IntegerField()
	selected_answer = models.CharField(max_length=100)
	submitted_date = models.DateTimeField(auto_now_add=True)