import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server

@anvil.server.callable
def batch_detection():
  rows = app_tables.charts.search(Active= True)
  for row in rows:
#     print (row('Chart_Name'))
#     t = app_tables.charts.get(chartid = chartid)
    tablename =row['tablename']

#     print(enddate)
#     startdate =  datetime(day=1, month=10, year=2022)
#     enddate =  datetime(day=1, month=9, year=2022)
#     enddate = enddate + timedelta(days=1)
#     print(tablename)
#     print(columnname)
#     print(startdate)
#     print(enddate)
      
#     if showexcluded == False:
#   #     print(enddate)
#           waitinglist= getattr(app_tables, tablename).search(q.all_of(
#                                                   Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
#                                                                           q.greater_than_or_equal_to(startdate)) ,
#                                                   exclude_point = False 
#                                                                           )
#                                                 )

#     else:                                             
      
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
#     total_rows = len(waitinglist) 
#     total_excluded = len(excludedlist)
# #     print (waitinglist)
    
#     dicts = [{'Date_Entered': r['Date_Entered'],columnname: r[columnname],'NoteCol':r['noteCol']}
#             for r in waitinglist]
    
 
# #     print ('dicts',dicts)
 
#     df = pd.DataFrame.from_dict(dicts)
 
#     df['Date_Entered'] = pd.to_datetime(df['Date_Entered'], utc= True)
#     df.sort_values(by=['Date_Entered'], inplace=True , ascending=True)
#     df['Mean']= df[columnname].mean()
#     pointdate= 'Date_Entered'
#     pointname = columnname
#     notecol = df['NoteCol']
#     Mean = df[columnname].mean()
#     SD = df[columnname].std()
#     total_rows = total_rows = df[columnname].count() - 1
# #     if total_rows > 5:
    
    
#     ninebelow , mean9belowline = outofcontrol9below(df, pointdate, pointname, total_rows, Mean, SD , showexcluded, tablename)
#     nineabove, mean9aboveline = outofcontrol9above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename )
#     down6, mean6fallline  = outofcontrol6fall(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename )
#     up6 ,mean6riseline,   = outofcontrol6rise(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename   )
#     four5above, mean45line = outofcontrol45above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename)
#     two3above,stagemeandictline = outofcontrol23above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename )
#     oneabove3 = outofcontrol1above(df, pointdate, pointname, total_rows, Mean, SD,showexcluded , tablename )

