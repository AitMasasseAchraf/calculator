from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the grid
grid_size = 37  # Numbers from 0 to 36
fields = [0] * grid_size

@app.route('/', methods=['GET', 'POST'])
def index():
    global fields
    warnings_70 = {
        "0_10_20_30": None,
        "1_11_21_31": None,
        "2_12_22_32": None,
        "3_13_23_33": None,
        "4_14_24_34": None,
        "5_15_25_35": None,
        "6_16_26_36": None,
        "7_17_27": None,
        "8_18_28": None,
        "9_19_29": None,
    }
    warnings_50={
                    "1 2 3 4 5 6":None,
                    "7 8 9 10 11 12":None,
                    "13 14 15 16 17 18":None,
                    "19 20 21 22 23 24":None,
                    "25 26 27 28 29 30":None,
                    "31 32 33 34 35 36":None
                }
    warnings_25={
                    "1 2 3 4 5 6 7 8 9 10 11 12":None,
                    "13 14 15 16 17 18 19 20 21 22 23 24":None,
                    "25 26 27 28 29 30 31 32 33 34 35":None  
                }
    
    additional_warnings = {
        "8_times": None,
        "40_times": None,
        "150_times": None,
    }

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Submit':
            number = int(request.form.get('number', 0))  # Get the submitted number
            if 0 <= number < grid_size:
                # Increment all fields by 1
                fields = [x + 1 for x in fields]
                # Set the field under the submitted number to 0
                fields[number] = 0
 # Check thresholds for 70 times
                threshold_70_groups = {
                    "0_10_20_30": [0, 10, 20, 30],
                    "1_11_21_31": [1, 11, 21, 31],
                    "2_12_22_32": [2, 12, 22, 32],
                    "3_13_23_33": [3, 13, 23, 33],
                    "4_14_24_34": [4, 14, 24, 34],
                    "5_15_25_35": [5, 15, 25, 35],
                    "6_16_26_36": [6, 16, 26, 36],
                    "7_17_27": [7, 17, 27],
                    "8_18_28": [8, 18, 28],
                    "9_19_29": [9, 19, 29]
                }
                

                for group_name, indices in threshold_70_groups.items():
                    group_values = [fields[i] for i in indices]
                    if all(value % 70==0 and value !=0 for value in group_values):
                        warnings_70[group_name] = f"{indices} "

                # Additional condition checks
                eight_times_group = [1, 2, 11, 12, 21, 31, 22, 32, 7, 17, 27, 8, 18, 28, 9, 19, 29]
                if all(fields[i] % 8==0 and fields[i]!=0 for i in eight_times_group):
                    additional_warnings["8_times"] = "[1, 2, 11, 12, 21, 31, 22, 32, 7, 17, 27, 8, 18, 28, 9, 19, 29]"

                twohundred_times_group = [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
                one_list=[]
                for i in twohundred_times_group:
                    if fields[i] % 250==0 and fields[i]!=0 :
                        one_list.append(i)
                additional_warnings["250_time"]=one_list        
                
                forty_times_group = [7, 17, 27, 8, 18, 28, 9, 19, 29]
                if all(fields[i] % 40==0 and fields[i]!=0 for i in forty_times_group):
                    additional_warnings["40_times"] = " [7, 17, 27, 8, 18, 28, 9, 19, 29 ]"

                hundred_fifty_times_groups = [
                    [26, 32],
                    [28, 29]
                ]
                hundred_list=[]
                for i, group in enumerate(hundred_fifty_times_groups):
                    if all(fields[idx] % 150==0 and fields[idx]!=0 for idx in group):
                        hundred_list.append(group)
                additional_warnings["150_times"] = f" {str(hundred_list)} "
                
                threshold_50_groups ={
                    "1 2 3 4 5 6":[1 ,2 ,3 ,4 ,5 ,6],
                    "7 8 9 10 11 12":[7 ,8 ,9 ,10 ,11 ,12],
                    "13 14 15 16 17 18":[13 ,14 ,15 ,16 ,17 ,18],
                    "19 20 21 22 23 24":[19 ,20 ,21 ,22 ,23 ,24],
                    "25 26 27 28 29 30":[25 ,26 ,27 ,28 ,29 ,30],
                    "31 32 33 34 35 36":[31 ,32 ,33 ,34 ,35 ,36]
                }
                for group_name, indices in threshold_50_groups.items():
                    group_values = [fields[i] for i in indices]
                    if all(value % 50==0 and value !=0 for value in group_values):
                        warnings_50[group_name] = f"{indices} "

                threshold_25_groups ={
                    "1 2 3 4 5 6 7 8 9 10 11 12":[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12],
                    "13 14 15 16 17 18 19 20 21 22 23 24":[13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24],
                    "25 26 27 28 29 30 31 32 33 34 35":[25 ,26 ,27 ,28 ,29 ,30 ,31 ,32 ,33 ,34 ,35]
                    
                }
                for group_name, indices in threshold_25_groups.items():
                    group_values = [fields[i] for i in indices]
                    if all(value % 25==0 and value !=0 for value in group_values):
                        warnings_25[group_name] = f"{indices} "        

        elif action == 'Clear':
            # Reset fields to initial state
            fields = [0] * grid_size

    return render_template('index.html', fields=fields, warnings_70=warnings_70,warnings_50=warnings_50,warnings_25=warnings_25, additional_warnings=additional_warnings)

if __name__ == '__main__':
    app.run(debug=True)
