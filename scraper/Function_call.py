import requests
import time
from Crawler import Get_Related_Post,Get_Product_Details,Get_Product_Details_Using_API,Get_Order_History



# start_time = time.time()
# link = '''thomson-phoenix-108-cm-43-inch-qled-ultra-hd-4k-smart-google-tv-dolby-vision-atmos/p/itm70a7a64aa66d3?pid=TVSGSHZRWZPTZ47Z&lid=LSTTVSGSHZRWZPTZ47ZXMEUVE&marketplace=FLIPKART&q=tv&store=ckf%2Fczl&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&fm=organic&iid=a9fe665a-e80d-4be2-80ea-5b9e64cc8c9b.TVSGSHZRWZPTZ47Z.SEARCH&ppt=sp&ppn=sp&ssid=4u06416bc00000001724000578453&qH=c9a1fdac6e082dd8'''
# Get_Product_Details_Using_API(link)
# # End time
# end_time = time.time()

# # Calculate the time taken
# execution_time = end_time - start_time

# print(f"Time taken to execute api code: {execution_time} seconds")





# # Start time
# start_time = time.time()

# link = '''https://www.flipkart.com/food-products/dry-fruit-nut-seed/pr?sid=eat%2Cltb&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&param=9552&hpid=KM6Pjnf8EGhpAF17AzVGxqp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJVcHRvIDc1JSBPZmYiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJOREZHRTNZVzdEVUs4UVJVIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiRHJ5IEZydWl0cyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D'''

# # Your code execution
# for _ in range(3):

#     ans = Get_Related_Post(link)
#     if(len(ans) > 0):
#         print(len(ans))
#         break

# # End time
# end_time = time.time()

# # Calculate the time taken
# execution_time = end_time - start_time

# print(f"Time taken to execute manual scraper: {execution_time} seconds")




# # Start time
# start_time = time.time()

# link = '''https://www.flipkart.com/thomson-phoenix-108-cm-43-inch-qled-ultra-hd-4k-smart-google-tv-dolby-vision-atmos/p/itm70a7a64aa66d3?pid=TVSGSHZRWZPTZ47Z&lid=LSTTVSGSHZRWZPTZ47ZXMEUVE&marketplace=FLIPKART&q=tv&store=ckf%2Fczl&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&fm=organic&iid=a9fe665a-e80d-4be2-80ea-5b9e64cc8c9b.TVSGSHZRWZPTZ47Z.SEARCH&ppt=sp&ppn=sp&ssid=4u06416bc00000001724000578453&qH=c9a1fdac6e082dd8'''

# Get_Product_Details(link)

# # End time
# end_time = time.time()

# # Calculate the time taken
# execution_time = end_time - start_time

# print(f"Time taken to execute manual product details scraping: {execution_time} seconds")



# Start time
start_time = time.time()

cookies = {
    '_gid': 'GA1.2.376810832.1723973383',
    'T': 'SD.8297445a-c3a7-454c-8db2-08c7f7f57a35.1723973442100',
    '_fbp': 'fb.1.1723973445369.584970553217977911',
    '_gac_UA-172010654-1': '1.1723974918.Cj0KCQjwt4a2BhD6ARIsALgH7Dq71gYehZuxgpal5uXIRb3oCj9cy9uZBEoT3zG9JGgsb1X6iVtJVCEaAt5-EALw_wcB',
    '_gcl_gs': '2.1.k1$i1723975268',
    '_gcl_aw': 'GCL.1723975304.Cj0KCQjwt4a2BhD6ARIsALgH7Dq71gYehZuxgpal5uXIRb3oCj9cy9uZBEoT3zG9JGgsb1X6iVtJVCEaAt5-EALw_wcB',
    '_gcl_au': '1.1.316233740.1723973445.2093527625.1723987793.1723987881',
    '_ga_2P94RMW04V': 'GS1.2.1723987560.2.1.1723988664.0.0.0',
    'vh': '695',
    'vw': '1536',
    'dpr': '1.25',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19954%7CMCMID%7C21476465616184877218592220524603309424%7CMCAAMLH-1724602689%7C12%7CMCAAMB-1724602689%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724005090s%7CNONE%7CMCAID%7CNONE',
    'mp_9ea3bc9a23c575907407cf80efd56524_mixpanel': '%7B%22distinct_id%22%3A%20%22ACC1CA692790CD146EC9021F458F9DC60D3%22%2C%22%24device_id%22%3A%20%2219164d53f8d5d7-0e4475eac7b911-26001e51-144000-19164d53f8e13ab%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%22ACC1CA692790CD146EC9021F458F9DC60D3%22%7D',
    '_ga': 'GA1.1.1985921494.1723973383',
    'AMCV_55CFEDA0570C3FA17F000101%40AdobeOrg': '-227196251%7CMCIDTS%7C19954%7CMCMID%7C65944996142707664201684694952521642495%7CMCAAMLH-1724578251%7C12%7CMCAAMB-1724610805%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724013205s%7CNONE%7CMCAID%7CNONE',
    '_ga_TVF0VCMCT3': 'GS1.1.1724006004.3.0.1724006005.59.0.0',
    '_ga_0SJLGHBL81': 'GS1.1.1724006004.3.1.1724006043.0.0.0',
    's_nr': '1724006061720-Repeat',
    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDgxOTE3MjAzNTY0NkJRSE40M1ciLCJma0RldiI6bnVsbH0sImV4cCI6MTczOTg0ODIzNSwiaWF0IjoxNzI0MDY4MjM1LCJqdGkiOiI4N2Y1Mzc3Ny1iNGRjLTQyN2ItODZmNi0xMTU4YmM0YTEyNGIifQ.G4wok2LFh1UPXO2mNYhd6sPHxBLEYIO5QyfrtXrLqGo',
    'ud': '4.yLMB0bKfvQdG3yvxWxMfS-rYCYvI9X15on9Jpz-4oS7aNvHr_lZoqd39zDhtjUA-dg_CHVgGAdkIRYEebo8qRF_78VktRbNcWW5n8wG0gbf7zM4PP3cCoaPoMVMxLE-ldMk0OW-XcBTKdUC0VA7BFbvDyIxSlE2pIzv-KEqKFhZDsUk7nDM8_wjmHgETMML5',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MjQwNzM4MzYsImlhdCI6MTcyNDA3MjAzNiwiaXNzIjoia2V2bGFyIiwianRpIjoiNTU1YjgxYmYtMjA4Yi00OWVhLWE5NWItYmM3NGQ2ODg5ZTUxIiwidHlwZSI6IkFUIiwiZElkIjoiU0QuODI5NzQ0NWEtYzNhNy00NTRjLThkYjItMDhjN2Y3ZjU3YTM1LjE3MjM5NzM0NDIxMDAiLCJiSWQiOiI0VUtaRlYiLCJrZXZJZCI6IlZJOUZGQkE5NjJERTRGNEU2NzkzQzFCRDE3ODNEQTc0OTkiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImFKSkRCcHRmTkFZYWhYWkpnSndVSGZfMEdYb05sN0I2MUlMWU1FR19JOHN6dV95bnZ3LVpHdz09IiwidnMiOiJMSSIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.DBCcNLNvFmFm12X_UhP9vNCgGnbPgr5RanUhavImEA0',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3Mzk5Njk2MzYsImlhdCI6MTcyNDA3MjAzNiwiaXNzIjoia2V2bGFyIiwianRpIjoiMTM0YmU2MTQtYWNjOC00MDQ2LTk0MTQtYzBlYjgzNmQxYTNiIiwidHlwZSI6IlJUIiwiZElkIjoiU0QuODI5NzQ0NWEtYzNhNy00NTRjLThkYjItMDhjN2Y3ZjU3YTM1LjE3MjM5NzM0NDIxMDAiLCJiSWQiOiI0VUtaRlYiLCJrZXZJZCI6IlZJOUZGQkE5NjJERTRGNEU2NzkzQzFCRDE3ODNEQTc0OTkiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiQkxVTjBaIn0.GwXJZF9bmvyhzt_8Gc89-9hjWa2WSn3lCBIJ9MEOIrs',
    'Network-Type': '4g',
    'gpv_pn': 'HomePage',
    'gpv_pn_t': 'FLIPKART%3AHomePage',
    's_sq': 'flipkart-prd%3D%2526pid%253DHomePage%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Faccount%25252Forders%25253Flink%25253Dhome_orders%2526ot%253DA',
    'K-ACTION': 'null',
    'S': 'd1t19EG41Pz8aCWg3NWwhPz88P04lmR/p+iIk8FB/7fKg+5vogftd/ASvcf87/12CHFZ52oJcPRxylLhURm/cwqCaJw==',
    'vd': 'VI9FFBA962DE4F4E6793C1BD1783DA7499-1723997889278-5.1724072246.1724072036.157882264',
    'SN': 'VI9FFBA962DE4F4E6793C1BD1783DA7499.TOK92737F6595C3415085C54EBF91F0CCD0.1724072252.LI',
}

data = Get_Order_History(cookies)

# End time
end_time = time.time()

# Calculate the time taken
execution_time = end_time - start_time

print(f"Time taken to get order history : {execution_time} seconds")



