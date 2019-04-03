# -*- coding: utf-8 -*-
import mindwave,time

def bacadata():
	headset = mindwave.Headset('COM4', '1425')
	time.sleep(1)

	headset.connect()
	print "Connecting..."

	headset.status != 'connected':
	time.sleep(1)
		headset.status == 'standby':
		headset.connect()
		print "Retrying connect..."
	print "Connected."


	print headset.raw_value
	time.sleep(1)

bacadata() 



import mindwave,time,csv

def hasilcsv():
	headset = mindwave.Headset('COM4', '1425')
	time.sleep(1)
	 with open('hasil.csv', mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

	headset.connect()
	print "Connecting..."

	while headset.status != 'connected':
		time.sleep(1)
		if headset.status == 'standby':
			headset.connect()
			print "Retrying connect..."
	print "Connected."

	while True:
		print headset.raw_value
		time.sleep(1)
		
hasilcsv()