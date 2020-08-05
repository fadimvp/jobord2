from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Job
from .serializers import JoSerializer



@api_view(['GET'])
def joblistapi(request):
    all_jobs = Job.objects.all()
    data = JoSerializer(all_jobs,many=True).data
    context ={
        'data':data
    }
    return Response(context)


@api_view(['GET'])
def job_detial_api(request,id):
    job_detial = Job.objects.get(id=id)
    data = JoSerializer(job_detial).data
    context ={
        'data': data

    }
    return Response(context)
