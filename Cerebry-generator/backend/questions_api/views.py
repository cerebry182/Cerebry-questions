from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# Create your views here.
from rest_framework import viewsets

from rest_framework.views import APIView

from .serializers import QuestionSerializer
from .models import Question


# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = Question.objects.all().order_by('ct_name')
#     serializer_class = QuestionSerializer


# class QuestionViewSet(APIView):
#     def get(self,request):
#         questions = Question.objects.all().order_by('ct_name')
#         serializer = QuestionSerializer(questions,many=True)
#         return Response(serializer.data)


class QuestionViewSet(APIView):

    # def get(self,request):
    #     questions = Question.objects.all().order_by('ct_name')
    #     serializer = QuestionSerializer(questions, many=True)
    #     return Response(serializer.data)

    def get(self,request,ct_name):
        print("ct_name is : ",type(ct_name))
        question = Question.objects.get(ct_name=ct_name)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
