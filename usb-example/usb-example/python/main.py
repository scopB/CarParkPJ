from practicum import find_mcu_boards,McuBoard,PeriBoard
import time
import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb://192.168.1.4:27017")
db = cluster["carpark"]
col = db["park"]

LDR1 = 2
LDR2 = 3
crossline = 800

OLD_light1 = True 
OLD_light2 = True 

# Carpark1 = 0
carpark = 0

devices = find_mcu_boards()
mcu = McuBoard(devices[0])
peri = PeriBoard(mcu)


while True:
    
    # print(f"PC2 - > {peri.get_light(LDR1)}")
    print(f"PC3 - > {peri.get_light(LDR2)}")
    # NEW_light1 = peri.get_light(LDR1)>crossline #LDR
    NEW_light2 = peri.get_light(LDR2)<crossline #LDR

    ################################

    #Carpark = Pymongo #GET
    ans = col.find({"idName":1})
    carpark = ans["light"]

    ############LOGIC###############
    
    # PARK 1

    # if OLD_light1 and not NEW_light1 : #เปลี่ยนจาก ไม่มีรถ -> มีรถ
    #     Carpark1 = 1 #จอดไม่ได้
    # elif not OLD_light1 and NEW_light1 : #เปลี่ยนจาก มีรถ -> ไม่มีรถ
    #     Carpark1 = 0 #จอดได้
        
    # PARK 2

    if OLD_light2 and not NEW_light2: #เปลี่ยนจาก ไม่มีรถ -> มีรถ
        carpark = 1 #จอดไม่ได้
    elif not OLD_light2 and NEW_light2 : #เปลี่ยนจาก มีรถ -> ไม่มีรถ
        carpark = 0 #จอดได้
        

    #################################
    
    #Pymongo = Carpark #POST
    
    newvalues = { "$set": { 'light': carpark } }
    col.update_one({'idName': 1},newvalues)

    #################################
    print(Carpark1)
    # peri.set_led(0, Carpark1) #LED
    peri.set_led(1, carpark) #LED

    OLD_light1 = NEW_light1
    OLD_light2 = NEW_light2
    
    time.sleep(1)
