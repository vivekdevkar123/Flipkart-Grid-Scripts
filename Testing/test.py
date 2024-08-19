import requests
import time
from scraper.Crawler import Get_Related_Post,Get_Product_Details,Get_Product_Details_Using_API



start_time = time.time()
link = '''thomson-phoenix-108-cm-43-inch-qled-ultra-hd-4k-smart-google-tv-dolby-vision-atmos/p/itm70a7a64aa66d3?pid=TVSGSHZRWZPTZ47Z&lid=LSTTVSGSHZRWZPTZ47ZXMEUVE&marketplace=FLIPKART&q=tv&store=ckf%2Fczl&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&fm=organic&iid=a9fe665a-e80d-4be2-80ea-5b9e64cc8c9b.TVSGSHZRWZPTZ47Z.SEARCH&ppt=sp&ppn=sp&ssid=4u06416bc00000001724000578453&qH=c9a1fdac6e082dd8'''
Get_Product_Details_Using_API(link)
# End time
end_time = time.time()

# Calculate the time taken
execution_time = end_time - start_time

print(f"Time taken to execute api code: {execution_time} seconds")





# Start time
start_time = time.time()

link = '''https://www.flipkart.com/food-products/dry-fruit-nut-seed/pr?sid=eat%2Cltb&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&param=9552&hpid=KM6Pjnf8EGhpAF17AzVGxqp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJVcHRvIDc1JSBPZmYiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJOREZHRTNZVzdEVUs4UVJVIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiRHJ5IEZydWl0cyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D'''

# Your code execution
for _ in range(3):

    ans = Get_Related_Post(link)
    if(len(ans) > 0):
        print(len(ans))
        break

# End time
end_time = time.time()

# Calculate the time taken
execution_time = end_time - start_time

print(f"Time taken to execute manual scraper: {execution_time} seconds")




# Start time
start_time = time.time()

link = '''https://www.flipkart.com/thomson-phoenix-108-cm-43-inch-qled-ultra-hd-4k-smart-google-tv-dolby-vision-atmos/p/itm70a7a64aa66d3?pid=TVSGSHZRWZPTZ47Z&lid=LSTTVSGSHZRWZPTZ47ZXMEUVE&marketplace=FLIPKART&q=tv&store=ckf%2Fczl&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&fm=organic&iid=a9fe665a-e80d-4be2-80ea-5b9e64cc8c9b.TVSGSHZRWZPTZ47Z.SEARCH&ppt=sp&ppn=sp&ssid=4u06416bc00000001724000578453&qH=c9a1fdac6e082dd8'''

Get_Product_Details(link)

# End time
end_time = time.time()

# Calculate the time taken
execution_time = end_time - start_time

print(f"Time taken to execute manual product details scraping: {execution_time} seconds")



