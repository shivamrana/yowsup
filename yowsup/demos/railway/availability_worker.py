import urllib2
import json


def get_availability(train, src, dest, date):
	class_list = ["1A", "2A", "FC", "3A", "CC", "SL", "2S"]
	message = ""

	for clas in class_list:
		request_url = 'http://api.railwayapi.com/check_seat/train/%s/source/%s/dest/%s/date/%s/class/%s/quota/gn/apikey/ttcuk4344/' % (train, src, dest, date, clas)
		request = urllib2.Request(request_url)
		response = urllib2.urlopen(request)
		data = json.load(response)

		availability = data["availability"]
		if len(availability) > 0:
			message = message + " Class: " + clas
			message = message + " Status: " + availability[0]["status"]

	if len(message) == 0:
		return "You gave wrong query!"
	return message


