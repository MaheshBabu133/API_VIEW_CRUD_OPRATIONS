from django.shortcuts import render

# Create your views here.
from app.serializers import *
from app.models import *

from rest_framework.views import APIView
from rest_framework.response import Response

class ProductData(APIView):
    def get(self,request,id):
        pdatas=Product.objects.all()
        psd=ProductMS(pdatas,many=True)
        return Response(psd.data)



    def post(self,request,id):
        psd=ProductMS(data=request.data)
        if psd.is_valid():
            psd.save()
            return Response({"The data is inserted"})
        else:
            return Response({"the data is invalid"})


    def put(self,request,id):
        d=request.data['id']
        po=Product.objects.get(id=d)
        psd=ProductMS(po,data=request.data)
        if psd.is_valid():
            psd.save()
            return Response(('The data is Updated Successfully'))

        else:
            return Response({'message':'The data is invalid'})

    def delete(self,request,id):
        pdo=Product.objects.filter(id=id).delete()
        return Response({"the data is deleted"})

    def patch(self,request,id):
        id=request.data['id']
        po=Product.objects.get(id=id)
        po.pname=request.data['pname']
        po.save()
        return Response({"The data is updated"})
        