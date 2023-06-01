from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def page_main(request: HttpRequest):
    return HttpResponse("Store Page")


def page_login(request: HttpRequest):
    return HttpResponse("Log In page")
