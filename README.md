# discord-music-bot

This is a Fixed Fork of [CreepyD246's Discord Music Bot](https://github.com/CreepyD246/discord-music-bot)  
Streams music from YT URL's. 

## Requirements
You'll need to install the following modules/libraries:  

For Linux:  
```Python3```  
```pip3 install yt_dlp```  
```pip3 install discord```  
```ffmpeg```

For Windows:  
```Python3```  
```pip install yt_dlp```  
```pip install discord```  
```ffmpeg*```  

You'll also need to create a Bot Application on [Discord Developer Portal](https://discord.com/developers/docs/intro)  

*On Windows You'll need to download and set up ffmpeg, like in the process of doing that in the [CreepyD246's tutorial video](https://youtu.be/xyVY4n4_0MQ).  
On linux just download package using your Package Manager (APT, Pacman, etc.)

## Features
- The bot can only play 1 song at a time and can't queue songs.
- The bot can pause, resume, and stop music
- The bot uses yt_dlp to stream the music, but doesn't download the music file onto the computer
