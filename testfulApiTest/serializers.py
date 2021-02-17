from rest_framework import serializers
from testfulApiTest.models import reportInfo

class reportInfoSer(serializers.ModelSerializer):

    class Meta:
        model = reportInfo
        fields = '__all__'