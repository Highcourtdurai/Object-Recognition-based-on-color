import json
import base64#for encoding
import requests
from authKey import secret_key

IMAGE_PATH='first.jpg'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64=base64.b64encode(image_file.read())
    
url=''
r=requests.post(urldata=img_base64)

num_plate=(json.dumps(r.json(),indent=2))
info=(list(num_plate.split("candidates")))
print(info)
plate=info[1]
plate=plate.split(',')[0:3]
p=plate[1]
p1=p.split(":")
number=p1[1]
number=number.replace('"','')
number=number.lstrip()
print(number)

if number == "MH120E4433":
    print("-----------------------")
    print("Owner Name:Champ")
    print("Vehicle Number: %s"%number)
    print("Address: MAHARASHTRA")
    

