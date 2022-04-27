from datetime import datetime
from api_requests import ApiRequests
from database import Database
from endpoints.blockchair_bitcoin_stats import BitcoinStats
from endpoints.blockchair_ethereum_stats import EthereumStats
from endpoints.blockchair_waves_stats import WavesStats


class CryptoStatsDataProcessing:
    
    def start(self):
        blockchains = [BitcoinStats(), EthereumStats()]
        for item in blockchains:
            self.__getBlockchainStats(blockchain=item)

        self.__getCryptoStats(cryptoCurrency=WavesStats())


    def __getCryptoStats(self, cryptoCurrency):
        response = ApiRequests.getDataByGetRequest(cryptoCurrency.getUrl(), [])
        cryptoStats = response['data']

        attributes = [cryptoStats['transactions'], cryptoStats['transactions_24h'], datetime.today().date()]
        recordsToInsert = [tuple(attributes)]

        Database().insertDataIntoDatabase(entity=cryptoCurrency, recordsToInsert=recordsToInsert)


    def __getBlockchainStats(self, blockchain):
        response = ApiRequests.getDataByGetRequest(blockchain.getUrl(), [])
        cryptoStats = response['data']

        attributes = [cryptoStats['transactions'], cryptoStats['transactions_24h'], cryptoStats['average_transaction_fee_usd_24h'], cryptoStats['market_price_usd_change_24h_percentage'], cryptoStats['market_dominance_percentage']]
        recordsToInsert = [tuple(attributes)]

        Database().insertDataIntoDatabase(entity=blockchain, recordsToInsert=recordsToInsert)