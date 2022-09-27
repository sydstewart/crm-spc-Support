import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pymysql
import pandas as pd
from datetime import datetime, time , date
import plotly.graph_objects as go
import anvil.media


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
@anvil.server.callable
def store_data(file):
  with anvil.media.TempFile(file) as file_name:
    if file.content_type == 'text/csv':
      df = pd.read_csv(file_name)
    else:
      df = pd.read_excel(file_name)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.waiting_on_4s.add_row(**d)

def connect():
  connection = pymysql.connect(host='51.141.236.29',
                               port=3306,
                               user='CRMReadOnly',
                               password=anvil.secrets.get_secret('CRM'),
                               database = 'infoathand',
                               cursorclass=pymysql.cursors.DictCursor)
  return connection


@anvil.server.callable
def get_waiting_on_4s():
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
    t = app_tables.charts.search(chartid = 4)
    
    for row in t:

       chartsql = row['ChartSQL']

    with conn.cursor() as cur:
     cur.execute(chartsql
       
     )  
     
    dicts = [{'Date_Entered': today(), 'All_Cases_with_4S': r['All_Cases_with_4S']}
            for r in cur.fetchall()]
    
    return cur.fetchall() 


anvil.server.callable
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
#     print(startdate)
#     print(enddate)
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
    
    df = pd.DataFrame.from_dict(dicts)
    df['YM'] = pd.to_datetime(df['YM'])
    df = (df.set_index('YM')
      .reindex(pd.date_range(startdate, enddate, freq='MS'))
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
#     df = pd.DataFrame.from_dict(dicts)
    return Scatter

@anvil.server.callable
def get_daily_cases_arriving(startdate, enddate, show_dropped):
#     print(startdate)
#     print(enddate)
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
    
    df = pd.DataFrame.from_dict(dicts)
    df['Date_Entered'] = pd.to_datetime(df['Date_Entered'])
    df = (df.set_index('Date_Entered')
      .reindex(pd.date_range(startdate, enddate, freq='B'))
      .rename_axis(['Date_Entered'])
      .fillna(0)
      .reset_index())
#     print(df)
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
#     df = pd.DataFrame.from_dict(dicts)
    return Scatter


@anvil.server.callable
def get_daily_cases_closed(startdate, enddate, show_dropped):
#     print(startdate)
#     print(enddate)
    conn = connect()
    t = app_tables.charts.search(chartid=3)
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
     
    dicts = [{'Date_Closed': r['Date_Closed'], 'All_Cases_Closed': r['All_Cases_Closed']}
            for r in cur.fetchall()]
    
    df = pd.DataFrame.from_dict(dicts)
    df['Date_Closed'] = pd.to_datetime(df['Date_Closed'])
    df = (df.set_index('Date_Closed')
      .reindex(pd.date_range(startdate, enddate, freq='B'))
      .rename_axis(['Date_Closed'])
      .fillna(0)
      .reset_index())
#     print(df)
    if show_dropped == False:
          missd= df[df['Date_Closed']=='2022-09-19'].index.values.astype(int)
          missd1= df[df['Date_Closed']=='2022-08-29'].index.values.astype(int)
          missd2= df[df['Date_Closed']=='2022-06-02'].index.values.astype(int)
          missd3= df[df['Date_Closed']=='2022-06-03'].index.values.astype(int)
          missd4= df[df['Date_Closed']=='2022-05-02'].index.values.astype(int)
          df = df.drop(labels = missd, axis=0)
          df = df.drop(labels = missd1, axis=0)
          df = df.drop(labels = missd2, axis=0)
          df = df.drop(labels = missd3, axis=0)
          df = df.drop(labels = missd4, axis=0)
    df['Mean'] = df['All_Cases_Closed'].mean()
#     df['SD'] = df['All_Cases'].stdev()
    mean1 = df['All_Cases_Closed'].mean()
    SD1 = df['All_Cases_Closed'].std()
  
    Scatter=[
    
    go.Scatter(
                        x = df['Date_Closed'] ,
                        y = df['All_Cases_Closed'],
                        mode ='markers + lines',
                        name= ' All_Cases_Closed'),
    go.Scatter(
                        x=df['Date_Closed'],
                        y = df['Mean'] ,
                          mode='lines',
                          name= ' All_Cases_Closed Average' + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'green',
                          width=2
#                           dash='dash'                   
                            )),
    go.Scatter(
                        x=df['Date_Closed'],
                        y = df['Mean'] +  3 * SD1  ,
                          mode='lines',
                          name= ' All_Cases_Closed 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'red',
                          width=2
#                           dash='dash'                   
                            )),
    go.Scatter(
                        x=df['Date_Closed'],
                        y = df['Mean'] +  2 * SD1  ,
                          mode='lines',
                          name= ' All_Cases_Closed 2SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'black',
                          width=2
#                           dash='dash'                   
                            ))
                                
    ]
#     print(dfx)
#     print (df)
#     df = pd.DataFrame.from_dict(dicts)
    return Scatter
#    For each row, pull out only the data we want to put into pd
#     dicts = [{'YM': r['YM'], 'NewandExisting_Invoice_total': r['NewandExisting_Invoice_total']}
# #             for r in db_data]
#     print(dicts)
#     df = pd.DataFrame.from_dict(dicts)
#     print(df['YM'])
#     df['YM'] = pd.to_datetime(df['YM'])
#     print(df['YM'])
#     freq= 'MS'


  
#     df = (df.set_index('YM')
#       .reindex(pd.date_range('2008-02-01', '2022-08-01', freq='MS'))
#       .rename_axis(['YM'])
#       .fillna(0)
#       .reset_index())
    
#     print ('from server',df)
#     df = pd.DataFrame.to_dict(df)
#     print(all_dates)
#     return df
#     return  df 

@anvil.server.callable
def get_data(startdate, enddate, show_dropped, chartid, Date_Column, Measure_Column):
#     print(startdate)
#     print(enddate)
    conn = connect()
    t = app_tables.charts.search(chartid=chartid)
    for row in t:
#        print(row['ChartSQL'])
        
      chartsql = row['ChartSQL']
      with conn.cursor() as cur:
            cur.execute( chartsql)

      dicts = [{Date_Column: r[Date_Column], Measure_Column: r[Measure_Column]}
      for r in cur.fetchall()]

      df = pd.DataFrame.from_dict(dicts)
      df[Date_Column] = pd.to_datetime(df[Date_Column])
      
    
    df = (df.set_index(Date_Column)
      .reindex(pd.date_range(startdate, enddate, freq='B'))
      .rename_axis([Date_Column])
      .fillna(0)
      .reset_index())
#     print(df)
    if show_dropped == False:
          missd= df[df[Date_Column]=='2022-09-19'].index.values.astype(int)
          missd1= df[df[Date_Column]=='2022-08-29'].index.values.astype(int)
          missd2= df[df[Date_Column]=='2022-06-02'].index.values.astype(int)
          missd3= df[df[Date_Column]=='2022-06-03'].index.values.astype(int)
          missd4= df[df[Date_Column]=='2022-05-02'].index.values.astype(int)
          missd5= df[df[Date_Column]=='2022-04-15'].index.values.astype(int)
          missd6= df[df[Date_Column]=='2022-04-18'].index.values.astype(int)
          df = df.drop(labels = missd, axis=0)
          df = df.drop(labels = missd1, axis=0)
          df = df.drop(labels = missd2, axis=0)
          df = df.drop(labels = missd3, axis=0)
          df = df.drop(labels = missd4, axis=0)
          df = df.drop(labels = missd5, axis=0)
          df = df.drop(labels = missd6, axis=0)
    df['Mean'] = df[Measure_Column].mean()
#     df['SD'] = df['All_Cases'].stdev()
    mean1 = df[Measure_Column].mean()
    SD1 = df[Measure_Column].std()
    total_rows = df[Measure_Column].count() - 1
    
    print()
    print ('Find 1 above 3 sd')
    print ('-------------------------------------------')
    print()

    outofcontrol1above = pd.DataFrame()
    for i in range(0,total_rows):
        countx = 0
        if (df[Measure_Column].iloc[i]  > ((3 * SD1) + mean1)):
            countx = 1

        if countx == 1:
                outofcontrol1above = outofcontrol1above.append({Date_Column: df[Date_Column].iloc[i],Measure_Column:df[Measure_Column].iloc[i]}, ignore_index=True)

#     if outofcontrol1above.empty:
#         print('Empty')
    print('outofcontrol1above',outofcontrol1above)

    if outofcontrol1above.empty:
        print('empty')
        outofcontrolabove1 = go.Scatter(
            visible='legendonly',
            name='One above 3 X SD')
    
    else:
    
        outofcontrolabove1 = go.Scatter(
                          x=outofcontrol1above[Date_Column],
                          y=outofcontrol1above[Measure_Column],
                          mode='markers',
                          name='One above 3 X SD',
                          marker=dict(
                                                color='red',
                                                size=2,
                                                line=dict(
                                                    color='red',
                                                    width=8
                                                ))
                    )
      
    outofcontrol6fall = pd.DataFrame() 
    for i in range(5,total_rows):
        countx = 0
        if (df[Measure_Column].iloc[i]  < df[Measure_Column].iloc[i-1]):
                countx = 1
#                 print(df[Measure_Column].iloc[i], i, countx)
        if (df[Measure_Column].iloc[i-1]  < df[Measure_Column].iloc[i-2]):
                countx = countx + 1
#                 print(df[Measure_Column].iloc[i-1], i-1, countx)
        if (df[Measure_Column].iloc[i-2]  < df[Measure_Column].iloc[i-3]):
                countx = countx + 1
#                 print(df[Measure_Column].iloc[i-2],i-2, countx)
        if (df[Measure_Column].iloc[i-3]  < df[Measure_Column].iloc[i-4] ):
                countx = countx + 1
#                 print(df[Measure_Column].iloc[i-3], i-3, countx)
        if (df[Measure_Column].iloc[i-4]  < df[Measure_Column].iloc[i - 5]):
                countx = countx + 1
#                 print(df[Measure_Column].iloc[i-4], i-4, countx)
        if (df[Measure_Column].iloc[i - 5]  < df[Measure_Column].iloc[i-6] ):
                countx = countx + 1
#                 print(df[Measure_Column].iloc[i-5], i-5, countx)
#                if (df[Measure_Column].iloc[i - 6]  < df[Measure_Column].iloc[i-7] ):
#                        countx = countx + 1
#         print(countx)
        if countx == 6:
                outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-5],Measure_Column:df[Measure_Column].iloc[i-5]}, ignore_index=True)
                outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-4],Measure_Column:df[Measure_Column].iloc[i-4]}, ignore_index=True)
                outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-3],Measure_Column:df[Measure_Column].iloc[i-3]}, ignore_index=True)
                outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-2],Measure_Column:df[Measure_Column].iloc[i-2]}, ignore_index=True)
                outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i-1],Measure_Column:df[Measure_Column].iloc[i-1]}, ignore_index=True)
                outofcontrol6fall = outofcontrol6fall.append({Date_Column: df[Date_Column].iloc[i],Measure_Column:df[Measure_Column].iloc[i]}, ignore_index=True)
    

    if outofcontrol6fall.empty:
        print('Empty')

    if outofcontrol6fall.empty:
        down6 = go.Scatter(
            visible='legendonly')

    else:
        down6 = go.Scatter(  # x=df[Date_Column],
            # y=df[Measure_Column],
            x=outofcontrol6fall[Date_Column],
            y=outofcontrol6fall[Measure_Column],
            mode='markers',
            name='6 rising in sucession',
            marker=dict(
                             color='red',
                size=2,
                line=dict(
                    color='lavender',
                    width=8
                ))
        )
    
    
    print()
    print ('Nine or more Points on high side of the mean')
    print ('-------------------------------------------')
    print()


    outofcontrol9above = pd.DataFrame() 
    for i in range(8,total_rows):
        countx = 0
        if (df[Measure_Column].iloc[i]  > (mean1)):
            countx = 1
            
        if (df[Measure_Column].iloc[i-1]  > (mean1)):
                countx = countx + 1
                
        if (df[Measure_Column].iloc[i-2]  > (mean1)):
                countx = countx + 1
                
        if (df[Measure_Column].iloc[i-3]  > (mean1)):
                countx = countx + 1
                
        if (df[Measure_Column].iloc[i-4]  > (mean1)):
                countx = countx + 1

        if (df[Measure_Column].iloc[i - 5]  > (mean1)):
                countx = countx + 1
              
        if (df[Measure_Column].iloc[i-6]  > (mean1)):
                countx = countx + 1
                
        if (df[Measure_Column].iloc[i-7]  > (mean1)):
                countx = countx + 1
            
        if (df[Measure_Column].iloc[i-8]  > (mean1)):
                countx = countx + 1

        if countx == 9:
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-8],Measure_Column:df[Measure_Column].iloc[i-8]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-7],Measure_Column:df[Measure_Column].iloc[i-7]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-6],Measure_Column:df[Measure_Column].iloc[i-6]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-5],Measure_Column:df[Measure_Column].iloc[i-5]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-4],Measure_Column:df[Measure_Column].iloc[i-4]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-3],Measure_Column:df[Measure_Column].iloc[i-3]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-2],Measure_Column:df[Measure_Column].iloc[i-2]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i-1],Measure_Column:df[Measure_Column].iloc[i-1]}, ignore_index=True)
                outofcontrol9above = outofcontrol9above.append({Date_Column: df[Date_Column].iloc[i],Measure_Column:df[Measure_Column].iloc[i]}, ignore_index=True)
    print()

    if outofcontrol9above.empty:
        print('Empty')
                
    if outofcontrol9above.empty:
        nineabove = go.Scatter(
            visible='legendonly',
            name='9 consecutively below mean')
    else:
        nineabove = go.Scatter(
            x=outofcontrol9above[Date_Column],
            y=outofcontrol9above[Measure_Column],
            mode='markers',
            name='9 consecutively above mean',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='powderblue',
                    width=8
                ))
        )
    Scatter=[
    
    go.Scatter(
                        x = df[Date_Column] ,
                        y = df[Measure_Column],
                        mode ='markers + lines',
                        name= Measure_Column),
    go.Scatter(
                        x=df[Date_Column],
                        y = df['Mean'] ,
                          mode='lines',
                          name= ' All_Cases_Closed Average' + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'green',
                          width=2
#                           dash='dash'                   
                            )),
    go.Scatter(
                        x=df[Date_Column],
                        y = df['Mean'] +  3 * SD1  ,
                          mode='lines',
                          name= Measure_Column + ' 3SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'red',
                          width=2
#                           dash='dash'                   
                               )),
    go.Scatter(
                        x=df[Date_Column],
                        y = df['Mean'] +  2 * SD1  ,
                          mode='lines',
                          name= Measure_Column  + ' 2SD', # + ' ' + 'Average  =' + str(round(mean1,0)),
                          line=dict(
                          color= 'black',
                          width=1
#                           dash='dash'                   
                            )),
     
    outofcontrolabove1,down6, nineabove
    ]
    return Scatter