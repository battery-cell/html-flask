from flask import Flask, render_template

app = Flask(__name__)

# Function that will be triggered when the button is clicked
def my_function():
    print("Button was clicked!")  # Example of a Python function being triggered

@app.route('/')
def home():
    return render_template('index.html')

# Route that will be triggered when the button is clicked
@app.route('/click', methods=['POST'])
def button_clicked():
    my_function()  # Call the Python function
    return "Button clicked and function triggered!"

if __name__ == '__main__':
    app.run(debug=True)
