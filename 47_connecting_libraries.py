import requests
from pprint import pprint

# r = requests.get('https://api.github.com/events')
#
# pprint(r)
#
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
#
# pprint(r)
#
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
#
# r = requests.get('https://httpbin.org/get', params=payload)
#
# pprint(r.url)
#
# r = requests.get('https://api.github.com/events')
# pprint(r.json())


r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

r = requests.get('https://api.vk.com/method/users.get?user_ids=743784474&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.199')

