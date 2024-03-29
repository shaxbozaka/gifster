from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from .utils import fb2cal


class FriendsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = self.request.data.get('username')
        pwd = self.request.data.get('pwd')
        response = fb2cal.get_Friends(username, pwd)
        return Response(response, status=response['status'])

