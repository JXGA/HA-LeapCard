# HA-LeapCard

![GitHub release](https://img.shields.io/github/release/xt16johnny/HA-LeapCard?color=dark-green)

Display Dublin Leap Card balance in Home Assistant

![HA_IMG](https://raw.githubusercontent.com/xt16johnny/HA-LeapCard/master/images/sensor_img.png)


# Instructions
1. Add leap_sensor to your /config/custom_components/ folder
2. Add Leap Card credentials to 'leap_sensor/sensor.py'
3. Add the following to your configuration.yaml:
```
  - platform: leap_sensor
    scan_interval:
      minutes: 5
```

# Notes
* This sensor uses a Fork of PyLeapCard by @skhg (https://github.com/skhg/pyleapcard).
* Limitations of PyLeapCard apply, for example only the first registered card will be displayed in HA. 
* Scan_Interval required otherwise it will fetch the balance every 30 seconds. I feel 5 minutes is good enough for this use. 
* Don't forget to setup a low-balance automation!
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
