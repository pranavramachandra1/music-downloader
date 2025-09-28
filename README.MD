# MUSIC DOWNLOADER

Hello! This is a small locally-run app that you can use to download youtube audio files AND entire playlists. 

# Before getting started:

Run:

` pip install -r requirements.txt `

After, run:

`brew install ffmpeg`

# Troubleshooting:

This code is very minimal, so there are for sure some bugs and improvements to be made. 

When looking at a youtube link you might initially see:

> https://www.youtube.com/watch?v=6ayiOciWuto&list=RD6ayiOciWuto&start_radio=1

Remove all other arguments (list, radio, or whatever nonsense google decides to add to the end). 