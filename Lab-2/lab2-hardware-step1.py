from sense_hat import SenseHat

sense = SenseHat()

first = True;

while True:
  event = sense.stick.wait_for_event()
  if (event.action == "released"):
    if(first):
      sense.show_letter('J')
    else:
      sense.show_letter('N')
    first = not first