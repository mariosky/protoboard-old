__author__ = 'mariosky'
#Facebook backend basado en: http://djangosnippets.org/snippets/2065/
# 16 June 2010 Added missing imports. Cleaned up the template.
#Shouts out to @obeattie and @whalesalad
#Author: barnardo
#Posted: June 15, 2010
import datetime
from django.contrib.auth import models as auth_models
from activitytree.models import FacebookSession, GoogleSession,UserProfile

import urllib
import json
from decimal import Decimal

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


def google_query_me(access_token, fields=None):
    url = 'https://www.googleapis.com/plus/v1/people/me'
    params = {'access_token':access_token}
    if fields:
            params['fields'] = fields

    url += '?' + urllib.urlencode(params)

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

    def authenticate(self,app, **kwargs):
        if app == "facebook":
            access_token = kwargs["access_token"][0]
            expires = kwargs["expires"][0]

            profile = facebook_query_me(access_token)
            if 'email' not in profile:
                print profile
                return None


            try:
                #This user/email exists?
                user = auth_models.User.objects.get(email=profile['email'])

                #if found and email is associated with the same facebook account, no problem
                if hasattr(user, 'userprofile') and user.userprofile.facebook_uid == Decimal(profile['id']):
                    pass
                else:
                    #We must abort, log to your previous account
                    print "Correo en uso"
                    return None

            except auth_models.User.DoesNotExist, e:
                # We create a new user

                user = auth_models.User(username=profile['id'], email=profile['email'], is_active=True, first_name = profile['first_name'], last_name= profile['last_name'])
                user.set_unusable_password()
                user.save()
                user_profile = UserProfile(facebook_uid = profile['id'],user=user)
                user_profile.save()

            #Renew or create facbook session
            try:
                FacebookSession.objects.get(user=user).delete()
            except FacebookSession.DoesNotExist, e:
                pass

            facebook_session = FacebookSession.objects.get_or_create(access_token=access_token)[0]

            facebook_session.uid = profile['id']
            facebook_session.expires = expires
            facebook_session.user = user
            facebook_session.save()

            return user

        elif app == "google":

            print kwargs
            access_token = kwargs["access_token"]
            expires_in = kwargs["expires_in"]
            refresh_token = kwargs["id_token"]
            profile = google_query_me(access_token)

            email = "emails" in profile and profile["emails"] and profile["emails"][0]["value"] or None
            print profile

            if not email:
                print "No "
                return None

            try:

                #This user/email exists?
                user = auth_models.User.objects.get(email=email)

                #if found and email is associated with the same facebook account, no problem
                if hasattr(user, 'userprofile') and user.userprofile.google_uid == Decimal(profile['id']):
                    print "Existe coreo y es google"
                else:
                    #We must abort, log to your previous account
                    print "Existe correo y es NO google"
                    return None

            except auth_models.User.DoesNotExist, e:
                # We create a new user
                print e
                user = auth_models.User(username=email, email=email, is_active=True, first_name = profile["name"]['givenName'], last_name= profile["name"]['familyName'])
                user.set_unusable_password()
                user.save()
                print  profile['id']
                user_profile = UserProfile(google_uid = profile['id'],user=user)
                user_profile.save()
                print user.userprofile.google_uid


            #Renew or create google  session

            try:
                GoogleSession.objects.get(user=user).delete()
            except GoogleSession.DoesNotExist, e:
                print e

            google_session = GoogleSession.objects.get_or_create(access_token=access_token, user = user)[0]
            google_session.expires_in = expires_in
            google_session.refresh_token = refresh_token
            google_session.save()


            return user







    def get_user(self, user_id):

        try:
            return auth_models.User.objects.get(pk=user_id)
        except auth_models.User.DoesNotExist:
            return None