from django.shortcuts import render
from shope.models import Product
from django.db.models import Q

def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query:
            # Filter products based on the search query
            products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))

    return render(request, 'search.html', {'query': query, 'products': products})
