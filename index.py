import requests
import json
import csv

# Original URL for reference
# http://www.sgx.com/proxy/SgxDominoHttpProxy?timeout=100&dominoHost=http%3A%2F%2Finfofeed.sgx.com%2FApps%3FA%3DCOW_CorpAnnouncement_Content%26B%3DAnnouncementLast12Months%26R_C%3D%26C_T%3D10000

# Change this according to desired scope
scope = 'AnnouncementLast12Months'
# Change this according to maximum number of results desired
limit = '100'
url = 'http://www.sgx.com/proxy/SgxDominoHttpProxy?timeout=100&dominoHost=http%3A%2F%2Finfofeed.sgx.com%2FApps%3FA%3DCOW_CorpAnnouncement_Content%26B%3D{0}%26R_C%3D%26C_T%3D{1}'.format(scope, limit)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Making the request to SGX
result = requests.get(url, headers=headers)
cleaned_result = result.content[4:]
result_obj = json.loads(cleaned_result)
# do we need to know about number of shares?
# num_of_shares = result_obj['SHARES']
items = result_obj['items']

# Writing results to csv file
with open('result.csv', 'wb') as csvfile:
    fieldnames = ['key', 'Date', 'Time', 'IssuerName', 'SecurityName', 'GroupCode', 'CategoryCode', 'CategoryName', 'AnnTitle', 'BroadcastDateTime', 'Siblings']
    my_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    my_writer.writeheader()
    for item in items:
        my_writer.writerow(item)
