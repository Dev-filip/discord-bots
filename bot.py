import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} je aktivní')
    print("""
  _______  _______ _________ _______  _______ _________ _______ 
 (  ____ \(  ____ \\__   __/(  ____ \(  ____ )\__   __/(  ____ \
 | (    \/| (    \/   ) (   | (    \/| (    )|   ) (   | (    \/
 | (__    | (_____    | |   | (__    | (____)|   | |   | (_____ 
 |  __)   (_____  )   | |   |  __)   |     __)   | |   (_____  )
 | (            ) |   | |   | (      | (\ (      | |         ) |
 | (____/\/\____) |   | |   | (____/\| ) \ \_____) (___/\____) |
 (_______/\_______)   )_(   (_______/|/   \__/\_______/\_______)
                                                               
    """) 

@bot.command()
async def ruby(ctx, user_id: int, count: int):
    user = await bot.fetch_user(user_id)
    
    embed = discord.Embed(
        title=f"Hráč **{user.name}** si právě zakoupil **{count}** rubínů!", 
        color=discord.Color(0x800080)  
    )
    
    embed.add_field(name="Děkujeme!", value="Děkujeme za tvou podporu! Užij si své rubíny.", inline=False)
    embed.add_field(name="Informace", value="Pro zakoupení rubínů, kontaktuj majitele do dm.", inline=False)
    
    embed.set_thumbnail(url=user.avatar.url)

    embed.set_footer(
        text="Esteris | 2024",
        icon_url="https://media.discordapp.net/attachments/1221123386457980998/1239617221559451749/logo.png?ex=66d9de00&is=66d88c80&hm=ee92f070fd096f9d3e6e43b7bc76e8610ddad2356e0f88b7b47f6b29e45ea95e&=&format=webp&quality=lossless"
    )

    await ctx.send(embed=embed)


bot.run('Insert bot token here <3')
