# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events, functions, types
import time
 
  
# get your api_id, api_hash, token
# from telegram as described above
api_id='74547'
api_hash='e2ed769d120d90e47b9ac28a44f7e3fc'
token = 'bot token'
message = "Working..."
#LorenzoCicolin 208311687
#Serpizzotransatlantico 926151784
#oDiru 41206465
 
# your phone number
phone = '+393487061825'
  


start = time.time()  
# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)
  
# connecting and building the session
client.connect()
 
# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():
  
    client.send_code_request(phone)
     
    # signing in the client
    client.sign_in(phone, input('Enter the code: '))
  
  
try:
    #print(client.get_me())

    #client.send_message(1392291184, 'montecatini collassata ora')
    #client.send_file('username', '/home/myself/Pictures/holidays.jpg')

    #client.download_profile_photo('me')
    group_entity = client.get_entity(1392291184)

    @client.on(events.NewMessage(chats=1392291184))
    async def my_event_handler(event):
        end = time.time()
        if end - start > 60 * 60 * 5 :
            exit()
        print(event.text)
        if (event.from_id.user_id == 208311687 and 'PARTECIPAZIONE HUNGER GAMES' in event.text.lower()) or \
            (event.from_id.user_id == 926151784 and 'cazzo' in event.text.lower()):
            async with TelegramClient('reaction', api_id, api_hash) as client:
                result = await client(functions.messages.SendReactionRequest(
                    peer= group_entity,
                    msg_id=event.message.id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon='🔥'
                    )]
                ))
            """ client.send_reaction(
                peer=1392291184,
                msg_id=event.message.id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(
                    emoticon='fire'
                )]
            ) """

    client.run_until_disconnected()
    #messages = client.iter_messages(1392291184)
    """ 
    count_m = 0
    for message in messages:
        if count_m <= 10 :
            print(message.message)  
        else :
            break
        count_m += 1
         """
    
    #messages[2].download_media()
    #print(client.get_dialogs()[3])




    """ @client.on(events.NewMessage(pattern='(?i)hi|hello'))
    async def handler(event):
        await event.respond('Hey!') """
except Exception as e:
     
    # there may be many error coming in while like peer
    # error, wrong access_hash, flood_error, etc
    print(e); 
 
# disconnecting the telegram session


