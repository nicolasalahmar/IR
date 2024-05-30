import urllib.parse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Offline.Helper.ORM import get_record
from Search import get_index, indexes
from Search.serializers import SearchRequestSerializer

from Offline.Pipeline.index.index import Index


class Search(APIView):
    def get_docs(self, top_documents):
        arr = []
        for i in range(len(top_documents)):
            rec = get_record(top_documents[i][0], model='Corpus')
            res = {'doc_id': top_documents[i][0], 'score': top_documents[i][1], 'rank': top_documents[i][2],
                   'text': rec.text}
            arr.append(res)
        return arr

    def get(self, request, dataset, search_field):
        serializer = SearchRequestSerializer(data={'dataset': dataset, 'search_field': search_field})
        if serializer.is_valid():
            search_field = urllib.parse.unquote(search_field)

            chosen_dataset = serializer.validated_data['dataset']

            index = indexes[chosen_dataset]

            top_documents = index.search(search_field)

            top_documents = self.get_docs(top_documents)

            return Response(top_documents)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
