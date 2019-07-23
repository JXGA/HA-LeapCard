# HA-LeapCard
Display Dublin Leap Card balance in Home Assistant

![HA_IMG](https://raw.githubusercontent.com/xt16johnny/HA-LeapCard/master/images/sensor_img.png)


# Instructions
1. Run 'pip3 install pyleapcard' - See note below regarding issue of PyLeapCard. 
2. Add leap_sensor to your /config/custom_components/ folder
3. Add Leap Card credentials to 'leap_sensor/sensor.py'
4. Add the following to your configuration.yaml:
```
  - platform: leap_sensor
    scan_interval:
      minutes: 5
```

# Notes
* Limitations of PyLeapCard apply, for example only the first registered card will be displayed in HA. (https://github.com/skhg/pyleapcard)
* Outstanding issue of PyLeapCard not yet resolved, and requires manual editing of PyLeapCard.py (https://github.com/skhg/pyleapcard/pull/6)
* Scan_Interval required otherwise it will fetch the balance every 30 seconds. I feel 5 minutes is good enough for my use. 
* Don't forget to setup a low-balance automation!
```
  - alias: Leap Balance
    initial_state: true
    trigger:
      platform: numeric_state
      entity_id: sensor.leap_card_balance
      below: 5
    action:
      - service: notify.ios_jiphone
        data:
          title: "Leap: Balance Low"
          message: "Johnny Balance Low!"
```
