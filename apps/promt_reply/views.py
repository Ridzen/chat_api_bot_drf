from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import ChatRequestSerializer, ChatResponseSerializer
import openai

class ChatAPIView(APIView):

    @swagger_auto_schema(
        request_body=ChatRequestSerializer,
        responses={
            200: ChatResponseSerializer(),
            400: 'Bad Request'
        }
    )
    def post(self, request):
        openai.api_key = ''
        serializer = ChatRequestSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data.get("prompt")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            output = response['choices'][0]['message']['content']
            response_serializer = ChatResponseSerializer(data={"response": output})
            if response_serializer.is_valid():
                return Response(response_serializer.data)
            else:
                return Response(response_serializer.errors, status=400)
        else:
            return Response(serializer.errors, status=400)
