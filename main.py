from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from time import sleep
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
api_id = 2776086
api_hash = "a873cc6bf92417d1fd96c865522c96a5"
session_name = '.session'




sec = datetime.now().strftime("%S")

sec = int(sec)


'''while sec != '00':
    print(sec)
    sleep(1)
    sec = datetime.now().strftime("%S")'''

first_run = 1
with TelegramClient(session_name, api_id, api_hash) as client:

    while True:

        now = datetime.now()
        current_time = now.strftime("%H:%M")


        image = Image.open("pic.jpg")


        text = current_time
        font = ImageFont.truetype('Rajdhani-Bold.ttf', 200)

        image_editable = ImageDraw.Draw(image)

        image_editable.text((1000 ,2500), text, (237, 230, 211), font=font)

        image.save("profile.jpg")

        client(UploadProfilePhotoRequest(client.upload_file('profile.jpg')))
        client(DeletePhotosRequest([client.get_profile_photos('me')[-1]]))
        print(current_time)

        if first_run:
            sleep(60 - sec)
            first_run = 0
        else:
            sleep(60)




















