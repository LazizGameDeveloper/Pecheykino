from app.models import *
from django.http import JsonResponse
from django.views.generic import View

class ActiveProducts(View):

    def get(self, request):
        categories = Products.objects.filter(is_active=True)
        if categories is None:
            return

        serialized_data = []
        for category in categories:
            serialized_data.append({
                "name": category.name,
                "key": category.key
            })

        data = {
            'data': serialized_data,
        }
        return JsonResponse(data)

    
class InactiveProducts(View):

    def get(self, request):
        categories = Products.objects.filter(is_active=False)
        if categories is None:
            return

        serialized_data = []
        for category in categories:
            serialized_data.append({
                "name": category.name,
                "key": category.key
            })

        data = {
            'data': serialized_data,
        }
        return JsonResponse(data)