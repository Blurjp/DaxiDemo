import Common.BaseHandler
import simplejson
import time


class PlaceOrderHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        orderSummary = self.get_argument('orderSummary')
        products = self.get_argument('products')
        totalPrice = self.get_argument('totalPrice')
        shippingType = self.get_argument('shippingType')
        shippingAddress = self.get_argument('shippingAddress')
        shippingFee = self.get_argument('shippingFee')
        paymentMethod = self.get_argument('paymentMethod')  
        orderType = self.get_argument('orderType')  # 0: purchase  1: home try
        
        
        if product and len(product)>0:
           order = self.db.get(INSERT INTO orders (totalPrice, shippingType, shippingAddress, shippingFee, paymentMethod, status, type, useremail, date) VALUES (%s, %s, %s, %s, %s, %s), totalPrice, shippingType, shippingAddress, shippingFee, paymentMethod, 'processing', orderType, self.current_user['email'], time.strftime('%Y-%m-%d %H:%M:%S'))
	   if order and len(order)>0:
              orderId = order[1]
        
           for productItem in products:
              if 'productId' in productItem and 'quantity' in productItem:
                  self.db.get(INSERT INTO itemorders (orderid, productid, quantity) VALUES (%s, %s, %s), orderId, productItem['productId'], productItem['quantity'])
  
 class CancelOrderHandler(BaseHandler):
 
     @tornado.web.authenticated
     def get(self):
         orderId = self.get_argument('orderId')
         self.db.query(UPDATE orders SET status = %s where orderid = %s, 'cancelled', orderId)
 
 
 class BrowseOrderHandler(BaseHandler):
 
     @tornado.web.authenticated
     def get(self):
         orders = self.db.query(SELECT FROM orders where useremail = %s ORDER BY date DESC, self.current_user['email'])
         self.render("browseorder.html", orders=orders, token = self.xsrf_token)