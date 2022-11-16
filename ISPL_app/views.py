from rest_framework.views import APIView
import json
from rest_framework.response import Response
# Create your views here.


class All_infoAPIView(APIView):
    def get (self, request, format = None):
        file = open("ISPL_data.json","r")
        x = file.read()
        reference_data = json.loads(x)
        return Response(reference_data)