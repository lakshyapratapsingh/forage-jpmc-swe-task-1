import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        # Sample quotes with information about stocks
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Iterate through each stock quote
        for quote in quotes:
            # Call the function getDataPoint with a stock quote
            stock, top_bid_price, top_ask_price, calculated_price = getDataPoint(quote)

            # Check if the values returned by getDataPoint match the expected values in the stock quote
            # We're making sure the stock name, bid price, ask price, and calculated price are correct
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(top_bid_price, float(quote['top_bid']['price']))
            self.assertEqual(top_ask_price, float(quote['top_ask']['price']))
            
            # Calculate what we expect the average price to be and check if it matches the calculated price
            expected_calculated_price = (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2
            self.assertAlmostEqual(calculated_price, expected_calculated_price)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        # Another set of stock quotes where bid price is greater than ask price
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Iterate through each stock quote
        for quote in quotes:
            # Call the function getDataPoint with a stock quote
            stock, top_bid_price, top_ask_price, calculated_price = getDataPoint(quote)

            # Check if the values returned by getDataPoint match the expected values in the stock quote
            # We're making sure the stock name, bid price, ask price, and calculated price are correct
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(top_bid_price, float(quote['top_bid']['price']))
            self.assertEqual(top_ask_price, float(quote['top_ask']['price']))
            
            # Calculate what we expect the average price to be and check if it matches the calculated price
            expected_calculated_price = (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2
            self.assertAlmostEqual(calculated_price, expected_calculated_price)

            # Additional check to make sure bid price is greater than ask price
            self.assertGreater(top_bid_price, top_ask_price)

    """ ------------ Add more unit tests ------------ """

if __name__ == '__main__':
    unittest.main()
