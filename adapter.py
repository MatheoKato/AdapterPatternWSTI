import requests
import json
from goldService import GoldService
from goldPriceReader import GoldPriceReader


class Adapter(GoldService, GoldPriceReader):

    def get_price(self) -> str:
        return GoldPriceReader().get_prices()
