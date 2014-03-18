__author__ = 'mariosky'

from django.core.exceptions import ObjectDoesNotExist
import requests


def user_data(request):
        if request.user.is_authenticated() and request.user != 'AnonymousUser' :
            social = None
            response= None
            try:
                social = request.user.social_auth.get(provider='google-plus')
                response = requests.get('https://www.googleapis.com/plus/v1/people/me/',
                params={'access_token': social.extra_data['access_token']})
            except ObjectDoesNotExist:
                pass
            if social:
                user_plus_data = response.json()


                return {'user_name' : user_plus_data['displayName'], 'user_image' : user_plus_data['image']['url'] }
            else:
                return {'user_name' :  request.user.username}

        else:
            return {}
