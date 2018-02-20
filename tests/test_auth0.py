from auth0.v3.authentication.users import Users
import json
# import requests
domain = 'fuzeday-ultron.auth0.com'
clientID = 'VrgR8b6jaHPnI7E8yfzwRCtNUsyAMflH'
#
u = Users(domain=domain)
# s = GetToken(domain)

# s.
user_info = json.loads(u.userinfo('n66HltzIlr9ekRZSSZupiv-G7TdnikSA'))

# url = 'https://' + domain + '/userinfo'
# headers = {'authorization': 'Bearer n66HltzIlr9ekRZSSZupiv-G7TdnikSA'}
# resp = requests.get(url, headers=headers)
# userinfo = resp.json()
#
print(user_info)

