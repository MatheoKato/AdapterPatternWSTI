from goldService import GoldService
from goldPriceReader import GoldPriceReader
from adapter import Adapter


gold_service = GoldService()
gold_price_reader = GoldPriceReader()
gold_service.get_price()
adapter = Adapter()
print(gold_service.get_price())
print(gold_price_reader.get_prices())
print(adapter.get_price())

