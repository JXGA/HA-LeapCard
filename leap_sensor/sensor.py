from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from datetime import timedelta
import voluptuous as vol
import json
from pyleapcardapi import *

CONF_NAME = 'name'
CONF_USERNAME = 'username'
CONF_PASSWORD = 'password'

SCAN_INTERVAL = timedelta(minutes=5)

DEFAULT_NAME = 'Leap Card Balance'
ICON = 'mdi:credit-card'

def leap_balance(username, password):
   session = LeapSession()

   session.try_login(username,password)
   overview = session.get_card_overview()

   recoded = json.loads(json.dumps(vars(overview)))

   balance_output = str(recoded["balance"])
   return balance_output

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_USERNAME): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    name = config.get(CONF_NAME)
    leap_username = config.get(CONF_USERNAME)
    leap_password = config.get(CONF_PASSWORD)
    add_devices([LeapSensor(name, leap_username, leap_password)])

class LeapSensor(Entity):

    def __init__(self, name, leap_username, leap_password):
        """Initialize the sensor."""
        self._state = None
        self._name = name
        self.username = leap_username
        self.password = leap_password

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return ICON

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor. """
        self._state = leap_balance(self.username, self.password)
