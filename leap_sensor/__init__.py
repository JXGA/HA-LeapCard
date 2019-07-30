""" TFI Leap Card Sensor for Home Assistant
Displays balance as a sensor, refreshing every 5 minutes.

Add the following to configuration.yaml

  - platform: leap_sensor
    name: 'My Leap Card Balance'    << Optional
    username: 'username'            << Required
    password: 'password'            << Required
    (or better, password: !secret leap_pw)

"""
