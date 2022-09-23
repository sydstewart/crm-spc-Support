import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pymysql
import pandas
from datetime import datetime, time , date
import plotly.graph_objects as go

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#


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
  
@anvil.server.callable
def get_df_Sales_Existing_and_New(startdate, enddate):
    print(startdate)
    print(enddate)
    conn = connect()
    t = app_tables.charts.search(chartid = 1)
#     t.update(Start_Date  = date(startdate), End_Date = date(enddate))
    
    for row in t:
#        print(row['ChartSQL'])
       chartsql = row['ChartSQL']
#        row['StartDate'] =  datetime.strptime(startdate, '%Y-%m-%d').date()
#        row['EndDate'] = datetime.strptime(enddate, '%Y-%m-%d').date()
    with conn.cursor() as cur:
     cur.execute(chartsql
       
#                 "Select Date_Format(invoice.date_entered, '%Y/%m/%01') As YM \
#                       , Sum(invoice.amount_usdollar) As \
#                       NewandExisting_Invoice_total \
#                 From invoice Inner Join \
#                   invoice_cstm On invoice_cstm.id_c = invoice.id Inner Join \
#                   accounts On invoice.shipping_account_id = accounts.id \
#                 Where (invoice_cstm.newexistingormaintenance_c = 'New') Or \
#                   (invoice_cstm.newexistingormaintenance_c = 'Existing') \
#                 Group By YM \
#                 Order By Date_Format(Date(invoice.date_entered), '%Y/%m')"
     )  
     
    dicts = [{'YM': r['YM'], 'NewandExisting_Invoice_total': r['NewandExisting_Invoice_total']}
            for r in cur.fetchall()]
    
    df = pandas.DataFrame.from_dict(dicts)
    df['YM'] = pandas.to_datetime(df['YM'])
    df = (df.set_index('YM')
      .reindex(pandas.date_range(startdate, enddate, freq='MS'))
      .rename_axis(['YM'])
      .fillna(0)
      .reset_index())
    df['Mean'] = df['NewandExisting_Invoice_total'].mean()
#     df['SD'] = df['NewandExisting_Invoice_total'].stdev()
    mean1 = df['NewandExisting_Invoice_total'].mean()
    SD1 = df['NewandExisting_Invoice_total'].std()
  
    Scatter=[
    
    go.Scatter(
                        x = df['YM'] ,
                        y = df['NewandExisting_Invoice_total'],
                        mode ='markers + lines',
                        name= ' New and Existing Sales'),
    go.Scatter(
                        x=df['YM'],
                        y = df['Mean'] ,
                          mode='lines',
                          name= ' New and Existing Sales Average' + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'green',
                          width=2
#                           dash='dash'                   
                            )),
    go.Scatter(
                        x=df['YM'],
                        y = df['Mean'] +  3 * SD1  ,
                          mode='lines',
                          name= ' New and Existing Sales 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'red',
                          width=2
#                           dash='dash'                   
                            ))
                                
    ]
#     print(dfx)
#     print (df)
#     df = pandas.DataFrame.from_dict(dicts)
    return Scatter

@anvil.server.callable
def get_daily_cases_arriving(startdate, enddate, show_dropped):
    print(startdate)
    print(enddate)
    conn = connect()
    t = app_tables.charts.search(chartid=2)
    for row in t:
#        print(row['ChartSQL'])
       chartsql = row['ChartSQL']
#     print (chartsql)
    with conn.cursor() as cur:
     cur.execute( chartsql
#        " Select  Date(cases.date_entered) As Date_Entered,  Count(cases.id) As All_Cases \
#                   From cases Inner Join \
#                                 cases_cstm On cases_cstm.id_c = cases.id \
#                                   Group By (Date(cases.date_entered))"
     )  
     
    dicts = [{'Date_Entered': r['Date_Entered'], 'All_Cases': r['All_Cases']}
            for r in cur.fetchall()]
    
    df = pandas.DataFrame.from_dict(dicts)
    df['Date_Entered'] = pandas.to_datetime(df['Date_Entered'])
    df = (df.set_index('Date_Entered')
      .reindex(pandas.date_range(startdate, enddate, freq='B'))
      .rename_axis(['Date_Entered'])
      .fillna(0)
      .reset_index())
    print(df)
    if show_dropped == False:
          missd= df[df['Date_Entered']=='2022-09-19'].index.values.astype(int)
          missd1= df[df['Date_Entered']=='2022-08-29'].index.values.astype(int)
          missd2= df[df['Date_Entered']=='2022-06-02'].index.values.astype(int)
          missd3= df[df['Date_Entered']=='2022-06-03'].index.values.astype(int)
          missd4= df[df['Date_Entered']=='2022-05-02'].index.values.astype(int)
          df = df.drop(labels = missd, axis=0)
          df = df.drop(labels = missd1, axis=0)
          df = df.drop(labels = missd2, axis=0)
          df = df.drop(labels = missd3, axis=0)
          df = df.drop(labels = missd4, axis=0)
    df['Mean'] = df['All_Cases'].mean()
#     df['SD'] = df['All_Cases'].stdev()
    mean1 = df['All_Cases'].mean()
    SD1 = df['All_Cases'].std()
  
    Scatter=[
    
    go.Scatter(
                        x = df['Date_Entered'] ,
                        y = df['All_Cases'],
                        mode ='markers + lines',
                        name= ' All_Cases'),
    go.Scatter(
                        x=df['Date_Entered'],
                        y = df['Mean'] ,
                          mode='lines',
                          name= ' All_Cases Average' + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'green',
                          width=2
#                           dash='dash'                   
                            )),
    go.Scatter(
                        x=df['Date_Entered'],
                        y = df['Mean'] +  3 * SD1  ,
                          mode='lines',
                          name= ' All_Cases 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'red',
                          width=2
#                           dash='dash'                   
                            ))
                                
    ]
#     print(dfx)
#     print (df)
#     df = pandas.DataFrame.from_dict(dicts)
    return Scatter
#    For each row, pull out only the data we want to put into pandas
#     dicts = [{'YM': r['YM'], 'NewandExisting_Invoice_total': r['NewandExisting_Invoice_total']}
# #             for r in db_data]
#     print(dicts)
#     df = pandas.DataFrame.from_dict(dicts)
#     print(df['YM'])
#     df['YM'] = pandas.to_datetime(df['YM'])
#     print(df['YM'])
#     freq= 'MS'


  
#     df = (df.set_index('YM')
#       .reindex(pandas.date_range('2008-02-01', '2022-08-01', freq='MS'))
#       .rename_axis(['YM'])
#       .fillna(0)
#       .reset_index())
    
#     print ('from server',df)
#     df = pandas.DataFrame.to_dict(df)
#     print(all_dates)
#     return df
#     return  df 