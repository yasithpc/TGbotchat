import os
import telebot


bot = telebot.TeleBot("1914396081:AAHNFA2409oexT-JMVr5eOnkFMaXb__3xkg")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, """
Hello!😊 I'm BST Community Chat Bot.💖
  
my command list :

/botcreator - Find my owner
/monitor - Find our Class ref.
/subject - Find our subject
/lecvideo - Get google drive link

mention word :
Hi,hi,
Bst,bst,
Univotec,univotec,
Uppala,uppala,
Namindu,namindu
  
Thank you.❤ Your request.💖
  """)


@bot.message_handler(commands=["botcreator"])
def send_message(message):
  bot.reply_to(message, """
I am built by yasith praharshana.🧑
He is Univotec BST Class Member.🏘

Thank you.❤ Your request.💖
  """)
  
@bot.message_handler(commands=["monitor"])
def send_message(message):
  bot.reply_to(message, """
Namindu👦 and Uppala👧. 
They are our Class representative.☺❤

Thank you.❤ Your request.💖
""")

@bot.message_handler(commands=["subject"])
def send_message(message):
  bot.reply_to(message, """
1️⃣--- First Semester Subject ---1️⃣
  
👩‍🏫 Construction Technology - Ms. Samantha
👨‍🏫 Fluid mechanics - Mr. Tharinda
👩‍🏫 English (com. Skill) - Ms. Kokila
👩‍🏫 Engineering Physics - Ms. Chamila
👩‍🏫 Theory of elecricity - Ms. Chamila
👨‍🏫 Engineering Maths - Mr. Naveen
👨‍🏫 Construction Drawing - Mr. Sampath
  
Thank you.❤ Your request.💖
  """)
    
def handle_messages(messages):
	for message in messages:
		if message.text == "hi" or message.text == "Hi":
		# Do something with the message
			bot.reply_to(message, 'Hi my dear, I am Bst univotec bot.🤗 How are you.❤')
			
		if message.text == ".bot hi" or message.text == ".bot Hi":
		# Do something with the message
			bot.reply_to(message, """Hi my dear, I am Bst univotec bot.🤗 How are you.❤
Monawa karannada bn. ara gon yasithaya ".bot" command ekta program karala na.🥴 Sorry ahh.😐
ala irath thekka command tikkakui.wachanayak dammama msg ekk ena widiye deyak hadala thiyenne.😪
yalu /start meka uda touch karama ganna puluwan. mage command set eka...☺
			""")
			
		if message.text == "univotec" or message.text == "Univotec":
			bot.reply_to(message, """ 
Our University is University of Vocational Technology.🏙 It is located by Ratmalana.🌄 Our university is best in Sri Lanka.❤ We Love Our University.💖

🏘 Official Website - http://univotec.ac.lk
 
🏘 Univotec info :
 	Chancellor - Dayantha Wijeyesekera
 	Vice-Chancellor - Ranjith Premalal De Silva
 	Founded - 2009
 	Number of students: 3,850
 	Undergraduates - 1,600
 	Motto - යාවජීව අධ්‍යාපනය සැමට (Life Long Learning for All!, Sinhala)
 
🏘 Univotec Student LMS - http://lms.univotec.ac.lk
 
🏘 Univotec Cantact info: 
 	Phone-  +94-112630700
 	Fax - +94-112630705
	Email - univotec@univotec.ac.lk
	Address - University of Vocational Technology, No. 100, Kandawala Road, Ratmalana, Sri Lanka
	
Thank You for mention this word.💖
 """)
		if message.text == "Bst" or message.text == "bst":
			bot.reply_to(message, """ 
👉 Our University is University of Vocational Technology.❤
👉 Our faculty is "Engineering Technology".❤
👉 And Our department is "Building service technology".💖
👉 Our coodinator is Ms.Samantha manawadu.
👉 Batch year: 2020
👉 Class Time: 8.30 A.M. - 6.15 P.M.
👉 Student: 45
👉 Ref: Uppla and Namindu
👉 our whatsapp Group: 
	🙏 BST 20 B1 official
	🙏 BST Community
	🙏 BST/B1/(Notes & Links)
	
	🙏 Communication Skill 20B1
	🙏 BST Mathematics
	
	🙏 2K2K Batch Groups
	
Thank You for mention this word.💖
""")
		if message.text == "Uppala" or message.text == "uppala":
			bot.reply_to(message, """ 
She is Our Class representative.
Her name is Uppala jayasekara.

your class member mention you.😁😁😁
I am BST Bot.😉😋
I love you. Uppala.😚💖
Stay Safe.😊❤💝
""")
		if message.text == "Namindu" or message.text == "namindu":
			bot.reply_to(message, """ 
He is Our Class representative.
His name is Namindu Fernando.

your class member mention you.😉
I am BST Bot.😊
I like you. Namindu.🤩
Stay Safe.❤
""")
			
@bot.message_handler(commands=["lecvideo"])
def send_message(message):
  bot.reply_to(message, """
1️⃣--- Lecture video Link in google drive ---1️⃣
  
👩‍🏫 Store 1 - https://drive.google.com/drive/folders/17iWwmC8o8fzcOTawutV2HCdObeS5ng99?usp=sharing
👨‍🏫 Store 2 - https://drive.google.com/drive/folders/1-C1dd0b9pnl5bralMDWJZZHHPXeGW16i?usp=sharing
👩‍🏫 Store 3 - https://drive.google.com/drive/folders/1JxtTTb1m9lJUABV3Knn7F8ZLdPYmeGna?usp=sharing
👩‍🏫 Store 4 - https://drive.google.com/drive/folders/1C_aOfD4OGDiW-bnXz3vGnVvdI7boHT6l?usp=sharing
👩‍🏫 Store 5 - https://drive.google.com/drive/folders/1C_aOfD4OGDiW-bnXz3vGnVvdI7boHT6l?usp=sharing
👨‍🏫 Store 6 - https://drive.google.com/drive/folders/1APwbC3KHUQHvhmc5W5phSwxxVzLcTqd0?usp=sharing
  
Thank you.❤ Your request.💖
  """)
			
bot.set_update_listener(handle_messages)
bot.polling()
