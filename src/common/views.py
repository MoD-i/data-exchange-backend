from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from utils.multichain_api_toran import api, get_tx_data
from utils import hex_to_json, hex_to_char
import json


# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(methods=['GET'], detail=False)
    def get_by_dep(self, request, dep):
        """
        Returns all notification for particular dep.
        """

        noti = Notification.objects.filter(to__iexact=dep)
        page = self.paginate_queryset(noti)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(noti, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# @action(methods=['GET'], detail=False, url_path='^dep/(?P<dep>[a-zA-Z0-9]+)', url_name='get-by-dep')
# def get_by_dep(self, request, dep):
#     """
#     Returns all notification for particular dep.
#     """
# 
#     noti = Notification.objects.filter(to__iexact=dep)
#     page = self.paginate_queryset(noti)
#     if page is not None:
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)
# 
#     serializer = self.get_serializer(noti, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_tx_data(request):
    """
    JSON Needed:
        1. txid

    E.g.:
        {"txid": "hgjsyher6ygfdg"}
    """
    txid = request.data['txid']
    try:

        # req_hex_data = get_tx_data(txid)
        req_hex_data = api.gettxoutdata(txid,0) # TODO
    except:
        return Response(status=status.HTTP_403_FORBIDDEN, data={'status': 'failure',
            'message': 'Request Unsuccessful. Error while connecting with blockchain node'})
    try:
        # get requested data from txid
        req_json_data = hex_to_json(req_hex_data) # TODO: this is LIST
        return Response(data=req_json_data, status=status.HTTP_202_ACCEPTED)
    except Exception as  e:
        return Response(data={"status":"failure", "message": "Something Wrong Occurred."
            # ,"exception":e
            }, 
            status=status.HTTP_403_FORBIDDEN)
