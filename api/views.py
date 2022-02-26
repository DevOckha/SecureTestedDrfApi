from webbrowser import get
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from business.models import Customer
from api.serializers import CustomerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class CustomerView(APIView):
    permission_classes = (IsAuthenticated, )


    def get(self, request, format=None):
        customers = Customer.published.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomerDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk, format=None):
        customer = get_object_or_404(Customer, status='published', pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        customer = get_object_or_404(Customer, status='published', pk=pk)
        serializer = CustomerSerializer(customer, request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        customer = get_object_or_404(Customer, status='published', pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)