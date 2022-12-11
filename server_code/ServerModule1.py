import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pymysql
import pandas as pd
from datetime import datetime, time , date , timedelta
import plotly.graph_objects as go
import plotly
import anvil.media
from .outofcontrol.outofcontroltwo3above import outofcontrol23above
from .outofcontrol.outofcontrol9below  import outofcontrol9below
from .outofcontrol.outofcontrol9above import outofcontrol9above
# from .OutofControlChecks import outofcontrol1above
from .outofcontrol.outofcontrol6fall import outofcontrol6fall
from .outofcontrol.outofcontrol6rise import outofcontrol6rise
from .outofcontrol.outofcontrol45above import outofcontrol45above
from .outofcontrol.outofcontrol1above3SD import outofcontrol1above
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.javascript:void(0)
#


@anvil.server.callable
def add_test(tablename, new_test):
  
  
  getattr(app_tables, tablename).add_row(
#     new_test['exclude_point'] == False,
#   new_test['Date_Entered'] = datetime(new_test['Date_Entered'])
    **new_test, 
    exclude_point = False
    
  )
#    t= app_tables.test.get()

@anvil.server.callable
def update_result(self_item):
  # check that the article given is really a row in the ‘articles’ table
  if app_tables.test.has_row(test):
#     article_dict['updated'] = datetime.now()
    test.update(**result_dict, Date_Entered = datetime.now())
  else:
    raise Exception("Result does not exist")

# @anvil.server.callable
# def edit_test(Date_Entered, test_result, last_name, team, pay_grade):
#   employee.update(first_name=first_name, last_name=last_name, team=team, pay_grade=pay_grade)    
    
    
    
    
# @anvil.server.callable    
# def edit_test(self):
#     first_name, last_name = parse_employee_name(self.text_box_employee_edit.text)
#     anvil.server.call(
#       'edit_employee',
#       self.item,
#       first_name=first_name,
#       last_name=last_name,
#       team=self.drop_down_teams_edit.selected_value,
#       pay_grade=self.text_box_grade_edit.text,
#     )    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
@anvil.server.callable
def delete_test(test):
  test.delete()  
      
def refresh_test(self, **event_args):
    self.repeating_panel_1.items = app_tables.test.search()  
    
# @anvil.server.callable
# def get_4S_Waiting():
#   conn = connect()
#   t = app_tables.charts.search(chartid = 4)
 
    
#   for row in t:

#      chartsql = row['ChartSQL']

#      with conn.cursor() as cur:
#        cur.execute(chartsql)
#        dicts = [{'All_Cases_with_4S': r['All_Cases_with_4S']}
#             for r in cur.fetchall()]
# #        print (dicts)
#      df = pd.DataFrame.from_dict(dicts)
# #      print(df['All_Cases_with_4S'][0])
#      swait = df['All_Cases_with_4S'][0]
#      today=datetime.today()
#      app_tables.waiting_on_4s.add_row(Date_Entered = today,All_Cases_with_4S = swait)
 
#   return  swait


# # @anvil.server.callable
# def get_Cases_Arriving_update():
#   conn = connect()
#   t = app_tables.charts.search(chartid = 2)
 
    
#   for row in t:

#      chartsql = row['ChartSQL']

#      with conn.cursor() as cur:
#        cur.execute(chartsql)
#        dicts = [{'All_Cases': r['All_Cases']}
#             for r in cur.fetchall()]
# #        print (dicts)
#      df = pd.DataFrame.from_dict(dicts)
# #      print(df['All_Cases'][0])
#      swait = df['All_Cases'][0]
#      today=datetime.today()
#      app_tables.cases_arriving.add_row(Date_Entered = today,Cases_Arriving= swait)
 
#   return  swait


@anvil.server.callable
def get_total_rows(tablename,columnname, startdate, enddate, showexcluded):
      
    if showexcluded == False:
  #     print(enddate)
          waitinglist= getattr(app_tables, tablename).search(q.all_of(
                                                  Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
                                                                          q.greater_than_or_equal_to(startdate)) ,
                                                  exclude_point = False 
                                                                          )
                                                )

    else:                                             
      
          waitinglist = getattr(app_tables, tablename).search(q.all_of(
                                                  Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
                                                                          q.greater_than_or_equal_to(startdate)) ,
                                                  
                                                                          )
                                                )
        
    excludedlist= getattr(app_tables, tablename).search(q.all_of(
                                              Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
                                                                      q.greater_than_or_equal_to(startdate)) ,
                                              exclude_point = True 
                                                                    ))
    total_rows = len(waitinglist) 
    total_excluded = len(excludedlist)

    return total_rows


# @anvil.server.callable
# def write_a_file(my_string):
#   with open('/CRMSPCBackup', 'w+') as f:
#     f.write(my_string)













@anvil.server.callable
def get_Waiting_on_4S(tablename,columnname, startdate, enddate, showexcluded, chartid):
#     t = app_tables.charts.get(chartid = chartid)
#     tablename =t['Chart_Name']
#     enddate =t['EndDate']
#     print(enddate)
#     startdate =  datetime(day=1, month=10, year=2022)
#     enddate =  datetime(day=1, month=9, year=2022)
#     enddate = enddate + timedelta(days=1)
    print(tablename)
    print(columnname)
    print(startdate)
    print(enddate)
      
    if showexcluded == False:
  #     print(enddate)
          waitinglist= getattr(app_tables, tablename).search(q.all_of(
                                                  Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
                                                                          q.greater_than_or_equal_to(startdate)) ,
                                                  exclude_point = False 
                                                                          )
                                                )

    else:                                             
      
          waitinglist = getattr(app_tables, tablename).search(q.all_of(
                                                  Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
                                                                          q.greater_than_or_equal_to(startdate)) ,
                                                  
                                                                          )
                                                )
        
    excludedlist= getattr(app_tables, tablename).search(q.all_of(
                                              Date_Entered = q.all_of(q.less_than_or_equal_to(enddate),
                                                                      q.greater_than_or_equal_to(startdate)) ,
                                              exclude_point = True 
                                                                    ))
    total_rows = len(waitinglist) 
    total_excluded = len(excludedlist)
#     print (waitinglist)
    
    dicts = [{'Date_Entered': r['Date_Entered'],columnname: r[columnname],'NoteCol':r['noteCol']}
            for r in waitinglist]
    
 
#     print ('dicts',dicts)
 
    df = pd.DataFrame.from_dict(dicts)
 
    df['Date_Entered'] = pd.to_datetime(df['Date_Entered'], utc= True)
    df.sort_values(by=['Date_Entered'], inplace=True , ascending=True)
    df['Mean']= df[columnname].mean()
    pointdate= 'Date_Entered'
    pointname = columnname
    notecol = df['NoteCol']
    Mean = df[columnname].mean()
    SD = df[columnname].std()
    total_rows = total_rows = df[columnname].count() - 1
#     if total_rows > 5:
    
    
    ninebelow , mean9belowline = outofcontrol9below(df, pointdate, pointname, total_rows, Mean, SD , showexcluded, tablename, chartid)
    nineabove, mean9aboveline = outofcontrol9above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename, chartid )
    down6, mean6fallline  = outofcontrol6fall(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename, chartid )
    up6 ,mean6riseline,   = outofcontrol6rise(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename, chartid   )
    four5above, mean45line = outofcontrol45above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded , tablename, chartid)
    two3above,stagemeandictline = outofcontrol23above(df, pointdate, pointname, total_rows, Mean, SD, showexcluded, tablename, chartid )
    oneabove3 = outofcontrol1above(df, pointdate, pointname, total_rows, Mean, SD,showexcluded , tablename, chartid )
    Scatter=[
    
    go.Scatter(
                        x = df['Date_Entered'] ,
                        y = df[columnname],
                        mode =('markers + lines'),
                        name= columnname
    ),
      
    go.Scatter(
                        x = df['Date_Entered']  ,
                        y = df[columnname],
                        mode='text',
                        name='', 
                        text=df['NoteCol'],
#                         showarrow=True,
#                         arrowhead= 2,                      
                        textposition='top left',
                        textfont=dict(
                                  family="sans serif",
                                  size=14,
                                  color="black")
#                         arrowhead= 4,
#                       arrowhead=2,
#                         arrowsize=6,
#                       arrowwidth=2,
#                       arrowcolor="#636363",
#                       ax=20,
#                       ay=-30,
#                       bordercolor="#c7c7c7",
#                       borderwidth=2,
#                       borderpad=4,
#                       bgcolor="#ff7f0e",
                      ),
          
    go.Scatter(
                        x=df['Date_Entered'],
                        y = df['Mean'] ,
                          mode='lines',
                          name= columnname + ' ' +  'Average  =' + str(round(Mean,0)),
                          line=dict(
                          color= 'green',
                          width=2
#                           dash='dash'                   
                            )),
    
          go.Scatter(
                        x=df['Date_Entered'],
                        y = df['Mean'] -  2 * SD  ,
                          mode='lines',
                          name=  '2SD below line', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'black',
                          width=2,
                          dash='dash'                   
                            )),
#        go.Scatter(x=df['Date_Entered'], y= df['Mean'] +  2 * SD, fill='tozeroy'),
      
#        go.Scatter(x=df['Date_Entered'], y= df['Mean'] +  3 * SD, fill='tonexty'),
     
      go.Scatter(
                        x=df['Date_Entered'],
                        y = df['Mean'] +  3 * SD  ,
                          mode='lines',
                          name= columnname + ' ' + '3SD above', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'red',
                          width=2
#                           dash='dash'                   
                            )),
    go.Scatter(
                        x=df['Date_Entered'],
                        y = df['Mean'] +  2 * SD  ,
                          mode='lines',
                          name=  '2SD above line', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'orange',
                          width=2
#                           dash='dash'                   
                            )),
      
    go.Scatter(
                        x=df['Date_Entered'],
                        y = df['Mean'] +  1 * SD  ,
                          mode='lines',
                          name= columnname + ' ' + '1SD above', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'greenyellow',
                          width=2,
                          dash='dash'                   
                            )),
    two3above, ninebelow, nineabove, oneabove3, down6, up6, four5above, mean45line, mean6riseline , mean9aboveline, mean9belowline, stagemeandictline,mean6fallline
    ]
    json_object = plotly.io.to_html(Scatter, 'name.html')
#     print('mean= ',Mean)
    
    return Scatter, total_rows, total_excluded, Mean, SD, waitinglist

    
# @anvil.server.callable
# def get_Cases_Arriving():
#       return app_tables.cases_arriving.search()
  
@anvil.server.callable
def store_data(file , tablename):
  with anvil.media.TempFile(file) as file_name:
    if file.content_type == 'text/csv':
      df = pd.read_csv(file_name)
    else:
      df = pd.read_excel(file_name)
    df['Date_Entered'] = pd.to_datetime(df['Date_Entered'], format='%d/%m/%Y')
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      getattr(app_tables, tablename).add_row(**d, exclude_point = False)

def connect():
  connection = pymysql.connect(host='51.141.236.29',
                               port=3306,
                               user='CRMReadOnly',
                               password=anvil.secrets.get_secret('CRM'),
                               database = 'infoathand',
                               cursorclass=pymysql.cursors.DictCursor)
  return connection

@anvil.server.callable
def get_Sales_Existing_and_New():
  conn = connect()
  with conn.cursor() as cur:
    cur.execute(
                "Select Date_Format(invoice.date_entered, '%Y/%m/%01') As YM \
                      , Sum(invoice.amount_usdollar) As \
                      NewandExisting_Invoice_total \
                From invoice Inner Join \
                  invoice_cstm On invoice_cstm.id_c = invoice.id Inner Join \
                  accounts On invoice.shipping_account_id = accounts.id \
                Where (invoice_cstm.newexistingormaintenance_c = 'New') Or \
                  (invoice_cstm.newexistingormaintenance_c = 'Existing') \
                Group By YM \
                Order By Date_Format(Date(invoice.date_entered), '%Y/%m')")  
    
    
    return cur.fetchall() 
  
# @anvil.server.callable
# def get_df_Sales_Existing_and_New(startdate, enddate):
# #     print(startdate)
# #     print(enddate)
#     conn = connect()
#     t = app_tables.charts.search(chartid = 1)
# #     t.update(Start_Date  = date(startdate), End_Date = date(enddate))
    
#     for row in t:
# #        print(row['ChartSQL'])
#        chartsql = row['ChartSQL']
# #        row['StartDate'] =  datetime.strptime(startdate, '%Y-%m-%d').date()
# #        row['EndDate'] = datetime.strptime(enddate, '%Y-%m-%d').date()
#     with conn.cursor() as cur:
#      cur.execute(chartsql
       
# #                 "Select Date_Format(invoice.date_entered, '%Y/%m/%01') As YM \
# #                       , Sum(invoice.amount_usdollar) As \
# #                       NewandExisting_Invoice_total \
# #                 From invoice Inner Join \
# #                   invoice_cstm On invoice_cstm.id_c = invoice.id Inner Join \
# #                   accounts On invoice.shipping_account_id = accounts.id \
# #                 Where (invoice_cstm.newexistingormaintenance_c = 'New') Or \
# #                   (invoice_cstm.newexistingormaintenance_c = 'Existing') \
# #                 Group By YM \
# #                 Order By Date_Format(Date(invoice.date_entered), '%Y/%m')"
#      )  
     
#     dicts = [{'YM': r['YM'], 'NewandExisting_Invoice_total': r['NewandExisting_Invoice_total']}
#             for r in cur.fetchall()]
    
#     df = pd.DataFrame.from_dict(dicts)
#     df['YM'] = pd.to_datetime(df['YM'])
#     df = (df.set_index('YM')
#       .reindex(pd.date_range(startdate, enddate, freq='MS'))
#       .rename_axis(['YM'])
#       .fillna(0)
#       .reset_index())
#     df['Mean'] = df['NewandExisting_Invoice_total'].mean()
# #     df['SD'] = df['NewandExisting_Invoice_total'].stdev()
#     mean1 = df['NewandExisting_Invoice_total'].mean()
#     SD1 = df['NewandExisting_Invoice_total'].std()
  
#     Scatter=[
    
#     go.Scatter(
#                         x = df['YM'] ,
#                         y = df['NewandExisting_Invoice_total'],
#                         mode ='markers + lines',
#                         name= ' New and Existing Sales'),
#     go.Scatter(
#                         x=df['YM'],
#                         y = df['Mean'] ,
#                           mode='lines',
#                           name= ' New and Existing Sales Average' + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'green',
#                           width=2
# #                           dash='dash'                   
#                             )),
#     go.Scatter(
#                         x=df['YM'],
#                         y = df['Mean'] +  3 * SD1  ,
#                           mode='lines',
#                           name= ' New and Existing Sales 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'red',
#                           width=2
# #                           dash='dash'                   
#                             ))
                                
#     ]
# #     print(dfx)
# #     print (df)
# #     df = pd.DataFrame.from_dict(dicts)
#     return Scatter

# @anvil.server.callable
# def get_daily_cases_arriving(startdate, enddate, show_dropped):
# #     print(startdate)
# #     print(enddate)
#     conn = connect()
#     t = app_tables.charts.search(chartid=2)
#     for row in t:
# #        print(row['ChartSQL'])
#        chartsql = row['ChartSQL']
# #     print (chartsql)
#     with conn.cursor() as cur:
#      cur.execute( chartsql
# #        " Select  Date(cases.date_entered) As Date_Entered,  Count(cases.id) As All_Cases \
# #                   From cases Inner Join \
# #                                 cases_cstm On cases_cstm.id_c = cases.id \
# #                                   Group By (Date(cases.date_entered))"
#      )  
     
#     dicts = [{'Date_Entered': r['Date_Entered'], 'All_Cases': r['All_Cases']}
#             for r in cur.fetchall()]
    
#     df = pd.DataFrame.from_dict(dicts)
#     df['Date_Entered'] = pd.to_datetime(df['Date_Entered'])
#     df = (df.set_index('Date_Entered')
#       .reindex(pd.date_range(startdate, enddate, freq='B'))
#       .rename_axis(['Date_Entered'])
#       .fillna(0)
#       .reset_index())
# #     print(df)
#     if show_dropped == False:
#           missd= df[df['Date_Entered']=='2022-09-19'].index.values.astype(int)
#           missd1= df[df['Date_Entered']=='2022-08-29'].index.values.astype(int)
#           missd2= df[df['Date_Entered']=='2022-06-02'].index.values.astype(int)
#           missd3= df[df['Date_Entered']=='2022-06-03'].index.values.astype(int)
#           missd4= df[df['Date_Entered']=='2022-05-02'].index.values.astype(int)
#           df = df.drop(labels = missd, axis=0)
#           df = df.drop(labels = missd1, axis=0)
#           df = df.drop(labels = missd2, axis=0)
#           df = df.drop(labels = missd3, axis=0)
#           df = df.drop(labels = missd4, axis=0)
#     df['Mean'] = df['All_Cases'].mean()
# #     df['SD'] = df['All_Cases'].stdev()
#     mean1 = df['All_Cases'].mean()
#     SD1 = df['All_Cases'].std()
  
#     Scatter=[
    
#     go.Scatter(
#                         x = df['Date_Entered'] ,
#                         y = df['All_Cases'],
#                         mode ='markers + lines',
#                         name= ' All_Cases'),
#     go.Scatter(
#                         x=df['Date_Entered'],
#                         y = df['Mean'] ,
#                           mode='lines',
#                           name= ' All_Cases Average' + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'green',
#                           width=2
# #                           dash='dash'                   
#                             )),
#     go.Scatter(
#                         x=df['Date_Entered'],
#                         y = df['Mean'] +  3 * SD1  ,
#                           mode='lines',
#                           name= ' All_Cases 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'red',
#                           width=2
# #                           dash='dash'                   
#                             ))
                                
#     ]
# #     print(dfx)
# #     print (df)
# #     df = pd.DataFrame.from_dict(dicts)
#     return Scatter


# @anvil.server.callable
# def get_daily_cases_closed(startdate, enddate, show_dropped):
# #     print(startdate)
# #     print(enddate)
#     conn = connect()
#     t = app_tables.charts.search(chartid=3)
#     for row in t:
# #        print(row['ChartSQL'])
#        chartsql = row['ChartSQL']
# #     print (chartsql)
#     with conn.cursor() as cur:
#      cur.execute( chartsql
# #        " Select  Date(cases.date_entered) As Date_Entered,  Count(cases.id) As All_Cases \
# #                   From cases Inner Join \
# #                                 cases_cstm On cases_cstm.id_c = cases.id \
# #                                   Group By (Date(cases.date_entered))"
#      )  
     
#     dicts = [{'Date_Closed': r['Date_Closed'], 'All_Cases_Closed': r['All_Cases_Closed']}
#             for r in cur.fetchall()]
    
#     df = pd.DataFrame.from_dict(dicts)
#     print(df)
#     df['Date_Closed'] = pd.to_datetime(df['Date_Closed'])
#     df = (df.set_index('Date_Closed')
#       .reindex(pd.date_range(startdate, enddate, freq='B'))
#       .rename_axis(['Date_Closed'])
#       .fillna(0)
#       .reset_index())
# #     print(df)
#     if show_dropped == False:
#           missd= df[df['Date_Closed']=='2022-09-19'].index.values.astype(int)
#           missd1= df[df['Date_Closed']=='2022-08-29'].index.values.astype(int)
#           missd2= df[df['Date_Closed']=='2022-06-02'].index.values.astype(int)
#           missd3= df[df['Date_Closed']=='2022-06-03'].index.values.astype(int)
#           missd4= df[df['Date_Closed']=='2022-05-02'].index.values.astype(int)
#           df = df.drop(labels = missd, axis=0)
#           df = df.drop(labels = missd1, axis=0)
#           df = df.drop(labels = missd2, axis=0)
#           df = df.drop(labels = missd3, axis=0)
#           df = df.drop(labels = missd4, axis=0)
#     df['Mean'] = df['All_Cases_Closed'].mean()
# #     df['SD'] = df['All_Cases'].stdev()
#     mean1 = df['All_Cases_Closed'].mean()
#     SD1 = df['All_Cases_Closed'].std()
  
#     Scatter=[
    
#     go.Scatter(
#                         x = df['Date_Closed'] ,
#                         y = df['All_Cases_Closed'],
#                         mode ='markers + lines',
#                         name= ' All_Cases_Closed'),
#     go.Scatter(
#                         x=df['Date_Closed'],
#                         y = df['Mean'] ,
#                           mode='lines',
#                           name= ' All_Cases_Closed Average' + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'green',
#                           width=2
# #                           dash='dash'                   
#                             )),
#     go.Scatter(
#                         x=df['Date_Closed'],
#                         y = df['Mean'] +  3 * SD1  ,
#                           mode='lines',
#                           name= ' All_Cases_Closed 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'red',
#                           width=2
# #                           dash='dash'                   
#                             )),
#     go.Scatter(
#                         x=df['Date_Closed'],
#                         y = df['Mean'] +  2 * SD1  ,
#                           mode='lines',
#                           name= ' All_Cases_Closed 2SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'black',
#                           width=2
# #                           dash='dash'                   
#                             ))
                                
#     ]
# #     print(dfx)
# #     print (df)
# #     df = pd.DataFrame.from_dict(dicts)
#     return Scatter
# #    For each row, pull out only the data we want to put into pd
# #     dicts = [{'YM': r['YM'], 'NewandExisting_Invoice_total': r['NewandExisting_Invoice_total']}
# # #             for r in db_data]
# #     print(dicts)
# #     df = pd.DataFrame.from_dict(dicts)
# #     print(df['YM'])
# #     df['YM'] = pd.to_datetime(df['YM'])
# #     print(df['YM'])
# #     freq= 'MS'


  
# #     df = (df.set_index('YM')
# #       .reindex(pd.date_range('2008-02-01', '2022-08-01', freq='MS'))
# #       .rename_axis(['YM'])
# #       .fillna(0)
# #       .reset_index())
    
# #     print ('from server',df)
# #     df = pd.DataFrame.to_dict(df)
# #     print(all_dates)
# #     return df
# #     return  df 







# @anvil.server.callable
# def get_data(startdate, enddate, show_dropped, chartid, Date_Column, Measure_Column):
# #     print(startdate)
# #     print(enddate)
#     conn = connect()
#     t = app_tables.charts.search(chartid=chartid)
#     for row in t:
# #        print(row['ChartSQL'])
        
#       chartsql = row['ChartSQL']
#       with conn.cursor() as cur:
#             cur.execute( chartsql)

#       dicts = [{Date_Column: r[Date_Column], Measure_Column: r[Measure_Column]}
#       for r in cur.fetchall()]

#       df = pd.DataFrame.from_dict(dicts)
#       df[Date_Column] = pd.to_datetime(df[Date_Column])
      
# #     print(df) 
#     df = (df.set_index(Date_Column)
#       .reindex(pd.date_range(startdate, enddate, freq='B'))
#       .rename_axis([Date_Column])
#       .fillna(0)
#       .reset_index())
# #     print(df)
#     if show_dropped == False:
#           missd= df[df[Date_Column]=='2022-09-19'].index.values.astype(int)
#           missd1= df[df[Date_Column]=='2022-08-29'].index.values.astype(int)
#           missd2= df[df[Date_Column]=='2022-06-02'].index.values.astype(int)
#           missd3= df[df[Date_Column]=='2022-06-03'].index.values.astype(int)
#           missd4= df[df[Date_Column]=='2022-05-02'].index.values.astype(int)
#           missd5= df[df[Date_Column]=='2022-04-15'].index.values.astype(int)
#           missd6= df[df[Date_Column]=='2022-04-18'].index.values.astype(int)
#           df = df.drop(labels = missd, axis=0)
#           df = df.drop(labels = missd1, axis=0)
#           df = df.drop(labels = missd2, axis=0)
#           df = df.drop(labels = missd3, axis=0)
#           df = df.drop(labels = missd4, axis=0)
#           df = df.drop(labels = missd5, axis=0)
#           df = df.drop(labels = missd6, axis=0)
#     df['Mean'] = df[Measure_Column].mean()
# #     df['SD'] = df['All_Cases'].stdev()
#     mean1 = df[Measure_Column].mean()
#     SD1 = df[Measure_Column].std()
#     total_rows = df[Measure_Column].count() - 1
    
#     print()
#     print ('Find 2 out 3 above 2 sd')
#     print ('-------------------------------------------')
#     print()

#     outofcontrol23above = pd.DataFrame()
#     for i in range(2,total_rows):
#         countx = 0
#         if (df[Measure_Column].iloc[i]  > (2 * SD1 + mean1)):
#             countx = 1
# #             print(df[Measure_Column].iloc[i],i)
#         if (df[Measure_Column].iloc[i-1]  > (2 * SD1 + mean1)):
#                 countx = countx + 1
# #                 print(df[Measure_Column].iloc[i -1], i-1)
#         if (df[Measure_Column].iloc[i-2]  > (2 * SD1 + mean1)):
#                 countx = countx + 1
# #                 print(df[Measure_Column].iloc[i - 2],1-2)
#         if countx == 2:
#                 outofcontrol23above = outofcontrol23above.append({Date_Column: df[Date_Column].iloc[i-2],Measure_Column:df[Measure_Column].iloc[i-2]}, ignore_index=True)
#                 outofcontrol23above = outofcontrol23above.append({Date_Column: df[Date_Column].iloc[i-1],Measure_Column:df[Measure_Column].iloc[i-1]}, ignore_index=True)
#                 outofcontrol23above = outofcontrol23above.append({Date_Column: df[Date_Column].iloc[i],Measure_Column:df[Measure_Column].iloc[i]}, ignore_index=True)
# #     print('outofcontrol23above', outofcontrol23above)
    
#     if not outofcontrol23above.empty: 
#             #Filter out Orders below (2 * SD1 + mean1)
#             outofcontrol23abovefilter =  outofcontrol23above[Measure_Column] > (2 * SD1 + mean1)
#             outofcontrol23above =  outofcontrol23above[outofcontrol23abovefilter] 
#             print('outofcontrol23above with measures above 2 * SD1 filtered out')
    
#     if outofcontrol23above.empty:
#         two3above = go.Scatter(
#             visible='legendonly',
#              name='2 out 3 above 2 X SD')

#     else:
#         two3above = go.Scatter(  # x=df[pointdate],
#             # y=df[pointname],
#             x=outofcontrol23above[Date_Column],
#             y=outofcontrol23above[Measure_Column],
#             mode='markers',
#             name='2 out 3 above 2 X SD',
#             marker=dict(
#                 color='yellow',
#                 size=2,
#                 line=dict(
#                     color='yellow',
#                     width=8
#                 ))
#         )
            
# #     return outofcontrol23above
#     print()
#     print ('Find 1 above 3 sd')
#     print ('-------------------------------------------')
#     print()

#     outofcontrol1above = pd.DataFrame()
#     for i in range(0,total_rows):
#         countx = 0
#         if (df[Measure_Column].iloc[i]  > ((3 * SD1) + mean1)):
#             countx = 1

#         if countx == 1:
#                 outofcontrol1above = outofcontrol1above.append({Date_Column: df[Date_Column].iloc[i],Measure_Column:df[Measure_Column].iloc[i]}, ignore_index=True)

# #     if outofcontrol1above.empty:
# #         print('Empty')
#     print('outofcontrol1above',outofcontrol1above)

#     if outofcontrol1above.empty:
#         print('empty')
#         outofcontrolabove1 = go.Scatter(
#             visible='legendonly',
#             name='One above 3 X SD')
    
#     else:
    
#         outofcontrolabove1 = go.Scatter(
#                           x=outofcontrol1above[Date_Column],
#                           y=outofcontrol1above[Measure_Column],
#                           mode='markers',
#                           name='One above 3 X SD',
#                           marker=dict(
#                                                 color='red',
#                                                 size=2,
#                                                 line=dict(
#                                                     color='red',
#                                                     width=8
#                                                 ))
#                     )
      
#     outofcontrol6fall = pd.DataFrame() 
#     for i in range(5,total_rows):
#         countx = 0
#         if (df[Measure_Column].iloc[i]  < df[Measure_Column].iloc[i-1]):
#                 countx = 1
# #                 print(df[Measure_Column].iloc[i], i, countx)
#         if (df[Measure_Column].iloc[i-1]  < df[Measure_Column].iloc[i-2]):
#                 countx = countx + 1
# #                 print(df[Measure_Column].iloc[i-1], i-1, countx)
#         if (df[Measure_Column].iloc[i-2]  < df[Measure_Column].iloc[i-3]):
#                 countx = countx + 1
# #                 print(df[Measure_Column].iloc[i-2],i-2, countx)
#         if (df[Measure_Column].iloc[i-3]  < df[Measure_Column].iloc[i-4] ):
#                 countx = countx + 1
# #                 print(df[Measure_Column].iloc[i-3], i-3, countx)
#         if (df[Measure_Column].iloc[i-4]  < df[Measure_Column].iloc[i - 5]):
#                 countx = countx + 1
# #                 print(df[Measure_Column].iloc[i-4], i-4, countx)
#         if (df[Measure_Column].iloc[i - 5]  < df[Measure_Column].iloc[i-6] ):
#                 countx = countx + 1
# #                 print(df[Measure_Column].iloc[i-5], i-5, countx)
# #                if (df[Measure_Column].iloc[i - 6]  < df[Measure_Column].iloc[i-7] ):
# #                        countx = countx + 1
# #         print(countx)
#         if countx == 6:
#                 outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-5],Measure_Column:df[Measure_Column].iloc[i-5]}, ignore_index=True)
#                 outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-4],Measure_Column:df[Measure_Column].iloc[i-4]}, ignore_index=True)
#                 outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-3],Measure_Column:df[Measure_Column].iloc[i-3]}, ignore_index=True)
#                 outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-2],Measure_Column:df[Measure_Column].iloc[i-2]}, ignore_index=True)
#                 outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-1],Measure_Column:df[Measure_Column].iloc[i-1]}, ignore_index=True)
#                 outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i],Measure_Column:df[Measure_Column].iloc[i]}, ignore_index=True)
    

#     if outofcontrol6fall.empty:
#         print('Empty')

#     if outofcontrol6fall.empty:
#         down6 = go.Scatter(
#             visible='legendonly')

#     else:
#         down6 = go.Scatter(  # x=df[Date_Column],
#             # y=df[Measure_Column],
#             x=outofcontrol6fall[Date_Column],
#             y=outofcontrol6fall[Measure_Column],
#             mode='markers',
#             name='6 rising in sucession',
#             marker=dict(
#                              color='red',
#                 size=2,
#                 line=dict(
#                     color='lavender',
#                     width=8
#                 ))
#         )
    
    
#     print()
#     print ('Nine or more Points on high side of the mean')
#     print ('-------------------------------------------')
#     print()


#     outofcontrol9above = pd.DataFrame() 
#     for i in range(8,total_rows):
#         countx = 0
#         if (df[Measure_Column].iloc[i]  > (mean1)):
#             countx = 1
            
#         if (df[Measure_Column].iloc[i-1]  > (mean1)):
#                 countx = countx + 1
                
#         if (df[Measure_Column].iloc[i-2]  > (mean1)):
#                 countx = countx + 1
                
#         if (df[Measure_Column].iloc[i-3]  > (mean1)):
#                 countx = countx + 1
                
#         if (df[Measure_Column].iloc[i-4]  > (mean1)):
#                 countx = countx + 1

#         if (df[Measure_Column].iloc[i - 5]  > (mean1)):
#                 countx = countx + 1
              
#         if (df[Measure_Column].iloc[i-6]  > (mean1)):
#                 countx = countx + 1
                
#         if (df[Measure_Column].iloc[i-7]  > (mean1)):
#                 countx = countx + 1
            
#         if (df[Measure_Column].iloc[i-8]  > (mean1)):
#                 countx = countx + 1

#         if countx == 9:
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-8],Measure_Column:df[Measure_Column].iloc[i-8]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-7],Measure_Column:df[Measure_Column].iloc[i-7]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-6],Measure_Column:df[Measure_Column].iloc[i-6]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-5],Measure_Column:df[Measure_Column].iloc[i-5]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-4],Measure_Column:df[Measure_Column].iloc[i-4]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-3],Measure_Column:df[Measure_Column].iloc[i-3]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-2],Measure_Column:df[Measure_Column].iloc[i-2]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-1],Measure_Column:df[Measure_Column].iloc[i-1]}, ignore_index=True)
#                 outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i],Measure_Column:df[Measure_Column].iloc[i]}, ignore_index=True)
#     print()

#     if outofcontrol9above.empty:
#         print('Empty')
                
#     if outofcontrol9above.empty:
#         nineabove = go.Scatter(
#             visible='legendonly',
#             name='9 consecutively below mean')
#     else:
#         nineabove = go.Scatter(
#             x=outofcontrol9above[Date_Column],
#             y=outofcontrol9above[Measure_Column],
#             mode='markers',
#             name='9 consecutively above mean',
#             marker=dict(
#                 color='red',
#                 size=2,
#                 line=dict(
#                     color='powderblue',
#                     width=8
#                 ))
#         )
#     Scatter=[
    
#     go.Scatter(
#                         x = df[Date_Column] ,
#                         y = df[Measure_Column],
#                         mode ='markers + lines',
#                         name= Measure_Column),
#     go.Scatter(
#                         x=df[Date_Column],
#                         y = df['Mean'] ,
#                           mode='lines',
#                           name= ' All_Cases_Closed Average' + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'green',
#                           width=2
# #                           dash='dash'                   
#                             )),
#     go.Scatter(
#                         x=df[Date_Column],
#                         y = df['Mean'] +  3 * SD1  ,
#                           mode='lines',
#                           name= Measure_Column + ' 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'red',
#                           width=2
# #                           dash='dash'                   
#                                )),
#     go.Scatter(
#                         x=df[Date_Column],
#                         y = df['Mean'] +  2 * SD1  ,
#                           mode='lines',
#                           name= Measure_Column  + ' 2SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
#                           line=dict(
#                           color= 'black',
#                           width=1
# #                           dash='dash'                   
#                             )),
     
#     outofcontrolabove1,two3above, down6, nineabove
#     ]
#     return Scatter