import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        #=======================================================================
        # if not hasattr(self, '_db'):
        #    self._db = asyncmongo.Client(pool_id='mytestdb', host='127.0.0.1', port=27017, maxcached=10, maxconnections=50, dbname='TripShare')
        #=======================================================================
        #return self._db
        return self.application.db
    
    @property
    def syncdb(self):
        return self.application.syncdb

    
    def get_current_user(self):
        #self.clear_all_cookies()
        user_id = self.get_secure_cookie("email")
        if not user_id: return None
        
        #return tornado.escape.json_decode(user_id)
        return self.syncdb.users.find_one({'user_id': bson.ObjectId(str(user_id))})
    
    
    def get_current_username(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None 
        return self.syncdb.users.find_one({'user_id': bson.ObjectId(str(user_id))})["username"]
        
    def get_db_user_id(self):
        user_id = self.get_secure_cookie("user")
        return bson.ObjectId(str(user_id))
    
    def _on_response(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        #self.render('template', full_name=response['full_name'])
        logging.info('response: +++++++++++++++++++++++=' + str(response))
        
    
    def _on_action(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        #self.render('template', full_name=response['full_name'])
        logging.info('_on_action: +++++++++++++++++++++++=' + str(response))
        
    def _get_trips(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        friends = self.current_user['friends']
        self.render("browsetrip.html", trips=response, friends = friends)