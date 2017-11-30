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
first_day_of_year = datetime.strptime("01/01/2017", "%m/%d/%Y")
col_with_perform = 5
com_count = 0
performance_days = []
performances = []
performances_with_min = []
colon_start = ''

if __name__ == '__main__':

  # open and parse csv performance column
  with open(dir+fn, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
      perform_col = row[col_with_perform]
      if perform_col != '' and perform_col != 'Perform':
        performance_days.append(perform_col)
        if ':' in perform_col and colon_start == '':
          colon_start = row[0]

  # slice cells into individual performances
  for day in performance_days:
    if ' ' in day:
      for x in day.split(' '):
        performances.append(x)
    else:
      performances.append(day)

  # calculate days in year
  today = datetime.now()
  days_in_year = today - first_day_of_year
  
  # calculate days since I started logging minutes
  start_date = datetime.strptime(colon_start, "%m/%d/%Y")
  time_diff = today - start_date
  weeks_with_time = float(time_diff.days/7.0)

  print str(days_in_year.days) + " DAYS IN THE YEAR SO FAR (counting today)"
  print ""
  print str(len(performances)) +  " total performances on " + str(len(performance_days)) + " unique days"

  # count/log 'Com' and 'Busk' Occurrences
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
  print "  " + str(int(busk_count)) +"x  busk"
  print "  " + str(int(len(performances)-com_count-busk_count)) +"x  misc"
  print ""
  
  # count total minutes logged and 'Com' minutes logged
  total_min = 0
  com_min = 0
  com_min_count = 0
  for p in performances_with_min:
    total_min = total_min + float(p.split(':')[1])
    if "Com" in p:
      com_min = com_min + float(p.split(':')[1])
      com_min_count = com_min_count + 1

  # calculate/log meta
  com_min_weekly = float(com_min/weeks_with_time)
  total_min_weekly = float(total_min/weeks_with_time)

  print str(int(colon_count)) + " total performances with minutes logged in last " + str(weeks_with_time) + " weeks since " + colon_start + "."
  print "  " + str(float(total_min/60)) + " total hours logged (" + str(total_min) + " min)"
  print "  " + str(float(total_min_weekly/60)) + " hours per week is average total stage time"
  print ""
  print str(com_min_count) + " comedy performances with minutes logged since " + colon_start
  print "  " + str(float(com_min/60)) + " comedy hours logged (" + str(com_min) + " min)"
  print "  " + str(float(com_min/com_min_count)) + " minutes is average comedy set length"
  print "  " + str(float(com_min_count/weeks_with_time)) + " average comedy performances per week"
  print "  " + str(float(com_min_weekly/60)) + " hours per week is average comedy stage time"
  print ""
  print "Keep up this average and a year will yield "
  print "  " + str(float(com_min_weekly*52/60)) + " comedy stage hours"
  print "  " + str(float(total_min_weekly*52/60)) + " total stage hours"
  print ""
