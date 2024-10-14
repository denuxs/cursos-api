from .models import Survey, Question, Answer
from .serializers import SurveySerializer, SurveyDetailSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return SurveySerializer
        return SurveyDetailSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        questions = data.pop("questions")

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            evaluation = serializer.save()

            for question in questions:
                answers = question.pop("answers")

                item = {}
                item["question"] = question["question"]
                item["question_type"] = question["question_type"]
                item["survey"] = evaluation

                question = Question.objects.create(**item)

                for answer in answers:
                    obj = {}
                    obj["answer"] = answer["answer"]
                    obj["question"] = question

                    Answer.objects.create(**obj)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = request.data.copy()
        questions = data.pop("questions")

        evaluation = self.get_object()
        serializer = self.get_serializer(evaluation, data=data)
        if serializer.is_valid():
            evaluation = serializer.save()

            for question in questions:
                question_id = question["id"]
                answers = question.pop("answers")

                item = {}
                item["question"] = question["question"]
                item["question_type"] = question["question_type"]
                item["survey"] = evaluation

                if question_id:
                    q = Question.objects.get(pk=question_id)

                    q.question = item["question"]
                    q.question_type = item["question_type"]
                    q.save()
                else:
                    q = Question.objects.create(**item)
                    
                for answer in answers:
                    answer_id = answer["id"]
                    
                    obj = {}
                    obj["answer"] = answer["answer"]
                    obj["question"] = q

                    if answer_id:
                        a = Answer.objects.get(pk=answer_id)

                        a.answer = obj["answer"]
                        a.save()
                    else:                        
                        Answer.objects.create(**obj)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
