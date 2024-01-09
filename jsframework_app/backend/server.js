// server.js
const express = require('express');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;

const app = express();
app.use(bodyParser.json());

// Connect to MongoDB
const client = new MongoClient('mongodb://localhost:27017/');
let db;
client.connect(err => {
    db = client.db('mydatabase');
});

app.post('/', (req, res) => {
    const num1 = parseFloat(req.body.num1);
    const num2 = parseFloat(req.body.num2);
    const result = num1 + num2;

    // Store the numbers and result in the database
    db.collection('results').insertOne({ num1, num2, result }, (err, r) => {
        res.send({ result });
    });
});

app.listen(3000, () => console.log('Server running on port 3000'));