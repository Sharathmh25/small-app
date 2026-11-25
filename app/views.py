from django.shortcuts import render,redirect
from .serializers import ProfileSerializer,ProductSerializer
from .models import Profile,Product
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import search_and_rank_products


class ProductSearchAPIView(APIView):
    # Enable once JWT auth is ready; keep AllowAny while testing search first
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get("q", "").strip()
        category_filter = request.query_params.get("category_filter", "").strip() or None
        raw_limit = request.query_params.get("limit", "20")

        if not query:
            return Response(
                {"error": "Query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            limit = int(raw_limit)
            if limit < 1 or limit > 100:
                raise ValueError()
        except ValueError:
            return Response(
                {"error": "'limit' must be an integer between 1 and 100."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        total_results, results = search_and_rank_products(
            query=query,
            category_filter=category_filter,
            limit=limit,
        )

        return Response(
            {
                "query": query,
                "total_results": total_results,
                "results": results,
            },
            status=status.HTTP_200_OK,
        )
class ProfileView(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
class ProfilePost(generics.CreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
class 



