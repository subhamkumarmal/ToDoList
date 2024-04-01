from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

class UserLogin(View):
    http_method_names = ['post']

    def post(request: HttpResponse, *args: tuple, **kwargs: dict) -> JsonResponse:
        "This method will always create a new user"
        return HttpResponse("Good works!!")

