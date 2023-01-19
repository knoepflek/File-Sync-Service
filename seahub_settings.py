## Insert this into seahub_settings.py file. Replace the information within "<>" with your information from the Seafile client you have created in Keycloak. 
## You find the information in the credentials
ENABLE_OAUTH = True
OAUTH_ENABLE_INSECURE_TRANSPORT = True

OAUTH_CLIENT_ID = "seafile"
OAUTH_CLIENT_SECRET = "<replace-with-client-secret>"
OAUTH_REDIRECT_URL = 'https://<seafile-url>/oauth/callback/'
 
OAUTH_PROVIDER_DOMAIN   = '<seafile-url-without https>'
OAUTH_AUTHORIZATION_URL = 'https://<keycloak-url>/auth/realms/master/protocol/openid-connect/auth'
OAUTH_TOKEN_URL         = 'https://<keycloak-url>/auth/realms/master/protocol/openid-connect/token'
OAUTH_USER_INFO_URL     = 'https://<keycloak-url>/auth/realms/master/protocol/openid-connect/userinfo'
OAUTH_SCOPE = ["profile", "email"]
OAUTH_ATTRIBUTE_MAP = {
    "id":    (False, "not used"),
    "name":  (False, "full name"),
    "email": (True, "email"),
}
