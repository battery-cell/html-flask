from flask import Flask, render_template, request

app = Flask(__name__)

def my_function():
    print("okay bud")

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        message = my_function()  # Call the Python function
    if request.method == 'POST':
        message = my_function()  # Call the Python function
    return render_template('index.html', message=message)
if __name__ == '__main__':
    app.run(debug=True)
