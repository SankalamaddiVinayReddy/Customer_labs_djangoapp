# webhook_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from destinations.models import Destination
import request

@api_view(['POST'])
def incoming_data(request):
    token = request.headers.get('CL-X-TOKEN')
    if not token:
        return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        account = Account.objects.get(app_secret_token=token)
    except Account.DoesNotExist:
        return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    for destination in account.destinations.all():
        if destination.http_method.upper() == 'GET':
            response = requests.get(destination.url, params=data, headers=destination.headers)
        elif destination.http_method.upper() == 'POST':
            response = requests.post(destination.url, json=data, headers=destination.headers)
        elif destination.http_method.upper() == 'PUT':
            response = requests.put(destination.url, json=data, headers=destination.headers)

    return Response({"message": "Data sent to all destinations"}, status=status.HTTP_200_OK)

