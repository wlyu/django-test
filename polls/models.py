from django.db import models


class BatchRecord(models.Model):
    # version.uuid
    version_uuid = models.CharField( max_length=50)
    #
    todo_type = models.CharField(max_length=50)
    # 批次序号
    batch_seq = models.IntegerField()
    # 批次uuid
    batch_uuid = models.CharField(primary_key=True,max_length=50)
    # 批次总数
    batch_total_seq = models.IntegerField()
    # 回调结果
    batch_back_status = models.CharField(max_length=50)
    create_at = models.DateTimeField(null=True, blank=True, verbose_name="创建时间")
    update_at = models.DateTimeField(null=True, blank=True, verbose_name="修改时间")

    class Meta:
        db_table = "batch_record"
        verbose_name = "批次回调记录"
