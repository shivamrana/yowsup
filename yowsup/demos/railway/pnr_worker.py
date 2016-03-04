import urllib2
import json


def get_pnr(pnr):
	request_url = 'http://api.railwayapi.com/pnr_status/pnr/%s/apikey/ttcuk4344/' % (pnr)
	request = urllib2.Request(request_url)
	response = urllib2.urlopen(request)
	data = json.load(response)
	
	if data["error"] == True:
		return "Wrong PNR!"

	train_number = data["train_num"]
	train_name = data["train_name"]
	doj = data["doj"]
	clas = data["class"]
	from_station = data["from_station"]["name"]
	to_station = data["to_station"]["name"]
	message = "Train Number: " + train_number
	message = message + "  Train Name: " + train_name
	message = message + "  DOJ: " + doj
	message = message + "  Class: " + clas
	message = message + "  From: " + from_station
	message = message + "  To: " + to_station
	for passenger in data["passengers"]:
		message = message + "  Passenger " + str(passenger["no"]) + ": "
		message = message + "  Booking Status: " + passenger["booking_status"]
		message = message + "  Current Status: " + passenger["current_status"]
	return message