from rest_framework import viewsets, mixins, status
from .models import Scheme, Ticket
from .serializers import SchemeSerializer, TicketSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from utils.multichain_api import api, publish_stream, get_tx_data
from utils import hex_to_json,  notify
from uuid import uuid4
from common.models import Notification
import json
# Create your views here.

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    
    # @action(methods=['POST'], detail=False, url_path='^request/', url_name='submit-request')
    # def make_request(self, request):
    #     """
    #     Requests other department to fetch data.

    #     JSON needed with:
    #         1. department
    #         2. aadhar
    #     """
    #     data = request.data
    #     stream = 'scheme'
    #     ticket_no = fetch_next_id('dep1_ticket')
    #     frm = 'dep1'
    #     to = 'dep2'  # request.data['department']
    #     key = f'{frm}-{to}-{ticket_no}'
    #     data_to_publish = request.data['aadhar']  #TODO: get it from request.data
    #     txid = publish_stream(stream, key, data_to_publish, data_format='json')
    #     
    #     if txid:
    #         notify(Notification, frm, to, ticket_no, txid, stream, key)
    #     else:
    #         pass  # inform user about failure



@api_view(['POST'])
def make_request(request):
    """
    JSON needed with:
        1. department
        2. aadhar(list of JSON objects)
    E.g.:
        {
            "department": "dep2",
            "aadhar": [{"aadhar": "12345677"}, {"aadhar":"52345234"}]
        }
    """
    data = request.data
    stream = 'scheme'
    # ticket_no =  fetch_next_id('dep1_ticket')
    frm = 'dep1'
    to = 'dep2'  # request.data['department']
    # key = f'{frm}-{to}-{ticket_no}'
    data_to_publish = request.data['aadhar']  #TODO: get it from request.data
    try:
        txid = publish_stream(stream, key, data_to_publish, data_format='json')
    except:
        return Response(status=status.HTTP_403_FORBIDDEN, data={'status': 'failure',
            'message': 'Request Unsuccessful. Error while connecting with blockchain node'})
    try: 
        if txid:
            # record ticket number in dep. ticket table
            ticket  = Ticket.objects.create(txid=txid, status='O', frm=frm, to=to) 
            ticket.save()
            key = f'{frm}-{to}-{ticket.id}'

            
            # record notification in Nootification table
            notify(Notification, frm, to, ticket.id, txid, stream, key)

            return Response(status=status.HTTP_201_CREATED, data={'status': 'success',
                'message': 'Request Sent Successfully.'})

        else:
            pass  # inform user about failure
        return Response(status=status.HTTP_403_FORBIDDEN, data={'status': 'failure',
            'message': 'Request Unsuccessful. Error while publishing data to the blockchain'})
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'status': 'failure',
            'message': 'Request Unsuccessful. Something unusual occurred.'})


@api_view(['POST'])
def load_data(request):
    """
    JSON needed with:
        1. txid
    """
    txid = request.data[txid]
    try:
        tx_data = get_tx_data(txid)
    except:
        return Response(status=status.HTTP_403_FORBIDDEN, data={'status': 'failure',
            'message': 'Request Unsuccessful. Error while connecting with blockchain node'})
    json_data = hex_to_json(tx_data)
    datum = json.loads(str(json_data))
    try:

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
        return Response(status=status.HTTP_201_CREATED, data={'status': 'success', 'message': 'Data Loaded Successfully.'})
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, datat={'status': 'failure',
            'message': 'Data Loading Unsuccessful. Something unusual occurred.'})



class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
