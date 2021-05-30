import regex as re
import requests
import json

link = 'https://api.stocktwits.com/api/2/streams/trending.json?'

r = requests.get(link, allow_redirects=True)

# Lösung 1

# create regex that separates each full message
message_re = re.compile(r'"id":\d+,"body":.*?"sentiment":.*?}')

# check
len(message_re.findall(r.text))  # 30 since each request pull 30 tweets


# create regex for each sub-information using lookarounds
id_re = re.compile(r'(?<="id":)\d+(?=,)')

"""
YOUR REGEXES HERE
"""

# create results dict
results_dict = {'id': [],
                'user_id': [],
                'user_name':  [],
                'body':  [],
                'created_at':  [],
                'sentiment':  [],
                }

# first extract each message
messages = message_re.findall(r.text)

# than loop through messages
for m in messages:
    results_dict['id'].append(id_re.search(m).group())

"""
YOUR CODE HERE
"""

# Lösung 2

# This is a much easier solution to extract the data ;)
# load dictionary from JSON format
st_dict = json.loads(r.text)

# explore dict
st_dict.keys()

# explore first message with index 0
st_dict['messages'][0].keys()

# example: extract body text
st_dict['messages'][0]['body']
