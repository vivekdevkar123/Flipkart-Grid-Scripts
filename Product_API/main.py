import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from Crawler import Get_Order_History,Get_Product_Details,Get_Related_Post

app = Flask(__name__)
CORS(app)

@app.route('/get_product_details', methods=['POST'])
def get_product_details():
    if request.method == 'POST':
        try:
            data = request.get_json()
            url = data.get('url')

            for _ in range(3):
                product_details = Get_Product_Details(url)
                if product_details:
                    break

            # Formatting the offers
            offers_str = "\n".join([
                f"  - {offer.get('Offer_type')}: {offer.get('Offer_Description')}"
                for offer in product_details.get("offers", [])
            ])

            # Formatting the specifications
            specs_str = "\n".join([
                f"  - {spec.get('title')}:\n" + "\n".join([
                    f"    - {detail.get('property')}: {detail.get('value')}"
                    for detail in spec.get("details", [])
                ])
                for spec in product_details.get("specs", [])
            ])

            # Formatting the highlights
            highlights_str = "\n".join([
                f"  - {highlight}"
                for highlight in product_details.get("highlights", [])
            ])

            formatted_response = f'Product Name: {product_details.get("name")}\nDescription: {product_details.get("product_description")}\nCurrent Price: ₹{product_details.get("current_price")}\nOriginal Price: ₹{product_details.get("original_price")}\nDiscount: {product_details.get("discount_percent")}%\nRating: {product_details.get("rating")}\nNumber of Ratings: {product_details.get("no_of_rating")}\nNumber of Reviews: {product_details.get("no_of_reviews")}\nHighlights:\n{highlights_str}\nOffers:\n{offers_str}\nSpecifications:\n{specs_str}\n'

            with open('product_details.txt', 'w', encoding='utf-8') as file:
                file.write(formatted_response)
            
            return jsonify(product_details), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/get_order_history', methods=['POST'])
def get_order_history():
    if request.method == 'POST':
        try:
            data = request.get_json()
            cookies = data.get('cookies')

            for _ in range(3):
                order_details = Get_Order_History(cookies)
                if order_details:
                    break

            formatted_response = ""

            for order in order_details:
                order_str = f"Order ID: {order['order_id']}\nProduct Name: {order['product_title']}\nPrice: {order['product_price']}\nProduct Category: {order['product_category']}\nOrder Date: {order['order_date']}\nNo of Items: {order['number_of_items']}\nMarketPlace: {order['marketplace']}\n\n"

                formatted_response += order_str
            
            with open('order_history.txt', 'w', encoding='utf-8') as file:
                file.write(formatted_response)

            return jsonify(order_details), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/get_related_post', methods=['POST'])
def get_related_post():
    if request.method == 'POST':
        try:
            data = request.get_json()
            url = data.get('url')

            for _ in range(3):
                order_details = Get_Related_Post(url)
                if order_details:
                    break

            formatted_response = ""
            for order in order_details:

                order_str = f"Product Name: {order['Product_Name']}\nProduct Url: {order['Product_URL']}\nCurrent Price: ₹{order['Current_Price']}\nOriginal Price: ₹{order['MRP_Price']}\nDiscount: {order['Product_offer']}\nRating: {order['Product_Rating']}\n\n"

                formatted_response += order_str
            
            with open('product_recomandation.txt', 'w', encoding='utf-8') as file:
                file.write(formatted_response)

            return jsonify(order_details), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        

if __name__ == '__main__':
    app.run(debug=True)
