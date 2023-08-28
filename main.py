import requests
import json
import datetime
from datetime import date
from datetime import timedelta
import logging

logging.basicConfig(filename='logs_robot',filemode='w', level= logging.INFO, format='%(asctime)s %(levelname)s || %(message)s')


def get_date(dey = None):
    if dey == None:
        current_date = date.today()
    else:    
        current_date = datetime.datetime.strptime(dey, "%d.%m.%Y")
    last_date = datetime.timedelta(weeks=1)
    start_date = current_date - last_date
    interval = f'{start_date.strftime("%d.%m.%Y")} - {current_date.strftime("%d.%m.%Y")}'
    return interval


def contracts(**kwargs):
   params = {**kwargs}
   try:
      logging.INFO('request successful'+ url, params)
      url = f'http://openapi.clearspending.ru/restapi/v3/contracts/search/'
      data = requests.get(url, params)
      return data
   except Exception as e:
      logging.exception(e)
   try:
      logging.INFO('conversion to json is successful')
      data_json = data.json()
      return data_json
   except Exception as e:
      logging.exception(e) 
      
       
    

result = contracts(customerregion = 23, daterange = get_date() )
#запись в файл
with open('resut_json','w') as f:
    json.dump(result, f)



with open('resut_json','r') as f:
   json_data = json.loads(f.read())
   contract =  json_data['contracts']['data']

         
def recurs(kei, val):
   if val == None:
      return None
   else:
      if kei in val:
         return val[kei]
      if type(val) == dict or type(val) == list:
         for k, v in val.items():          
            if type(v) == dict:
               result =  recurs (kei, v)
               if result is not None:
                  return result
                  
            if type(v) == list:
               for i in range(len(v)):
                  result = recurs(kei, v[i-1])
                  if result is not None: 
                     return result

for i in contract:
   organiseihen = {}
   date_protocol = recurs('protocolDate', i) 
   name = recurs('fullName', i)
   inn = recurs('inn', i)
   organiseihen[name]  = inn
   price = recurs('price', i)
   products = recurs('products', i)
   #for el in products:
   product = '; '.join([ recurs('name', el) for el in products])
    

   
   print(organiseihen)       
   print(date_protocol)
   print(price)
   print(product, end='\n\n')
     
