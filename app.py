from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the grid
grid_size = 37  # Numbers from 0 to 36
fields = [0] * grid_size

@app.route('/', methods=['GET', 'POST'])
def index():
    global fields
    warning_20 = None
    warning_90 = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Submit':
            number = int(request.form.get('number', 0))  # Get the submitted number
            if 0 <= number < grid_size:
                # Increment all fields by 1
                fields = [x + 1 for x in fields]
                # Set the field under the submitted number to 0
                fields[number] = 0

                # Check if any of the specified fields reach or exceed 20
                if any(fields[i] >= 20 for i in [7, 8, 9, 17, 18, 19, 27, 28, 29]):
                    warning_20 = "Warning: [7, 8, 9, 17, 18, 19, 27, 28, 29] those numbers have reached or exceeded a value of 20!"

                # Check if fields 28 and 29 reach or exceed 90
                if fields[28] >= 90 or fields[29] >= 90:
                    warning_90 = "Warning: Fields 28 or 29 have reached or exceeded a value of 90!"

        elif action == 'Clear':
            # Reset fields to initial state
            fields = [0] * grid_size

    return render_template('index.html', fields=fields, warning_20=warning_20, warning_90=warning_90)

if __name__ == '__main__':
    app.run(debug=True)
