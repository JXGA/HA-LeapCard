# HA-LeapCard

[![GitHub release](https://img.shields.io/github/release/xt16johnny/HA-LeapCard?color=dark-green)](#)

Display Transport For Ireland (TFI) Leap Card balance in Home Assistant

![HA_IMG](https://raw.githubusercontent.com/xt16johnny/HA-LeapCard/master/images/sensor_img.png)


# Instructions
1. Add leap_sensor files to /config/custom_components/leap_sensor folder
2. Add Leap Card credentials to configuration.yaml
```
 - platform: leap_sensor
   name: 'My Leap Card Balance'    # Optional, defaults to 'Leap Card Balance'
   username: 'username'            # Required
   password: 'password'            # Required
   (or better, password: !secret leap_pw)
```

# Notes
* This sensor uses an updated version of PyLeapCard by @skhg (https://github.com/skhg/pyleapcard).
* Limitations of PyLeapCard apply, for example only the first registered card will be displayed in HA.
* Multiple Leap Cards can be included in Home Assistant by using multiple copies of the 'leap_sensor' platform in configuration.yaml, just change the credentials.
* This module runs an update every 5 minutes. On HA load, it will show 'Unknown' until 5 minutes have passed. This allows HA to stabilise before pulling data from TFI.
* Don't forget to setup automations! Example below for Low Balance, but an increase of balance (i.e. top-up) could be done!
```
  - alias: Leap Balance
    initial_state: true
    trigger:
      platform: numeric_state
      entity_id: sensor.leap_card_balance
      below: 5
    action:
      - service: notify.ios_iphone
        data:
          title: "Leap: Balance Alert"
          message: "Balance Low!"
```
