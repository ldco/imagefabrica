import PySimpleGUIQt as sg
import app as app


_window = sg.Window('')
displayHeight = _window.get_screen_dimensions()[1]
displayWidth = _window.get_screen_dimensions()[0]

uifont = "PTSans"
sz = (10,20)

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)/2, (screen_height - win_height)
    window.move(x, y)

# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['f21theme'] = {'BACKGROUND': '#303030', 'TEXT': '#efefef', 'INPUT': '#303030',
'TEXT_INPUT': '#efefef', 'SCROLL': '#000000', 'BUTTON': ('#efefef', '#303030'), 'PROGRESS': ('#efefef', '#303030'), 'BORDER': 10, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, }

# Switch to use your newly created theme
sg.theme('f21theme')
# sg.theme('SystemDefaultForReal')
sg.set_options(font=(uifont, 12))

col1 = [
            [sg.HorizontalSeparator()],
            # [sg.Image(filename="file-image.svg", size=(5, 6))]
            [sg.Text("Choose a file: ")],
            [sg.FileBrowse(size=(300, 60)), sg.Text("*Path to file*", font=(uifont, 8), justification='right')],
            [sg.Text("OR",font=(uifont, 9))],
            [sg.Text("Choose a folder: ")],
            [sg.FolderBrowse(size=(300, 60)), sg.Text("*Path to folder*", font=(uifont, 8), justification='right')],
            [sg.HorizontalSeparator()],
            [sg.Text("Scale with 'Real-ESRGAN'", font=(uifont, 9))],
            [sg.HorizontalSeparator()],
            [sg.Checkbox("Scale", default=True)],
            [sg.Radio('Both', "RADIO1", default=True), sg.Radio('X4', "RADIO1"), sg.Radio('X16', "RADIO1")],
            [sg.HorizontalSeparator()],
            [sg.Text("Remove BG with 'backgroundremover'", font=(uifont, 9))],
            [sg.HorizontalSeparator()],
            [sg.Checkbox('Remove Background', default=True)],
            [sg.Radio('All', "RADIO2", default=True), sg.Radio('By postfix', "RADIO2")],
            [sg.HorizontalSeparator()],
            [sg.Text("Compress with PNGQUANT", font=(uifont, 9))],
            [sg.HorizontalSeparator()],
            [sg.Checkbox('Compress', default=True)],
            [sg.Radio('Rewrite files', "RADIO3", default=True), sg.Radio('New files', "RADIO3")],
            [sg.HorizontalSeparator()],
            [sg.HorizontalSeparator()],
            [sg.Button('OK', key='Submit', size=(displayWidth/5, 80)), sg.Button('CANCEL', key='Cancel', size=(displayWidth/5, 80)), sg.Button('CLOSE', key='Close', size=(displayWidth/5, 80))]
            ]
col2 = [
            [sg.HorizontalSeparator()],
            [sg.Output()],
            [sg.HorizontalSeparator()]
            ]

# col_layout = [[col1], [col2]]

layout = [
    [sg.Column(col1)],
    [sg.Column(col2)]
    
    ]


# Create the Window
window = sg.Window('Image Fabrica', layout, size=(displayWidth/2, displayHeight), finalize=True)

# Event Loop to process "events" and get the "values" of the inputs
move_center(window)
# _window.close()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break
    if event == 'Submit':
        app.submitRequest();
    if event == 'Cancel':
        app.cancelRequest();

_window.close()
window.close()
