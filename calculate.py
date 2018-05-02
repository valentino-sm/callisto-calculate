import json
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36')]

print("TH Diff: ",end='')
x = json.loads(opener.open("http://callistopool.org/api/stats").read().decode())
th_diff = float(x['nodes'][0]['difficulty']) / 1000 / 1000 / 1000 / 1000
print("%.6fGH" % th_diff)

print("Nicehash market: ", end='')
x = json.loads(opener.open("https://api.nicehash.com/api?method=orders.get&location=0&algo=20").read().decode())
x = sorted(x['result']['orders'], key=lambda x:float(x['price']))
for _ in x:
    if float(_['accepted_speed']) > 1:
        btc_ghash_day = float(_['price'])
        break
print("%.4f BTC/GH/day " % btc_ghash_day)

print("BTCUSD: ", end='')
x = json.loads(opener.open("https://api.coinmarketcap.com/v1/ticker/?limit=10").read().decode())
for _ in x:
    if _['symbol'] == 'BTC':
        btc_price = float(_['price_usd'])
print("%.2f$" % btc_price)

th_per_day = 60 * 60 * 24 / 1000
clo_per_block = 420
print("%.4f$ / CLO" % (btc_price * btc_ghash_day / (th_per_day / th_diff) / clo_per_block))
#print("%.4f$ / CLO" % (btc_price * btc_ghash_day  * network_ghash / clo_per_day))
