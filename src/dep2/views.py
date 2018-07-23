from rest_framework import viewsets, mixins, status
from .models import Scheme
from .serializers import SchemeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.multichain_api import api, publish_stream, get_tx_data
from utils import hex_to_json, fetch_next_id, notify, jsonify
from uuid import uuid4
from common.models import Notification
import json

# Create your views here.

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer


@api_view(['POST'])
def make_response(request):
    """
    JSON needed with:
        1. txid
        2. ticket_no
        3. stream
        4. key
    """
    # will read notification on hit & get txid
    req_txid = request.data['txid']
    ticket_no = request.data['ticket_no']
    stream = request.data['stream']
    key = request.data['key']
    # get requested data from txid
    try:
        req_hex_data = get_tx_data(req_txid)
    except:
        return Response(status=status.HTTP_403_FORBIDDEN, data={'status': 'failure',
            'message': 'Request Unsuccessful. Error while connecting with blockchain node'})
    req_json_data = hex_to_json(req_hex_data)
    #datum = json.loads(str(req_json_data))
    datum = req_json_data
    try:

        if isinstance(datum, list):
            obj_list = []
            for d in datum:
                aadhar = d["aadhar"]
                count = Scheme.objects.filter(aadhar_number=aadhar).count()
                if count > 0:
                    obj = Scheme.objects.get(aadhar_number=aadhar)
                    d["aadhar_number"] = aadhar
                    d["beneficiary_name"] =  obj.beneficiary_name
                    d["address"] = obj.address 
                    d["gender"] =  obj.gender 
                    d["member_age"] =  obj.member_age 
                    d["dist_name"] = obj.dist_name  
                    d["scheme_name"] = obj.scheme_name  
                    obj_list.append(d)
                    res_json_data = jsonify(obj_list)
        else:
            aadhar = datum["aadhar"]
            count = Scheme.objects.filter(aadhar_number=aadhar).count()
            if count > 0:
                obj = Scheme.objects.get(aadhar_number=aadhar)
                d = dict()
                d["aadhar_number"] = aadhar
                d["beneficiary_name"] =  obj.beneficiary_name
                d["address"] = obj.address 
                d["gender"] =  obj.gender 
                d["member_age"] =  obj.member_age 
                d["dist_name"] = obj.dist_name  
                d["scheme_name"] = obj.scheme_name  
                res_json_data = jsonify(d)

        res_data = res_json_data
        res_txid = publish_stream(stream,key, res_data, data_format='json')
        notify(Notification, 'dep2', 'dep1', ticket_no, res_txid, stream, key)
        return Response(status=status.HTTP_201_CREATED, data={'status': 'success', 'message': 'Response Sent Successfully.'})
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'status': 'failure',
            'message': 'Response Unsuccessful. Something unusual occurred.'})

