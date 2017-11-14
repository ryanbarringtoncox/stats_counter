#!/usr/bin/python

'''
TO-DONES:
  0. Count performance days
  1. Count total # of performances
  2. Give the # of each unique type of performance
  3. Report total minutes performed and start date for minutes logged.
  4. Report comedy minues logged since start date.
  5. Check values "find" feature in word doc
TO_DOs?:
Not sure these are necessary if I'm diligent entering values in spreadsheet w/ consistent format.
  Make this non-case sensitive i.e. 'com' == 'Com'
  Make it forgiving of white space i.e. 'Com: 9.5' == 'Com:9.5'
'''

import re, csv
from datetime import datetime

dir = '/Users/rbc/Downloads/'
fn = 'Counting 2017 - Sheet1.csv'
col_with_perform = 5
com_count = 0
performance_days = []
performances = []
performances_with_min = []
colon_start = ''

if __name__ == '__main__':

  with open(dir+fn, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
      perform_col = row[col_with_perform]
      if perform_col != '' and perform_col != 'Perform':
        performance_days.append(perform_col)
        if ':' in perform_col and colon_start == '':
          colon_start = row[0]

  for day in performance_days:
    if ' ' in day:
      for x in day.split(' '):
        performances.append(x)
    else:
      performances.append(day)

  print "YEAR TO DATE:"
  print ""
  print str(len(performances)) +  " total performances on " + str(len(performance_days)) + " days"

  com_count = 0
  busk_count = 0
  colon_count = 0
  for performance in performances:
    if 'Com' in performance:
      com_count = com_count + 1
    if 'Busk' in performance:
      busk_count = busk_count + 1
    if ':' in performance:
      colon_count = colon_count + 1
      performances_with_min.append(performance)

  print "  " + str(int(com_count)) + "x comedy"
  print "  " + str(int(busk_count)) +"x busk"
  print ""
  
  # calculate days that since started logging minutes
  start_date = datetime.strptime(colon_start, "%m/%d/%Y")
  today = datetime.now()
  time_diff = today - start_date
  weeks_with_time = float(time_diff.days/7.0)

  #print str(int(colon_count)) + " performances with minutes logged in last " + str(time_diff.days) + " days (since " + colon_start + ")."
  print str(int(colon_count)) + " performances with minutes logged in last " + str(weeks_with_time) + " weeks (since " + colon_start + ")."

  total_min = 0
  com_min = 0
  com_min_count = 0
  for p in performances_with_min:
    total_min = total_min + float(p.split(':')[1])
    if "Com" in p:
      com_min = com_min + float(p.split(':')[1])
      com_min_count = com_min_count + 1

  print "  " + str(total_min) + " min == " + str(float(total_min/60)) + " total hours logged"
  print "  " + str(com_min) + " min == " + str(float(com_min/60)) + " comedy hours logged"
  print ""

  print str(com_min_count) + " comedy performances with minutes logged"
  print str(float(com_min/com_min_count)) + " minutes is average comedy set length since " + colon_start
  com_min_weekly = float(com_min/weeks_with_time)
  print str(com_min_weekly) + " minutes per week is average comedy stage time since " + colon_start
  print "Keeping up this average will yield " + str(float(com_min_weekly*52/60)) + " comedy stage hours in a year."
  print ""
