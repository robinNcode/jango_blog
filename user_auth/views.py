from rest_framework.views import APIView
from rest_framework.response import Response

# user_auth serializer
from user_auth.serializer import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'User added successfully'})
            else:
                return Response({'status': 'failed', 'message': serializer.errors})

        except Exception as e:
            return Response({'status': 'failed', 'message': str(e)})
