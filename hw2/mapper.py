#!/usr/bin/env python
import sys
import json

def get_tweet(line):
	try:
		tweet = json.loads(line.strip())
	except:
		tweet = {}

	return tweet

for line in sys.stdin:
	tweet = get_tweet(line)

	# original tweets
	if "retweeted_status" not in tweet:
		# reply tweets
		if "in_reply_to_status_id" in tweet and tweet["in_reply_to_status_id"] != None:
			print("<%s, %s, %s, %s>" % (\
				tweet["id"],\
				tweet["user"]["id"],\
				tweet["in_reply_to_status_id"],\
				tweet["in_reply_to_user_id"]\
			))
