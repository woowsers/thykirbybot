import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import sys
from threading import Thread

Client = discord.Client()
client = commands.Bot(command_prefix = "-")

#owner list
owner = "228677452208013313"

@client.event
async def on_ready():
    print(await client.change_presence(game=discord.Game(name='Star Allies is already GOTY')))

@client.event
async def on_message(message):
        
    if message.content.upper().startswith('IN MY OPINION'):
        userID = message.author.id
        await client.send_message(message.channel, "No one asked you for your opinion Hunty keep your mouth closed.")

    if message.content.upper().startswith('-BITCH'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/309168904310095886/423280459162583060/bitch.png")

    if message.content.upper().startswith('-KEKKARONI'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/259708376391483393/394356030345314305/image.jpg")

    if message.content.upper().startswith('LOLIS'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/369981472314097664/415936915259392000/waw.jpg")

    if message.content.upper().startswith('LOLI'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/369981472314097664/415936915259392000/waw.jpg")

    if message.content.upper().startswith('-TWIBBON'):
        userID = message.author.id
        await client.send_message(message.channel, "Please help support kirby, add a #Twibbon now! https://twibbon.com/support/kirby-3/twitter")

    if message.content.upper().startswith('KIRBY SUCKS'):
        userID = message.author.id
        await client.send_message(message.channel, "*inhales <@%s> and gets the bad comedian ability*" % (userID))

    if message.content.upper().startswith('KIRBY SUX'):
        userID = message.author.id
        await client.send_message(message.channel, "*inhales <@%s> and gets the bad comedian ability*" % (userID))

    if message.content.upper().startswith('KIRBY SUCCS'):
        userID = message.author.id
        await client.send_message(message.channel, "*inhales <@%s> and gets the bad comedian ability*" % (userID))

    if message.content.upper().startswith('KIRBY SUXS'):
        userID = message.author.id
        await client.send_message(message.channel, "*inhales <@%s> and gets the bad comedian ability*" % (userID))
        
    if message.content.upper().startswith('IMO'):
        userID = message.author.id
        await client.send_message(message.channel, "No one asked you for your opinion Hunty keep your mouth closed.")

    if message.content.upper().startswith('-HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "poyo! https://pastebin.com/X2zQDLFr")

    if message.content.upper().startswith('DELETE THAT'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/354063147214176269/415949809397137408/dededelet.jpg")

    if message.content.upper().startswith('DELET THAT'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/354063147214176269/415949809397137408/dededelet.jpg")

    if message.content.upper().startswith('DELETE DAT'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/354063147214176269/415949809397137408/dededelet.jpg")

    if message.content.upper().startswith('DELET DAT'):
        userID = message.author.id
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/354063147214176269/415949809397137408/dededelet.jpg")

    if message.content.upper().startswith('-INVITE'):
        userID = message.author.id
        await client.send_message(message.channel, "https://discordapp.com/api/oauth2/authorize?client_id=408077334550282240&permissions=0&scope=bot")

    elif message.content.upper().startswith("HI"):
         await client.send_message(message.channel, random.choice(["Hai!",
                                                                   "sup",
                                                                   "*down taunt*",
                                                                   "hai, how u doin'",
                                                                   "haaaaaaaiiiiiii"]))

    elif message.content.upper().startswith("HELLO"):
         await client.send_message(message.channel, random.choice(["Hai!",
                                                                   "sup b",
                                                                   "*down taunt*",
                                                                       "hai, how u doin'",
                                                                   "haaaaaaiiiiiii"]))
    elif message.content.upper().startswith("-NSFW"):
         await client.send_message(message.channel, random.choice(["https://cdn.discordapp.com/attachments/391434450837307392/418351903827558400/index.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/418350112775864321/nsfw.jpg",
                                                                   "https://cdn.discordapp.com/attachments/290224485603213323/394768236635357184/nakedegg.png"]))         

    elif message.content.upper().startswith("POYO"):
         await client.send_message(message.channel, random.choice(["Po, yo.",
                                                                   "pooooyooooo",
                                                                   "pOOYO",
                                                                   "*gets mike ability* pOYO POOOYOOO POYO POYO POYO POYO POYOOOO",
                                                                   "p-poyo!?!",
                                                                   "Pooyoo!",
                                                                   "P-p-p-p-p-poyo!!!!",
                                                                   "https://www.youtube.com/watch?v=XBvRzwXxzSQ",
                                                                   "POOOOOOOYOOOOOOOOOOOOooooo",
                                                                   "p-p-p-poyo"]))

    elif message.content.upper().startswith("-SHITPOST"):
         await client.send_message(message.channel, random.choice(["https://youtu.be/f4fWKKBNvMA",
                                                                   "https://www.youtube.com/watch?v=KfvKd_wnyV4",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/414839545998082049/Oup0fplcpsYCAGmv8lYLLFg22L0jNQopZbuXM3Sk0lU_copy.png",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/414839546568769547/FUCK.png",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/414839546568769549/IMG_20180217_045431.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/414839547260698644/image-164.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/414839547805827082/sakurai.png",
                                                                   "https://www.youtube.com/watch?v=CDJWhdz5NAg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414840258069266433/twok___king_dedede_dating_simulator__download__by_warpstars-dagd30n.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414883306761355277/i_can_t_draw_nova_by_warpstars-dao6v8q.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414872379215446027/8993ae0.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414885224929951765/Capture_2018-02-10-18-58-28.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414886076671590412/10p8bc7dcwGwpK.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414887036768616448/289.png",
                                                                   "https://cdn.discordapp.com/attachments/132720341058453504/414967345295917056/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/182899928140480512/237008848131588097/eJwNwkEOhCAMAMC_cJdSoAH9DUGCJmoJ7Z42_n03M1_zmZfZzKE6ZAPYT6k8dyvKs_RmO3O_Whmn2Mo3FNVSj7s9KoDBJ-9CREc5UiAXAXNG9Ohy-qM1UgKkBe14unl_k4Egiw.OhYI1LdimkcqiuMr4CD_BXLlTyM.png",
                                                                   "https://cdn.discordapp.com/attachments/182899928140480512/237009066403037186/B5srRkVrhu6AbQERggK5i-axeRsp1XAZuveAVIrPS1c.jpg",
                                                                   "https://cdn.discordapp.com/attachments/226171970008383488/414905117406527488/image.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415025935834808320/beamed.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415026561365049344/KDL2SoundTestINT.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415074510648377354/image-1-1_1.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415042939861991434/1519018391005.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415197783314661376/delet.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415198809933611011/blood.jpg",
                                                                   "https://78.media.tumblr.com/463bac2a9071ec59402ba890f95f32c5/tumblr_onwxerVQmb1ue65n9o1_500.png",
                                                                   "https://www.youtube.com/watch?v=GjJZmLpmqXI",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414979357132587020/2f916a2efZORd.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/414985938607800323/nltw9e0zete01.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203287156129802/17_-_1.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203289504940052/2392490209ee3c8f02ea743474293e3f71183073_hq.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203292088500233/1492685818831.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203295930482698/f3cef799cbda804d796670f1ad42865ddebd775b_hq.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203297738358786/f403e3dd7006909f9a012648cd36ac4722ff2caev2_00.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203308441960458/kirbydoesntcare.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203298983804928/breaking-news_1.png",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203310866530305/kerbecanessarsez.png",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203316319125511/8PrcUzD.gif",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415203318583787542/sponsored_by_skittles.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415201596167684106/pinkandfurious.gif",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415203020830277657/DQ3urNSWkAM1VQB.jpg",
                                                                   "https://pbs.twimg.com/media/DWaT-Q-UQAAQckB.jpg",
                                                                   "https://pbs.twimg.com/media/DWV4-WDXkAEox8P.jpg",
                                                                   "https://www.youtube.com/watch?v=iQC7NWoO538",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415209021662953472/one_wish.jpg",
                                                                   "https://www.youtube.com/watch?v=0Dpw0VvH4m0",
                                                                   "https://www.youtube.com/watch?v=VyiwEHzsg14",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415265068931088415/final_boss_2.jpg",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415265320530477056/laser.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415265386007756805/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415267747992174602/tac.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415288090467500032/shitpostingtothemaximum.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415323175560151061/goose.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/415326664512372746/totallyrealsmash4tierlist.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415327288159109130/ghost_trick.jpg",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415327372556894208/not_clear.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415327519341019137/no_u.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415325860648976415/Copy.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415327713985822732/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415327790569750538/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/412781746044796939/smart_kirb_meem.jpg",
                                                                   "https://cdn.discordapp.com/attachments/369981472314097664/415349510961889290/delet.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415345616970055681/image.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415359248906715147/metatheknight.png",
                                                                   "https://www.youtube.com/watch?v=toHtBSNvdpM",
                                                                   "https://www.youtube.com/watch?v=urJf-FNG6Nc",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415397984432291841/END_CAPITALISM-1.jpg",
                                                                   "'if you slap kirby, does he jiggle?' if you slap kirby, you die.",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/415409508379262976/kirbyloss.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415613916446720031/Webp.net-gifmaker_6.gif",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415616229357780993/image.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415663269613928448/kerbe_meme_2.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415700759296999434/image.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415701440032538624/20180220_190626.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415711095152443393/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/412701316788518932/unknown.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/404389663642484736/1766D3B1-5330-41BC-AC26-862A03C4F67B-11471-00000AAD98D46ED4_tmp.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/404388462326972436/DJpCQtPVwAAoEUj.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/404328198118047744/wholesome_kirb.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/404155545369575425/C-ohj_OVYAADBYh.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/404104699650899968/image.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/404104607736791041/kirby_expanding_brain.PNG",
                                                                   "https://pbs.twimg.com/media/DT5T7CYXcAEdINJ.jpg",
                                                                   "https://www.youtube.com/watch?v=gm5mgoR2Aeg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/403812211136659456/magik.jpg",
                                                                   "https://cdn.discordapp.com/attachments/236988598036070400/415722278748160001/tumblr_inline_p1l1maLjPH1tqmwkj_540.png",
                                                                   "https://pbs.twimg.com/media/DWiCgtIVQAACV3f.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415731712723517471/EGG_LABORATORY.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/415733539288383498/sketch-1519188895757.png",
                                                                   "What the poyo did you just puffing say about me, you little Noddy? I'll have you know I got gold medals on the EX Challenge Stages in Kirby's Dream Collection, and I've been involved in several universe-threatening fights, and I have over 300 confirmed boss kills. I am trained in the Hammer Ability and I'm the top Archer in the entire Dream Land. You are nothing to me but just another meal. I will eat you up with aggressive eating which has never been seen before on Pop Star, mark my words. You think you can get away with saying that junk to me over the Internet? Think again. As we speak I am contacting my wish-granting clockwork machine and you are being watched right now so you better prepare for the storm. The storm that wipes out the pathetic little things you call your extra lives. You're doomed, kid. I can be anywhere, anytime, and I can defeat you in over fifty different ways, and that's just with my Copy Abilities. Not only am I extensively trained in oral combat, but I have access to the entire arsenal of six Animal Buddies and I will use it to its full extent to wipe your miserable grin off your face. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your tongue. But you couldn't, you didn't, and now you're paying the price, you goshdarn doodoohead. I will poop all over you and you will drown in it. You're gonna have a game over, kiddo.",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/415758081092485120/image.jpg",
                                                                   "https://www.youtube.com/watch?v=toHtBSNvdpM",
                                                                   "https://cdn.discordapp.com/attachments/342885974520496130/415982958055522307/image-55.png",
                                                                   "help me https://cdn.discordapp.com/attachments/195706171762540544/415993589537964032/more_jpeg.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/416026691542974465/image.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/416035257913966592/Screen_Shot_2018-02-18_at_11.02.07_AM.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/416035241321562122/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/416044925814177795/pain.jpg",
                                                                   "​https://cdn.discordapp.com/attachments/201511701345075200/416017337729417236/escargoon.gif",
                                                                   "https://cdn.discordapp.com/attachments/226171970008383488/416096391085948938/Screenshot_2018-02-21-23-58-22.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/416364126797824000/kirbytale.png",
                                                                   "https://pbs.twimg.com/media/DWp4CHUU0AA6tle.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/416395275029184512/look.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/416487611956461568/d71.gif",
                                                                   "https://media.discordapp.net/attachments/184670008117297162/393201043900465172/image.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/416688744796651520/soosoos.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/414583130410713108/j2nnWmG.png",
                                                                   "https://cdn.discordapp.com/attachments/401898480332701707/416814468337631232/tumblr_inline_p48t93Idz01t68a9p_500.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/416818556299247617/image-51.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/416830358978297857/dad.png",
                                                                   "https://cdn.discordapp.com/attachments/369981472314097664/417053227025170453/357635180824887296.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/417080459206590464/98cdf1a.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417086327482482689/5dde5211ploy.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417086406117294092/unknown.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417086550879502357/communism.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417086752818331678/JX96o4U.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417087133648683008/unknown.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417087779386687500/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417088103271104513/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417088807242956810/unknown.png",
                                                                   "https://i.redd.it/m9xbrlr0lvh01.jpg",
                                                                   "https://i.redd.it/xynlngk0xig01.jpg",
                                                                   "https://youtu.be/jzm3sNl8VwQ",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417089780807892992/425633A8-C315-4F89-94A3-2368DF71FFF5.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417090026523066379/unknown_1.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417090610823168001/buff_king_dedede.jpg",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417090901131919391/unknown.png",
                                                                   "https://i.redd.it/ih65qxvvlub01.png",
                                                                   "https://i.redd.it/4dovdywuxxa01.jpg",
                                                                   "https://i.redd.it/irlb3uqgg8a01.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417092333289472000/tumblr_oqz9bgDZZO1w61idto1_1280.jpg",
                                                                   "https://i.redd.it/mxcud4vg94a01.jpg",
                                                                   "https://i.redd.it/t0r421laxn901.jpg",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417093614288633866/supehstah.png",
                                                                   "https://i.redd.it/i7f53i70oytz.png",
                                                                   "https://i.redd.it/y7l8i661jvmz.jpg",
                                                                   "http://i.imgur.com/lbcTHXP.jpg",
                                                                   "https://i.imgur.com/NLhacSJ.jpg",
                                                                   "https://i.redd.it/bcy12bjlc6fz.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417096455313162240/image.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417096619729616896/spidloss.png",
                                                                   "https://i.redd.it/gqxewfqivm8z.png",
                                                                   "https://i.redd.it/0tgpfpbvvd6z.png",
                                                                   "https://i.redd.it/twt6sd2siz5z.jpg",
                                                                   "https://i.redd.it/ftfwmqdrz13z.jpg",
                                                                   "https://i.redd.it/kg5hvjilv80z.jpg",
                                                                   "https://i.redd.it/ug5ajsz8o0yy.png",
                                                                   "https://i.redd.it/5kyabpjnttxy.gif",
                                                                   "https://i.redd.it/5yffqv1y0ovy.jpg",
                                                                   "https://i.redd.it/3orb8ee196vy.png",
                                                                   "https://i.redd.it/w03yigwy9vty.png",
                                                                   "https://i.redd.it/q7prd3johxry.jpg",
                                                                   "https://cdn.discordapp.com/attachments/369981738698407936/417098214450397195/merge.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417098868745043980/image.png",
                                                                   "https://cdn.discordapp.com/attachments/356209253574246420/417100561369006080/image.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/417210787350839296/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/417226215359774741/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/417378317382057994/unknown.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/417867923319816192/relatable.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/417860618477895691/getting_and_instantly_dropping_fire_and_ice.png",
                                                                   "https://www.youtube.com/watch?v=8jp0IeDDYmE",
                                                                   "https://pbs.twimg.com/media/DW8uDFNUMAAoQsz.jpg",
                                                                   "https://www.youtube.com/watch?v=DY0Fm6dlTMg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418108152798511104/loss.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418108404247035914/loss.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418185777130897420/tctrSlqnIjdpQjA2VZa8Zn7ePKy4Zeyl89npIMbIYbc.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418212565940830228/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418231212201476096/daro.jpg",
                                                                   "https://imgur.com/3sLlei0",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418556636177891335/DIICTATORSHIP.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418572791407837205/1519729559381.png",
                                                                   "https://snackkracker.tumblr.com/post/170097725052/remind-kids-dont-swear-xd",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/418637777349902337/massborbattack.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/418776321485963275/bonkston.png",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/418907274967252992/no.png",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/419016647077003274/StarAllies.png",
                                                                   "https://www.youtube.com/watch?v=sC7V0WoQnZ0",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/419659109026103307/IMG_20180114_231459.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/420281442912698370/image.jpg",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/420336186972962816/1472091979872a.png",
                                                                   "https://78.media.tumblr.com/ce1f2b145dfc5ef922fac3a6dfed36d5/tumblr_p54wx1KJeJ1wezag6o1_540.gif",
                                                                   "https://cdn.discordapp.com/attachments/371726024137900035/420360131335946241/1520290244796.gif",
                                                                   "https://cdn.discordapp.com/attachments/195706171762540544/420688353118388225/switchsplit.jpg"]))

    elif message.content.upper().startswith("-GOOEY"):
         await client.send_message(message.channel, random.choice(["https://cdn.discordapp.com/attachments/391434450837307392/414840880822747145/normal_Kirby_Gooey.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/414840950238609412/tumblr_ohvij42fir1twf1two2_1280.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/414841003158011925/dd8.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/414841155881140235/soda.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/414841366686859285/kirby_gooey.png",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/414841462581362688/tumblr_ohvij42fir1twf1two5_1280.png"]))

    elif message.content.upper().startswith("-DANCE"):
         await client.send_message(message.channel, random.choice(["https://cdn.discordapp.com/attachments/354063147214176269/413560800993607690/tumblr_n7eozjWugj1st9d31o1_500.gif",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413560387108208661/Kirby_runs_around_and_then_clones_himself_because_that_is_a_normal_thing_kirby_can_do_dont_judge_him.gif",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413560340807417857/tumblr_ojuex2utcz1r7sijxo1_400.gif",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413561647144108034/giphy.gif",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413561864283357184/Kirby_Dance.gif",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413564082961252352/thekirbydance.gif",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413565042147983361/tumblr_opwi480i121qlh9h7o1_500.gif"]))

    elif message.content.upper().startswith("-SONIC"):
         await client.send_message(message.channel, random.choice(["mania's studiopolis act 1 song is very good",
                                                                   "fast boy!!!",
                                                                   "forces might not be very good but thats ok because they *kinda* tried",
                                                                   "follow me, set me free",
                                                                   "sonic 06 is a really good game"]))
    elif message.content.upper().startswith("-MERCH"):
         await client.send_message(message.channel, random.choice(["https://cdn.discordapp.com/attachments/354063147214176269/413958364759064576/IMG_20180205_122141.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958364759064577/IMG_20180124_133344.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958365379690496/IMG_20180208_161556.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958365866098688/IMG_20180208_161555.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958365866098689/IMG_20180208_161553.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958366541643796/IMG_20180208_161551.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958366541643797/IMG_20180209_205629.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958367384567819/IMG_20180209_205632.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958367904530432/tumblr_p3szimyP8W1uc5pzno1_500.png",
                                                                   "http://i.imgur.com/cWSwcvK.jpg",
                                                                   "https://gonintendo.com/system/file_uploads/uploads/000/020/792/original/cute.png",
                                                                   "(this thing actually exists please make it stop) http://img1.ak.crunchyroll.com/i/spire4/3362f16b07801e70f77ce0e59c954dd51512240729_full.jpg",
                                                                   "https://nintendowire.com/wp-content/uploads/2017/02/Banner-Kirby-MerchRoundup2.jpg",
                                                                   "https://i.pinimg.com/736x/e7/15/94/e715941afaa95b10547aa621bccc9d75.jpg",
                                                                   "https://pbs.twimg.com/media/DU2qR18X0AIGqjo.jpg",
                                                                   "https://78.media.tumblr.com/29d2cd34d45f56233c8af455f8bb7407/tumblr_oue26i8qjw1rl04amo1_500.jpg",
                                                                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQipTdGBb_7PlSFQWWFLe8aPTpp90e1rJYLaY-_5tBLAYgMiY7o",
                                                                   "https://abload.de/img/1_answ0.jpg",
                                                                   "https://nintendowire.com/wp-content/uploads/2017/02/Kirby-25thAnniversary-Plush-Classic.jpg",
                                                                   "https://nintendowire.com/wp-content/uploads/2017/02/Kirby-25thAnniversary-Plush-Classic2.jpg",
                                                                   "https://pbs.twimg.com/media/DDdQfKNU0AA5kMV.jpg",
                                                                   "https://78.media.tumblr.com/d8e42dae8a355a0b7c5e5bab6072ba9d/tumblr_p0yqycnVPj1tdiryzo1_500.jpg",
                                                                   "https://pbs.twimg.com/media/DWYer0GUMAACIsg.jpg",
                                                                   "https://cdn.discordapp.com/attachments/236988598036070400/415722276160405524/GOODS-00172738.jpg",
                                                                   "https://cdn.discordapp.com/attachments/236988598036070400/415722276160405525/s-l400_2.jpg",
                                                                   "https://cdn.discordapp.com/attachments/236988598036070400/415722276802002944/s-l400.jpg",
                                                                   "https://cdn.discordapp.com/attachments/236988598036070400/415722277515296779/s-l400_3.jpg",
                                                                   "https://cdn.discordapp.com/attachments/236988598036070400/415722278748160000/il_340x270.1307446192_7bd5.jpg",
                                                                   "https://buyanimeaus.com.au/wp-content/uploads/2018/01/45867_1-600x600.jpg",
                                                                   "https://images-na.ssl-images-amazon.com/images/I/41jklG2pcSL._SY300_.jpg",
                                                                   "https://aitaikuji.com/content/images/thumbs/0002971_ichiban-kuji-kirby-sweets-party-kirby-sleepy-plush_550.png",
                                                                   "https://gonintendo.com/system/file_uploads/uploads/000/031/092/original/kir.png",
                                                                   "https://gonintendo.com/system/stories/promo_images/000/266/298/original/lsa.png?1475691611",
                                                                   "https://img00.deviantart.net/227a/i/2016/168/3/1/my_kirby_plushie_collection__by_kirbyfan1234-da6mpeq.png",
                                                                   "https://www.dhresource.com/0x0s/f2-albu-g2-M00-BA-F9-rBVaGlSJFDeACEAvAAFow2sAn84847.jpg/3-7cm-nintendo-super-mario-bros-kirby-plush.jpg",
                                                                   "http://randomnintendo.com/wp-content/gallery/extra-the-merchandise-of-nintendo-world/kirbyplushes.jpg",
                                                                   "http://img4.meristation.as.com/files/imagenes/general/merchandisingkirby3.jpg",
                                                                   "https://i5.walmartimages.com/asr/52ad591e-c5b1-476d-9470-0247947429ad_1.ee3d2a81168552f83079afb5ac858895.jpeg",
                                                                   "http://www.kirbysrainbowresort.net/info/merchandise/extrarare1.GIF",
                                                                   "http://www.kirbysrainbowresort.net/info/merchandise/6402Kirbyplush9.jpeg",
                                                                   "https://pbs.twimg.com/media/DWTldo9WAAEW71h.jpg",
                                                                   "https://pbs.twimg.com/media/DWg3IHOVwAUDXE9.jpg",
                                                                   "https://pbs.twimg.com/media/DWsXpg2VQAA630G.jpg"]))
         
    elif message.content.upper().startswith("-COOKIES"):
         await client.send_message(message.channel, random.choice(["https://pbs.twimg.com/media/DV_DcNqVAAAA2aH.jpg",
                                                                   "https://pbs.twimg.com/media/DV_DbCDU0AEX_9l.jpg",
                                                                   "https://pbs.twimg.com/media/DV_DZ6TU8AEymnw.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413613120020545536/IMG_20180214_030942.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413613745969954817/kirbycookies.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413613956855365643/469274977208631296_35s_d.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413614299798568960/12174_04.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413614463451791370/maxresdefault_1.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413614693261770754/some_kirby_cookies_i_made__d_by_hanbambam-d5lladg.jpg",
                                                                   "https://78.media.tumblr.com/ae433b2c1a12a2c9a992f6535d3f71d6/tumblr_mpl5x00dkQ1rjiu2eo1_500.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413956257158922250/IMG_20180215_133256.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413956257834074123/IMG_20180215_133258.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413956258262155264/IMG_20180215_133301.jpg",
                                                                   "https://cdn.discordapp.com/attachments/354063147214176269/413958367384567818/IMG_20180205_122312.jpg",
                                                                   "https://cdn.discordapp.com/attachments/391434450837307392/414613191331414016/443983196896362496_35s_d.jpg"]))

    elif message.content.upper().startswith("-KIRBY FACTS"):
         await client.send_message(message.channel, random.choice(["Kirby FACT 1: his name is Kirby",
                                                              "Kirby FACT 2: Kirby can float by puffing up",
                                                              "Kirby FACT 3: kirby can breathe underwater",
                                                              "Kirby FACT 4: first you draw a circle",
                                                              "Kirby FACT 5: He is pink",
                                                              "Kirby FACT 6: Kirby is straight edge",
                                                              "Kirby FACT 7: has a lung capacity of 400000 (impressive!)",
                                                              "Kirby FACT 8: the first kirby game came out in 1992 which is a long time",
                                                              "Kirby FACT 9: chatotic good",
                                                              "Kirby FACT 10: he was almost yellow but they decided not to",
                                                              "Kirby FACT 11: he is a hero!",
                                                              "Kirby FACT 12: kirby is popular all around the world!",
                                                              "Kirby FACT 13: he has the best videogames",
                                                              "Kirby FACT 14: its an easy name to remember. I'm Popopo",
                                                              "Kirby FACT 15: hes here to stay",
                                                              "Kirby FACT 16: kirby has attained total enlightenment",
                                                              "Kirby FACT 17: he loves to eat food",
                                                              "Kirby FACT 18: kirby is the best character in smahs because he can do everything the other ones can due to COPY ABILITY",
                                                              "Kirby FACT 19: he loves to have adventures",
                                                              "Kirby FACT 20: Kirby is brave!!",
                                                              "Kirby FACT 21: one time when I was fishing I caught some sea weed",
                                                              "Kirby FACT 22: KIRBY IS A FRIEND TO ALL HEROES!!!",
                                                              "Kirby FACT 23: he is not very smart but that's okay",
                                                              "Kirby FACT 24: you should clean your room because kirby cleans his room every day so you should too",
                                                              "Kirby FACT 25: kirby is friends with everyone who is good",
                                                              "Kirby FACT 26: he loves to sing but cant",
                                                              "Kirby FACT 27: he can count all the way to twelve",
                                                              "Kirby FACT 28: Kirby is a very good boy, and greets everyone he meets with a cheerful, positive attitude.",
                                                              "Kirby FACT 29: [REDACTED BY ORDER OF FEDERAL BUREAU OF INVESTIGATION'S NATIONAL SECURITY BRANCH]",
                                                              "Kirby FACT 30: can YOU collect all the kirby facts?????",
                                                              "Kirby FACT 31: my favorite copy ability is beam",
                                                              "Kirby FACT 32: there are many kirbys but kirby is the best one and cutest",
                                                              "Kirby FACT 33: he is just a baby",
                                                              "Kirby FACT 34: if you go in the bathroom with lights off and say: 'kirby kirby kirby' nothing happens but I think it sounds nice and its fun",
                                                              "Kirby FACT 35: one of the most interesting facts about kirby is that he is strechy like bubble gum",
                                                              "Kirby FACT 36: he is the star of the show",
                                                              "Kirby FACT 37: Kirby lives in a house and theres nothing in it but a bed",
                                                              "Kirby FACT 38: kirby has never once lost",
                                                              "Kirby FACT 39: kirby does NOT look both ways before crossing the street... he is bad ass",
                                                              "Kirby FACT 40: Kirby believes in you forever! <('O'<)",
                                                              "Kirby FACT 41: suck and cuck is the strongest smash strategy",
                                                              "Kirby FACT 42: if kirby copied you he'd be a pretty cool boy",
                                                              "Kirby FACT 43: if kirby copies kirby he becomes 200% more kirby",
                                                              "Kirby FACT 44: Kirby is beloved by all",
                                                              "Kirby FACT 45: once he's got you in his sights, there's no place to run",
                                                              "Kirby FACT 46: circle",
                                                              "Kirby FACT 47: biospark is a pretty cool ninja but with fire he's even cooler",
                                                              "Kirby FACT 48: he loves to sleep!!",
                                                              "Kirby FACT 49: melee kirby is just as good as fox its just that nobody plays as him trust me",
                                                              "Kirby FACT 50: everybody loves Kirby so much"]))
    elif message.content.upper().startswith("-MESSAGE"):
         await client.send_message(message.channel, random.choice(["study the following passage from the Book of Kirby, Testament of Creamsicles: “asdfghjefsfd hggf asdasf gvbjh sdfdmbvgg”",
                                                                   "everything's so colorful and there's so many cute things",
                                                                   "What else needs saying? TRIPLE STAR. That’s what you are! Amazing!",
                                                                   "kirby premium version",
                                                                   "draw circle (kirby)",
                                                                   "kirby can jump sooooo high up all the way to the sky with the hi jump copy ability!!",
                                                                   "if kirby was named Tinkle Popo instead of Kirby I would love him just the same...",
                                                                   "i love kirby he is nice and fun!! he goes on adventures",
                                                                   "Kooking with Kracko",
                                                                   ":o :O",
                                                                   "*face gets all big and puffed up looking* ha!",
                                                                   "“tch.. you’re ten years too early to Challenge me.. go and Wash your ears!!!” – words of galagda night",
                                                                   "kirby arrives as the rising sun, as the blush in the clouds, as the calm in the wind",
                                                                   "yep! it's Kirby",
                                                                   "three cheers for kirby! *cheering*",
                                                                   "nerdyboutkirby",
                                                                   "roly poly little hero",
                                                                   "Puff Puff (Pink Ver.)",
                                                                   "<('O')> *does a BIG puff*",
                                                                   "kirby arrives as the rising sun, as the blush in the clouds, as the calm in the wind",
                                                                   "#1inchtall",
                                                                   "My Little Galaxia",
                                                                   "Mondays am I right LOL",
                                                                   "(he is counting out loud to five)",
                                                                   "uwu",
                                                                   "*miscellaneous kirby noises*",
                                                                   "bwa",
                                                                   "kirby thinks you are a special thing",
                                                                   "Kirby Wiki Holy War",
                                                                   "unable to analyze the upper limits of Kirby's power (describing it as infinite)",
                                                                   "https://youtu.be/MA852XwsEqk",
                                                                   "PRESTO!!! it's Circle",
                                                                   "*drinking soda on the beach* hi",
                                                                   "And the winner is...... Kirby!!!!",
                                                                   "the shadow organidation known only as “league of the kirbyheads” (kirbyhead means a big fan of kirby)",
                                                                   "i don't understand k pop but it sounds like k(irby) pop(star) and im glad you are having fun. except for the freaks",
                                                                   "the best part about Kirby is that every body can draw him perfectly. every kirby drawing is Perfect",
                                                                   "Kirby who rescued a baby bird and fed it a bunch of cake",
                                                                   "Kirby loves you!",
                                                                   "*kirby voice* uwa",
                                                                   "various artifacts featuring the hero kirby uncovered in the lunar wastes",
                                                                   "softness went up by 5!",
                                                                   "<('.')> Kirby will never abandon you",
                                                                   "kirby has forcibly infiltrated the halberd and will not stop watching schoolhouse rock on the bridge's main viewscreen",
                                                                   "*drools* (just a little)",
                                                                   "he’s so round, he’s sometimes treated like a ball.",
                                                                   "round, pink life-form #lifehacks",
                                                                   "investigate flat earth",
                                                                   "(っ^‿^)っ",
                                                                   "um",
                                                                   "Episode 203: Kirby Learns to Read",
                                                                   "new copy ability: sad",
                                                                   "you are my sunshine",
                                                                   "poyo",
                                                                   "new copy ability: frog",
                                                                   "I.Q. 24",
                                                                   "thinking of………………………………………………………….. rain bows",
                                                                   "his myserious mask.. his mysterious wingspan….. his mysterious sword…. Aahh I'm gonan faint",
                                                                   "*eats nine hundred forty seven watermelons* hhmgggu",
                                                                   "I personally have enjoyed what I have watched of Kirby because I am a huge Kirby fan at heart",
                                                                   "My Favorite Song",
                                                                   "Kirby and the end of history",
                                                                   "*eats some leafs and spits them out* peh! poyo…",
                                                                   "Free Dream Land Vaction Click Here!!!!!!!!!!",
                                                                   "Episode 35: Watermelon Felon",
                                                                   "'It's an honor to serve my biggest hero, Meta Knight.' - Axe Knight",
                                                                   "2001 space odyessy monolith things except theyre all one of those little kirby figurines that come in sets",
                                                                   "juicy juice",
                                                                   "new copy ability: bunny (NOT SEXY. THE NORMAL KIND.)",
                                                                   "When the pink terror raises his fist, even the strong tremble in fear….",
                                                                   "how he do that",
                                                                   "https://www.youtube.com/watch?v=vIzzZzNVVnA",
                                                                   "kirby kirby Kirby thats a name you. that's a name you should star. Kirby kirby kirby that's who you are!!!",
                                                                   "oh its popstar like. pop star. like the. ohhhhhhh",
                                                                   "please consider the consequences of your actions",
                                                                   "blushing",
                                                                   "kirby ALWAYS uses floaties in the pool. safety first!",
                                                                   "kirbybot is not an arg. kirbybot is NOT an arg. cease investigation into the matter immediately.",
                                                                   "Kirby is shaped like a..... ENEMY!!!!! (GOes super sayain level ten and starts doing really cool and dangerous swords moves super fast )",
                                                                   "Kirby and the big circus parade",
                                                                   "Happy Sunrise",
                                                                   "more like NAGolor. Lol.",
                                                                   "magolor alive in Havana",
                                                                   "small brain: kirby. Big brain: kirby. Brain but with stars in it: kirby. Meditating galaxy man: Ten Kirbys.",
                                                                   "poppopo",
                                                                   "meta knight of the stellar ummah",
                                                                   ":O =3",
                                                                   "new copy ability: apple",
                                                                   "new copy ability: gamer mouse",
                                                                   "Nobody can beat Kirby!",
                                                                   "He loves to play and sleep, and can be utterly fascinated by even the most mundane things",
                                                                   "*kirby voice* jet",
                                                                   "That's Kirby, also known as 'Kirby from Dream Land'. He's from another planet--in other words, an extraterrestrial.",
                                                                   "(he wobbles and falls over) pah",
                                                                   "big smile. 'GREAT BIG' Smile,",
                                                                   "Kirby world is obviously like Star Wars world",
                                                                   "He is round and pink, ever so mischievous and is always up for a snack.",
                                                                   "We are all so proud of Kirby",
                                                                   "kirby and the blade of folded sunlight",
                                                                   "kirby always stays hydrated because he isnt stupid idiot",
                                                                   "The land was gone. I couldn0t believe it. Whole streches of the earth were all rent up, as though torn by some monstrous beast.",
                                                                   "new copy ability: minecraft",
                                                                   "Because of this, he is still only a baby.",
                                                                   "#life hacks",
                                                                   "<('.')> <('.')> hold hands",
                                                                   "Kirby loves you!",
                                                                   "Little Red Shoes",
                                                                   "https://www.youtube.com/watch?v=RAGDHpNiyZU",
                                                                   "https://www.youtube.com/watch?v=wJvVWQ239wM",
                                                                   "there is only one, 'soft boy', and that is, of course, kirby",
                                                                   "Meta Knight can do ANYthing",
                                                                   "dat… DEAR kirby",
                                                                   "new copy ability: the moon. just the whole moon. the joke is that he turns into the moon",
                                                                   "Jet",
                                                                   "I love havig one crystal",
                                                                   "have you done circle today?",
                                                                   "no one can beat kirby when he’s trying his best!",
                                                                   "*activates Sleep Copy Ability*",
                                                                   "(he has retracted his limbs and become a perfect sphere)",
                                                                   "Kirby and the munchies…",
                                                                   "new copy ability: mop",
                                                                   "new copy ability: pope",
                                                                   "new copy ability: W",
                                                                   "new copy ability: star of celestial balance",
                                                                   "Kirby and the big circus parade",
                                                                   "kirby day",
                                                                   "waddle… waddle waddle…",
                                                                   "https://www.youtube.com/watch?v=9mDngl11P3k",
                                                                   "Press and hold ↑, and then ↓ + B",
                                                                   "add a great big CIRCLE",
                                                                   "kirby looked confused….<('.')>  who was that mysterious stranger??",
                                                                   "a frick person thats the stuff i dont like",
                                                                   "My! 'Tis Kirby, come in from his frolicking! What delightful spectacle! What gaiety! Gran-papa, mayn't we take a commemorative 'photo?",
                                                                   "new copy ability: third bibliographic record of hemispheric philosophy",
                                                                   "Kirby and the munchies…",
                                                                   "*tries to drink the entire orange ocean and gets a tummyache* poyo.. (mournfully)"]))
                                                                                                                          
client.run("NDA4MDc3MzM0NTUwMjgyMjQw.DVKz0g.ijytN6W6Cyyo4TAuzGsSbmbO_aA")
