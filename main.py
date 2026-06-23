import discord
# 1. Nova importação lá no topo como solicitado
from discord.ext import commands   
# Importando a função do seu arquivo de lógica
from bot_logic import gen_pass  

# Configuração dos privilégios (Intents)
intents = discord.Intents.default()
intents.message_content = True

# 2. Definindo o bot e o prefixo escolhido ($)
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'O bot {bot.user} está online e pronto para os comandos!')

# 3. Criando as funções usando o decorador @bot.command()

# Comando: $hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

# Comando: $pasw (Chama a função gen_pass passando o valor 10)
@bot.command()
async def pasw(ctx):
    senha = gen_pass(10)
    await ctx.send(f"Sua senha gerada: {senha}")
    
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


# Execução do bot (substitua pelo seu token caso tenha resetado)
bot.run("token")
