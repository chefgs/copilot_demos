from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['results']

@app.route('/', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        result = num1 + num2

        # Store the numbers and result in the database
        collection.insert_one({'num1': num1, 'num2': num2, 'result': result})

        return render_template('result.html', result=result)
    else:
        return render_template('index.html')

@app.route('/results', methods=['GET'])
def get_results():
    # Fetch all documents from the collection
    documents = collection.find()

    # Convert documents into a list of dictionaries
    results = [doc for doc in documents]

    # Render a template with the results
    return render_template('results.html', results=results)
if __name__ == '__main__':
    app.run()