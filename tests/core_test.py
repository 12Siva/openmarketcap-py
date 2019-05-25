import unittest
from openmarketcap import Market


class CoreTest(unittest.TestCase):

    def test_listings_Successful(self):
        market = Market()
        listings = market.listings()
        self.assertIsNotNone(listings, "Listings should not be none.")


if __name__ == '__main__':
    unittest.main()
