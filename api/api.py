from .models import UserSession
from rest_framework import status
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from theeyecore.celery import create_new_session


class UserSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSession
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']


class UserSessionViewSet(viewsets.ModelViewSet):
    queryset = UserSession.objects.all()
    serializer_class = UserSessionSerializer

    def create(self, request, *args, **kwargs):
        create_new_session.delay(
            request=request.data
        )
        return Response({"Server Response": "Your data has been sent to a proccessing queue!"},
                        status=status.HTTP_201_CREATED)

