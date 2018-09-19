import urllib2
import pprint
import json
import webbrowser


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


def open_URL(url):
    req = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(req)
    return response


def get_code(response):
    print response.getcode()


def deunicodify_hook(pairs):
    new_pairs = []
    for key, value in pairs:
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        new_pairs.append((key, value))
    return dict(new_pairs)


def get_json_object(response):
    json_page = json.loads(response.read(), object_pairs_hook=deunicodify_hook)
    return json_page


def get_details(latest_launch):
    launch_details = latest_launch['details']
    return launch_details


def get_last_launch(json_page):
    latest_launch = json_page[-1]
    return latest_launch


def get_launch_status(latest_launch):
    launch_status = latest_launch.get('launch_success')
    return launch_status


def get_landing_status(latest_launch):
    landing_status = latest_launch['rocket']['first_stage']['cores'][0].get('land_success')
    return landing_status


def get_rocket_type(latest_launch):
    rocket_type = latest_launch['rocket']['rocket_name']
    print rocket_type
    return rocket_type


def open_video_link(launch_status, landing_status, rocket_type, response, latest_launch):
    if launch_status and landing_status and rocket_type == 'Falcon 9':
        print (launch_status, landing_status, rocket_type)
        response_code = response.getcode()
        try:
            video_links = latest_launch['links']['video_link']
            webbrowser.open(video_links)
            return response_code
        except KeyError:
            print "There is no video links"
    else:
        print 'False conditions'


def pretty_print(json_list):
    pprint.pprint(json_list)


def main():
    url = 'https://api.spacexdata.com/v2/launches'

    response = open_URL(url)
    get_code(response)
    json_page = get_json_object(response)
    last_launch = get_last_launch(json_page)
    details = get_details(last_launch)
    launch_status = get_launch_status(last_launch)
    landing_status = get_landing_status(last_launch)
    rocket_type = get_rocket_type(last_launch)
    open_video_link(launch_status, landing_status, rocket_type, response, last_launch)
    pretty_print(details)


if __name__ == '__main__':
    main()


