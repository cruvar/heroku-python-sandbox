import requests
import argparse
from datetime import date


parser = argparse.ArgumentParser(description='cimis api script')
parser.add_argument('--url', action='store', dest='url', type=str)
parser.add_argument('--zip', action='store', dest='zip_code', type=str)
parser.add_argument('--timeout', action='store', dest='timeout', default=60, type=int)
args = parser.parse_args()

url = args.url
zip_code = args.zip_code
timeout = args.timeout
start_date = date(1982, 6, 7)
end_date = date.today()

params = dict( 
    targets=zip_code, 
    startDate=str(start_date), 
    endDate=str(end_date), 
    dataItems='day-asce-eto', 
)

response = requests.get(url, params=params, timeout=timeout)

print(response.json())
