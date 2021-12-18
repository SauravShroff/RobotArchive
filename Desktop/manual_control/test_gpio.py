import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library
import keyboard
from sshkeyboard import listen_keyboard

GPIO.setmode(GPIO.BCM) 


GPIO.setup(13, GPIO.OUT)
pwm_R = GPIO.PWM(13, 10000)   # Initialize PWM on pwmPin 100Hz frequency

GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm_L = GPIO.PWM(12, 10000)   # Initialize PWM on pwmPin 100Hz frequency

global_speed = 0

pwm_R.start(global_speed)
pwm_L.start(global_speed)

def set_global_speed(speed):
  global_speed = speed
  pwm_R.ChangeDutyCycle(global_speed)
  pwm_L.ChangeDutyCycle(global_speed)

def set_left_speed(speed):
  pwm_R.ChangeDutyCycle(0)
  pwm_L.ChangeDutyCycle(speed)


def set_right_speed(speed):
  pwm_R.ChangeDutyCycle(speed)
  pwm_L.ChangeDutyCycle(0)

def increment_global_speed(increment):
  set_global_speed(max(min(global_speed + increment, 1), 0))

# try:
#   while True:                      # Loop until Ctl C is pressed to stop.
#     if keyboard.is_pressed('w'):
#       increment_global_speed(0.05)
#       print("ticked up bitch")
#     if keyboard.is_pressed('s'):
#       increment_global_speed(-0.05)
#       print("ticked down bitch")
#     time.sleep(0.25)
    
# except KeyboardInterrupt:
#   print("Ctl C pressed - ending program")

keep_listening = True

def key_press(key):
  print("IM HERE press")
  print(key + "fucker")
  #if escape is pressed make listening false and exit
  if key == "w":
    set_global_speed(100)
  if key == "a":
    set_left_speed(100)
  if key == "d":
    set_right_speed(100)
  if key == "^[":
    keepListening = False

def key_release(key):
  set_global_speed(0)
  print("IM HERE release")

listen_keyboard(
    on_press=key_press,
    on_release=key_release,
)



while keep_listening:
  pass

pwm_R.stop()                         
pwm_L.stop()
GPIO.cleanup()                     # resets GPIO ports used back to input mode

