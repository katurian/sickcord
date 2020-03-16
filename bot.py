import discord
from sickweather import getMarkersInRadius, markerCountInRadius, getForecast, getWeatherMaps, getIllnesses, getSickScoreInRadius, getSickScoreByZipcode, getColdFluScoreInRadius, getAllergySickScoreInRadius, submitReport, api_key

client = discord.Client()

def riskColour(sickscore):
    if int(sickscore) >= 76 and int(sickscore) <= 100:
        return discord.Colour.red()
    if int(sickscore) >= 51 and int(sickscore) <= 75:
        return discord.Colour.orange()
    if int(sickscore) >= 26 and int(sickscore) <= 50:
        return discord.Colour.gold()
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
    if message.content.startswith('!zipcodes'):    
        embed = discord.Embed(title=f"Universities", description = "Postal codes for the !sszip command.", colour = discord.Colour.light_grey())
        embed.add_field(name="Stanford", value="94305")
        embed.add_field(name="MIT", value="02139")
        embed.add_field(name="Caltech", value="91125")
        embed.add_field(name="Princeton", value="08544")
        embed.add_field(name="USC", value="90007")
        embed.add_field(name="Brown", value="02912")
        embed.add_field(name="Columbia", value="10027")
        embed.add_field(name="UNC", value="28223")
        embed.add_field(name="Johns Hopkins", value="21218")
        embed.add_field(name="Harvard", value="02138")
        embed.add_field(name="UVA", value="22904")
        embed.add_field(name="UPenn", value="19104")
        embed.add_field(name="UMich", value="48109")
        embed.add_field(name="Northwestern", value="60201")
        embed.add_field(name="Georgetown", value="20057")
        await message.channel.send(embed=embed)
    if message.content.startswith('!illnesses'):    
        embed = discord.Embed(title=f"Illnesses", description = "Illness codes for the !sszip command.", colour = discord.Colour.gold())
        embed.add_field(name="Bronchitis", value="2")
        embed.add_field(name="Common Cold", value="4")
        embed.add_field(name="Flu", value="1")
        embed.add_field(name="Pneumonia", value="15")
        embed.add_field(name="RSV", value="33")
        embed.add_field(name="Strep Throat", value="7")
        embed.add_field(name="Ticks", value="46")
        embed.add_field(name="Lice", value="48")
        embed.add_field(name="Cough", value="6")
        embed.add_field(name="Fever", value="11")
        embed.add_field(name="Ear Infection", value="23")
        embed.add_field(name="Nasal Congestion", value="5")
        embed.add_field(name="Sinus Infection", value="20")
        embed.add_field(name="Sore Throat", value="21")
        embed.add_field(name="Pink Eye", value="22")
        await message.channel.send(embed=embed)

client.run('Njg1NjIzODg4MDMzXXXXXXXXXXXXXXXXXXX')
