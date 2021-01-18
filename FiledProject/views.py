from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .payments_logic import Payment


con = Payment()

class ProcessPayment(APIView):
    """
    Process Payment
    """

    def post(self, request):
        """
        Process Payment
        :param request:
        :return:
        """
        data = request.data
        response_data = con. \
            process_payment(data)
        if response_data.get('code') == 200:
            status_code = status.HTTP_200_OK
        elif response_data.get('code') == 400:
            status_code = status.HTTP_400_BAD_REQUEST
        elif response_data.get('code') == 500:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(response_data, status=status_code)
