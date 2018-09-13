![Discord](https://cdn.vox-cdn.com/thumbor/ZpYQ4euN1Ce0mut6-NC-0SFR7GY=/0x0:2400x1600/1200x800/filters:focal(1008x608:1392x992)/cdn.vox-cdn.com/uploads/chorus_image/image/60778543/discord_logo_wordmark_2400.0.jpg)
[Image Source](https://www.polygon.com/2018/8/9/17665340/discord-game-sales-thq-deep-silver)

Hello everyone! This is my  first contribution after changing my account from @rodus to @rodux due to some difficulties. I've been working on this for some time. I started this bot while creating tutorials. In tutorials, I created commands but I wanted to improve it and here I am after improving it. If you don't know about this then here's a brief introduction for you.
### Github Repository
https://github.com/Rodux7/DiscordSteem
### Introduction
DiscordSteem is a bot built in Python language, using two main libraries. The first one is "Beem" and the second one is "Discord.py". This bot has many cool commands that you can use to get quick access to posts, comments, or even specifically contributions.
### Commands
Here are commands that bot has at the moment. I will be adding more commands in the future but these are the ones that are present at the moment.
- Blog Command
- Feed Command
- Comments Command
- Contributions Command
- Info Command
- Ticker Command
- Notes Commands
#### Blog Command
The first command is Blog Command. You will be able to get blog posts of any user using this command. Usage of this command is ```!blog <user> <amount>```.  There is one required parameter and the other one is optional. The required parameter is the "user", and this will be the username of any Steemit user whose blog you want. The second parameter which is optional is "amount" which is going to be the amount of posts you want. By default, this amount is set to 3. Here's how it looks like when it is working!

![Screenshot from 2018-09-12 19-59-11.png](https://ipfs.busy.org/ipfs/QmaDWo1zDqjQicUghG9AHRKDZUiaaw25mXwJ7HRnnAVGJN)

Clicking on "Check out this post!" will take you to the original post on Steemit. You can also assign the amount of post like down in the below image.

![Screenshot from 2018-09-12 20-04-18.png](https://ipfs.busy.org/ipfs/QmTsyPw6XmxP8JYjLwaaaiq52iCAA5tWvuwP2keFAMAJAv)

#### Feed Command
You will be able to get feed of any user using this command. Usage of this command is very similar to the last command. You can use this command by typing ```!feed <user> <amount>```. Again, there are two parameters that you can assign and out of those two parameters, one is required while other is not. Amount is set to 3 by default like last one. Here's how it looks when it is working.

![Screenshot from 2018-09-12 20-11-10.png](https://ipfs.busy.org/ipfs/QmdyqJXdLSyH1K3u5xgMx4Cdip67MmH9J1vwngzxfnTyUX)

Here's how it looks when we assign the custom amount.

![Screenshot from 2018-09-12 20-13-37.png](https://ipfs.busy.org/ipfs/QmPSFFjcoaet2mRPF7kFbvX1mfiYUHr2vGTPNPt61FFhAM)

### Comments Command
Using this command you will be able to get last comments of any user. Usage of this command is also very similar to last ones. Usage of this command is ```!comments <user> <amount>```. User will be any Steem user and it is required. The amount is optional and is set to 3 by default. Here's how it works!

![Screenshot from 2018-09-12 20-27-05.png](https://ipfs.busy.org/ipfs/QmZzCgWkKuc52bgK6NrHD5R6MrYpokqCTfqC5iYcFHgLsB)

Since comments don't actually have it's own title and I can't show full comment due to character limit, I used the title of the post in which comment was made. Here's how it works when we assign the amount.

![Screenshot from 2018-09-12 20-29-04.png](https://ipfs.busy.org/ipfs/QmRF8a7sxUDeAkXP2kFRGw8cAsrMzC5Vaw5sNXXwxjBCyR)

#### Contributions Command
Using this command, user will be able to check anyone's contributions that they have submitted through Utopian. This command will also be used like other commands ```!contributions <user> <amount>```. User will be any Steem username and amount will be any number. By default, is is 3.

![Screenshot from 2018-09-12 20-34-22.png](https://ipfs.busy.org/ipfs/Qma4Fs1EJxun1noy4j3waSqSXq7Lmf9aKpvDhNqjTB7JjF)

*Shoutout to @scipio for making awesome tutorials!*
#### Info Command
This command will give general information about any account like how many followers it has, how many people is account following, how many witnesses is account voting for and more. You can use this command by typing ```!info <user>```. User will be any Steem username and this is required. Here's how it works.

![Screenshot from 2018-09-12 20-39-12.png](https://ipfs.busy.org/ipfs/QmXGB5zhr3gbLGjj2X18wS38UAkX4hDJuXEaWsfX7EwKxq)

#### Ticker Command
This command can be used to get price of different coins in different currencies. You can use this command by typing ```!ticker <coin> <currency>```. Coin is necessary, while currency is set to USD by default. These currencies are supported at the moment.
> "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"

Here's how command looks when it working and correct parameters are assigned. As you can see in the below image, there should be full name of the coin. Short forms won't work.

![Screenshot from 2018-09-12 20-48-36.png](https://ipfs.busy.org/ipfs/QmcUvcj46oB3PXLBTFTwiEq3bchzMYx4wkQdrfpkLCexbX)

You can assign different currencies and coins like done in the image below.

![Screenshot from 2018-09-12 20-51-09.png](https://ipfs.busy.org/ipfs/QmXJJp4LqRKMBcyb9DvkSf4HpJmRckrTsEJaNzDohja1rQ)

#### Notes Commands
Notes commands are actually three commands that you can use to add, recall or delete notes. I have used PyMongo to store the notes in case the script stops. The three commands are ```!addnote "<note>"```, ```!note``` and ```!delnote```. When you add note, make sure that it is in quotation marks.```!note``` will recall notes and ```!delnote``` will delete all the notes.

![Screenshot from 2018-09-12 21-56-32.png](https://ipfs.busy.org/ipfs/QmWtKq3EbyETKQh3UZGJHwStDrdTnJQE2TkVouSJbQQNuK)

### How To Set It Up To Be Used In Server
First of all open the terminal and type ```git clone https://github.com/Rodux7/DiscordSteem```. This will clone the github repository, make sure you have the "git" installed.

After cloning the repository, run this command in the terminal ```sudo apt-get install build-essential libssl-dev python-dev```. This is necessary for the installation of Beem which is required for the bot to function properly. Now proceed to the directory by typing ```cd DiscordSteem```. Inside it type ```pip install -r requirements.txt```. This will install other necessary things.

Now go to [Discord Developer Page](https://discordapp.com/developers) and login. Create a new application and get the token. You can learn in depth from [here](https://steemit.com/utopian-io/@rodus/bots-in-python-2-or-creating-discord-bot-that-uses-beem-to-get-information-or-discordsteem-or-part-1). Replace the token in the DiscordSteem file. Add the bot to the discord server which is also present in [this link](https://steemit.com/utopian-io/@rodus/bots-in-python-2-or-creating-discord-bot-that-uses-beem-to-get-information-or-discordsteem-or-part-1). You can now run the bot by typing ```python DiscordSteem.py``` and this will make the bot online and commands will be working!
### Tutorials
If anyone of you are curious into looking how basic commands of this bot were made, you should look into the tutorials that are present below.
- [DiscordSteem (Part 3)](https://steemit.com/utopian-io/@rodus/bots-in-python-2-or-creating-ticker-and-notes-commands-or-discordsteem-or-part-3-1535188272667)
- [DiscordSteem (Part 2)](https://steemit.com/utopian-io/@rodus/bots-in-python-2-or-removing-improving-and-adding-commands-or-discordsteem-or-part-2)
- [DiscordSteem (Part 1)](https://steemit.com/utopian-io/@rodus/bots-in-python-2-or-creating-discord-bot-that-uses-beem-to-get-information-or-discordsteem-or-part-1)
### Have Fun!
