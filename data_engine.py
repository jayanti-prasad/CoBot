import os
import numpy as np
import pandas as pd
import re
from datetime import datetime
from common_utils import get_country_data

DATA_DIR="data"

def response(country, data):
   text  = "Country: " + country 
   text += ". Date: " + data['date'] 
   text += ", Confirmed:" + str(int(data['confirmed']))
   text += ", Deaths:" + str(int(data['deaths']))
   text += ", Recovered:" + str(int(data['recovered']))
   print("text:",text)   
   return text 
 


class Engine:
    def __init__(self,):
       self.count = 0
       self.df = pd.read_csv(DATA_DIR + os.sep + "covid-19-global.csv")
       self.countries = list(set(self.df['country'].to_list()))
       self.countries = [x.lower() for  x in self.countries] 
       self.country = None 

    def extract_country (self, text):
       y = text.split(" ")   
       y = [x.lower() for  x in y]
       common = list(set(y) & set(self.countries))

       try :
           country =  common[0] 
       except:
           print("Failed to get a country name !")
           country = None 
           print("text:",text)
           print("countries:",self.countries)
       return country 
  

    def extract_date (self, text):
       match = re.search(r'\d{4}-\d{2}-\d{2}', text)
       date = datetime.strptime(match.group(), '%Y-%m-%d').date()
       return date 


    def get_data (self, msg):
       if self.count == 0:
          welcome_msg = "Welcome to Covid-19 Information System developed by Jayanti Prasad !"
          welcome_msg = welcome_msg + "\n Please give a country"
          self.count +=1 
          return welcome_msg 
     
       if self.count > 0 : 
          country = self.extract_country (msg) 
          print ("Getting the information for:" + country)
          if country in ['us','uk']:
             df = get_country_data (self.df, country.upper()) 
          else:
             df = get_country_data (self.df, country.capitalize()) 
          self.count +=1
          return response (country,  df.iloc[-1]) 
          #else:
          #   print("extracted country:", self.extract_country(msg))
          #   return("Country: " + msg +\
          #    " Not found ! \n You can give any of the\
          #    following countries " + ",".join(self.countries)) 
