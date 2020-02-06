import discord


# アクセストークン(Acces token)
TOKEN = 'input the access token'

client = discord.Client()


# 起動時の処理(processing at startup)
@client.event
async def on_ready():
    print('We have logged in as %s' % client)

# メッセージを受信したとき、スタンプを送信する(output stamp if receive the message of keyword.)
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == '/img':
        await message.channel.send(file=discord.File('94b9510455559005c94619c7a81d23a2.png'))

    if message.content == '/1億':
        await message.channel.send(file=discord.File('stamp/1oku.jpg'))

    if message.content == '/古戦場':
        await message.channel.send(file=discord.File('stamp/kosenjo.png'))

    if message.content == '/ノルマ':
        await message.channel.send(file=discord.File('stamp/norma.png'))

    if message.content == "/ヨシ":
        await message.channel.send(file=discord.File('stamp/yosi.png'))


client.run(TOKEN)
