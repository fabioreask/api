
import sys
import requests
import json
import time

from auth import get_access_token

def metryc_point(access_token, lats, lons, tag=None):

    if type(lats) != type([]):
        lats = [lats]
        lons = [lons]

    url = 'https://api.reask.earth/v1/metryc/point'
    params = {
        'access_token': access_token,
        'lats': lats,
        'lons': lons,
    }
    if tag is not None:
        params['tag'] = tag

    start_time = time.time()
    res = requests.get(url, params=params)

    if res.status_code != 200:
        print(res.text)
        return None

    print('metryc/point took {}ms'.format(round((time.time() - start_time) * 1000)))

    return res.json()


def main():

    access_token = get_access_token()
    lats = [29.95747]
    lons = [-90.06295]

    ret = metryc_point(access_token, lats, lons, tag="Jackson_Square")
    with open('Jackson_Square_Metryc_Present_Day_API_Sample.json', 'w') as f:
        print(json.dumps(ret, indent=4), file=f)

    lats = [27.11]
    lons = [-82.46]

    # Add a point which should not be impacted.
    #lats.append(40)
    #lons.append(-100)

    ret = metryc_point(access_token, lats, lons, tag="Tampa")
    with open('Tampa_Metryc_Present_Day_API_Sample.json', 'w') as f:
        print(json.dumps(ret, indent=4), file=f)


if __name__ == '__main__':
    sys.exit(main())
