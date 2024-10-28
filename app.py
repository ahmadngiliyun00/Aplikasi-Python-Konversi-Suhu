from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

@app.route('/', methods=['GET', 'POST'])
def home():
    fahrenheit = None
    kelvin = None

    if request.method == 'POST':
        try:
            celsius = float(request.form['temperature'])
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
        except ValueError:
            fahrenheit = "Invalid input"
            kelvin = "Invalid input"

    return render_template('index.html', fahrenheit=fahrenheit, kelvin=kelvin)

if __name__ == '__main__':
    app.run(debug=True)
