from rest_framework import viewsets, mixins
from .models import Scheme
from .serializers import SchemeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.multichain_api import api, publish_stream, get_tx_data
from utils import hex_to_json, fetch_next_id, notify
from uuid import uuid4
from common.models import Notification


# Create your views here.

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer


@api_view(['POST'])
def make_response(request):
    # will read notification on hit & get txid
    req_txid = request.data['txid']
    ticket_no = request.data['ticket_no']
    stream = request.data['stream']
    key = request.data['key']
    # get requested data from txid
    req_hex_data = get_tx_data(req_txid)
    req_data = hex_to_json(req_hex_data)
    # TODO: fetch data from db
    res_data = {}
    res_txid = publish_stream(stream,key, res_data, data_format='json')
    notify(Notification, 'dep2', 'dep1', ticket_no, req_txid, stream, key)
