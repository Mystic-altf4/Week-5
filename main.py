
import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
username = "a"
msg = 0
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def tierlist(ctx):
    global username
    username = ctx.message.author.name

    imgName = random.choice(os.listdir('images'))
    
    with open(f'images/{imgName}' , 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

    await ctx.send(f'{username}, bu resim senin için!')
@bot.command()
async def human(ctx):
    await ctx.send("Arkadaşınız nasıl biridir?")
    await ctx.send("Eğer iyi tavırlı ve nazik geliyorsa ve yakından anlaşıyorsanız temiz insandır.")
    await ctx.send("Ama Eğer size karşı kaba davranıyorsa ve kötü biriyse kirli insandır.")
@bot.listen()
async def on_message(message):
    global username
    global msg
    username = message.author.name

    if message.author == bot.user:
        return
    #buglı hocaya sor
    elif message.author != bot.user:
        await message.channel.send(f'{username}, Merhaba!')
        msg += 1
        print(msg)
        if msg > 9:
            await message.channel.send(f'{username}, Çok mesaj attın, daha atarsan silerim!',delete_after = 3.0)
        await message.delete()







bot.run("TOKEN")
