import discord
from sickweather import getMarkersInRadius, markerCountInRadius, getForecast, getWeatherMaps, getIllnesses, getSickScoreInRadius, getSickScoreByZipcode, getColdFluScoreInRadius, getAllergySickScoreInRadius, submitReport, api_key
import json

client = discord.Client()

def riskColour(sickscore):
    if int(sickscore) >= 76 and int(sickscore) <= 100:
        return discord.Colour.red()
    if int(sickscore) >= 51 and int(sickscore) <= 75:
        return discord.Colour.orange()
    if int(sickscore) >= 26 and int(sickscore) <= 50:
        return discord.Colour.yellow()
    else:
        return discord.Colour.blue()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!sszip'):    
        input = message.content[7:len(message.content)]
        parameters = input.split("_")
        # ---------
        score = getSickScoreByZipcode(parameters[0], parameters[1], int(parameters[2]))
        disease_name = score[1]['illness_word']
        sickscore = score[0]['sickscore_overall']
        timestamp = score[1]['timestamp']
        disease_sickscore = score[1]['sick_score']
        zipcode = score[1]['zip']
        country = score[1]['country']
        # ---------
        embed = discord.Embed(title=f"{country} postal code {zipcode} has a SickScore of {sickscore}", description = "https://enterprise.sickweather.com/console/documentation/#!/SickScore/getSickScoreByZipcode", colour = riskColour(sickscore))
        embed.add_field(name="Date", value=timestamp[0:10])
        embed.add_field(name=disease_name.capitalize(), value=int(disease_sickscore))
        await message.channel.send(embed=embed)
    if message.content.startswith('!sscoord'):    
        input = message.content[9:len(message.content)]
        parameters = input.split("_")
        # ---------
        score = getSickScoreInRadius(parameters[0], parameters[1])
        embed = discord.Embed(title=f"The SickScore in a 25 mile radius around latitude {parameters[0]} and longitude {parameters[1]} is N/A", description = "https://enterprise.sickweather.com/console/documentation/#!/SickScore/getSickScoreInRadius", colour = riskColour(sickscore))
        await message.channel.send(embed=embed)


    
client.run('TOKEN')
