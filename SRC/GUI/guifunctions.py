import dearpygui.dearpygui as dpg
import SRC.Task_Features.task as task
import pandas as pd
import sys, datetime, threading, csv
import SRC.Task_Features.export_import.importToCSV as iCSV
from time import sleep

#imports year and month from datetime
current_month = int(datetime.datetime.now().month)
current_year = int(datetime.datetime.now().year)

#Set when to remind user about an assignment based on time from deadline
reminder_time = 1
tabCount = 0

#Prints each task as an individual tab
def printTabs(filename):
  file = pd.read_csv(filename)
  i = 0 
  global tabCount
  tabCount = 0
  with dpg.tab_bar(label='Tasks',tag='Task Bar', parent="Primary Window"):
    while (i < len(file)):
      with dpg.tab(label=file.iloc[i]['name']):
        dpg.add_text(file.iloc[i]['name'])
        dpg.add_text(f"Date Due: {file.iloc[i]['date']}")
        dpg.add_text(f"Time Due: {file.iloc[i]['time']}")
        dpg.add_text(file.iloc[i]['priority'])
        dpg.add_text(file.iloc[i]['type'])
        dpg.add_text(file.iloc[i]['description'])
        dpg.add_text(file.iloc[i]['status'])
        #set buttons as "Mark as complete", "set to in-progress",and "Discard Task"
        with dpg.group(horizontal=True):
          dpg.add_button(label='Mark as complete',callback=set_to_complete,user_data=i)
          #set to in-progress button: should change the status on the specific tab item and update the main window
          dpg.add_button(label="set as In Progress",callback=set_to_progress,user_data=i)
          #discard task: erases the tab and will erase the tab item from the csv file.
          dpg.add_button(label="Discard Task",callback=discard_task,user_data=i)
      i+=1
      tabCount += 1


# Function to add new tabs as more tasks are added. 
def update_tabs(filename):
  file = pd.read_csv(filename)
  global tabCount
  with dpg.tab(label=file.iloc[tabCount]['name'],parent='Task Bar'):
    dpg.add_text(file.iloc[tabCount]['name'])
    dpg.add_text(f"Date Due: {file.iloc[tabCount]['date']}")
    dpg.add_text(f"Time Due: {file.iloc[tabCount]['time']}")
    dpg.add_text(file.iloc[tabCount]['priority'])
    dpg.add_text(file.iloc[tabCount]['type'])
    dpg.add_text(file.iloc[tabCount]['description'])
    dpg.add_text(file.iloc[tabCount]['status'])
  
  
    with dpg.group(horizontal=True):
      dpg.add_button(label='Mark as complete', callback=set_to_complete)
            #set to in-progress button: should change the status on the specific tab item and update the main window
      dpg.add_button(label="set as In Progress",callback=set_to_progress)
            #discard task: erases the tab and will erase the tab item from the csv file.
      dpg.add_button(label="Discard Task",callback=discard_task)
    tabCount += 1
  
#identify tab name, use "Mark as complete","Set to In Progress", and "Discard Task" buttons to change attributes to the assignment attributess
''' this means adding a tag to every item iterated from print tabs function, then performing these tasks to that tag'''


def set_to_complete(sender, data, user_data):
  lines = list()
  with open('task_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      lines.append(row)
  lines[user_data+1][6] = "Done"
  with open('task_list.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(lines)
  dpg.delete_item("Task Bar")
  printTabs("task_list.csv")

def set_to_progress(sender, data, user_data):
  lines = list()
  with open('task_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      lines.append(row)
  lines[user_data+1][6] = "In Progress"
  with open('task_list.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(lines)
  dpg.delete_item("Task Bar")
  printTabs("task_list.csv")

def discard_task(sender, data, user_data):
  global tabCount
  tabCount -= 1
  lines = list()
  with open('task_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      lines.append(row)
  del lines[user_data+1]
  with open('task_list.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(lines)
  dpg.delete_item("Task Bar")
  printTabs("task_list.csv")



def create_new_PW():
  #made to copy popup window (import assignments window)
  with dpg.window(label="Import Assignments",
                  tag="Popup Window",
                  on_close=destroy_import_module):
    dpg.add_text("Class attributes")
    with dpg.group(horizontal=True):
      dpg.add_date_picker(label="date due",
                          tag='Date',
                          default_value={'year': current_year - 1900})
      dpg.add_time_picker(label="Time due",
                          tag='Time',
                          default_value={
                            'hour': 00,
                            "min": 00
                          })
    dpg.add_input_text(label='Name', tag='Name')
    dpg.add_input_text(label='Assignment Description', tag='Description')
    dpg.add_input_text(label='Type(for what class?)', tag='Type')
    dpg.add_radio_button(label='Status',
                         tag='Status',
                         items=["Not Done", "In Progress", "Done"],
                         horizontal=True,
                         default_value="Not Done")
    dpg.add_radio_button(
      label="Priority",
      tag='Priority',
      items=["Non-important", "Semi-important", "Priority-important"],
      horizontal=True,
      default_value="Non-important")
    with dpg.group(horizontal=True):
      dpg.add_button(label='Save and Exit', callback=save_ex)
      dpg.add_button(label='Save and Add more', callback=save_addpass)
      dpg.add_button(label='Exit Without Saving',
                     callback=destroy_import_module)



#tester to see if button works(placeholder)
def print_me(sender, app_data):
  print(f"Menu Item: {sender},{app_data}")
###########################################

  
def destroy_popup():
  dpg.delete_item("Reminder")


def destroy_import_module():
  dpg.delete_item("Popup Window")


def destroy_main():
  dpg.delete_item("Primary Window")
  sys.exit()

def destroy_error():
  dpg.delete_item("error")

def delete_disclaimer():
  dpg.delete_item("Disclaimer")

def grab_attributes(sender, app_data):
  t_name = dpg.get_value("Name")
  t_desc = dpg.get_value("Description")
  t_prior = dpg.get_value("Priority")
  t_stat = dpg.get_value("Status")
  t_dueD = dpg.get_value("Date")
  t_dueT = dpg.get_value("Time")
  t_type = dpg.get_value("Type")

  ## Format date and time properly
  t_dueD = iCSV.format_date(t_dueD)
  t_dueT = iCSV.format_time(t_dueT)
  #print(f"{t_dueD}\n\n{t_dueT}")
  #format : name,date,time,priority,type,description,status
  tempTask = task.Task(t_name, t_dueD, t_dueT, t_prior, t_type, t_desc, t_stat)
  #Task class attributes:
  #name, date, time, priority, class type, description,status
  iCSV.write_csv(tempTask)


def save_ex(sender, app_data):
  if dpg.get_value("Name"):
    grab_attributes(sender, app_data)
    destroy_import_module()
    dpg.delete_item("Task Bar")
    printTabs("task_list.csv")
  else:
    with dpg.window(label="Error", tag="error"):
      dpg.add_text("Can't add assignment without a name!")
      dpg.add_button(label="Ok", callback=destroy_error)


def save_addpass(sender, app_data):
  if dpg.get_value("Name"):
    grab_attributes(sender, app_data)
    recycle_window()
    dpg.delete_item("Task Bar")
    printTabs("task_list.csv")
  else:
    with dpg.window(label="Error", tag="error"):
      dpg.add_text("Can't add assignment without a name!")
      dpg.add_button(label="Ok", callback=destroy_error)


def recycle_window():
  dpg.delete_item("Popup Window")
  create_new_PW()


def launcher():
  d = threading.Thread(name='daemon', target=background, daemon=True)
  d.start()


def background():
  while True:
    "refreshing..."
    sleep(10.0)


#this window should determine how much time when the date is due as well as functionality of what specified time would the user like to be reminded (may need a local attribute for that to be functional)
#################################reminder window###################################################

def reminder_win(rem_num):
  #time left is denoted by the "get_reminder" variable
  file = pd.read_csv("task_list.csv")
  i = 0
  while (i < len(file)):
      t_time = file.iloc[i]["time"]
      t_name = file.iloc[i]["name"]
      t_dict = t_time.split(":")
      t_hournum = list(t_dict)
      t_hour = int(t_hournum[0])
      now = datetime.datetime.now()
      if (int(t_hour - rem_num) == int(now.strftime('%H')) - 18):
        time_left = str(int(t_hour) - (int(now.strftime('%H')) - 18))
        with dpg.window(label="Notification Window", tag="Reminder"):
            dpg.add_text(
          f"This is a notification that {t_name} is due in {time_left}! "
          )
            dpg.add_button(label="Ok", callback=destroy_popup)
            break
      else:
          pass
      i += 1

###################################################################################################
def get_reminder():
  global reminder_time
  reminder_time = int(dpg.get_value("set_r"))
  reminder_win(reminder_time)
  dpg.delete_item("Set time")


def set_reminder():
  with dpg.window(label="How much time left for next assignment?", tag="Set time"):
    dpg.add_slider_int(label="Hour",
                       tag="set_r",
                       width=200,
                       min_value=1,
                       max_value=24,
                       default_value=1)
    dpg.add_button(label="Ok", callback=get_reminder)


#can add minutes too if you want.

#make disclaimer if tabs does not load in properly
def disclaimer():
  with dpg.window(label="Disclaimer", tag="Disclaimer"):
    dpg.add_text("If the tabs are incorrect or did not work properly\n after importing a class, please restart the program to see the effects...")
    dpg.add_button(label="Ok",callback=delete_disclaimer)