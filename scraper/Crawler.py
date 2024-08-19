import json
import re
import requests
from bs4 import BeautifulSoup as bs

def Get_Related_Post(url: str):
    '''
    Example Url

    1. https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=cbf12b63-0b14-4eeb-b131-afc9e1695106

    2. https://www.flipkart.com/sports/cycling/electric-cycle/pr?sid=abc%2Culv%2Ctwp&hpid=IN6WQymhhksnM1l95t0Z6Kp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJVcCB0byA0MCUgT2ZmIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiRUNZSDJYNjQyQ0hYRERDViIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkVsZWN0cmljIEN5Y2xlIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D

    '''
    response = requests.get(url)

    soup = bs(response.text, 'html.parser')
    elements = soup.find_all("div", class_="_75nlfW")[:10]
    results = []

    try:
        for element in elements:
            try:
                product_url = "https://www.flipkart.com" + element.find("a")['href']
                offer_percentage = element.find("span", string=lambda text: text and "% off" in text).text.replace('off', '').replace('%', '')
                curr_price = element.find("div", class_="Nx9bqj").text[1:].replace(',', '')
                mrp_price = element.find("div", class_="yRaY8j").text[1:].replace(',', '')

                try:
                    name = element.find("a", class_="WKTcLC")['title']
                except:
                    name = element.find("img", class_="DByuf4")['alt']

                try:
                    rating = element.find('div', attrs={'class':'hGSR34'})
                except:
                    rating = None

                results.append({
                    'Product_Name': name,
                    'Product_Rating': rating,
                    'Current_Price': curr_price,
                    'MRP_Price': mrp_price,
                    'Product_offer': offer_percentage,
                    'Product_URL':product_url
                })
                

            except Exception as e:
                print(f"Error processing element: {e}")
                continue

    except:
        return results

    return results



def Get_Product_Details(url:str):
    '''
    Example url : https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_2&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&fm=search-autosuggest&iid=25e70862-cf70-4e13-ac60-fe7660686dfc.MOBGTAGPTB3VS24W.SEARCH&ppt=sp&ppn=sp&ssid=mni1rvlby80000001724048231675&qH=eb4af0bf07c16429
    '''
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    product = soup.find('div', class_=['DOjaWF', 'YJG4Cf'])

    result = {}

    try:
        name = product.find("h1", class_="_6EBuvT").text
        current_price = product.find("div", class_="Nx9bqj CxhGGd").text.replace(',', '').replace('₹', '')
        original_price = product.find("div", class_="yRaY8j A6+E6v").text.replace(',', '').replace('₹', '')
        discount_percent = product.find("div", class_=re.compile(r'\bUkUFwK\b.*\bWW8yVX\b')).text.replace('off', '').replace('%', '')
        rating = product.find("div", class_="XQDdHH").text
        rating_count_span = product.find("span", class_="Wphh3N").find_all("span")
        matches = re.findall(r'(\d{1,3}(?:,\d{3})*)', rating_count_span[0].text)
        if matches and len(matches) == 2:
            no_of_rating = matches[0].replace(',', '')
            no_of_reviews = matches[1].replace(',', '')
        else:
            no_of_rating = rating_count_span[1].text.split(" ")[0].replace(',', '')
            no_of_reviews = rating_count_span[3].text.split(" ")[0].replace(',', '')

        All_offer_tags = product.find("div", class_="I+EQVr").find_all("span")
        offers = []
        for offer in All_offer_tags:
            try:
                all_span = offer.find("li").find_all('span')
                offer_type = all_span[0].text
                offer_description = all_span[1].text
                offers.append({
                    "Offer_type":offer_type,
                    "Offer_Description":offer_description
                })
            except Exception as e:
                continue

        highlights = []
        try:
            all_highlights_tag = product.find("div", class_="xFVion").find_all("li")
            for highlight in all_highlights_tag:
                highlights.append(highlight.text)
        except:
            highlights = []

        Payment_Options = []
        try:
            Payment_Options_tag = product.find("div", class_="HQijVm").find_all("li")
            for option in Payment_Options_tag:
                Payment_Options.append(option.text)
        except:
            Payment_Options = []

        try:
            product_description = product.find("div", class_="yN+eNk w9jEaj").text
        except:
            product_description = ""

        specs = []

        All_specs_tag = product.find("div",class_="_1OjC5I")
        if All_specs_tag:
            for spec in All_specs_tag.find_all("div"):
                try:
                    title = spec.find("div").text
                    details = []
                    table_rows = spec.find("table",class_="_0ZhAN9").find_all("tr")
                    for each_row in table_rows:
                        all_property = each_row.find_all("td")
                        pro = all_property[0].text
                        val = all_property[1].text
                        details.append({
                            "property": pro,
                            "value": val
                        })
                    
                    specs.append({
                        "title":title,
                        "details":details
                    })
                except:
                    continue
                
        result = {
            "name": name,
            "current_price": current_price,
            "original_price": original_price,
            "discount_percent": discount_percent,
            "rating": rating,
            "no_of_rating": no_of_rating,
            "no_of_reviews": no_of_reviews,
            "highlights": highlights,
            "offers": offers,
            "Payment_Options": Payment_Options,
            "product_description": product_description,
            "specs": specs
        }

    except:
        return result

    return result

def Get_Product_Details_Using_API(url:str):
    '''
    Example URL : thomson-phoenix-108-cm-43-inch-qled-ultra-hd-4k-smart-google-tv-dolby-vision-atmos/p/itm70a7a64aa66d3?pid=TVSGSHZRWZPTZ47Z&lid=LSTTVSGSHZRWZPTZ47ZXMEUVE&marketplace=FLIPKART&q=tv&store=ckf%2Fczl&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&fm=organic&iid=a9fe665a-e80d-4be2-80ea-5b9e64cc8c9b.TVSGSHZRWZPTZ47Z.SEARCH&ppt=sp&ppn=sp&ssid=4u06416bc00000001724000578453&qH=c9a1fdac6e082dd8

    '''
    response = requests.get("http://localhost:3000/product/" + url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("bad request",response.status_code)