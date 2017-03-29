from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.filters import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.exceptions import NotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from wordfencer.parser import ChineseParser
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.utils import IntegrityError

from core.services import fetch_article
from core.decorators import required_request_data
from core.exceptions import Raise403
from .models import PublicDefinition, UserDefinition, Article, PublicWord, UserWord
from .filters import (
    PublicWordFilter,
    PublicDefinitionFilter,
    OwnerOnlyFilter,
    OwnerWordOnlyFilter,
    WordFilter,
    UserWordFilter,
    UserDefinitionFilter
)
from .serializers import PublicDefinitionSerializer, PublicWordSerializer, TokenSerializer, UserWordSerializer, UserDefinitionSerializer
from core.utils import Token, get_object_or_403, is_punctuation
from .permissions import OnlyOwnerCanAccess, OnlyOwnerCanDelete, NoPutAllowed, OnlyEaseCanChange


parser = ChineseParser()


@api_view(['GET'])
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({
        'words': reverse('public-word-list', request=request, format=format),
        })


class PublicDefinitionViewSet(viewsets.ReadOnlyModelViewSet):
    """Defines a list view for the `PublicDefinition` model that is publically accessible.

    This view should be read-only, as public information should be protected from deletion.
    This means that only the GET method need be supported.


    .. todo: Change OwnerOnlyFilter to PublicFilter for clarity

    """
    queryset = PublicDefinition.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = PublicDefinitionSerializer
    filter_backends = (DjangoFilterBackend, WordFilter)
    filter_class = PublicDefinitionFilter


class UserDefinitionViewSet(viewsets.ModelViewSet):
    """Defines a list view for the `Definition` model that is only accessible by an authenticated user.

    This view should allow the creation and reading of definitions because user's can create and read definitions
    they have saved for themselves.

    :Supported Methods:

        GET, POST

    """
    queryset = UserDefinition.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (OnlyOwnerCanAccess,)
    serializer_class = UserDefinitionSerializer
    filter_backends = (DjangoFilterBackend, OwnerOnlyFilter, WordFilter,)
    filter_class = UserDefinitionFilter


class UserWordViewSet(viewsets.ModelViewSet):
    """Defines a view for users to create, modify, or delete a single word in their account.

    The primary use of this view is adding a word to a user's account and changing the `ease` of a stored word as a learner comes to know the word more as
    time passes.
    """
    queryset = UserWord.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (OnlyOwnerCanAccess, NoPutAllowed, OnlyEaseCanChange)
    serializer_class = UserWordSerializer
    filter_class = UserWordFilter
    filter_backends = (DjangoFilterBackend, OwnerOnlyFilter,)
    lookup_field = 'word'

    


class PublicWordViewSet(viewsets.ReadOnlyModelViewSet):
    """Defines a view for the `Word` model that is public accessible.

    This view should be read-only because the public should not be allowed to delete publically available
    words, this only the GET method is supported.

    """
    queryset = PublicWord.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PublicWordSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PublicWordFilter
    lookup_field = 'word'


class ParseView(CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        string = request.data['string']
        parser = ChineseParser()
        segments = parser.parse(string)
        return Response(data=segments)


class URLImportView(APIView, LoginRequiredMixin):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = request.user
        url = request.data['url']
        article = Article.objects.filter(url=url)
        if not article:
            title, text = fetch_article(url)
            Article.objects.create(title=title, text=text, url=url, owner=user)
            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PublicArticleView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        title = request.data['title']
        title = self.parse_into_json(title)
        text = request.data['text']
        paragraphs = []
        for splitted in text.split('\n'):
            paragraph = self.parse_into_json(splitted)
            paragraphs.append(paragraph)

        data = {
            'title': title,
            'paragraphs': paragraphs,
        }

        return Response(data)


    def parse_into_json(self, text):
        title_words = []
        parser_results = (p for p in parser.parse(text) if not p.isspace())
        for i, segment in enumerate(parser_results):
            try:
                word = PublicWord.objects.get(word=segment)
                definitions = PublicDefinition.objects.filter(word=word)
                word = {
                    'word': word.word,
                    'index': i,
                    'pinyin': word.pinyin,
                    'definition': [d.definition for d in definitions]
                }
            except:
                word = {
                    'word': segment,
                    'index': i,
                    'pinyin': '',
                    'definition': '',
                }

            title_words.append(word)

        return title_words
