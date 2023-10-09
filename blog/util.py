from ctypes.wintypes import HINSTANCE
from rest_framework import status
from rest_framework.response import Response
from django.forms.models import model_to_dict


def getAllInstances(model, serializerClass):
    instances = model.objects.all()
    serializer = serializerClass(instances, many=True)
    myData = serializer.data
    return Response(myData)


def getSingleInstance(model, serializerClass, pk):
    try:
        instance = model.objects.get(id=pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    myData = serializerClass(instance).data
    return Response(myData)


def createInstance(model, serializerClass, data):
    serializer = serializerClass(data=data)
    instance = model(**data)
    instance.save()
    return Response(data=serializer.initial_data, status=status.HTTP_201_CREATED)


def updateInstance(model, serializerClass, pk, data):
    if model.objects.filter(id=pk).exists():
        instanceBerofeUpdate = model.objects.get(id=pk)
        serializer = serializerClass(instanceBerofeUpdate, data=data)
        if serializer.is_valid():
            model.objects.filter(id=pk).update(**data)
            return Response(model_to_dict(model.objects.get(id=pk)))
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def deleteInstance(model, serializerClass, pk):
    try:
        instance = model.objects.get(id=pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
