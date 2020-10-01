from modules.geocoder import run_geocoder

API_KEY = 'set_api_key'
#is_reverse=TRUE - geocoding by address
#is_reverse=False - geocoding by coordinates
run_geocoder(API_KEY, is_reverse=False)
