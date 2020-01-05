from django.shortcuts import render

from .models import Search
from groups.models import Group


def search(request):
    query = request.GET.get('q', None)

    user = None

    if request.user.is_authenticated:
        user = request.user
        context = {'query':query}

    if query is not None :
        searches = Search.objects.create(query=query)
        group_query = Group.objects.search(query=query)
        context['group_query'] = group_query

    return render(request, 'searches/search.html', context)
