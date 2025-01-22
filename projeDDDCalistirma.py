# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:31:25 2025

@author: ekulac
"""



    
import requests
import base64
import json

# DDD dosyasını okuyun ve Base64 ile kodlayın
with open(r"C:\Users\ekulac\Downloads\example-1.ddd", "rb") as f:
    encoded_ddd = base64.b64encode(f.read()).decode('utf-8')

# Web servisine GET isteği gönderin
url = 'http://localhost:8000/'
params = {'ddd': encoded_ddd}
response = requests.get(url, params=params)

# JSON yanıtını alın
result = response.json()

# JSON verisini bir dosyaya yazdırın
output_file = r"C:\Users\ekulac\Downloads\output.json"
with open(output_file, "w") as json_file:
    json.dump(result, json_file, indent=4)

print(f"Sonuç başarıyla {output_file} dosyasına yazıldı.")
