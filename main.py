from drp_agent import DRP_Agent
from d42_agent import D42_Agent

conf = {
    'd42': {
        'server': 'https://10.42.2.241/api/1.0/',
        'user': 'admin',
        'pwd': 'adm!nd42',
        'verify_certificate': False
    },
    'drp': {
        'server': 'https://147.75.69.1:8092',
        'user': 'rocketskates',
        'pwd': 'r0cketsk8ts',
    }
}


d42 = D42_Agent(
    server=conf['d42']['server'],
    user=conf['d42']['user'],
    pwd=conf['d42']['pwd'],
)

res = d42.get(
    url='/api/1.0/devices/id/15',
    headers={
        'Accept': 'application/json', 
    },
)
print("response from D42s: %s" % (res))
exit()


drp = DRP_Agent(
    server=conf['drp']['server'],
    user=conf['drp']['user'],
    pwd=conf['drp']['pwd'],
)

get_machines_uri = '/api/v3/machines'
params = {'Uuid': 'ec72bb80-acb6-45a0-85ec-6a4952cf0680'}
response = drp.get(
    get_machines_uri,
    headers={
        'Accept': 'application/json', 
    },
    params=params
)

print("response from DRP: %s" % (response))
