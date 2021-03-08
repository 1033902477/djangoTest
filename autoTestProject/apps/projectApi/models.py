from django.db import models


# 接口API表
class projectApiInfo(models.Model):

    id = models.IntegerField(primary_key=True)
    expect = models.CharField(max_length=512)
    type = models.IntegerField()
    last_actual = models.CharField(max_length=512)
    name = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'projectApi'
