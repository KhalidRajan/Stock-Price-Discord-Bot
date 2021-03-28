import discord
from discord.ext import commands
import os
import requests
from requests.exceptions import HTTPError
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN=os.getenv("DISCORD_TOKEN")

api_key=os.getenv("API_KEY")


bot=commands.Bot(command_prefix="$")


@bot.command(name="stockPrice", help="Returns eod data for a stock given the stock ticker and optionally a specified date")
async def stockPrice(ctx, *args):
    stock_ticker=args[0]  # Getting the stock symbol

    date=args[1] # Getting eod stock data for a specified date

    if date=="latest":
        date="latest"
    else:
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")

        except:
            raise ValueError

    # If the API request is not successful ("doesn't return status code 200), an exception will be raised and caught in the error handler
    try:
        response=requests.get("http://api.marketstack.com/v1/eod/"+date+"?access_key="+api_key+"&symbols="+stock_ticker)

        print("Successfully fetched data from API")

        output=response.json()
        if args[2]=="open":
            reply=output["data"][0]["open"]
        elif args[2]=="high":
            reply=output["data"][0]["high"]
        elif args[2]=="low":
            reply=output["data"][0]["low"]
        elif args[2]=="close":
            reply=output["data"][0]["close"]
        elif args[2]=="volume":
            reply=output["data"]["volume"]




        await ctx.send(reply) # Send the eod data back to the user if the api request is successful

    except:
        raise HTTPError


@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, HTTPError):
        await ctx.send("The Stock Ticker you entered does not exist.")
    elif isinstance(error, ValueError):
        await ctx.send("The date you entered is not in the correct format of YYYY-MM-DD or the word \"latest\"")


bot.run(TOKEN)


















