from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import reportInfo
from .serializers import reportInfoSer
from rest_framework.response import Response
from rest_framework import status


# @csrf_exempt
# def reportList(request):
#
#     if request.method == 'GET':
#         reportInfoV = reportInfo.objects.all()
#         seriallizer = reportInfoSer(reportInfoV, many=True)
#         return JsonResponse(seriallizer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         seriallizer = reportInfoSer(data=data)
#         if seriallizer.is_valid():
#             seriallizer.save()
#             return JsonResponse(seriallizer.data, status=201)
#         return JsonResponse(seriallizer.errors, status=400)
#
#
# @csrf_exempt
# def reportDetail(request, pk):
#     try:
#         reportInfoV = reportInfo.objects.get(pk=pk)
#     except reportInfo.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'get':
#         seriallizer = reportInfoSer(reportInfoV)
#         return JsonResponse(seriallizer.data)

# @api_view(['GET', 'POST'])
# def reportList(request, format=None):
#
#     if request.method == 'GET':
#         reportInfoV = reportInfo.objects.all()
#         seriallizer = reportInfoSer(reportInfoV, many=True)
#         return JsonResponse(seriallizer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         seriallizer = reportInfoSer(data=data)
#         if seriallizer.is_valid():
#             seriallizer.save()
#             return JsonResponse(seriallizer.data, status=201)
#         return JsonResponse(seriallizer.errors, status=400)
#
# @api_view(['GET'])
# def reportDetail(request, pk, format=None):
#     try:
#         reportInfoV = reportInfo.objects.get(pk=pk)
#     except reportInfo.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'get':
#         seriallizer = reportInfoSer(reportInfoV)
#         return JsonResponse(seriallizer.data)

class reportList(APIView):

    def get(self, request, format=None):
        reportInfoV = reportInfo.objects.all()
        serializer = reportInfoSer(reportInfoV, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = reportInfoSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)