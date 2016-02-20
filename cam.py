import RPi.GPIO as GPIO
import subprocess 
import time

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

Current_State  = 0 
Previous_State = 0

try:
 
  print "Waiting for PIR to settle ..."
 
  # Loop until PIR output is 0
  while GPIO.input(sensor)==1:
    Current_State = 0
 
  print "  Ready"
 
  # Loop until I quit with CTRL-C
  while True :
 
    # Read PIR state
    Current_State = GPIO.input(sensor)
 
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      start_time=time.time()
      print "  Motion detected!"
      subprocess.call("./camera.sh")
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      stop_time=time.time()
      print "  Ready ",
      elapsed_time=int(stop_time-start_time)
      print " (Elapsed time : " + str(elapsed_time) + " secs)"
      Previous_State=0
 
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
