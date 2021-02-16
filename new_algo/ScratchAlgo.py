import ccxt


class CryptoGraph(object):

	def __init__(self, nodes):
		graph = {}
		# All nodes will be connected to one another
		for node in nodes:
			graph[node] = [i for i in nodes if i != node]
		self.graph = graph


ex = ccxt.binance()

rates = {
	'BTC/ETH':1000,
	'ETH/RPL':0.25,
	'RPL/BTC':0.04
}


for pair in fxgraph.keys():
	pass

