# Work with Python 3.6
import discord
import time
import random
client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!anonymous hello'):
        msg = 'Hello {0.author.mention}, welcome! If you want to learn hacking, type !ddos {site/connections} . You can also trackback IPs by typing !track {ip} . Have Luck!'.format(message)
        await client.send_message(message.author, msg)
    if message.content.startswith('!ddos '):
        author = message.author
        vals = message.content.split(" ")
        site = vals[1]
        conns = vals[2]
        if int(conns) < 100:
            msg = 'Please enter a number over 100'
            await client.send_message(message.channel, msg)
        if int(conns) > 1000:
            msg = 'Please enter a number under 1000'
            await client.send_message(message.channel, msg)
        if int(conns) > 100:
            msg = ' :biohazard: Now we DDOS ' + str(site) + " :biohazard:".format(message)
            await client.send_message(message.channel, msg)
            for i in range(int(conns)):
                pass
            msg = ':biohazard: Finished attack for' + str(site) + " :biohazard:"
            await client.send_message(message.channel, msg)
            fin = random.randint(0,40)
            if fin > 0:
                msg = 'You are now a hacker :white_check_mark:'
                await client.send_message(message.channel, msg)
                time.sleep(0.5)
                try:
                    example = discord.utils.get(message.server.roles,name='DDOS-Hacker')
                    await client.add_roles(message.author, example)
                except discord.Forbidden:
                    print("Sorry")
            if fin == 0:
                msg = 'Website not down, please try again :negative_squared_cross_mark:'
                await client.send_message(message.channel, msg)
    if message.content.startswith('!track '):
        author = message.author
        vals = message.content.split(" ")
        ip = vals[1]
        msg = 'Trackback for ' + ip
        await client.send_message(message.channel, msg)
        example = discord.utils.get(message.server.roles,name='IP-Tracker')
        await client.add_roles(message.author, example)
        msg = 'You are now IP-Tracker'
        await client.send_message(message.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run('XXXXXXXXXXXXXXXXXXX') #Token
