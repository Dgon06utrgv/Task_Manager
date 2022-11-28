import dearpygui.dearpygui as dpg
import SRC.GUI.guifunctions as gui
import SRC.Calendar_Features.Taskcalendar as cal
import SRC.Task_Features.export_import.exportCSV as ex

dpg.create_context()
dpg.create_viewport(title='Task Manager', width=1280, height=720)

#main window so tabs will need to be implemented
with dpg.window(label="Main Menu", tag="Primary Window"):
  #####################################menu bar################################
  with dpg.menu_bar():
    with dpg.menu(label=" File Settings "):
      #have 2 options: extract CSV and preview CSV file
      dpg.add_menu_item(label="Extract CSV", callback=ex.saved_csv)
      dpg.add_menu_item(label="Add Another Assignment",
                        callback=gui.create_new_PW)
    with dpg.menu(label=" Calendar "):
      #send a command towards the Taskcalendar.py file and that will be using tkinter to make a calendar
      dpg.add_menu_item(label="Open Calendar", callback=cal.cal_safe)
    with dpg.menu(label=" Options "):
      dpg.add_menu_item(label="See specific time left for assignment", callback=gui.set_reminder)
    with dpg.menu(label=" Exit Application "):
      #send exit command using function
      dpg.add_menu_item(label="Confirm Exit", callback=gui.destroy_main)
################################tab bar##################################################
  '''printing tabs from function gui file'''
  gui.printTabs("task_list.csv")
################################################################################
#import classes with their attributes (secondary window)
'''creating a import assignments window'''
gui.create_new_PW()
'''add disclaimer to warn user'''
gui.disclaimer()
########################################################################
dpg.set_frame_callback(60, gui.launcher)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
