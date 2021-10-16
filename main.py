from GoogleNews import GoogleNews
from discord.colour import Color
import discord
from discord.ext import commands
from discord import Intents
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext



googlenews = GoogleNews()

bot = commands.Bot(command_prefix='-')
slash = SlashCommand(bot, sync_commands = True)

@slash.slash(
    name ="hello",
    description='testing message'
)
async def _hello(ctx:SlashContext):
    await ctx.send("hey")


@slash.slash(name='say', description = 'a testing command')
async def _say(ctx:SlashContext, *, text):
    say_em = discord.Embed(
        title = text, 
        colour = discord.Color.dark_grey()
    )
    await ctx.send(embed = say_em)


@slash.slash(name = 'news', description = 'shows you news regarding the topic you are interested in', guild_ids=[802781269494726677])
async def _news(ctx: SlashContext, *, search):
    sear = str(search)
    googlenews = GoogleNews(lang='en', period='10d')
    googlenews.search(search)
    #googlenews.get_page(2)
    googlenews.page_at(2)

    texts = googlenews.get_texts()
    urls = googlenews.get_links()
    img = googlenews.get_texts()
    news_em = discord.Embed(
        title = f'News regarding {sear}', 
        color = discord.Color.dark_gold(), 
    )
    

    for j in range(10, len(img)):
        news_em.add_field(name=str(img[j]), value=f'[Click to read the full article]({str(urls[j])}) \n --------- \n', inline=False)
    await ctx.send(embed = news_em)


bot.remove_command('help')
@bot.command()
async def test(ctx):
    await ctx.send("Bot is functional!")

@bot.command()
async def invite(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=898497859257769984&permissions=0&scope=bot%20applications.commands')
@bot.command()
async def news(ctx, *, search):
    sear = str(search)
    googlenews = GoogleNews(lang='en', period='10d')
    googlenews.search(search)
    #googlenews.get_page(2)
    googlenews.page_at(2)

    texts = googlenews.get_texts()
    urls = googlenews.get_links()
    img = googlenews.get_texts()
    news_em = discord.Embed(
        title = f'News regarding {sear}', 
        color = discord.Color.dark_gold(), 
    )
    

    for j in range(10, len(img)):
        news_em.add_field(name=str(img[j]), value=f'[Click to read the full article]({str(urls[j])}) \n --------- \n', inline=False)
    await ctx.send(embed = news_em)

        

@bot.command()
async def help(ctx):
    help_em = discord.Embed(
        title = 'Noah Miller, v0.1', 
        color = discord.Color.red()
    )
    help_em.add_field(name = 'About:', value=f'Hey, Im Noah Miller. Im a bot designed by <@452737276812984330>. \n I am basically a news bot which shows the user **the latest news**, regarding the topic the user asks for.', inline=False)
    help_em.add_field(name = 'Commands: ', value=f'Write `-cmd` to know the commands')
    help_em.set_footer(text = 'v1.0 [Unreleased]')
    await ctx.send(embed = help_em)

@bot.command()
async def cmd(ctx):
    cmd_em = discord.Embed(
        title = 'Commands for Noah', 
        colour = discord.Color.dark_gold()
    )
    cmd_em.add_field(name = 'News Command', value='```-news [topic you want to search]``` ```-help, -cmd```')
    await ctx.send(embed = cmd_em)



@bot.event
async def on_ready():
    print(f'{bot.user} is online')
bot.run('ODk4ODQzMTcyMzI5ODkzOTA4.YWqG7w.wqyEXSLAaEXlsMX5Ljtfwd5H57g')


