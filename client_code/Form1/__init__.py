from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
 
    self.repeating_panel_1.items = anvil.server.call('get_Sales_Existing_and_New')
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['YM'], reverse=False )
#     build_Sales_Existing_and_New_graph(self)
    
    
#   def build_Sales_Existing_and_New_graph(self):
    # self.plot_1.data = go.Bar(y=[100,400,200,300,500])
    db_data = anvil.server.call('get_Sales_Existing_and_New')
  
    # Create a Scatter plot with this data, and change the colour of the markers
    self.Sales_Existing_and_New_Chart.data = go.Scatter(
      x = [x['YM'] for x in db_data],
      y = [x['NewandExisting_Invoice_total'] for x in db_data],
#       name = 'PICK Chart',
      mode ='markers + lines')
#       marker=dict(size=([x['IPS'] for x in db_data])),  
#       hovertext =  ([x['Project_Name'] for x in db_data])#  + ' ' + ([x['Accounts'] for x in db_data])
    df = anvil.server.call('get_df_Sales_Existing_and_New', db_data)
    
    print(df)



#  dfcsv[dateCol] = pd.to_datetime(dfcsv[dateCol])
#         if t['fill_missing_dates'] == True:
#            freq = t['obs_interval']
#            if freq == 'Month':
#                 freq= 'MS'
#                 all_dates = pd.DataFrame({dateCol:pd.date_range(start=dfcsv[dateCol].min(),
#                                                     end=datetime.now(),  #dfcsv[dateCol].max(),
#                                                     freq=freq)})
# #               elif freq == 'Week':
# #                 freq= 'W'
#            else:
#                 freq == 'Day'
#                 freq= 'B'
       
#                 all_dates = pd.DataFrame({dateCol:pd.bdate_range(start=dfcsv[dateCol].min(),
#                                                     end=dfcsv[dateCol].max(),
#                                                     freq=freq)})
# #               if freq == 'Day':

# else:
#                 freq == 'Day'
#                 freq= 'B'
       
#                 all_dates = pd.DataFrame({dateCol:pd.bdate_range(start=dfcsv[dateCol].min(),
#                                                     end=dfcsv[dateCol].max(),
#                                                     freq=freq)})
# #               if freq == 'Day':
#                 all_dates = pd.tseries.offsets.CustomBusinessDay( weekmask = 'Mon Tues Wed')
                
#            print(all_dates) 

#            dfcsv = pd.merge(all_dates, dfcsv, how="left", on=dateCol).fillna(0)