'''
Created on Dec 24, 2010

@author: jason
'''
import string
import bson
import logging
import tornado.web
import datetime
import simplejson
import Common.BaseHandler



class BrowseHandler(BaseHandler):
    
    def get(self):
         
        menglasses = self.db.query("SELECT thumbnail FROM glasses WHERE sex='m' LIMIT 20")
        womenglasses = self.db.query("SELECT thumbnail FROM glasses WHERE sex = 'f' LIMIT 20")
            #trips = self.db.query("SELECT trip_id, slug, title FROM trips where owner_id = %s ORDER BY published DESC LIMIT 10", self.current_user.user_id)
            #self.db.trips.find({'owner_id':self.get_db_user_id()}, limit = 10, sort = [('published', -1)], callback=self._get_trips)
            #self.db.trips.find({}, limit = 10, sort = [('published', -1)], callback=self._get_trips)
            
        self.render("browseglass.html", menglasses = menglasses, womenglasses = womenglasses, token = self.xsrf_token)
        
        
class EntryHandler(BaseHandler):
    
    cart = None
    def get(self, glassid):
        
        self.cart = self.syncdb.get("SELECT cart from users where email = %s", self.current_user['email'])
               
        self.db.query(SELECT thumbnail, picture, description FROM glasses WHERE glassid=%s, glassid)   
        
        
    def _trip_entry(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        users = []
        for group in self.singletrip['groups']:
            for user in group['members']:
                users.append(user)
        users.reverse()
        
        self.render("Trips/edittrip.html", current_user=self.current_user, expense = self.singletrip['expense'], users = users ,group_id=self.singletrip['groups'][0]['group_id'] , singletrip=self.singletrip, dest_place = unicode(simplejson.dumps(self.singletrip['groups'][0]['dest_place'], cls=MongoEncoder.MongoEncoder.MongoEncoder)),token = self.xsrf_token, trips=response)
        
class TripPageHandler(BaseHandler):

    def get(self, _section, _index):
       
        section = _section
        index = string.atoi(_index)

        skip_number = index*3
        if section == "newtrips":
            latest_trip_ids = self.syncdb.trips.find().skip(skip_number).limit(3).sort("published", pymongo.DESCENDING)
        elif section == "hottrips":
            
            t = datetime.datetime.now()  
            latest_trip_ids = self.syncdb.trips.find({"end_date": {"$gt": t}}).skip(skip_number).limit(3).sort("members_count", pymongo.DESCENDING)
        elif section == "endtrips":
            t = datetime.datetime.now()
            latest_trip_ids = self.syncdb.trips.find({"end_date": {"$lt": t}}).skip(skip_number).limit(3).sort("published", pymongo.DESCENDING)
            
        if latest_trip_ids.count() > 0:
                for latest_trip_id in latest_trip_ids:
                        latest_trip_id['check_join'] = False
                        
                        members = latest_trip_id['groups'][0]['members']
                        if self.current_user:
                            for member in members:
                                if member['user_id'] == self.current_user['user_id']:
                                    latest_trip_id['check_join'] = True
                                    # print("true")
                                    break
                        
                        #temp_dumps = json.dumps(latest_trip_id, cls=MongoEncoder.MongoEncoder)
                       
                        #_latest_trip_id = json.loads(temp_dumps)
                        #_latest_trip_id['html'] = self.render_string("Module/trip.html", trip = latest_trip_id) + "||||"
                     
                        #self.write(_latest_trip_id['html'])
                        self.write(self.render_string("Module/trip.html", trip = latest_trip_id) + "||||")
     
    
