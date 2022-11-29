import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
from datetime import datetime, time , date , timedelta
import pandas as pd
from .outofcontrol.outofcontroltwo3above import outofcontrol23above
from .outofcontrol.outofcontrol9below  import outofcontrol9below
from .outofcontrol.outofcontrol9above import outofcontrol9above
# from .OutofControlChecks import outofcontrol1above
from .outofcontrol.outofcontrol6fall import outofcontrol6fall
from .outofcontrol.outofcontrol6rise import outofcontrol6rise
from .outofcontrol.outofcontrol45above import outofcontrol45above
from .outofcontrol.outofcontrol1above3SD import outofcontrol1above


@anvil.server.callable
def batch_detection():
  rows = app_tables.charts.search(Active= True)
  for row in rows:
#     print (row('Chart_Name'))
    t = app_tables.charts.get(chartid = row['chartid'])
    tablename =row['tablename']
    startdate = (row['StartDate'])
    enddate = (row['EndDate'])
    chartid = row['chartid']
#     print(enddate)
#     startdate =  datetime(day=1, month=8, year=2022)
#     enddate =  datetime.now()
#     enddate = enddate + timedelta(days=1)
    print(tablename)
#     print(columnname)
    print(startdate)
    print(enddate)
      
  
  #     print(enddate)
    waitinglist= getattr(app_tables, tablename).search(q.all_of(
                                                  Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
                                                                          q.greater_than_or_equal_to(startdate)) ,
                                                  exclude_point = False 
                                                                          )
                                                )

                                               
      
#           waitinglist = getattr(app_tables, tablename).search(q.all_of(
#                                                   Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
#                                                                           q.greater_than_or_equal_to(startdate)) ,
                                                  
#                                                                           )
#                                                 )
        
#     excludedlist= getattr(app_tables, tablename).search(q.all_of(
#                                               Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
#                                                                       q.greater_than_or_equal_to(startdate)) ,
#                                               exclude_point = True 
#                                                                     ))
    total_rows = len(waitinglist) 
#     total_excluded = len(excludedlist)
#     print (waitinglist)
    
    dicts = [{'Date_Entered': r['Date_Entered'],'Measure_Value': r['Measure_Value'],'NoteCol':r['noteCol']}
            for r in waitinglist]
    
 
#     print ('dicts',dicts)
 
    df = pd.DataFrame.from_dict(dicts)
 
    df['Date_Entered'] = pd.to_datetime(df['Date_Entered'], utc= True)
    df.sort_values(by=['Date_Entered'], inplace=True , ascending=True)
    df['Mean']= df['Measure_Value'].mean()
    pointdate= 'Date_Entered'
    pointname = 'Measure_Value'
    notecol = df['NoteCol']
    Mean = df['Measure_Value'].mean()
    SD = df['Measure_Value'].std()
    total_rows = total_rows = df['Measure_Value'].count() - 1
    print('Table=', tablename,' No. of Rows', total_rows)
#     if total_rows > 5:
    showexcluded = False
    
    ninebelow , mean9belowline = outofcontrol9below(df, pointdate, pointname, total_rows, Mean, SD , showexcluded, tablename,chartid)
    nineabove, mean9aboveline = outofcontrol9above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename,chartid )
    down6, mean6fallline  = outofcontrol6fall(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename,chartid )
    up6 ,mean6riseline,   = outofcontrol6rise(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename,chartid   )
    four5above, mean45line = outofcontrol45above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename,chartid)
    two3above,stagemeandictline = outofcontrol23above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename,chartid )
    oneabove3 = outofcontrol1above(df, pointdate, pointname, total_rows, Mean, SD,showexcluded , tablename,chartid )

# anvil.server.launch_background_task()
# def batch_detection():
#   rows = app_tables.charts.search(Active= True)
#   for row in rows:
# #     print (row('Chart_Name'))
#     t = app_tables.charts.get(chartid = row['chartid'])
#     tablename =row['tablename']
#     startdate = (row['StartDate'])
#     enddate = (row['EndDate'])
#     chartid = row['chartid']
# #     print(enddate)
# #     startdate =  datetime(day=1, month=8, year=2022)
# #     enddate =  datetime.now()
# #     enddate = enddate + timedelta(days=1)
#     print(tablename)
# #     print(columnname)
#     print(startdate)
#     print(enddate)
      
  
#   #     print(enddate)
#     waitinglist= getattr(app_tables, tablename).search(q.all_of(
#                                                   Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
#                                                                           q.greater_than_or_equal_to(startdate)) ,
#                                                   exclude_point = False 
#                                                                           )
#                                                 )

                                               
      
# #           waitinglist = getattr(app_tables, tablename).search(q.all_of(
# #                                                   Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
# #                                                                           q.greater_than_or_equal_to(startdate)) ,
                                                  
# #                                                                           )
# #                                                 )
        
# #     excludedlist= getattr(app_tables, tablename).search(q.all_of(
# #                                               Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
# #                                                                       q.greater_than_or_equal_to(startdate)) ,
# #                                               exclude_point = True 
# #                                                                     ))
#     total_rows = len(waitinglist) 
# #     total_excluded = len(excludedlist)
# #     print (waitinglist)
    
#     dicts = [{'Date_Entered': r['Date_Entered'],'Measure_Value': r['Measure_Value'],'NoteCol':r['noteCol']}
#             for r in waitinglist]
    
 
# #     print ('dicts',dicts)
 
#     df = pd.DataFrame.from_dict(dicts)
 
#     df['Date_Entered'] = pd.to_datetime(df['Date_Entered'], utc= True)
#     df.sort_values(by=['Date_Entered'], inplace=True , ascending=True)
#     df['Mean']= df['Measure_Value'].mean()
#     pointdate= 'Date_Entered'
#     pointname = 'Measure_Value'
#     notecol = df['NoteCol']
#     Mean = df['Measure_Value'].mean()
#     SD = df['Measure_Value'].std()
#     total_rows = total_rows = df['Measure_Value'].count() - 1
#     print('Table=', tablename,' No. of Rows', total_rows)
# #     if total_rows > 5:
#     showexcluded = False
    
#     ninebelow , mean9belowline = outofcontrol9below(df, pointdate, pointname, total_rows, Mean, SD , showexcluded, tablename,chartid)
#     nineabove, mean9aboveline = outofcontrol9above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename,chartid )
#     down6, mean6fallline  = outofcontrol6fall(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename,chartid )
#     up6 ,mean6riseline,   = outofcontrol6rise(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename,chartid   )
#     four5above, mean45line = outofcontrol45above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename,chartid)
#     two3above,stagemeandictline = outofcontrol23above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename,chartid )
#     oneabove3 = outofcontrol1above(df, pointdate, pointname, total_rows, Mean, SD,showexcluded , tablename,chartid )
