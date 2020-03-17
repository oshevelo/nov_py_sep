from django.test import TestCase
from rest_framework.test import APIClient
from apps.shipments.models import Shipment
from apps.orders.models import Order
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid

class shipmentsTest(TestCase):

    def setUp(self):
        self.APIclient=APIClient()
        self.user_1=User.objects.create_user(username="Test", password="Test")
        self.order_1 = Order.objects.create(user=self.user_1, accepting_time=now())
        self.order_2 = Order.objects.create(user=self.user_1, accepting_time=now(), is_paid=True)
        self.shipment_1=Shipment.objects.create(order=self.order_1,destination_city="Testville", destination_zip_code = 1111, destination_adress_street="Test str", destination_adress_building="1a")

    
    def test_shipment_create(self):
        self.APIclient.login(username='Test', password='Test')
        response=self.APIclient.post('/shipments/', 
        {'order': {
                    'id':self.order_1.id,
                    'pub_id': self.order_1.pub_id,
                    },
         'shipment_status': 1,
         'shipment_type': 'HOME',                
         'destination_city': 'test',
         'destination_zip_code': '11111',
         'destination_adress_street': 'test',
         'destination_adress_building': '1t',
        }, format='json')
        response_json=response.json()
        uuid=Shipment.objects.get(destination_city='test').uuid
        expected={'uuid': str(uuid),
                    'order': {
                              'id':self.order_1.id,
                              'pub_id': str(self.order_1.pub_id),
                              'user': {
                                       'id': self.user_1.id,
                                       'email':'',
                                       'username': 'Test'
                                       },
                              'accepting_time':self.order_1.accepting_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                              'status':self.order_1.status
                              },
         'shipment_status': 1,
         'shipment_type': 'HOME',
         'shipment_date': None,                
         'destination_city': 'test',
         'destination_zip_code': '11111',
         'destination_adress_street': 'test',
         'destination_adress_building': '1t',
         'destination_other_details':''
        }
        self.assertEqual(response_json, expected)
        self.assertEqual(response.status_code, 201)
    
    def test_negative_shipment_create_order_not_editable(self): 
        self.APIclient.login(username='Test', password='Test')
        response=self.APIclient.post('/shipments/', 
        {'order': {
                    'id': self.order_2.id,
                    },
         'shipment_status': 1,
         'shipment_type': 'HOME',                
         'destination_city': 'test',
         'destination_zip_code': '11111',
         'destination_adress_street': 'test',
         'destination_adress_building': '1t',
        }, format='json')
        self.assertEqual(response.status_code, 400)
    
    def test_negative_shipment_create(self):
        self.APIclient.login(username='Test', password='Test') 
        response=self.APIclient.post('/shipments/', 
        {'order': {
                    'id': 123321123321,
                    'pub_id': self.order_1.pub_id,
                    },
         'shipment_status': 1,
         'shipment_type': 'HOME',                
         'destination_city': 'test',
         'destination_zip_code': '11111',
         'destination_adress_street': 'test',
         'destination_adress_building': '1t',
        }, format='json')
        self.assertEqual(response.status_code, 400)

    def test_shipment_list(self):
        self.APIclient.login(username='Test', password='Test')
        response = self.APIclient.get('/shipments/')
        self.assertEqual(response.status_code, 200)

    def test_shipment_retrieve(self):
        self.APIclient.login(username='Test', password='Test')
        uuid = self.shipment_1.uuid
        response = self.APIclient.get('/shipments/{}'.format(uuid))
        self.assertEqual(response.status_code, 200)

    def test_shipment_retrieve_negative(self):
        self.APIclient.login(username='Test', password='Test')
        uuid = "1234"  #invalid uuid
        response = self.APIclient.get('/shipments/{}'.format(uuid))
        self.assertEqual(response.status_code, 404)

    def test_shipment_list_paged(self):
        self.APIclient.login(username='Test', password='Test')
        response = self.APIclient.get('/shipments/?limit=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)
    
    def test_shipment_destroy(self):
        self.APIclient.login(username='Test', password='Test')
        uuid = self.shipment_1.uuid
        response = self.APIclient.delete('/shipments/{}'.format(uuid))
        self.assertEqual(response.status_code, 204)
        updated_response = self.APIclient.delete('/shipments/{}'.format(uuid))
        self.assertEqual(updated_response.status_code, 404)
 

    def test_shipment_update(self):
        self.APIclient.login(username='Test', password='Test')
        uuid = self.shipment_1.uuid
        new_destination_city = "Testopolis"
        response = self.APIclient.patch('/shipments/{}'.format(uuid), 
                                 {'destination_city': new_destination_city})
        self.assertEqual(response.status_code, 200)

    

    
        
            
