import discord, os, random
from discord.ext import commands
from generatore import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def inquinamento(ctx):
    with open('inquinamento.txt', 'r', encoding='utf-8') as f:
        
        await ctx.send(f.read())


@bot.command()
async def inquinamento2(ctx):
    with open('images/bottiglia.jpg', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

@bot.command()
async def inquinamento3(ctx):
    idee = ['utilizzare vetro','ridurre utilizzo di plastica' ,'non abbandonare rifiuti']
    risposta = random.choice(idee)
    await ctx.send(risposta)

@bot.command()
async def inquinamento4(ctx):
    with open('inquinamento.txt', 'w', encoding='utf-8') as f:
        new_text = 'Contaminazione dannosa dell ambiente'
        f.write(new_text)



bot.run("token")
