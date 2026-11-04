from rest_framework import serializers
from exam_app.models import QuestionDb

class QuestionSerializer(serializers.Serializer):
	question = serializers.CharField()
	option_a = serializers.CharField()
	option_b = serializers.CharField()
	option_c = serializers.CharField()
	option_d = serializers.CharField()
	correct_answer = serializers.CharField()

class AnswerSubmissionSerializer(serializers.Serializer):
	student_name = serializers.CharField()
	question = serializers.IntegerField()
	selected_answer = serializers.CharField()
	submitted_date = serializers.DateTimeField(read_only=True)

	def validate(self, validated_data):
		question = validated_data.get("question")
		if not QuestionDb.objects.filter(id=question).exists():
			raise serializers.ValidationError("Question does not exist...!")
		return validated_data