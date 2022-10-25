import PySimpleGUI as sg
import client


text1 = "Luggage Cost Calculator:\n"
instructions = 'How to use the calculator:\n 1st - select the number of people up to a max of 5\n \
2nd - Select the airline you will be flying on\n 3rd - select any additional luggage options you need\n \
4th - hit the calculate button and get your results\n'
output = "output goes here:"
sg.theme('DarkAmber')
select_people = [0,1,2,3,4,5]
select_airline = ['United', 'Delta', 'Southwest', 'American']
select_luggage = ['Oversized bag', 'Overweight bag', 'Extra bag']
toggle_value = 0
collapsed = False

arrows = [sg.SYMBOL_DOWN, sg.SYMBOL_UP]


#multiline object
baggage_details = [[sg.Text('Luggage that is free to bring:', font='default 12 underline')],
            [sg.Text('One personal bag that is capable of fitting under the seat in front of you (backpack, purse, laptop bag) \n\
                and one carry on bag that fits in the the overhead bin', pad=(25,0))],
            [sg.Text('Oversized luggage:', font='default 12 underline')],
            [sg.Text('Oversize luggage is any carry on bag that isn\'t capable of fitting in the overhead bin, the max size of a \n\
                carry on is 9in x 14in x 22in', pad=(25,0))],
            [sg.Text('Overweight luggage:', font='default 12 underline')],
            [sg.Text('Any bag over 50 pounds is considered overweight, bags over 100lbs arent able to be checked at all. \n\
                The only exceptions are musical instruments (up to 165lbs) and assistive devices', pad=(25,0))]
            ]


#each new list is a row in gui layout - layout is a list of lists
layout = [[sg.Text(text1, font='any 18 bold')],
        [sg.Button('Show/Hide instructions')],
        [sg.Text(instructions, key='instructions')], 
        [], 
        [sg.Text("Select options below:")],
        [sg.Combo(select_people, readonly = True, enable_events = True, key='-people-'), sg.Combo(select_airline, readonly = True, enable_events = True, key = '-airline-'), 
        sg.Combo(select_luggage, readonly= True, enable_events = True, key = '-luggage-'), sg.Button('Calculate')],
        [sg.Text(output)],
        [sg.Multiline(size=(50,5), key='output', disabled=True, default_text = 'output goes here'), sg.Button('Save Calculation', key = '-save-')],
        [sg.Button('Exit')],
        [],
        [sg.Column([[sg.T(arrows[1], enable_events=True, key='-arrow-'),
                       sg.T('Luggage options details', enable_events=True, key='key'+'-TITLE-')],
                      [sg.pin(sg.Column(baggage_details, key='-testing-', visible= collapsed, metadata=sg.SYMBOL_DOWN))]], pad=(0,0))]                 
        ]

window = sg.Window("Luggage Cost Calculator", layout, resizable=True, size=(875, 650))


#initial values for calculations, and last calculation for passing data to save microservice
selected_values = [None, None, None]
last_calculation = [None, None, None, None]


#event loop
while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        client.send_data('exit')
        break

    if event == 'Show/Hide instructions':
        toggle_value += 1
        if toggle_value%2 == 1:
            window['instructions'].update(visible = False)
        else:
            window['instructions'].update(visible = True)

    if event == "Calculate":
        print("test")
        print(text1)

        if(None in selected_values):
            window['output'].update("One or more selections is missing, please select an option for each input before calculating")
        
        
        else:
            #send data to client function -> calls server to get data need for calculation then calculation takes place -> update window
            print('time to calculate fee')
            cost  = int(selected_values[0]) * float(client.send_data(selected_values))
            cost = format(cost, '.2f')
            window['output'].update(f"Number of people selected: {selected_values[0]} \nAirline selected: {selected_values[1]} \nLuggage Option selected: {selected_values[2]} \n\ntotal cost: ${cost}")
            last_calculation[0] = selected_values[0]
            last_calculation[1] = selected_values[1]
            last_calculation[2] = selected_values[2]
            last_calculation[3] = cost
        

    if event == '-arrow-':
   
        if collapsed == True:
            window['-arrow-'].update(arrows[1])
            collapsed = False
            window['-testing-'].update(visible = False)
            
        else:    
            window['-arrow-'].update(arrows[0])
            collapsed = True
            window['-testing-'].update(visible = True)

    if event == '-people-':
        selected_values[0] = (values['-people-'])

    if event == '-airline-':
        selected_values[1] = (values['-airline-'])

    if event == '-luggage-':
        selected_values[2] = (values['-luggage-'])

    if event == '-save-':
        if None in last_calculation:
            sg.popup('No previous Calculation to be saved', keep_on_top = True, no_titlebar = True, auto_close = True, auto_close_duration = 1)

        else:
            print(f'Data to be saved: {last_calculation[0]} {last_calculation[1]} {last_calculation[2]} {last_calculation[3]}')
            #handle passing data to microservice here.
            client.save_data(last_calculation)
            sg.popup('Calculation saved', keep_on_top = True, no_titlebar = True, auto_close = True, auto_close_duration = 1)

window.close()
