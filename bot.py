import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
from discord import Game
import random
import urllib
import urllib.request
from discord.utils import get






bot_token = os.environ['BOT_TOKEN']



Bot = commands.Bot(command_prefix = "!")

@Bot.event
async def on_ready():
    print("Bot is ready")
    
@Bot.event
async def on_member_join(member):



    server = member.server.default_channel

    fmt = ' {0.mention} :tada:  :heart: اهلا وسهلا نورت سيرفرنا !'
    channel = member.server.get_channel("453675065876152330")


    await Bot.send_message(channel, fmt.format(member, server))

@Bot.event
async def on_member_remove(member):
    
    server = member.server.default_channel
    fmt = '{0.mention} :slight_frown: غادر للاسف'
    channel = member.server.get_channel("453675065876152330")
    await Bot.send_message(channel,fmt.format(member, server))        
@Bot.event
async def on_message(message):
    if message.content == "هلا":
        userID = message.author.id
        await Bot.send_message(message.channel,"  <@%s> :raised_hand:  أهلين وسهلين  "% (userID))
        
        
    if message.content == "كلب":
        userID = message.author.id
        await Bot.send_message(message.channel,"  <@%s> :rage:   لا تسب  " % (userID))
    

    if message.content == "محمد":
         msg = discord.Embed(title=' :red_circle:', colour=808080)
         msg.set_author(name="Moh", icon_url="http://www9.0zz0.com/2018/06/12/01/785068534.png")
         msg.set_footer( text=' Do Not Disturb')
         await Bot.send_message(message.channel,embed=msg)
         
         
        
         
         
    if message.content == "نايف":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> نايف  " % (userID))
        


    if message.content == "اسحبوني":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :smirk:  والله ما نسحبك  " % (userID))

    if message.content == "تسمعني":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :upside_down:  لا  " % (userID))

    if message.content == "يحيى":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> يحيى  " % (userID))

    if message.content == "مازن":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>  مازن " % (userID))

    if message.content == "حمد":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :sunglasses:  حمد " % (userID))


    if message.content == "برب":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :walking:  خذ راحتك " % (userID))
         
    if message.content == "باك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :top:  ولكم باك " % (userID))

         
    if message.content == "كل زق":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :rage:  عيب يا بابا  " % (userID))

         
    if message.content == "كل تبن":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :rage:  عيب يا بابا  " % (userID))
         
    if message.content == "بوت":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> هلا؟ " % (userID))
         
            

    if message.content == "من يلعب؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :upside_down: جدتي " % (userID))
         await Bot.send_message(message.channel,"  <@%s> :cry:  أمزح ,تلعبو بدوني؟ " % (userID))

         
    if message.content == "من يلعب":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :upside_down: جدتي " % (userID))
         await Bot.send_message(message.channel,"  <@%s> :cry:  أمزح ,تلعبو بدوني؟ " % (userID))

    if message.content == "عمان":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :flag_om:   " % (userID))

         
    if message.content == "السعودية":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :flag_sa:   " % (userID))

    if message.content == "الكويت":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>  :flag_kw:   " % (userID))

         

    if message.content == "الامارات":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>  :flag_ae:   " % (userID))

    if message.content == "البحرين":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>  :flag_bh:    " % (userID))

         

    if message.content == "قطر":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>   :flag_qa:    " % (userID))
         
    if message.content == "العراق":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>   :flag_iq:     " % (userID))
         

    if message.content == "تلعب":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :exclamation:  مشغول الحين سوري " % (userID))


    if message.content == "دقيقة":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :unamused:  أوك بس لا تطول " % (userID))

         
    if message.content == "ثواني":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :unamused:  أوك بس لا تطول " % (userID))   
         
    if message.content == "مرحبا":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :v: مرحبتين " % (userID))

         
    if message.content == "شرايك ف البوت":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart_eyes: مبدع  " % (userID))

    if message.content == "holycow":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :thinking: مين هاذا ؟ " % (userID))
         await Bot.send_message(message.channel,"  <@%s> اها قصدك Therealholycow " % (userID))

    if message.content == "يب":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :cool:  " % (userID))
         
    if message.content == "حمار":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :rage: عيب يا بابا  " % (userID))
         
    if message.content == "يا حمار":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :rage: عيب يا بابا  " % (userID))
         
    if message.content == "اصبر":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :frowning2:  " % (userID))
        
    if message.content == "ايش بتسوي":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :upside_down: ولا شي امزح  " % (userID)) 
        
    if message.content == "هاي":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart_eyes_cat:  هايات     " % (userID))  
        
    if message.content == "باي":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :walking:  الله معك     " % (userID)) 
        
    if message.content == "شباب":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :no_mouth:  أمر اخوي ايش بغيت   " % (userID))   
        
    if message.content == "السلام عليكم":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart:  وعليكم السلام ورحمة الله وبركاته " % (userID)) 
        
    if message.content == "استغفر الله":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart:  أستغفر الله " % (userID)) 
         await Bot.send_message(message.channel,"  <@%s> :yellow_heart:  أستغفر الله " % (userID))  
         await Bot.send_message(message.channel,"  <@%s> :blue_heart:  أستغفر الله " % (userID))
        
    if message.content == "هايبكسل":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :persevere:  مالي نفس العبها والله " % (userID)) 
        
    if message.content == "ازك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))
        
    if message.content == "أزك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID)) 
        
    if message.content == "سيرفر ازك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))
        
    if message.content == "azk":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))  
        
    if message.content == "AZK":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))   
        
    if message.content == "افا":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ايه والله افا بس " % (userID))
        
    if message.content == "احبك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :blush:  لا تحرجني " % (userID))  
        
    if message.content == "بخير الحمدلله":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart:  عسى دووم " % (userID)) 
        
    if message.content == "اذكار":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :blue_heart:  سبحان الله   والحمد لله ولا إله إلا الله و الحمد لله حمداَ كثيرا" % (userID))    
        
    if message.content == "كيف الحال":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> بخيير الحمد لله , علومك انت " % (userID))  
        
    if message.content == "بخير ابشرك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> عسى دوووم " % (userID))
        
    if message.content == "بخير":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> عسى دوووم " % (userID))
        
    if message.content == "تعالو ازك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))
        
    if message.content == "تعال ازك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))
      
    if message.content == "تعال سيرفر ازك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))
        
    if message.content == "حياك بسيرفر ازك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))
        
    if message.content == "حياك بأزك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :name_badge:  خلاص كفاية سحب اعضاء " % (userID))
        
    if message.content == "ultracraft":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart_eyes: :heart:  احسن سيرفر" % (userID))
        
    if message.content == "الترا كرافت":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart_eyes: :heart:  احسن سيرفر" % (userID))
        
    if message.content == "عيال":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :no_mouth:  أمر اخوي ايش بغيت  " % (userID)) 
     
    if message.content == "xD":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ¯\_(ツ)_/¯ " % (userID))  
        
    if message.content == "XD":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ¯\_(ツ)_/¯ " % (userID))
        
    if message.content == "xd":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ¯\_(ツ)_/¯ " % (userID))
        
    if message.content == "Xd":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ¯\_(ツ)_/¯ " % (userID))
        
    if message.content == "كل عام وانتم بخير":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :gift:  وأنت بألف خبر حبيبي " % (userID))
         await Bot.send_message(message.channel,"  <@%s> :money_with_wings:  عاد لا تنسى العيدية " % (userID))
            
            
    if message.content == "عيدكم مبارك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :confetti_ball:  كل سنة وأنت طيب " % (userID))
         await Bot.send_message(message.channel,"  <@%s> :moneybag:  من العايدين والفايزين" % (userID))
            
    if message.content == "من العايدين و الفايزين":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :confetti_ball:  من السالمين والغانمين " % (userID))
         await Bot.send_message(message.channel,"  <@%s> :tongue:  هههه تحسبني ما اعرف ارد " % (userID))
            
    if message.content == "عيد":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>  :upside_down:  سعيد " % (userID))
        
    if message.content == "فلوس":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :money_mouth:   " % (userID))
        
    if message.content == "عساكم من عواده":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart:   ينعاد علينا وعليك بالخير  " % (userID))
        
    if message.content == "من العايدين":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :kissing:  من الفايزين  " % (userID))
        
        
    if message.content == "تعالو":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> تعال انت  :gun:  " % (userID))
        
    if message.content == "كل تبن انت":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :no_entry:   **لا تسب عيب يا بابا** " % (userID))
        
    if message.content == "كل زق انت":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :no_entry:   **لا تسب عيب يا بابا** " % (userID)) 
        
    if message.content == "كيف حالك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>    الحمدلله اخبارك انت ؟ " % (userID)) 
        
        
      
        
        
        
   
        
        
@Bot.event
async def on_ready():
     statuses=["Im in cloud 9","To be Or Not To Be","No pain , no gain","eye to eye","Live and learn","Zzz","So far so good","Make a long story short"]
     updated_game = discord.Game(name = random.choice(statuses))
     await Bot.change_presence(game = updated_game)
     print("Bot is ready")
     print("Logged in as " + Bot.user.name)
        
        
      


@Bot.command(pass_context=True)

async def say(ctx):


    msg_id = ctx.message

    repeat = ctx.message.content[5:]

    await Bot.say(repeat)

    await asyncio.sleep(120)

    await Bot.delete_message(msg_id)
    
    
    
    
@Bot.event

async def on_message_delete(message):

    fmt = '{0.author.name} :point_down:  مسح الرسالة \n{0.content}'

    await Bot.send_message(message.channel, fmt.format(message))    
  

Bot.run(bot_token)



    

