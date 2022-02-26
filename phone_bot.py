
import requests,json,discord
from discord.ext import commands
bot = commands.Bot(command_prefix='>')
import time

token = '5sim api key'
country = 'russia'
operator = 'any'
product = 'discord'
bot_token = 'discordbot token'
headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}


# def get_sms(self):
#     response1 = requests.get('https://5sim.net/v1/user/check/' + id, headers=headers)
#     response1 = response1.json()
#     response1 = response1['text']
#     return response1
def discordx():
    @bot.command()
    async def get(ctx):
        await ctx.send("getting number....")
        number = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)
        number = number.json()
        no_id = str(number['id'])
        number = number['phone']
        await ctx.send("Successfully Claimed Number for Discord :"+ number)
        await ctx.send("your inbox id : "+no_id)
    @bot.command()
    async def getsms(ctx,id):
        await ctx.send("looking for messages....")
        code = requests.get('https://5sim.net/v1/user/check/' + str(id), headers=headers)
        code = code.text
        await ctx.send("Here is your message: "+code)



    bot.run(bot_token)
discordx()
