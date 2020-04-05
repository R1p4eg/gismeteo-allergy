from bs4 import BeautifulSoup
import logging

from homeassistant.helpers.aiohttp_client import async_get_clientsession


_LOGGER = logging.getLogger(__name__)


class GismeteoParser:
    def __init__(self, hass):
        self.hass = hass
        self.url = 'https://www.gismeteo.ru/weather-{0}/10-days/'
        self.session = async_get_clientsession(hass)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

    async def parse(self, city: str):
        try:
            url_parse = self.url.format(city)
            r = await self.session.get(
                url_parse,
                headers=self.headers)
            data = await r.text()

            soup = BeautifulSoup(data, features="html.parser")
            allergy_div = soup.find("div", {"data-widget-id": "allergy"})
            forecast = allergy_div.find_all("div", {'class': 'widget__item'})

            attributes = dict()

            for item in forecast:
                if not f"day_{item.attrs['data-item']}" in attributes:
                    attributes[f"day_{item.attrs['data-item']}"] = dict()
                date = item.find_all('div', {'class': 'w_date'})
                value = item.find_all('div', {'class': 'widget__value'})
                if date:
                    text_day = item.text.replace('\n', ' ')
                    attributes[f"day_{item.attrs['data-item']}"]['day'] = ' '.join(text_day.split())
                if value:
                    text_value = item.text.replace('\n', '')
                    attributes[f"day_{item.attrs['data-item']}"]['value'] = int(''.join(text_value.split()))
            return attributes

        except Exception as e:
            _LOGGER.error(f"Can't parse: {e}")

        return None