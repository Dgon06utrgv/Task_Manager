import dearpygui.dearpygui as dpg
def saved_csv():
  with dpg.window(label="Export CSV Notice", tag="excsv"):
    dpg.add_text("the file is saved in this program's path location.\nTo send in a new csv file, please use the same filename as the file you have extracted\n then insert it back to the program's path location.")
    dpg.add_button(label="Ok",callback=destroy_excsv)

def destroy_excsv():
  dpg.delete_item("excsv")