# Add Numbers with DB

This is a simple Python Flask application that adds two numbers together and stores the result in a MongoDB NOSql database.

Notably this entire source code has been created using GitHub Copilot Chat feature.

## Setup

1. Set up your environment: Create a virtual environment and install the necessary packages. You can do this with the following commands:

```bash
python3 -m venv env
source env/bin/activate
pip install flask pymongo
```

2. Install MongoDB
```
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew tap mongodb/brew
brew install mongodb-community@4.4
```

3. Start your MongoDB service: Depending on your operating system, the command to do this will vary. On macOS with Homebrew, you can use brew services start mongodb-community@4.4.

```
brew services start mongodb-community@4.4
```

## Running and Accessing the application
1. Run the application: You can start the Flask application with the following command:
```
python add_numbers_with_db.py
```
or
```
python add_numbers.py
```

2. Visit the application: Open your web browser and navigate to http://localhost:5000. You can enter two numbers and submit the form to add them together.

3. View the results: Navigate to http://localhost:5000/results to see a list of all previous results.

## Files
`add_numbers_with_db.py`: This is the Python file for the Flask application. It defines two routes: one for adding numbers and one for viewing results. Also stores the data into MongoDB database

`add_numbers.py`: This is the Python file for the Flask application. It defines two routes: one for adding numbers and one for viewing results.

`templates/index.html`: This template includes a form for the user to enter two numbers.

`templates/results.html`: This template displays a list of all previous results.

`templates/result.html`: This template displays the result of the addition.

