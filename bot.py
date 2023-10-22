import discord, responses, re, os
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
USERS_WHITE_LIST = [224957447096238081]
USERS_BLACK_LIST = []
CURRENT_PREFIX = '?'

async def send_message(message: discord.Message, user_mesage: str, is_private: bool):
    try:
        response = responses.handle_response(message.channel.id, user_mesage)
        if len(response) > 0:
            await message.author.send(response) if is_private else await message.channel.send(response) 
    except Exception as e:
        print(e)

async def add_reaction(reaction: discord.Reaction, user: discord.User):
    try:
        await reaction.message.add_reaction('💖')     
    except Exception as e:
        print(e)
        
def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    
    @client.event
    async def on_ready():
        await tree.sync(guild=discord.Object(id=322616525527973890))
        print(f'{client.user} is now running!')
        
    @client.event
    async def on_message(message: discord.Message):
        if message.author.id not in USERS_WHITE_LIST or message.author == client.user or message.author.bot:
            return
        user_name = str(message.author.name)
        user_message = str(message.content)
        channel = str(message.channel.name)
        
        print(f'{user_name} said: {user_message} in {channel}')
        
        if len(user_message) > 0 and re.search(f'^\{CURRENT_PREFIX}.+', user_message):
            command = user_message[len(CURRENT_PREFIX):]
            await send_message(message, command, is_private=False)
            
    @client.event
    async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
        if user.id not in USERS_WHITE_LIST or user.bot:
            return
        await add_reaction(reaction, user)
    
    @tree.command(name='roll', description= 'Mudae rolls', guild=discord.Object(id=322616525527973890))
    @app_commands.describe(type='Roll type(wa | ha | ma)', amount='Times to roll')
    async def first_command(interaction: discord.Interaction, type: str, amount: int):
        if (interaction.user.id in USERS_BLACK_LIST):
            await interaction.response.send_message('You are blacklisted')
            return
        if (type not in ['wa', 'ha', 'ma']):
            await interaction.response.send_message(f'Type {type} is not valid')
            return
        await interaction.response.send_message(f'Rolling for {type}!')
        responses.handle_response(interaction.channel_id, f'{type} {amount}')

    client.run(BOT_TOKEN)
