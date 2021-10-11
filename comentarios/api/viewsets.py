from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ComentariosSerializer
from comentarios.models import Comentario


class ComentarioViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)