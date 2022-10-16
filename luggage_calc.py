from tkinter import N, UNDERLINE
import PySimpleGUI as sg


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

#sg.theme('DarkAmber')

#each new list is a row - layout is a list of lists
layout = [[sg.Text(text1, font='any 18 bold')],
        [sg.Button('Show/Hide instructions')],
        [sg.Text(instructions, key='instructions')], 
        [], 
        [sg.Text("Text 2 here")],
        [sg.Combo(select_people, readonly = True), sg.Combo(select_airline, readonly = True), sg.Combo(select_luggage, readonly= True), sg.Button('Calculate')],
        [sg.Text(output)],
        [sg.Multiline(size=(50,3), key='output', disabled=True, default_text = 'output goes here')],
        [sg.Button('Exit')],
        [],
        [sg.Column([[sg.T(arrows[1], enable_events=True, key='-arrow-'),
                       sg.T('Luggage options details', enable_events=True, key='key'+'-TITLE-')],
                      [sg.pin(sg.Column(baggage_details, key='-testing-', visible= collapsed, metadata=sg.SYMBOL_DOWN))]], pad=(0,0))]                 
        ]

window = sg.Window("Title here", layout, resizable=True, size=(875, 650))
 
while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == 'Show/Hide instructions':
        toggle_value += 1
        if toggle_value%2 == 1:
            window['instructions'].update(visible = False)
        else:
            window['instructions'].update(visible = True)

    if event == "Calculate":
        #test_button.Update(text1) #testing updating elements of gui
        print("test")
        print(text1)
        window['output'].update("this should show different text now")
        
        #window['testkey'].Update(visible=True)
        #window.refresh()

    if event == '-arrow-':
   
        if collapsed == True:
            window['-arrow-'].update(arrows[1])
            collapsed = False
            window['-testing-'].update(visible = False)
            
        else:    
            window['-arrow-'].update(arrows[0])
            collapsed = True
            window['-testing-'].update(visible = True)


window.close()
