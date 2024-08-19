import json
import time
from scraper.Crawler import Get_Related_Post,Get_Product_Details

links = [
    '''https://www.flipkart.com/search?q=shoes&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=shoes&requestId=43bd7b8e-b259-4842-b993-a6da28e2d749''',

    '''https://www.flipkart.com/search?q=t+shirts&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_3_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_3_0_na_na_na&as-pos=3&as-type=TRENDING&suggestionId=t+shirts&requestId=b7f8243a-ad38-4a92-9297-a9358c6494af''',

    '''https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=cbf12b63-0b14-4eeb-b131-afc9e1695106''',

    '''
    https://www.flipkart.com/sports/cycling/electric-cycle/pr?sid=abc%2Culv%2Ctwp&hpid=IN6WQymhhksnM1l95t0Z6Kp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJVcCB0byA0MCUgT2ZmIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiRUNZSDJYNjQyQ0hYRERDViIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkVsZWN0cmljIEN5Y2xlIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D''',
    
    '''https://www.flipkart.com/audio-video/headset/pr?sid=0pm%2Cfcn&p%5B%5D=facets.connectivity%255B%255D%3DBluetooth&sort=popularity&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D599&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.headphone_type%255B%255D%3DTrue%2BWireless&param=866&hpid=WqCPtE2MbDEYEbYbttXC1qp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJHcmFiIE5vdyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6IkFDQ0ZTREdYWDNTNkRWQkciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJCZXN0IFRydWV3aXJlbGVzcyBIZWFkcGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D''',


    '''https://www.flipkart.com/food-products/dry-fruit-nut-seed/pr?sid=eat%2Cltb&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&param=9552&hpid=KM6Pjnf8EGhpAF17AzVGxqp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJVcHRvIDc1JSBPZmYiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJOREZHRTNZVzdEVUs4UVJVIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiRHJ5IEZydWl0cyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D'''
]


# for i in range(50):
#     print(f"step : {i}")
#     for link in links:
#         flag = 1
#         for _ in range(3):
#             ans = Get_Related_Post(link)
#             if(len(ans) > 0):
#                 print(len(ans))
#                 flag = 0
#                 break
#         if(flag):
#             print(0)

#     print("\n\n")


# ans = Get_Related_Post(links[0])

# print(ans)


products = [
    '''https://www.flipkart.com/canon-mg2570s-multi-function-color-inkjet-printer/p/itme8pd6c9gcente?pid=PRNE8PD6M53KZZXA&lid=LSTPRNE8PD6M53KZZXAZEUAHX&marketplace=FLIPKART&store=6bo%2Ftia%2Fffn%2Ft64&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&fm=organic&iid=en_rCvRaXV-QInfUCYxYr_xpMGqQkUJ1M4iQ-pgEph6dK9bwFhcGcK1b4KFSMqKvOii7dvwvyb45BLTlpJUHMK7cw%3D%3D&ppt=hp&ppn=homepage&ssid=vqi9zksrlc0000001724047180970''',

    '''https://www.flipkart.com/fabbmate-trendy-sports-shoes-women-s-running-walking-memory-foam-running-women/p/itm2819ceb3ce43a?pid=SHOGZEZWYKE3RZ7C&lid=LSTSHOGZEZWYKE3RZ7CLI08VE&marketplace=FLIPKART&q=shoes&store=osp&srno=s_1_2&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=search-autosuggest&iid=en_vHPShxx5lYE-NNsJGRfofOc8i_VvBVqLA3-34Ga16bJWW83DPa4N4cVwexSjgLI0y3Pi2AdwK6VbDLQHlmelCA%3D%3D&ppt=sp&ppn=sp&ssid=4darejt77k0000001724048200921&qH=b0a8b6f820479900''',

    '''https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_2&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&fm=search-autosuggest&iid=25e70862-cf70-4e13-ac60-fe7660686dfc.MOBGTAGPTB3VS24W.SEARCH&ppt=sp&ppn=sp&ssid=mni1rvlby80000001724048231675&qH=eb4af0bf07c16429''',

    '''https://www.flipkart.com/kitchen-jungle-trail-mix-1-kg-perfect-mixture-healthy-dry-fruits-berries-raisins-assorted-seeds-nuts/p/itmea07720ceb752?pid=NDFGVMPGQFVNPYZ9&lid=LSTNDFGVMPGQFVNPYZ9QI98EB&marketplace=FLIPKART&store=eat%2Fltb&srno=b_1_1&otracker=browse&fm=organic&iid=en_K9TdFj4mEspMSH8VYL2J3ihaVN3eSf-QS__sE9y6fai3ZnuVku3qJQkUQuI74ytKhoSg8GjGbBxw4bjht5vjlg%3D%3D&ppt=browse&ppn=browse&ssid=dhes8q0b0g0000001724048266583'''
]


for i in range(50):
    print("step ",i)
    for link in products:
        flag = 1
        for _ in range(3):
            ans = Get_Product_Details(link)
            if ans:
                flag = 0
                print("found")
                break
        if(flag):
            print("not found")

    print("\n\n")
