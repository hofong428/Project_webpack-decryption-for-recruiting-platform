import requests
import execjs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

cookies = {
    '__c': '1679414290',
    'wd_guid': 'a44ff943-955c-4e0d-87dd-6380b692882c',
    '__g': '-',
    'historyState': 'state',
    'AB_T': 'abva',
    'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1679414298',
    '__l': 'r=&l=%2Fapi_to%2Fhome%2Frec.json%3Fb%3DiRmyDtaWeYNdvanuH8A6PQ~~%26kiv%3DDCa43CWscW1dwdFr',
    'R_SCH_CY_V': '5855',
    'W_CITY_S_V': '70',
    '__a': '52259603.1679414290..1679414290.4.1.4.4',
    'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1679423059',
}

headers = {
    'authority': 'www.kanzhun.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': '__c=1679414290; wd_guid=a44ff943-955c-4e0d-87dd-6380b692882c; __g=-; historyState=state; AB_T=abva; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1679414298; __l=r=&l=%2Fapi_to%2Fhome%2Frec.json%3Fb%3DiRmyDtaWeYNdvanuH8A6PQ~~%26kiv%3DDCa43CWscW1dwdFr; R_SCH_CY_V=5855; W_CITY_S_V=70; __a=52259603.1679414290..1679414290.4.1.4.4; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1679423059',
    'href': 'https://www.kanzhun.com/firm/recruit/0nx_3g~~.html?ka=com-recruit-module-expose',
    'pragma': 'no-cache',
    'referer': 'https://www.kanzhun.com/firm/recruit/0nx_3g~~.html?ka=com-recruit-module-expose',
    'reqsource': 'fe',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

encrypt_k = execjs.compile(open('./webpack_kanzhun.js', 'r', encoding='utf-8').read()).call('encrypt123')
# print(encrypt_k)

params = {
    'b': encrypt_k['b'],
    'kiv': encrypt_k['kiv'],
}

response = requests.get('https://www.kanzhun.com/api_to/cjr/info.json', params=params, cookies=cookies,
                        headers=headers).text

decrypt_k = execjs.compile(open('./data_decryptk.js', 'r', encoding='utf-8').read()).call('decrypt123')
print(decrypt_k)