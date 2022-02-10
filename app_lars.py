#import modules
import emoji

#import classes
from twitter_tweets_by_user import TwitterTweetsByUser
from twitter_users import TwitterUsers
from api_requests import ApiRequests
from database import Database
from waves_market_prices import WavesMarketPrices

#get data from api call

#get twitter user data
data = ApiRequests.getData(url=TwitterUsers.url, headers=TwitterUsers.headers)
Database.executeInsertStatement(TwitterUsers.tableName, data, TwitterUsers.tableAttributes, TwitterUsers.dynamicValues)
Database.executeSelectQuery(TwitterUsers.tableName)

#get waves market price data
data = ApiRequests.getData(url=WavesMarketPrices.url, headers=WavesMarketPrices.headers)
print(data)
Database.executeInsertStatement(WavesMarketPrices.tableName, data, WavesMarketPrices.tableAttributes, WavesMarketPrices.dynamicValues)

#get twitter tweets by user
data = ApiRequests.getData(url=TwitterTweetsByUser.url, headers=TwitterTweetsByUser.headers)
for d in data:
    d['text'] = emoji.demojize(d['text'])
print(data)
#Database.executeInsertStatement(TwitterTweetsByUser.tableName, data, TwitterTweetsByUser.tableAttributes, TwitterTweetsByUser.dynamicValues)
