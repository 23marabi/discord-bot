# bot.py
import discord
from discord.ext import commands
from random import choice, randrange
import pickle

images = ['bugfact.jpg','HAM.gif','Birb.png']
links = ['https://youtu.be/VD3TwFgPgZE','https://tenor.com/view/bouncy-garfield-cursed-im-sorry-jon-gif-15620009','https://cdn.discordapp.com/attachments/440261154439168001/700080379184545802/i249711442305187847.mp4','https://cdn.discordapp.com/attachments/297468195026239489/702777283701768213/nice_jacket.mp4','https://cdn.discordapp.com/attachments/531909307713847298/699422329066881126/KdEBTrVoc3TtSHya.mp4','https://cdn.discordapp.com/attachments/427106958152040448/697154909191012412/video0.mp4','https://cdn.discordapp.com/attachments/371829694728896514/696101353390604429/mario_die.mp4','https://cdn.discordapp.com/attachments/676207686353944576/696581605975916544/9dabc3a419518857.mp4','https://media.discordapp.net/attachments/628799245482459148/684630155762597911/bb9a8d9a843ada7e4acc71ad22ec6e8f209a4fa469ddf010559a05997e1d4d7a_1.gif.gif?RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_RAT_']

TOKEN = 'bot-token-here'

bot = commands.Bot(command_prefix=';')

def generate_ip():
    part1 = randrange(100,220)
    part2 = randrange(10,170)
    part3 = randrange(0,50)
    part4 = randrange(0,256)
    ip = str(part1)+'.'+str(part2)+'.'+str(part3)+'.'+str(part4)
    return ip

def log(msg):
    with open("log", "a") as myfile:
        myfile.write(msg)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello {0}!'.format(ctx.author))
    log("- sent hello"+"\n")

@bot.command()
async def customlog(ctx, arg):
    await ctx.send('Logged {0}'.format(arg))
    log("- "+arg+"\n")

@bot.command()
async def image(ctx):
    img = choice(images)
    await ctx.send(file=discord.File(img))
    log("- sent image "+img+"\n")

@bot.command()
async def rand(ctx):
    num = randrange(-52453465326,635725483853785)
    await ctx.send(num)
    log("- sent random number "+str(num)+"\n")

@bot.command()
async def ip(ctx):
    user_ip = generate_ip()
    await ctx.send(('{0}, Your IP is '+user_ip).format(ctx.author))
    log("- sent ip "+user_ip+"\n")

@bot.command()
async def video(ctx):
    link = choice(links)
    await ctx.send(link)
    log("- sent link "+link+"\n")

@bot.command()
async def nitro(ctx):
    await ctx.send(file=discord.File('nitro.gif'))
    log("- sent free nitro"+"\n")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
