import dearpygui.dearpygui as dpg
import SRC.GUI.guifunctions as gui
import SRC.Task_Features.Sorting_Features.sortingmethods as sm
import pandas as pd
# IMPORT CSV FILE HERE FOR READING OR HAVE A DIFFERENT METHOD TO GRAB ATTRIBUTES TO DISPLAY ON CALENDAR.
#filename is supposed to be the file being inserted after a sorted file is modified or created.
def cal_maker(filen):
    i = 0
    file = pd.read_csv(filen)
    with dpg.window(tag="Cal Window", label="Calendar",no_close=True):
        while (i < len(file)):
            with dpg.table(label="default table of assignments", resizable=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                dpg.add_table_column(label=file.iloc[i]['name'])
                with dpg.table_row(label="contents"):
                    dpg.add_button(label=f"Date Due: {file.iloc[i]['date']}\nTime Due: {file.iloc[i]['time']}\n{file.iloc[i]['priority']}\n{file.iloc[i]['status']}")
    # adding a tip as a hover for date picker showing what assignment is due
    # dpg.add_date_picker(tag="date",default_value={'year': current_year - 1900})
            i += 1
        with dpg.group(horizontal=True):
          #add functionality towards the sorting buttons. have them call cal_maker with the new csv file they create.
            dpg.add_button(label="Sort by Due Date", callback=sm.sortDueDate)
            dpg.add_button(label="Sort by Status", callback=sm.sortPriority)
            dpg.add_button(label="Sort by Priority", callback=sm.sortStatus)
            dpg.add_button(label="Exit",callback=delete_cal)

def delete_cal():
  dpg.delete_item("Cal Window")

def cal_safe():
  cal_maker("task_list.csv")