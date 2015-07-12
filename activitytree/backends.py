__author__ = 'mariosky'
#Facebook backend basado en: http://djangosnippets.org/snippets/2065/
# 16 June 2010 Added missing imports. Cleaned up the template.
#Shouts out to @obeattie and @whalesalad
#Author: barnardo
#Posted: June 15, 2010
import datetime
from django.contrib.auth import models as auth_models
from activitytree.models import FacebookSession, UserProfile

import urllib
import json

def facebook_query_me(access_token, fields=None, metadata=False):

        url = 'https://graph.facebook.com/me'

        params = {'access_token':access_token}

        if metadata:
            params['metadata'] = 1
        if fields:
            params['fields'] = fields

        url += '?' + urllib.urlencode(params)

        print urllib.urlencode(params)
        print url

        response = ''
        try:
            response = json.load(urllib.urlopen(url))

            if 'error' in response:
                error = response['error']
                raise Exception(error['type'], error['message'])
        except:
            return None



        return response


class FacebookBackend:

    def authenticate(self, access_token, expires):


        #get profile


        profile = facebook_query_me(access_token)

        try:
            user = auth_models.User.objects.get(username=profile['id'])
        except auth_models.User.DoesNotExist, e:
            user = auth_models.User(username=profile['id'], is_active=True)


        user.set_unusable_password()
        if 'email' in profile:
            user.email = profile['email']
            user.username = profile['id']
        else:
            user.email = profile['id']
            user.username = profile['id']


        user.first_name = profile['first_name']
        user.last_name = profile['last_name']
        user.save()

        if hasattr(user, 'userprofile'):
            print "ya tiene"
        else:
            print "no tiene"
            user_profile = UserProfile(facebook_uid = profile['id'],user=user)
            user_profile.save()



        try:
            FacebookSession.objects.get(uid=profile['id']).delete()
        except FacebookSession.DoesNotExist, e:
            pass

        facebook_session = FacebookSession.objects.get_or_create(
        access_token=access_token)[0]

        facebook_session.uid = profile['id']
        facebook_session.expires = expires
        facebook_session.user = user

        facebook_session.save()

        return user

    def get_user(self, user_id):

        try:
            return auth_models.User.objects.get(pk=user_id)
        except auth_models.User.DoesNotExist:
            return None