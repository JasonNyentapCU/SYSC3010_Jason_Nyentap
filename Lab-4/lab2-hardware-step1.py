from sense_emu import SenseHat

sense = SenseHat()

counter = 0

while True:
	event = sense.stick.wait_for_event()
	if (event.action == "released"):
		if (event.direction == "up"):
			counter = counter + 1
		elif (event.direction == "down"):
			counter = counter - 1

		sense.show_message(str(counter), text_colour=[255, 0, 0])
