from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the grid
grid_size = 37  # Numbers from 0 to 36
fields = [0] * grid_size

@app.route('/', methods=['GET', 'POST'])
def index():
    global fields
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Submit':
            number = int(request.form.get('number', 0))  # Get the submitted number
            if 0 <= number < grid_size:
                # Increment all fields by 1
                fields = [x + 1 for x in fields]
                # Set the field under the submitted number to 0
                fields[number] = 0
        elif action == 'Clear':
            # Reset fields to initial state
            fields = [0] * grid_size
    return render_template('index.html', fields=fields)

if __name__ == '__main__':
    app.run(debug=True)
