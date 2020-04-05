import logging
from datetime import timedelta

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, CONF_SCAN_INTERVAL
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_call_later
from homeassistant.helpers.typing import HomeAssistantType

from .utils import GismeteoParser

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'gismeteo_allergy'

SCAN_INTERVAL = timedelta(hours=12)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required('city'): cv.string,
    vol.Optional(CONF_NAME): cv.string,
    vol.Optional(CONF_SCAN_INTERVAL, default=SCAN_INTERVAL): cv.time_period
})


async def async_setup_platform(hass: HomeAssistantType, config: dict,
                               add_entities, discovery_info=None):
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = GismeteoParser(hass)

    add_entities([GismeteoAllergy(config, hass.data[DOMAIN])])

    return True


class GismeteoAllergy(Entity):
    def __init__(self, config: dict, parser: GismeteoParser):
        self._name = config.get(CONF_NAME)
        self._city = config['city']
        self._delay = config[CONF_SCAN_INTERVAL].total_seconds()

        self._parser = parser
        self._attrs = None

    async def async_added_to_hass(self) -> None:
        self.hass.async_create_task(self.update())

    @property
    def should_poll(self) -> bool:
        return False

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._attrs['day_0']['value'] if self._attrs else None

    @property
    def state_attributes(self):
        return self._attrs

    @property
    def unit_of_measurement(self):
        return 'ед./м3'

    async def update(self):
        _LOGGER.debug(f"Update {self.entity_id}")

        self._attrs = await self._parser.parse(self._city)

        self.async_schedule_update_ha_state()

        delay = self._delay if self._attrs else 60
        async_call_later(self.hass, delay, self.update())