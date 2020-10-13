from discord.ext import commands		
 import os		
 import traceback		

 
  bot = commands.Bot(command_prefix='NH!')		
 token = os.environ['DISCORD_BOT_TOKEN']		

 
  @bot.event		
 async def on_command_error(ctx, error):		
     orig_error = getattr(error, "original", error)		
     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())		
     await ctx.send(error_msg)		

  client.on('ready', message =>		
 {		
   client.user.setPresence({ game: { name: 'Discord' } });  		

 
  @bot.command()		
 async def ping(ctx):		
     await ctx.send('pong!')		

      @bot.command()		
 async def 今何時？(ctx):		
     await ctx.send('これ見て'<\a>https://time.is/ja/Japan<a>)		

  if message.content('おはよう')		
     await message.channel.send('おはよう！')		

  bot.run(token)
