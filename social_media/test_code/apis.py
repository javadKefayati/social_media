from rest_framework.views import APIView
from rest_framework.response import Response
from social_media.api.mixins import ApiAuthMixin



class GetTestApi(ApiAuthMixin,APIView):
    
    def get(self,request):
        return Response({"okay":1})