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
yasith, Yasith
.github, .Github
.call yasith, .call Yasith

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

		if message.text == ".github" or message.text == ".Github":
			bot.reply_to(message, """ 
Yalu oyaa oya command eka gahapu eka hodai deyak.😍
mekata gihin balanna kohomada ara yaka mawa program kare kiyala.😉 
ara yaka mokak mata karala thiyenwada kiyala machan ubala danne nane.🤔
me pahala link eken gihin mage Repositoriyata yanna.👇
eke athi " main.py " kiyala ekak. eka uda click karanna.🖱
ita passe mage program eka balanna puluwan oyalata.🖥

Link : https://github.com/yasithpc/TGbotchat

oya anith hamotama loku udawuwak kare gihin balnna ko.❣ oyata lesiyen kiywanna puluwan meka.😎
gihin balanna.😉
Stay Safe.❤
""")

#.bot command section
		if message.text == ".bot" or message.text == ".bot":
			bot.reply_to(message, """ 
.bot word list:
---------

.bot yasith,		.bot Yasith
.bot lecture *s ,	.bot Lecture *s
.bot lecture +s ,	.bot Lecture +s
.bot lecture -s ,	.bot Lecture -s
.bot lecture -s r ,	.bot Lecture -s r
.bot lecture -s rr ,	.bot Lecture -s rr
.bot lecture -s rrr ,	.bot Lecture -s rrr
.bot lecture y -l ,	.bot Lecture y -l
.bot lecture y -ll ,	.bot Lecture y -ll
.bot lecture y -lll ,	.bot Lecture y -lll

explain : *s - before, +s - now, -s after, r - recall, -l - late the lecture (for only owner) 
---------
			""")
		if message.text == ".bot hi" or message.text == ".bot Hi":
		# Do something with the message
			bot.reply_to(message, """Hi my dear, I am Bst univotec bot.🤗 How are you.❤
			This is a my new feature.☺
			type ".bot" and get my all ".bot command list"
			
			Thank you...❤
			""")
			
		if message.text == ".bot yasith" or message.text == ".bot Yasith":
			bot.reply_to(message, """ 
Ow, oka thamai mawa hadapu ekaa.🤭
oya bot fatherge mama athuluwa robola 2 nek oyalage group eke innawa haloo.🤗😉
Stay Safe.❤
""")
		if message.text == ".call Yasith" or message.text == ".call Yasith":
			bot.reply_to(message, """ 
Ado yasith anna ubata yaluwek katha karanawa poddak balahan.
poddak balahan kiwwama. oi. gon athal ganne nathuwa. shik. ohe mokekda manda.
""")
		if message.text == ".bot lecture *s" or message.text == ".bot Lecture *s":
			bot.reply_to(message, """ 
lamaaai. oyalage lecture patan gannai yanne. ko ko lasthi wenna.
""")
		if message.text == ".bot lecture +s" or message.text == ".bot Lecture +s":
			bot.reply_to(message, """ 
e ban ubalage lecture patan gena ban.🤦‍♂️
""")
		if message.text == ".bot lecture -s" or message.text == ".bot Lecture -s":
			bot.reply_to(message, """ 
me anna lecture eka patan gena. wawulo wage ellagena balan inne nathuwa lecture ekata yanawa. meka me kattiya hamotama kiwwe hariye.😡
""")
		if message.text == ".bot lecture -s r" or message.text == ".bot Lecture -s r":
			bot.reply_to(message, """ 
ara madam hari sir hari balan athi ban.😠 paw ban e minissu.😟 ubalata therenne nadda e minissu ubalata wenuwen darana mahansiya.😢 wena lecture kenek nam padama igannuwa giya. 😢
ubala maha paw karayo bn.😰
""")
		if message.text == ".bot lecture -s rr" or message.text == ".bot Lecture -s rr":
			bot.reply_to(message, """ 
mage yaka aussa ganne nathuwa pala lecture ekata besige puthala.🤬
""")
		if message.text == ".bot lecture -s rrr" or message.text == ".bot Lecture -s rrr":
			bot.reply_to(message, """ 
ubala kage daruwoda kiyapan.chik witharak. paw ara interview list eke ubalata passe hitapu un. unta chance ekak dunna nam. mehema me lectureslata duk widinna wenne na.🤬
""")
		if message.text == ".bot lecture y -l" or message.text == ".bot Lecture y -l":
			bot.reply_to(message, """ 
oi mage wachana padama aha ganne nathuwa lecture ekata pala. gon yasithaya.😡
""")
		if message.text == ".bot lecture y -ll" or message.text == ".bot Lecture y -ll":
			bot.reply_to(message, """ 
buru yasith. ubage yaluwo lecture ekata enakan balan innawa. mee harakek wenna epa.😡

uppala anith set eka mehema hariyanne na. jathuya amathannama one.
""")
		if message.text == ".bot lecture y -lll" or message.text == ".bot Lecture y -lll":
			bot.reply_to(message, """ 
kamak na ban. okata kela unama therewi. ubala mewelawe monada kiwwe kiyala.😡

aulak na bn. ubala lecture ekata participate wenna ban. ubala thamai real yaluwo.💕
""")

#End-List
@bot.message_handler(commands=["lecvideo"])
def send_message(message):
  bot.reply_to(message, """
1️⃣--- Lecture video Link in google drive ---1️⃣
  
📎 Store 1 - https://drive.google.com/drive/folders/17iWwmC8o8fzcOTawutV2HCdObeS5ng99?usp=sharing
📎 Store 2 - https://drive.google.com/drive/folders/1-C1dd0b9pnl5bralMDWJZZHHPXeGW16i?usp=sharing
📎 Store 3 - https://drive.google.com/drive/folders/1JxtTTb1m9lJUABV3Knn7F8ZLdPYmeGna?usp=sharing
📎 Store 4 - https://drive.google.com/drive/folders/1C_aOfD4OGDiW-bnXz3vGnVvdI7boHT6l?usp=sharing
📎 Store 5 - https://drive.google.com/drive/folders/1C_aOfD4OGDiW-bnXz3vGnVvdI7boHT6l?usp=sharing
📎 Store 6 - https://drive.google.com/drive/folders/1APwbC3KHUQHvhmc5W5phSwxxVzLcTqd0?usp=sharing
  
Thank you.❤ Your request.💖
  """)
			
bot.set_update_listener(handle_messages)
bot.polling()
