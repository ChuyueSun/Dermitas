import requests

def get_url(product_id, offset=0, limit=100):
  URL = 'https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId%3A{0}&Sort=Helpfulness%3Adesc&Limit={1}&Offset={2}&Include=Products%2CComments&Stats=Reviews&passkey=rwbw526r2e7spptqd2qzbkp7&apiversion=5.4'.format(product_id, limit, offset)
  return URL

def get_json_request(URL):
  r = requests.get(url = URL)
  return r.json()

def get_reviews(product_id):
  reviews = []
  offset = 0
  startURL = get_url(product_id, offset)
  data = get_json_request(startURL)

  current_reviews = data['Results']
  while len(current_reviews) > 0:
    offset += 100
    URL = get_url(product_id, offset)
    current_reviews = get_json_request(URL)['Results']
    reviews = reviews + current_reviews

  return reviews

def get_description():
  product_id = 'P400259'
  URL = get_url(product_id)
  data = get_json_request(URL)
  return data[product_id]['Description']
  
def init():
  product_id = 'P400259'
  reviews = get_reviews(product_id)
  return reviews

if __name__ == '__main__':
  init()