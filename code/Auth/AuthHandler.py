'''
Created on Nov 5, 2011

@author: jason
'''
import hmac
import bson
import datetime
import unicodedata
import simplejson
import tornado.auth
from Map.BrowseTripHandler import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render("signup.html")
        
   
    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        password_in_db = self.db.get("SELECT password from users where email = %s", email)
        # use MD5 hash algorithm
        if check:
            
            digest_marker = hmac.new(email)
            digest_marker.update(password)
            real_password = digest_marker.hexdigest()
            print("check password")
            
            if real_password == password_in_db:
                
                self.set_secure_cookie("email", email)
                self.redirect("/")
            else:
                self.redirect("/login")
        
        else:
            self.redirect("/login")

class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")

class CreateAccountHandler(BaseHandler):
    def get(self):
        self.render("signup.html")
    
    @tornado.web.asynchronous    
    def post(self):
        email = self.get_argument("email")
        #check  = self.syncdb.users.find_one( { 'email' : email })
        
        check  = self.db.get("SELECT user_id from users where email = %s", email)
       
        if check:
                raise tornado.web.HTTPError(500, "Auth failed because of duplicated email address");
        else:
                password = self.get_argument("password")
                # use MD5 hash algorithm
                digest_marker = hmac.new(email, password)
                #digest_marker.update(password)
                real_password = digest_marker.hexdigest()
                self.db.get("INSERT INTO users VALUES (%s, %s)", email, real_password)
                
                #===============================================================
                # Store basic information in cookie
                #===============================================================
               
                self.set_secure_cookie("email", email)
                self.redirect("/")
                


class AuthLoginFBHandler(BaseHandler, tornado.auth.FacebookGraphMixin):
    access_token = ''
    
    @tornado.web.asynchronous
    def get(self):
        my_url = (self.request.protocol + "://" + self.request.host +
                  "/auth/fblogin?next="+
                  tornado.escape.url_escape(self.get_argument("next", "/")))
        #print(my_url)
        if self.get_argument("code", False):
            self.get_authenticated_user(
            redirect_uri=my_url,
            client_id=self.settings["facebook_api_key"],
            client_secret=self.settings["facebook_secret"],
            code=self.get_argument("code"),
            callback=self._on_auth)
            return
        self.authorize_redirect(redirect_uri=my_url,
                              client_id=self.settings["facebook_api_key"],
                              extra_params={"scope": "user_about_me,email,user_website,publish_stream,read_friendlists,offline_access"})
 
    def handle_request(self, response):
        print('++++++++++++++++++++++++++++++'+response.body)
        user = simplejson.loads(response.body)
        
        slug  = user[0]['name']
        checkExist = self.syncdb.users.find_one({'fb_user_id':str(user[0]['uid'])})
        if checkExist:
            checkExist['access_token'] = self.access_token
            self.syncdb.user.save(checkExist)
            self.set_secure_cookie("user", str(checkExist['user_id']))
            self.redirect(self.get_argument("next", "/"))
            return
        
        
        while True:
            e = self.syncdb.users.find_one({'slug':slug})
            if not e: break
            slug += "-2"
            
        _user = {   'fb_user_id' : str(user[0]['uid']),
                    'username': user[0]['name'],
                    'lc_username': user[0]['name'].upper(),
                    'web_url': user[0]['website'],
                    'locale':user[0]['locale'],
                    'email': user[0]['email'],
                    'picture': user[0]['pic'],
                    'current_location': user[0]['current_location'],
                    'current_position':[],
                    'status': 'online',
                    'slug': slug,
                    'createdtime': datetime.datetime.utcnow(),
                    'access_token': self.access_token,  
                    'save_guide':[],
                    'like_guide':[],
                    'save_site':[],
                    'like_site':[],
                    'save_trip':[],
                    'like_trip':[],
                    'friends':[],
                    'city': [],
                    'country': [],
                    'trips':[],
                    'like_trip':[],
                    'bio':'',
                    'link': '',
                    'trip_count':0,
                    'current_location':'',
                    'current_position':[],
                    'new_notifications':[],
                    'notifications':[],
                    'search_type':'person'
                    
                }
        _user_db = self.syncdb.users.find_one({'email': user[0]['email']})
        
        slug = unicodedata.normalize("NFKD", unicode(user[0]['name'])).encode("ascii", "ignore")
        while True:
                    e = self.syncdb.users.find_one({'slug':slug})
                    if not e: break
                    slug += "-2"
        
        user_id = ''
        if _user_db:    
            user_id = _user_db['user_id']
            _user['_id'] = _user_db['_id']
        else:
            user_id = _user['user_id'] = bson.ObjectId()
            _user['createdtime']=datetime.datetime.utcnow()
        _user['slug'] = slug
        self.db.users.save(_user, callback=self._on_action)
        self.set_secure_cookie("user", str(user_id))
        self.redirect(self.get_argument("next", "/"))
    
    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Facebook auth failed")
        
        print(tornado.escape.json_encode(user))
        self.access_token = user['access_token']
        print(self.access_token)
        http_client = tornado.httpclient.AsyncHTTPClient()
       
        http_client.fetch("https://api.facebook.com/method/users.getInfo?uids="+user['id']+"&fields=uid%2C%20name%2C%20website%2C%20locale%2C%20pic%2C%20current_location%2C%20email&access_token="+self.access_token+"&format=json", self.handle_request)

        
class AuthLogoutFBHandler(BaseHandler, tornado.auth.FacebookGraphMixin):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))
        

class GoogleHandler(tornado.web.RequestHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        # Save the user with, e.g., set_secure_cookie()
        
class TwitterHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("oauth_token", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authorize_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Twitter auth failed")
        # Save the user using, e.g., set_secure_cookie()
