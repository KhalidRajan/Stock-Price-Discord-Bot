# Stock-Price-Discord-Bot
A Discord bot built in Python that provides EOD stock data

You can trigger this bot in any guild where it is configured by typing $stockPrice {date in format YYYY-MM-DD or the word "latest"} {Stock Ticker} {the word "open", "close", "high", "low", "volume" depending on what data you want}.

This bot only responds with End-of-day (EOD) stock data presently, as the MarketStack API only provides EOD and not real-time data in the free tier.
