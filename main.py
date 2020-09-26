import PySimpleGUI as sg
import os

root = os.path.dirname(__file__)
# image files in the project root directory
ico_image = os.path.join(root, 'ScreenGuideIcon.ico')
app_image = os.path.join(root, 'ScreenGuideIcon.png')
os_name = os.name

sg.theme('System Default')

# default colour for guide window
new_color = 'grey'
which_os = os_name


"""
Window icons
see F:\Py Projects\pysimplegui_window_icons.png
for windows, if filename, MUST be ico
for Linux MUST NOT be ico
"""


# if windows use ico - if linux use png
if which_os == 'nt':
    icon_image = ico_image
elif which_os == 'posix':
    icon_image = app_image


# where all the magic happens
def main_window():
    layout = [[sg.Text('Guide Colour', pad=((10, 20), 5)),
               sg.Combo(['None', 'Yellow', 'Orange', 'Red', 'Grey'], default_value='None',
                        enable_events=True, key='-COMBO-', pad=((40, 10), 10), readonly=True)],
              [sg.Button('About', pad=((10, 50), 10), key='-ABOUT-'), sg.CloseButton('Close', pad=((30, 10), 10))]]

    return sg.Window('Screen guide', layout, icon=icon_image, size=(250, 100)).finalize()


def guide_window():
    layoutg = [[sg.Text(background_color=new_color, size=(400, 200), key='-CANVAS-',)]]

    return sg.Window('guide', layoutg, alpha_channel=.5, resizable=True, keep_on_top=True,
                     icon=icon_image, grab_anywhere=False, size=(1000, 500)).Finalize()


def about_window():
    layouth = [[sg.Image(app_image, size=(50, 50)),
               sg.Text('Name: Screen Guide (For Linux)' '\n' '\n'
                       'Version: 0.2' '\n' '\n'
                       'Copyright: 2020' '\n' '\n'
                       'Author: BabsKy' '\n' '\n'
                       'Description: A guide to help you focus on a particular area of your screen.' '\n'
                       'Can also be used as a colour filter.', size=(50, 12))],
               [sg.CloseButton('Close')]]

    return sg.Window('About Screen Guide', layouth, icon=ico_image, modal=True).read()


# where all the function happens
def main():
    window1, window2 = main_window(), None
    while True:
        window, event, values = sg.read_all_windows()
        if window == window1 and event in (sg.WIN_CLOSED, 'Close'):
            break
        # handle main Window events
        elif event == '-ABOUT-':
            about_window()
        elif event == '-COMBO-':
            combo = values['-COMBO-']  # use the combo key
            if combo != 'None':
                new_color = values['-COMBO-']
                print(new_color)
                # minimise screen guide color selection window
                window1.minimize()
                # open or update guide window
                if window2 is None:
                    window2 = guide_window()
                    window2['-CANVAS-'].update(background_color=new_color)
                elif window2 is not None:
                    window2['-CANVAS-'].update(background_color=new_color)
            elif combo == 'None':
                if window2 is not None:
                    # close the guide if "None" is selected
                    window2.close()
                    window2 = None

        if window == window2 and event == sg.WIN_CLOSED:
            window2.close()
            window2 = None

    window1.close()
    if window2 is not None:
        window2.close()


if __name__ == '__main__':
    main()
