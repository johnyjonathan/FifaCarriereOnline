import json
from django.http import HttpResponse, HttpResponseServerError, JsonResponse, HttpResponseRedirect
from FIFACarrierApp import views
from FIFACarrierApp import models
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def playerSearch(request):
     if request.user.is_authenticated:
        if is_ajax(request):
            resp = None
            player_name = request.POST.get('player_name')
            query_set = models.PLayersData.objects.filter(short_name__icontains=player_name) | models.PLayersData.objects.filter(long_name__icontains=player_name)
            if len(player_name) > 0:
                if len(query_set) < 50:
                    data = []
                    for pos in query_set:
                        item = {
                            'pk': pos.pk,
                            'long_name': pos.long_name,
                            'club_name': pos.club_name,
                            'overall': pos.overall,
                            'potential': pos.potential,
                            'player_position': pos.player_position,
                            'player_face_url': pos.player_face_url,
                            'age': pos.age,

                        }
                        data.append(item)
                    resp = data
                elif len(query_set) == 0:
                    resp = 'No players found'
                else:
                    resp = 'Too many players found'
            else:
                resp = 'No player name'

            return JsonResponse({'data': resp})
        else:
            return JsonResponse({})