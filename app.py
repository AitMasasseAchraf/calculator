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
    warning_40 = None  # Warning for [0, 10, 20, 30]
    warning_new_20 = None  # New warning for [0, 5, 6, 1, 2, 3, 7, 8, 9]

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Submit':
            number = int(request.form.get('number', 0))  # Get the submitted number
            if 0 <= number < grid_size:
                # Increment all fields by 1
                fields = [x + 1 for x in fields]
                # Set the field under the submitted number to 0
                fields[number] = 0

                # Logic for warning_20: only show if any of the specified fields' values are exactly 20, 40, 60, etc.
                warning_20_values = [fields[i] for i in [7, 8, 9, 17, 18, 19, 27, 28, 29]]
                if any(value % 20 == 0 and value != 0 for value in warning_20_values):
                    warning_20 = "Warning: [7, 8, 9, 17, 18, 19, 27, 28, 29] those numbers have reached a threshold of 20, 40, 60, etc.!"

                # Logic for warning_90: only show if fields 28 or 29's values are exactly 90, 180, etc.
                if fields[28] % 90 == 0 and fields[28] != 0 or fields[29] % 90 == 0 and fields[29] != 0:
                    warning_90 = "Warning: Fields 28 or 29 have reached a threshold of 90, 180, etc.!"

                # Logic for warning_40: for numbers [0, 10, 20, 30], show if they reach 40, 80, 120, etc.
                warning_40_values = [fields[i] for i in [0, 10, 20, 30]]
                if any(value % 40 == 0 and value != 0 for value in warning_40_values):
                    warning_40 = "Warning: Fields [0, 10, 20, 30] have reached a threshold of 40, 80, 120, etc.!"

                # New logic for warning_new_20: for numbers [0, 5, 6, 1, 2, 3, 7, 8, 9], show if they reach 20, 40, etc.
                new_20_values = [fields[i] for i in [0, 5, 6, 1, 2, 3, 7, 8, 9]]
                if any(value % 20 == 0 and value != 0 for value in new_20_values):
                    warning_new_20 = "Warning: Fields [0, 5, 6, 1, 2, 3, 7, 8, 9] have reached a threshold of 20, 40, 60, etc.!"

        elif action == 'Clear':
            # Reset fields to initial state
            fields = [0] * grid_size

    return render_template('index.html', fields=fields, warning_20=warning_20, warning_90=warning_90, warning_40=warning_40, warning_new_20=warning_new_20)

if __name__ == '__main__':
    app.run(debug=True)
