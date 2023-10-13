import unittest
#  importing the class whose methods we want to test
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      dataPoint_ = getDataPoint(quote)
      stock_ = quote['stock']
      top_bid_price_ = quote['top_bid']['price']
      top_ask_price_ = quote['top_ask']['price']
      price_ = (top_bid_price_ + top_ask_price_) / 2
      self.assertEqual(dataPoint_, (stock_, top_bid_price_, top_ask_price_, price_))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      dataPoint_ = getDataPoint(quote)
      stock_ = quote['stock']
      top_bid_price_ = quote['top_bid']['price']
      top_ask_price_ = quote['top_ask']['price']
      price_ = (top_bid_price_ + top_ask_price_) / 2
      self.assertEqual(dataPoint_, (stock_, top_bid_price_, top_ask_price_, price_))


  def test_getRatio_priceA_IsZero(self):
    price_a = 0
    price_b = 121.68
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(price_a, price_b), 0.0)

  def test_getRatio_priceB_Is_Zero(self):
    price_a = 121.68
    price_b = 0
    """ ------------ Add the assertion below ------------ """
    try:
      getRatio(price_a, price_b)
    except ZeroDivisionError:
      self.fail("getRatio() raised ZeroDivisionError unexpectedly!")

  def test_getRatio_priceA_or_priceB_Is_Not_Float(self):
    price_a = 121.68
    price_b = 'zz'
    """ ------------ Add the assertion below ------------ """
    self.assertRaises(TypeError, getRatio, price_a, price_b)




if __name__ == '__main__':
    unittest.main()
