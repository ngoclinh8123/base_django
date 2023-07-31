from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class HomeView(APIView):
    def get(self, request):
        return Response("okkkk", 200)

    def post(self, request):
        print(request)
        print("-----------------")
        print(vars(request))
        return Response("post okkkkkk", 200)
