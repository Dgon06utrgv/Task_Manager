import pandas as pd


def format_date(dict):
  yyyy= str(dict['year'] + 1900)
  mm = str(dict['month'] + 1)
  dd = str(dict['month_day'])
  
  # format so it's always mm/dd/yyyy
  if len(dd) == 1:
    dd = '0' + dd 
  if len(mm)  == 1:
    mm = '0'+ mm
  
  return f"{mm}/{dd}/{yyyy}" 

def format_time(dict):
  hour = str(dict['hour'])
  minute = str(dict['min'])
  sec = str(dict['sec'])

  if len(minute) == 1:
    minute = '0' + minute
  if len(hour) == 1:
    hour = '0' + hour
  if len(sec) == 1:
    sec = '0' + sec

  if hour > str(12):
    hour = str(int(hour) - 12)
    timepart = "PM"
  else:
    timepart = "AM"
  # format so it's always hh:mm:ss

  return f"{hour}:{minute}:{sec}{timepart}"
  

def write_csv(task):
  name = getattr(task,'name')
  date = getattr(task,'date')
  time = getattr(task,'time')
  prior = getattr(task,'priority')
  type = getattr(task,'type')
  desc = getattr(task,'description')
  stat = getattr(task,'status')

  df = pd.DataFrame([(name,date,time,prior,desc,type,stat)])
  df.to_csv('task_list.csv', mode='a',header=False, index=False)


#testing append to csv
  '''
mytask = Task("Cool guys don't look at explosions", (datetime.date.today()).strftime("%m/%d/%Y"), "23:59:59", "important", "math", "WHAT", "incomplete")

write_csv(mytask)
'''

