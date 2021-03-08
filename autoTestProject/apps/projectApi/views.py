from django.http import JsonResponse
from rest_framework.views import APIView
from utils import comparion
from utils import time
from db.project.data import getApiExpect, updateApiRestul
from .models import projectApiInfo
import json


class ComparisonApi(APIView):

    def post(self, request):

        body = json.loads(str(request.body.decode()))
        self.actual = body['actual']
        self.expect = getApiExpect(name=body['apiName'])
        try:
            result = comparion.valueCheck(actualValues=self.actual, expectValues=eval(self.expect))
            c = updateApiRestul(lastActual=str(self.actual), createTime=time.currentTime(), status=result, apiName=body['apiName'])
            print(c)
            data = projectApiInfo.objects.get(name=body['apiName'])
            return JsonResponse(data={'name': data.name, 'status': data.status}, safe=False)
        except Exception as e:
            return JsonResponse(data=str(e), status=400)
