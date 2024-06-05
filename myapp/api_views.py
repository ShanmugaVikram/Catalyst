# core/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CompanyData

class QueryCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        filters = {}
        city = request.query_params.get('city')
        state = request.query_params.get('state')
        country = request.query_params.get('country')
        industry = request.query_params.get('industry')

        if city:
            filters['city__icontains'] = city
        if state:
            filters['state__icontains'] = state
        if country:
            filters['country__icontains'] = country
        if industry:
            filters['industry__icontains'] = industry

        count = CompanyData.objects.filter(**filters).count()
        return Response({'count': count})
