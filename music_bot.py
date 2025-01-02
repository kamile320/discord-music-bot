import discord
from discord.ext import commands
import asyncio
import yt_dlp as youtube_dl
from discord import *


# Discord bot Initialization
version = 1.2
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=intents)
key = "Your Bot Token"
voice_clients = {}
yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
ffmpeg_options = {'options': "-vn -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 2"}


#ClientEvent
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


    #Commands
#1 - play
@client.command(name='play', help='Plays your YT video from URL')
async def play(ctx, *, url):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except:
        print("Can't connect to Voice Channel!\nYou should connect first!")

    try:
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options)
        voice_clients[ctx.guild.id].play(player)
        await ctx.send(f'Playing from source: ```{url}```')
    except Exception as err:
        print(err)
        await ctx.send('Something went wrong.\nDo you typed correct URL?')


#2 - pause
@client.command(name='pause', help='Pause playing music')
async def pause(ctx):
    try:
        voice_clients[ctx.guild.id].pause()
        await ctx.send('Paused')
    except Exception as err:
        print(err)


#3 - resume
@client.command(name='resume', help='Resume playing music')
async def resume(ctx):
    try:
        voice_clients[ctx.guild.id].resume()
        await ctx.send('Resumed')
    except Exception as err:
        print(err)


#4 - stop
@client.command(name='stop', help='Stop playing music')
async def stop(ctx):
    try:
        voice_clients[ctx.guild.id].stop()
        await ctx.send('Stopped')
    except Exception as err:
        print(err)


#5 - join
@client.command(name='join', help='Joins to Voice Channel')
async def join(ctx):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
        await ctx.reply('Joined Voice Channel')
    except Exception as err:
        print(err)


#6 - leave
@client.command(name='leave', help='Leaves Voice Channel')
async def leave(ctx):
    try:
        await voice_clients[ctx.guild.id].disconnect()
        await ctx.send('Left Voice Channel')
    except Exception as err:
        print(err)



client.run(key)
