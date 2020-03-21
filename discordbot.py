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

    if message.content == '/hoge':
        await message.channel.send(file=discord.File('hogeimg.png'))

    if message.content == '/foo':
        await message.channel.send(file=discord.File('stamp/foo.jpg'))

    if message.content == '/bar':
        await message.channel.send(file=discord.File('stamp/bar.png'))


client.run(TOKEN)
