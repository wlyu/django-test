import uuid

from django.http import HttpResponse

# Create your views here.
from django.utils.timezone import now
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import BatchRecord
from .tasks import add

class TmpAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchRecord
        fields = '__all__'

class TestView(APIView):
    def get(self, request,uuid=None):
        cards = BatchRecord.objects.all()
        serializer = TmpAPISerializer(cards, many=True)
        return Response(serializer.data)


def update(request):
    version_uuid = '234'
    batch_back_status = 'FAILURE'
    update_at = now()
    BatchRecord.objects \
        .filter(batch_uuid=version_uuid) \
        .update(batch_uuid=version_uuid,
                batch_back_status=batch_back_status,
                update_at=update_at)
    return HttpResponse("update ok")


def hello(request):
    uuidList = []
    objList = []
    batch_total = 10
    todo_type = "123---"
    for i in range(batch_total):
        version_uuid = uuid.uuid4()
        version_uuid = version_uuid
        todo_type = todo_type
        batch_seq = i + 1
        batch_uuid = uuid.uuid4()
        batch_total_seq = batch_total
        batch_back_status = 'INIT'
        create_at = now()
        update_at = now()
        b = BatchRecord(version_uuid=version_uuid,
                        todo_type=todo_type,
                        batch_seq=batch_seq,
                        batch_uuid=batch_uuid,
                        batch_total_seq=batch_total_seq,
                        batch_back_status=batch_back_status,
                        create_at=create_at,
                        update_at=update_at)
        uuidList.append(batch_uuid)
        objList.append(b)
    BatchRecord.objects.bulk_create(objList)
    return HttpResponse("Hello, world. You're at the polls index.")


def task(request):
    mul_result = add.delay(4, 4)
    json_data = {"message": "ok", "errorCode": 0, "data": {}}
    return HttpResponse(json_data)


def list(request):
    version_uuid = '20210901111444'
    todo_type = 'DBupdate'
    uuid_list = ['167d0e33-8573-4e68-8d1a-5087ddedcf14', '345', '456']
    qs = BatchRecord.objects.filter(version_uuid=version_uuid,
                                    todo_type=todo_type,
                                    batch_uuid__in=uuid_list)
    for book in qs:
        print(book)
    return HttpResponse(qs)
