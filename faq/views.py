from django.shortcuts import render

# Create your views here.
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def faq_list(request):
    lang = request.GET.get('lang', 'en')
    cache_key = f"faqs_{lang}"
    faqs = cache.get(cache_key)

    if not faqs:
        faqs = FAQ.objects.all()
        if lang == 'hi':
            faqs = [{'question': faq.question_hi, 'answer': faq.answer} for faq in faqs]
        elif lang == 'bn':
            faqs = [{'question': faq.question_bn, 'answer': faq.answer} for faq in faqs]
        else:
            faqs = FAQSerializer(faqs, many=True).data

        cache.set(cache_key, faqs, timeout=60 * 5)  # Cache for 5 minutes

    return Response(faqs)

