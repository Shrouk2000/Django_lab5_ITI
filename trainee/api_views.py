from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trainee
from .serializers import TraineeSerializer

@api_view(['POST'])
def create_trainee(request):
    serializer = TraineeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_trainee(request, pk):
    try:
        trainee = Trainee.objects.get(pk=pk)
    except Trainee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TraineeSerializer(trainee)
    return Response(serializer.data)

@api_view(['PUT'])
def update_trainee(request, pk):
    try:
        trainee = Trainee.objects.get(pk=pk)
    except Trainee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TraineeSerializer(trainee, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_trainee(request, pk):
    try:
        trainee = Trainee.objects.get(pk=pk)
    except Trainee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    trainee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
