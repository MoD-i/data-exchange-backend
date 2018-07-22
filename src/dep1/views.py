from rest_framework import viewsets, mixins
from .models import Scheme
from .serializers import SchemeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.multichain_api import api, publish_stream
from uuid import uuid4

# Create your views here.

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

@api_view(['POST'])
def make_request(request):
    data = request.data
    stream = 'scheme'
    _ticket_no = 1  #TODO: get it from Ticket Model using prefetc_id() 
    _from = 'dep1'
    _to = 'dep2'  #TODO: get it from request.data
    key = f'{_from}-{_to}-{_ticket_no}'
    txid = publish_stream(stream, key, data)
    
    if txid:
        # TODO: define notify()
        notify(_from, _to, _ticket_no, txid, stream, key)
    else:
        pass  # inform user about failure

@api_view(['POST'])
def load_data(request):
    data = request.data


    
