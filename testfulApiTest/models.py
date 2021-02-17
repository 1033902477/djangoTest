from django.db import models

# Create your models here.

# 报告基本信息主表
class reportInfo(models.Model):

    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    test_plan_id = models.IntegerField()
    report_name = models.CharField(max_length=255)
    report_dir = models.CharField(max_length=255)
    period = models.BigIntegerField(max_length=8)
    create_time = models.DateTimeField(auto_now_add=True)

# 如何将bool值的false处理成为0

    class Meta:
        db_table = 'ui_autotest_report'
