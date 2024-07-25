import json
from zipfile import ZipFile
from io import BytesIO

# Define the file structure and contents
file_structure = {
    "idea-to-app-gpt/package.json": json.dumps({
        "name": "idea-to-app-gpt",
        "version": "1.0.0",
        "description": "A simple Node.js project for integrating GPT with a UI for generating app ideas.",
        "main": "server.js",
        "scripts": {
            "start": "node server.js"
        },
        "dependencies": {
            "axios": "^0.21.1",
            "dotenv": "^8.2.0",
            "express": "^4.17.1"
        },
        "author": "",
        "license": "ISC"
    }, indent=2),
    "idea-to-app-gpt/.env": "OPENAI_API_K_E_Y=""\n",
    "idea-to-app-gpt/server.js": """
require('dotenv').config();
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(express.json());

app.post('/generate', async (req, res) => {
    const prompt = req.body.prompt;
    try {
        const response = await axios.post(
            'https://api.openai.com/v1/engines/davinci-codex/completions',
            {
                prompt: `Generate an app idea: ${prompt}`,
                temperature: 0.7,
                max_tokens: 256,
                top_p: 1,
                frequency_penalty: 0,
                presence_penalty: 0,
            },
            { headers: { Authorization: `Bearer ${process.env.OPENAI_API_K_E_Y}` } }
        );
        res.json({ success: true, response: response.data.choices[0].text });
    } catch (error) {
        console.error('OpenAI API Error:', error);
        res.status(500).json({ success: false, message: 'Error generating app idea' });
    }
});

app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));
""",
    "idea-to-app-gpt/public/index.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Idea to App Generator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Idea to App Generator</h1>
    <textarea id="ideaInput" placeholder="Enter your app idea"></textarea>
    <button onclick="generateIdea()">Generate App Idea</button>
    <div id="ideaOutput"></div>
    <script src="script.js"></script>
</body>
</html>
""",
    "idea-to-app-gpt/public/style.css": """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0;
}

textarea {
    width: calc(100% - 22px);
    margin-bottom: 10px;
}

button {
    padding: 10px 15px;
    cursor: pointer;
}

#ideaOutput {
    margin-top: 20px;
    padding: 10px;
    background-color: #fff;
    border: 1px solid #ddd;
}
""",
    "idea-to-app-gpt/public/script.js": """
async function generateIdea() {
    const prompt = document.getElementById('ideaInput').value;
    const responseElement = document.getElementById('ideaOutput');
    responseElement.innerText = 'Generating...';

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt }),
        });

        const data = await response.json();
        if (data.success) {
            responseElement.innerText = data.response;
        } else {
            responseElement.innerText = 'Failed to generate idea. Please try again.';
        }
    } catch (error) {
        console.error('Error:', error);
        responseElement.innerText = 'An error occurred. Please try again.';
    }
}
"""
}

# Use BytesIO to create the ZIP file in memory
zip_buffer = BytesIO()
with ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for filepath, content in file_structure.items():
        zip_file.writestr(filepath, content)

# Prepare the ZIP file for downloading
zip_buffer.seek(0)
zip_filename = "/file/download/path/idea-to-app-gpt.zip"
with open(zip_filename, "wb") as f:
    f.write(zip_buffer.read())

zip_filename
