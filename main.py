import os
import telebot


bot = telebot.TeleBot("1914396081:AAHNFA2409oexT-JMVr5eOnkFMaXb__3xkg")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, """
Hello!π I'm BST Community Chat Bot.π
  
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
.github, .Github
.call yasith, .call Yasith

Thank you.β€ Your request.π
  """)


@bot.message_handler(commands=["botcreator"])
def send_message(message):
  bot.reply_to(message, """
I am built by yasith praharshana.π§
He is Univotec BST Class Member.π

Thank you.β€ Your request.π
  """)
  
@bot.message_handler(commands=["monitor"])
def send_message(message):
  bot.reply_to(message, """
Naminduπ¦ and Uppalaπ§. 
They are our Class representative.βΊβ€

Thank you.β€ Your request.π
""")

@bot.message_handler(commands=["subject"])
def send_message(message):
  bot.reply_to(message, """
1οΈβ£--- First Semester Subject ---1οΈβ£
  
π©βπ« Construction Technology - Ms. Samantha
π¨βπ« Fluid mechanics - Mr. Tharinda
π©βπ« English (com. Skill) - Ms. Kokila
π©βπ« Engineering Physics - Ms. Chamila
π©βπ« Theory of elecricity - Ms. Chamila
π¨βπ« Engineering Maths - Mr. Naveen
π¨βπ« Construction Drawing - Mr. Sampath
  
Thank you.β€ Your request.π
  """)
    
def handle_messages(messages):
	for message in messages:
		if message.text == "hi" or message.text == "Hi":
		# Do something with the message
			bot.reply_to(message, 'Hi my dear, I am Bst univotec bot.π€ How are you.β€')
			
		if message.text == "univotec" or message.text == "Univotec":
			bot.reply_to(message, """ 
Our University is University of Vocational Technology.π It is located by Ratmalana.π Our university is best in Sri Lanka.β€ We Love Our University.π

π Official Website - http://univotec.ac.lk
 
π Univotec info :
 	Chancellor - Dayantha Wijeyesekera
 	Vice-Chancellor - Ranjith Premalal De Silva
 	Founded - 2009
 	Number of students: 3,850
 	Undergraduates - 1,600
 	Motto - ΰΆΊΰ·ΰ·ΰΆ’ΰ·ΰ· ΰΆΰΆ°ΰ·βΰΆΊΰ·ΰΆ΄ΰΆ±ΰΆΊ ΰ·ΰ·ΰΆΈΰΆ§ (Life Long Learning for All!, Sinhala)
 
π Univotec Student LMS - http://lms.univotec.ac.lk
 
π Univotec Cantact info: 
 	Phone-  +94-112630700
 	Fax - +94-112630705
	Email - univotec@univotec.ac.lk
	Address - University of Vocational Technology, No. 100, Kandawala Road, Ratmalana, Sri Lanka
	
Thank You for mention this word.π
 """)
		if message.text == "Bst" or message.text == "bst":
			bot.reply_to(message, """ 
π Our University is University of Vocational Technology.β€
π Our faculty is "Engineering Technology".β€
π And Our department is "Building service technology".π
π Our coodinator is Ms.Samantha manawadu.
π Batch year: 2020
π Class Time: 8.30 A.M. - 6.15 P.M.
π Student: 45
π Ref: Uppla and Namindu
π our whatsapp Group: 
	π BST 20 B1 official
	π BST Community
	π BST/B1/(Notes & Links)
	
	π Communication Skill 20B1
	π BST Mathematics
	
	π 2K2K Batch Groups
	
Thank You for mention this word.π
""")
		if message.text == "Uppala" or message.text == "uppala":
			bot.reply_to(message, """ 
She is Our Class representative.
Her name is Uppala jayasekara.

your class member mention you.πππ
I am BST Bot.ππ
I love you. Uppala.ππ
Stay Safe.πβ€π
""")
		if message.text == "Namindu" or message.text == "namindu":
			bot.reply_to(message, """ 
He is Our Class representative.
His name is Namindu Fernando.

your class member mention you.π
I am BST Bot.π
I like you. Namindu.π€©
Stay Safe.β€
""")

		if message.text == ".github" or message.text == ".Github":
			bot.reply_to(message, """ 
Yalu oyaa oya command eka gahapu eka hodai deyak.π
mekata gihin balanna kohomada ara yaka mawa program kare kiyala.π 
ara yaka mokak mata karala thiyenwada kiyala machan ubala danne nane.π€
me pahala link eken gihin mage Repositoriyata yanna.π
eke athi " main.py " kiyala ekak. eka uda click karanna.π±
ita passe mage program eka balanna puluwan oyalata.π₯

Link : https://github.com/yasithpc/TGbotchat

oya anith hamotama loku udawuwak kare gihin balnna ko.β£ oyata lesiyen kiywanna puluwan meka.π
gihin balanna.π
Stay Safe.β€
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
			bot.reply_to(message, """Hi my dear, I am Bst univotec bot.π€ How are you.β€
			
			This is a my new feature.βΊ
			type ".bot" and get my all ".bot command list"
			
			
			Thank you...β€
			""")
			
		if message.text == ".bot yasith" or message.text == ".bot Yasith":
			bot.reply_to(message, """ 
Ow, oka thamai mawa hadapu ekaa.π€­
oya bot fatherge mama athuluwa robola 2 nek oyalage group eke innawa haloo.π€π
Stay Safe.β€
""")
		if message.text == ".call yasith" or message.text == ".call Yasith":
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
e ban ubalage lecture patan gena ban.π€¦ββοΈ
""")
		if message.text == ".bot lecture -s" or message.text == ".bot Lecture -s":
			bot.reply_to(message, """ 
me anna lecture eka patan gena. wawulo wage ellagena balan inne nathuwa lecture ekata yanawa. meka me kattiya hamotama kiwwe hariye.π‘
""")
		if message.text == ".bot lecture -s r" or message.text == ".bot Lecture -s r":
			bot.reply_to(message, """ 
ara madam hari sir hari balan athi ban.π  paw ban e minissu.π ubalata therenne nadda e minissu ubalata wenuwen darana mahansiya.π’ wena lecture kenek nam padama igannuwa giya. π’
ubala maha paw karayo bn.π°
""")
		if message.text == ".bot lecture -s rr" or message.text == ".bot Lecture -s rr":
			bot.reply_to(message, """ 
mage yaka aussa ganne nathuwa pala lecture ekata besige puthala.π€¬
""")
		if message.text == ".bot lecture -s rrr" or message.text == ".bot Lecture -s rrr":
			bot.reply_to(message, """ 
ubala kage daruwoda kiyapan.chik witharak. paw ara interview list eke ubalata passe hitapu un. unta chance ekak dunna nam. mehema me lectureslata duk widinna wenne na.π€¬
""")
		if message.text == ".bot lecture y -l" or message.text == ".bot Lecture y -l":
			bot.reply_to(message, """ 
oi mage wachana padama aha ganne nathuwa lecture ekata pala. gon yasithaya.π‘
""")
		if message.text == ".bot lecture y -ll" or message.text == ".bot Lecture y -ll":
			bot.reply_to(message, """ 
buru yasith. ubage yaluwo lecture ekata enakan balan innawa. mee harakek wenna epa.π‘

uppala anith set eka mehema hariyanne na. jathuya amathannama one.
""")
		if message.text == ".bot lecture y -lll" or message.text == ".bot Lecture y -lll":
			bot.reply_to(message, """ 
kamak na ban. okata kela unama therewi. ubala mewelawe monada kiwwe kiyala.π‘

aulak na bn. ubala lecture ekata participate wenna ban. ubala thamai real yaluwo.π
""")

#End-List
@bot.message_handler(commands=["lecvideo"])
def send_message(message):
  bot.reply_to(message, """
1οΈβ£--- Lecture video Link in google drive ---1οΈβ£
  
π Store 1 - https://drive.google.com/drive/folders/17iWwmC8o8fzcOTawutV2HCdObeS5ng99?usp=sharing
π Store 2 - https://drive.google.com/drive/folders/1-C1dd0b9pnl5bralMDWJZZHHPXeGW16i?usp=sharing
π Store 3 - https://drive.google.com/drive/folders/1JxtTTb1m9lJUABV3Knn7F8ZLdPYmeGna?usp=sharing
π Store 4 - https://drive.google.com/drive/folders/1C_aOfD4OGDiW-bnXz3vGnVvdI7boHT6l?usp=sharing
π Store 5 - https://drive.google.com/drive/folders/1C_aOfD4OGDiW-bnXz3vGnVvdI7boHT6l?usp=sharing
π Store 6 - https://drive.google.com/drive/folders/1APwbC3KHUQHvhmc5W5phSwxxVzLcTqd0?usp=sharing

Store 1 :
Building Construction
Maths

Store 2 :
Fluid mechanics

Store 3 :
Architecture
Chamila madam (Physics, Electricity)

Store 4 :
Autocad Drawing
English Lecture

Strore 5 :
Fluid 02 - foundation video

Store 6 :
Kuppi store.

Thank you.β€ Your request.π
  """)
			
bot.set_update_listener(handle_messages)
bot.polling()
