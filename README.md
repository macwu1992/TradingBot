# TradingBot
Cryptocurrency Trading Bot

加密货币交易机器人

功能模块：
1、通过与api交互，得到价格等信息
2、通过api进行买卖

用法：
在/TradingBot/Service/keys放入自己的私钥文件，json格式
数据库配置文件放在/TradingBot/database.json

上述两个文件自行配置
## Market APIs

1.[binance api](https://github.com/binance-exchange/binance-official-api-docs)

2.[huobi api](https://github.com/huobiapi/REST-API-demos)

---

目前项目设计：

1、将两个交易所的api封装为restful的api，并开发一个轻量级网站进行调用。以方便后续应用的开发。

2、将爬虫模块提取出来

3、简单策略的开发，均价以下5%挂单买入，均价以上5%卖出