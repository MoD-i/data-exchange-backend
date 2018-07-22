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
def make_request(request):
    """
    JSON needed with:
        1. department
        2. aadhar
    """
    data = request.data
    stream = 'scheme'
    ticket_no = fetch_next_id('dep1_ticket')
    frm = 'dep1'
    to = 'dep2'  # request.data['department']
    key = f'{frm}-{to}-{ticket_no}'
    data_to_publish = request.data['aadhar']  #TODO: get it from request.data
    txid = publish_stream(stream, key, data_to_publish, data_format='json')
    
    if txid:
        notify(Notification, frm, to, ticket_no, txid, stream, key)
    else:
        pass  # inform user about failure


@api_view(['POST'])
def load_data(request):
    """
    JSON needed with:
        1. txid
    """
    txid = request.data[txid]
    tx_data = get_tx_data(txid)
    json_data = hex_to_json(tx_data)
    datum = json.loads(str(json_data))
    if isinstance(datum, list):
        for d in datum:
            aadhar = d["aadhar_number"]
            count = Scheme.objects.filter(aadhar_number=aadhar).count()
            if count > 0:
                obj = Scheme.objects.get(aadhar)
                obj.beneficiary_name = d["beneficiary_name"]
                obj.address = d["address"]
                obj.gender = d["gender"]
                obj.member_age = d["member_age"]
                obj.dist_name = d["dist_name"]
                obj.scheme_name = d["scheme_name"]
                obj.save()
    else:
        aadhar = datum["aadhar_number"]
        count = Scheme.objects.filter(aadhar_number=aadhar).count()
        if count > 0:
            obj = Scheme.objects.get(aadhar)
            obj.beneficiary_name = d["beneficiary_name"]
            obj.address = d["address"]
            obj.gender = d["gender"]
            obj.member_age = d["member_age"]
            obj.dist_name = d["dist_name"]
            obj.scheme_name = d["scheme_name"]
            obj.save()


