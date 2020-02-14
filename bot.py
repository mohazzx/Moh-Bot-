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






bot_token = 'NDUxODY3OTgwMTc5OTYzOTE0.XkZWfw.WxYYR2RAsBiRPL6XAhmPsC2FYAQ'
#os.environ['BOT_TOKEN']



Bot = commands.Bot(command_prefix = "!")

@Bot.event
async def on_ready():
    print("Bot is ready")
    
@Bot.event
async def on_member_join(member):



    server = member.server.default_channel

    fmt = ' {0.mention} :tada:  :heart: اهلا وسهلا نورت سيرفرنا !'
    channel = member.server.get_channel("520250980734861324")


    await Bot.send_message(channel, fmt.format(member, server))

@Bot.event
async def on_member_remove(member):
    
    server = member.server.default_channel
    fmt = '{0.mention} :slight_frown: غادر للاسف'
    channel = member.server.get_channel("520250980734861324")
    await Bot.send_message(channel,fmt.format(member, server))        
@Bot.event
async def on_message(message):
    if message.content == "هلا":
        userID = message.author.id
        await Bot.send_message(message.channel,"  <@%s> :raised_hand:  أهلين وسهلين  "% (userID))
        
        
    if message.content == "احبك":
        userID = message.author.id
        await Bot.send_message(message.channel,"  <@%s> انا اموت فيك ❤️❤️❤️ " % (userID))

    if message.content == "استأذنكم":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ذنك معك حبي ❤️ " % (userID))

    if message.content == "تسمعني":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :upside_down:  لا  " % (userID))

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
         

    if message.content == "اقبل":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :exclamation:  مشغول الحين سوري " % (userID))


    if message.content == "دقيقة":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> تبي تلعب معي ادفع 2000 نقطه " % (userID))

         
    if message.content == "ثواني":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :unamused:  أوك بس لا تطول " % (userID))   
         
    if message.content == "مرحبا":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :v: مرحبتين " % (userID))

    if message.content == "انستا":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> https://www.instagram.com/borakan120/ " % (userID))

    if message.content == "انستا؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> https://www.instagram.com/borakan120/  " % (userID))
         
    if message.content == "السماعه؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> beyerdynamic DT 990 Pro 250 ohm Headphones, Gray, (459038) https://www.amazon.com/dp/B0011UB9CQ/ref=cm_sw_r_cp_api_i_nUE.DbZG4HY81 " % (userID))
         
    if message.content == "ايبك؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> sha7een " % (userID))
         
    if message.content == "اصبر":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :frowning2:  " % (userID))
        
        
    if message.content == "هاي":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart_eyes_cat:  هايات     " % (userID))  
        
    if message.content == "باي":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :walking:  الله معك     " % (userID)) 
        
    if message.content == "تحفيز؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> يوم الحياة تصفعك من يمين اصفعي من يسار ويوم تمردغك منيه مردغهي مناك/ كلمات شاهين   " % (userID))   
        
    if message.content == "السلام عليكم":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart:  وعليكم السلام ورحمة الله وبركاته " % (userID)) 
        
    if message.content == "استغفر الله":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart:  أستغفر الله " % (userID)) 
         await Bot.send_message(message.channel,"  <@%s> :yellow_heart:  أستغفر الله " % (userID))  
         await Bot.send_message(message.channel,"  <@%s> :blue_heart:  أستغفر الله " % (userID))
        
    if message.content == "تويتر":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> https://mobile.twitter.com/borakan120/ " % (userID)) 
         
        
    if message.content == "تويتر؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> https://mobile.twitter.com/borakan120/ " % (userID))
        
    if message.content == "احبك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :blush:  لا تحرجني " % (userID))  
        
    if message.content == "جافا؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> https://www.jgrasp.org/ " % (userID)) 
        
    if message.content == "اذكار":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :blue_heart:  سبحان الله   والحمد لله ولا إله إلا الله و الحمد لله حمداَ كثيرا" % (userID))    
        
    if message.content == "جج":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> بخيير الحمد لله , علومك انت " % (userID))  
        
    if message.content == "بخير ابشرك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> قود قيم 🙄" % (userID))
        
    if message.content == "جيجي":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> قود قيم 🙄 " % (userID))
        
        
    if message.content == "خالد":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> عيون خالد❤️❤️  " % (userID)) 
     
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
            
    if message.content == "خالد؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>  https://clips.twitch.tv/CorrectBumblingChipmunkM4xHeh " % (userID))
        
    if message.content == "فلوس":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :money_mouth:   " % (userID))
        
    if message.content == "شاهين":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :heart:  عيون شاهــيـــن  " % (userID))
        
    if message.content == "صباح":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ❤️😉🌅 صباح النور والهنا والسرور " % (userID))
        
        
    if message.content == "قلوب":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️  " % (userID))
        
    if message.content == "قوانين؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> خلك إنسان " % (userID))
        
    if message.content == "كام؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> LOGTICH 920 PRO " % (userID)) 
        
    if message.content == "كيف حالك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>    الحمدلله اخبارك انت ؟ " % (userID)) 
        
    if message.content == "كفو":
         userID = message.author.id
         await Bot.send_message(message.channel,"  كفوك الطيب 😘" % (userID))  
        
    if message.content == "كود":
         userID = message.author.id
         await Bot.send_message(message.channel,"  هاذا كود شوب shaheenoman  " % (userID)) 
        
    if message.content == "كود؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  هاذا كود شوب shaheenoman" % (userID)) 
            
    if message.content == "مسابقة؟":
         userID = message.author.id
         await Bot.send_message(message.channel,"  المسابقة بتكون كل جمعة الساعة ٢:٠٠ مساءاً بتوقيت مكة! احتمال يكون فيه هدايا!! الله أعلم" % (userID)) 
            
    if message.content == "مواصفات؟":
         userID = message.author.id
         await Bot.send_message(message.channel," https://clips.twitch.tv/NurturingEphemeralMonitorShazBotstix" % (userID)) 
        
        
    if message.content == "يوتيوب؟":
         userID = message.author.id
         await Bot.send_message(message.channel," خالد معنده قناة في اليوتيوب لكن أكثر تواجده في تويتش/ يمكن في المستقبل يسوي متعلم!!" % (userID)) 
        
        
   
        
        
@Bot.event
async def on_ready():
     statuses=["Hello World","https://www.twitch.tv/sha7een_ "]
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



    

