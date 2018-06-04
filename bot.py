import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio


bot_token = os.environ['BOT_TOKEN']







Bot = commands.Bot(command_prefix = "$")

@Bot.event
async def on_ready():
    print("Bot is ready")

              

@Bot.event
async def on_message(message):
    if message.content == "هلا":
        userID = message.author.id
        await Bot.send_message(message.channel,"  <@%s> :raised_hand:  أهلين وسهلين  "% (userID))
        
    if message.content == "كلب":
        userID = message.author.id
        await Bot.send_message(message.channel,"  <@%s> :rage:   لا تسب  " % (userID))
    
    if message.content == "محمد":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s>  :relaxed: عيووون محمد  " % (userID))
         
    if message.content == "نايف":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :joy:  اقطع يدي اذا منت بهاك " % (userID))


    if message.content == "اسحبوني":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :smirk:  والله ما نسحبك  " % (userID))

    if message.content == "تسمعني":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :upside_down:  لا  " % (userID))

    if message.content == "يحيى":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :upside_down:  لاحد يشوف الشات  " % (userID))

    if message.content == "مازن":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :scream_cat: أقطع يدي اذا ما معه تي أن تي " % (userID))

    if message.content == "حمد":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :nerd:  sleep or leave " % (userID))


    if message.content == "برب":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :walking:  خذ راحتك " % (userID))
         
    if message.content == "باك":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :top:  ولكم باك " % (userID))

         
    if message.content == "كل زق":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :x: :x: عيب يا بابا  " % (userID))

         
    if message.content == "كل تبن":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :x: :x: عيب يا بابا  " % (userID))
         
    if message.content == "بوت":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> مشغول الحين " % (userID))
         await Bot.send_message(message.channel,"  <@%s> روح لمحمد بيرد عليك " % (userID))

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
         await Bot.send_message(message.channel,"  <@%s> :neutral_face: عربي لو تسمح " % (userID))
         
    if message.content == "حمار":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :x: :x: عيب يا بابا  " % (userID))
         
    if message.content == "يا حمار":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :x: :x: عيب يا بابا  " % (userID))
         
    if message.content == "اصبر":
         userID = message.author.id
         await Bot.send_message(message.channel,"  <@%s> :frowning2:  " % (userID))

  

Bot.run(bot_token)



    

