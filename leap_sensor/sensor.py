from homeassistant.helpers.entity import Entity
import json
from pyleapcard import *

leap_username = "username"
leap_password = "password"

def leap_balance(user,password):
   session = LeapSession()

   session.try_login(user,password)
   overview = session.get_card_overview()

   encoded = (vars(overview))
   decoded = json.dumps(encoded)

   recoded = json.loads(decoded)
   balance_output = str(recoded["balance"])
   #print("Remaining Balance " + balance_output)
   return balance_output

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([LeapSensor()])


class LeapSensor(Entity):

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Leap Card Balance'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.
        """
        self._state = leap_balance(leap_username,leap_password)
