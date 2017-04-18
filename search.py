from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyCszAdNUh1tXp42SVANB1vxcOecmjN5kIo"
my_cse_id = "007023224152901261631:ysdy_oveuxy"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'resume+example+PDF', my_api_key, my_cse_id, num=10)
for result in results:
    pprint.pprint(result['link'])
