from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import Customer, Product
from django.contrib.auth import authenticate
from rest_framework import generics
from . import serializers


# Create your views here.


# @csrf_exempt
# def customer_register(request):
#     first_name = request.POST.get('first_name')
#     last_name = request.POST.get('last_name')
#     email = request.POST.get('email')
#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     try:
#         # Create a new user
#         user = User.objects.create_user(
#             username=username, email=email, password=password, first_name=first_name, last_name=last_name)
#         if user:
#             try:
#                 customer = Customer.objects.create(user=user)
#                 msg = {
#                     'bool': True,
#                     'user': user.id,
#                     'customer': customer.id,
#                     'msg': 'You have successfully registered.You can now login.'
#                 }
#             except:
#                 msg = {
#                     'bool': False,
#                 }
#         else:
#             msg = {
#                 'bool': False,
#                 'msg': 'Oops! Something went wrong. Please try again later.'
#             }
#     except IntegrityError:
#         msg = {
#             'bool': False,
#         }
#     return JsonResponse(msg)

@csrf_exempt
def customer_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate inputs
        if not username:
            return JsonResponse({'bool': False, 'msg': 'Username is required'})

        try:
            # Create a new user
            user = User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            if user:
                try:
                    customer = Customer.objects.create(user=user)
                    msg = {
                        'bool': True,
                        'user': user.id,
                        'customer': customer.id,
                        'msg': 'You have successfully registered. You can now log in.'
                    }
                except:
                    msg = {
                        'bool': False,
                    }
            else:
                msg = {
                    'bool': False,
                    'msg': 'Oops! Something went wrong. Please try again later.'
                }
        except IntegrityError:
            msg = {
                'bool': False,
                'msg': 'A user with that username already exists.'
            }
    else:
        msg = {
            'bool': False,
            'msg': 'Invalid request method.'
        }
    return JsonResponse(msg)


@csrf_exempt
def customer_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        customer = Customer.objects.get(user=user)
        msg = {
            'bool': True,
            'user': user.username,
            'id': customer.id,
        }
    else:
        msg = {
            'bool': False,
            'msg': 'Invalid username or password'
        }

    return JsonResponse(msg)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()



class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
        


