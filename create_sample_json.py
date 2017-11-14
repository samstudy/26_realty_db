import requests
import random
import json



def create_sample_file():
    url = 'https://devman.org/media/filer_public/e5/62/e56287d2-9519-4e18-878a-6d4849b628e2/ads.json'
    response = requests.get(url)    
    flats = response.json()
    result = [dict(flat, **{'is_expired':random.choice([True, False])}) for flat in flats]
    with open('sample.json', 'w') as file_handler:
       json.dump(result, file_handler, ensure_ascii=False)

if __name__ == '__main__':
	create_sample_file()