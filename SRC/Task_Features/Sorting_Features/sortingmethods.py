import pandas as pd
import SRC.Calendar_Features.Taskcalendar as TC
import dearpygui.dearpygui as dpg

def sortDueDate():
  dpg.delete_item("Cal Window")
  taskCsv = pd.read_csv("task_list.csv")
  taskCsv.sort_values(["date"],
                    inplace = True)
#Creates a blank csv to our temp "medium"
  pd.DataFrame({}).to_csv("medium.csv")
  taskCsv.to_csv('medium.csv',index=False)
  TC.cal_maker("medium.csv")


def sortPriority():
  dpg.delete_item("Cal Window")
  taskCsv = pd.read_csv("task_list.csv")
  taskCsv.sort_values(["priority"],
                    inplace = True)
#Creates a blank csv to our temp "medium"
  pd.DataFrame({}).to_csv("medium.csv")
  taskCsv.to_csv('medium.csv',index=False)
  TC.cal_maker("medium.csv")


def sortStatus():
  dpg.delete_item("Cal Window")
  taskCsv = pd.read_csv("task_list.csv")
  taskCsv.sort_values(["status"],
                    inplace = True)
#Creates a blank csv to our temp "medium"
  pd.DataFrame({}).to_csv("medium.csv")
  taskCsv.to_csv('medium.csv',index=False)
  TC.cal_maker("medium.csv")

  





