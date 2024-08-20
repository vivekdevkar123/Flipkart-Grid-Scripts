from flask import Flask, request, jsonify
from Crawler import Get_Order_History,Get_Product_Details,Get_Product_Details_Using_API,Get_Related_Post

app = Flask(__name__)

@app.route('/sendprompt', methods=['POST'])
def send_text():
    # Get the text data from the request
    data = request.json
    text = data.get('text', '')

    # Return the text data in the response
    return jsonify({
        'status': 'success',
        'received_text': text
    })


@app.route('/get_product_details', methods=['POST'])
def get_product_details():
    if request.method == 'POST':
        try:
            data = request.get_json()
            url = data.get('url')
            product_details = Get_Product_Details(url)
            
            return jsonify(product_details), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/get_order_history', methods=['POST'])
def get_order_history():
    if request.method == 'POST':
        try:
            data = request.get_json()
            cookies = data.get('cookies')
            order_details = Get_Order_History(cookies)
            
            return jsonify(order_details), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        


@app.route('/get_product_details_using_api', methods=['POST'])
def get_product_details_using_api():
    if request.method == 'POST':
        try:
            data = request.get_json()
            url = data.get('url')
            order_details = Get_Product_Details_Using_API(url)
            
            return jsonify(order_details), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/get_related_post', methods=['POST'])
def get_related_post():
    if request.method == 'POST':
        try:
            data = request.get_json()
            url = data.get('url')
            order_details = Get_Related_Post(url)
            
            return jsonify(order_details), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        

if __name__ == '__main__':
    app.run(debug=True)
