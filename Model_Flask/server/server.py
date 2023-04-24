from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_name',methods=['GET'])
def get_location_name():
    response = jsonify({
        'location':util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')    
    return response

@app.route('/predict_home_price',methods=['GET', 'POST'])
def predict_home_price():
    baths=int(request.form['baths'])
    bedrooms=int(request.form['bedrooms'])
    area=float(request.form['area'])
    location=request.form['location']
    
    response=jsonify({
        'Estimated_Price':util.predicted_price(location,baths,bedrooms,area)
            })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

if __name__=="__main__":
    print("Starting python flask server for home price prediction")
    util.load_saved_artifact()
    app.run()