# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs

def get_url(category):
    dic = {'moisturizers':'https://www.sephora.com/shop/moisturizing-cream-oils-mists',
           'cleansers':'https://www.sephora.com/shop/cleanser',
           'eye care':'https://www.sephora.com/shop/eye-treatment-dark-circle-treatment',
           'sun care':'https://www.sephora.com/shop/sunscreen-sun-protection',
           'lip treatment':'https://www.sephora.com/shop/lip-treatments'}
    URL = dic[category]
    return URL

def get_json_request(URL):
    r = requests.get(url = URL)
    soup = bs(r.text)
    print(soup.prettify())
 

def get_prices(category):
    


  startURL = get_url(category)
  data = get_json_request(startURL)
  print(data)

#  current_reviews = data['Results']
#  while len(current_reviews) > 0:
#    offset += 100
#    URL = get_url(product_id, offset)
#    current_reviews = get_json_request(URL)['Results']
#    reviews = reviews + current_reviews
#
#  return reviews

#def get_description():
#  product_id = 'P400259'
#  URL = get_url(product_id)
#  data = get_json_request(URL)
#  return data[product_id]['Description']
#  
#def init():
#  product_id = 'P400259'
#  reviews = get_reviews(product_id)
#  return reviews

if __name__ == '__main__':
  get_prices('moisturizers')