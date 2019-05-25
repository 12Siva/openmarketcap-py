# openmarketcap-py
Python wrapper around the https://openmarketcap.com/ api.

## Installation:

From source use

    $ python setup.py install

## API Documentation
**All results are cached for 60 seconds. Since currently OpenMarketCap doesn't update faster than once a minute.**

#### **`GET v1/tokens`**
- **`Description`** - This endpoint returns all cryptocurrency listings in one call. 
```python
>>> from openmarketcap import Market
>>> market = Market()
>>> market.get_tokens_data()

[Token(rank=1, name='Bitcoin', symbol='BTC', global_id='btc', price_usd='8029.60509350759300000000', volume_usd='1570865273.70', available_supply='17721612', price_change='-0.06', market_cap='142297545980.36528219991600000000', nvt='90.58545526644630555367'),
 Token(rank=2, name='Ethereum', symbol='ETH', global_id='eth', price_usd='250.61617315992385000000', volume_usd='302056894.17', available_supply='106217107', price_change='0.13', market_cap='26619724880.45815968730195000000', nvt='88.12818179040260138189'),
 Token(rank=3, name='XRP', symbol='XRP', global_id='xrp', price_usd='0.38513383041555826000', volume_usd='123992079.53', available_supply='42116677673', price_change='-0.88', market_cap='16220557396.57991088077272898000', nvt='130.81930279792857088775'),
 Token(rank=4, name='Bitcoin Cash', symbol='BCH', global_id='bch', price_usd='403.50781335065030000000', volume_usd='88405592.88', available_supply='17801750', price_change='-1.94', market_cap='7183145216.31493897802500000000', nvt='81.25215817584299173386'),
 Token(rank=5, name='Litecoin', symbol='LTC', global_id='ltc', price_usd='101.55359396395836000000', volume_usd='179461521.65', available_supply='61930651', price_change='0.11', market_cap='6289280185.57761177169236000000', nvt='35.04528507143420719843'),
 Token(rank=6, name='EOS', symbol='EOS', global_id='eos', price_usd='6.34869549489664600000', volume_usd='99490885.17', available_supply='913090691', price_change='-2.01', market_cap='5796934756.38376546972238600000', nvt='58.26598835138060587146'),
 Token(rank=7, name='Binance Coin', symbol='BNB', global_id='bnb', price_usd='35.00823960382590000000', volume_usd='359044792.21', available_supply='141175490', price_change='3.16', market_cap='4942305380.10752730719100000000', nvt='13.76514988474431299200')
 ...]
```