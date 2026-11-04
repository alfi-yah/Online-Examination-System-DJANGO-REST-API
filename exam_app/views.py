from django.shortcuts import render, get_object_or_404
from exam_app.models import QuestionDb , AnswerSubmissionDb
from exam_app.serializers import QuestionSerializer, AnswerSubmissionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class QuestionListCreateView(APIView):
	def get(self, request):
		qs = QuestionDb.objects.all()
		serializer_instance = QuestionSerializer(qs, many=True)
		return Response(serializer_instance.data)

	def post(self, request):
		form_data = request.data   										
		serializer_instance = QuestionSerializer(data=form_data)  		
		if serializer_instance.is_valid():    							
			actual_data = serializer_instance.validated_data  			
			QuestionDb.objects.create(**actual_data)   					
			return Response(data=serializer_instance.data)  			
		else:
			return Response(data=serializer_instance.errors)

class QuestionRetriveUpdateDeleteView(APIView):
	def get(self, request, pk):        					
		# qs = QuestionDb.objects.get(id=pk)
		qs = get_object_or_404(QuestionDb, id=pk)				
		serializer_instance = QuestionSerializer(qs) 	
		return Response(data=serializer_instance.data) 	

	def put(self, request, pk):   									
		form_data = request.data  
		serializer_instance = QuestionSerializer(data=form_data) 	
		if serializer_instance.is_valid():   						
			actual_data = serializer_instance.validated_data

			#modelname.objects.filter(id).update(filed=value)
			QuestionDb.objects.filter(id=pk).update(**actual_data) 	
			return Response(data=serializer_instance.data)			
		else:
			return Response(data=serializer_instance.errors)		

	def delete(self, request, pk):   											
		QuestionDb.objects.filter(id=pk).delete() 								
		return Response(data={"message" : "Question deleted successfully..!"}) 	


class AnswerSubmissionListCreateView(APIView):
	def get(self, request):
		qs = AnswerSubmissionDb.objects.all()
		serializer_instance = AnswerSubmissionSerializer(qs, many=True)
		return Response(data=serializer_instance.data)

	def post(self, request):
		form_data = request.data
		serializer_instance = AnswerSubmissionSerializer(data=form_data)
		if serializer_instance.is_valid():
			actual_data = serializer_instance.validated_data
			AnswerSubmissionDb.objects.create(**actual_data)
			return Response(data=serializer_instance.data)
		else:
			return Response(data=serializer_instance.errors)

class AnswerSubmissionRetriveUpdateDeleteView(APIView):
	def get(self, request, pk):        					
		# qs = QuestionDb.objects.get(id=pk)
		qs = get_object_or_404(AnswerSubmissionDb, id=pk)				
		serializer_instance = AnswerSubmissionSerializer(qs) 	
		return Response(data=serializer_instance.data) 	

	def put(self, request, pk):   									
		form_data = request.data  
		serializer_instance = AnswerSubmissionSerializer(data=form_data) 	
		if serializer_instance.is_valid():   						
			actual_data = serializer_instance.validated_data

			#modelname.objects.filter(id).update(filed=value)
			AnswerSubmissionDb.objects.filter(id=pk).update(**actual_data) 	
			return Response(data=serializer_instance.data)			
		else:
			return Response(data=serializer_instance.errors)		

	def delete(self, request, pk):   											
		AnswerSubmissionDb.objects.filter(id=pk).delete() 								
		return Response(data={"message" : "Answer deleted successfully..!"}) 	
