from django.http import JsonResponse
from patients.models import CIE10
from rest_framework.views import APIView

class SearchInCIE10(APIView):
    def get(self,request):
        codes = CIE10.objects.filter(name__icontains=request.GET.get("search[term]"))
        return JsonResponse({"results":[{"id":code_c.id,"text":code_c.code + " - " +code_c.name} for code_c in codes],"pagination": {"more": "true"}})
