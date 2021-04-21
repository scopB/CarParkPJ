# CarParkPJ

- [About Project](#About-Project)
- [Front-end](#Front-end)
- [Back-end](#Back-end)
- [Hardware](#Hardware)
- [Contributors](#Contributors)

## About Project


Project นี้เป็น iot ที่เดิน สถานะที่จอดรถของลานจอดรถบนหน้าเว็บไซต์ โดยเราสามารถสมัครสมาชิกเพื่อนจองที่จอดรถได้

## Front-end 
Fornt-end ของเว็บไซต์ถูกเก็บอยู่ใน โฟลเดอร์ fornt ซึ่งประกอบไปด้วยหน้าเว็บไซต์ 3 หน้าประกอบไปด้วย 
- resister เป็นหน้าสำหรับการสมัครสมาชิกเว็บไซต์
- login เป็นหน้า login เข้าเว็บโดยทุกคนต้อง login เข้าเว็บก่อนที่จะเข้าหน้า index ได้
- index เป็นหน้าที่แสดง สถานะต่างๆของลากจอดรถ รวมถึงการจองที่จอดรถในลานจอดรถ

โดยเขียนด้วย html,css,javascript

## Back-end
Back-end ถูกเก็บใน back.py ซึ่งเราใช้ flask และ pymongo ในการติดต่อสื่อสารกับหน้า front-end และ data base โดย data base ที่เราเลือกใช้คือ Mongodb ที่เราติดตั้งในเครื่อง rasberrypi3 ซึ่งประกอบไปด้วย library 
- flask
- flask-mongo
- flask-cors
- Pymongo
- bcrypt
- Pyusb

Database and Storage: Mongodb

                                  
## Hardware                                 
code สำหรับ hardware ถูกเก็บใน usb-example ซึ่งเป็นการประมวลผลสำหรับการทำงานผ่าน USB ซึ่งประกอบไปด้วย
- firmware โฟลเดอร์ สำหรับ firmware ของ microcontroler
- main.py โค้ดสำหรับควบคุมการทำงาน microcontroler
โดยเราใช้อุปกรณ์ที่ประกอบไปก้วย
- mcu Borad *1
- Rasberrypi3 *1
- 330 Resistor *2
- 10K Resistor *2
- PIN 2*5 *1
- PIN 2*8 *1
- LDR *2
                           
## Contributors

This project is part of the course Practicum 01204223 in Computer Engineering Faculty of Engineering Kasetsart University

-Project Link: <https://github.com/scopB/CarParkPJ>
-Present Link: <https://youtu.be/qMmpcOmm_og>

|                       |            |
| ----------------------| ---------- |
|Pawat Thirasakthana    | 6210500536 |
|Suprawit Pattanasin    | 6210500161 |

![Main pic](https://i.ibb.co/mvBb1Cb/pic1.jpg)
