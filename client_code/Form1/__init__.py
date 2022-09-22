from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go
from datetime import datetime, time 

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
 
    self.repeating_panel_1.items = anvil.server.call('get_Sales_Existing_and_New')
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['YM'], reverse=False )
    startdate = '2008-11-01'
    enddate = '2022-08-01'
    
    
    #     build_Sales_Existing_and_New_graph(self)
    
    
#   def build_Sales_Existing_and_New_graph(self):
    # self.plot_1.data = go.Bar(y=[100,400,200,300,500])
    db_data = anvil.server.call('get_Sales_Existing_and_New')
  
    # Create a Scatter plot with this data,
    self.Sales_Existing_and_New_Chart.data = go.Scatter(
      x = [x['YM'] for x in db_data],
      y = [x['NewandExisting_Invoice_total'] for x in db_data],
      mode ='markers + lines')
    self.Sales_Existing_and_New_Chart.layout.title = ' sales' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

#     dfx = anvil.server.call('get_df_Sales_Existing_and_New')
    self.plot_1.data = anvil.server.call('get_df_Sales_Existing_and_New', startdate, enddate)
    self.plot_1.layout.title = ' New and Existing Monthly Sales' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

      

#     self.plot_1.data = go.Scatter(
#       x = dfx['YM'] ,
#       y = dfx['NewandExisting_Invoice_total'],
#       mode ='markers + lines')
#     print(dfx)

     
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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    startdate = self.date_picker_1.date
    print (startdate)
    enddate = self.date_picker_2.date
    self.plot_1.data = anvil.server.call('get_df_Sales_Existing_and_New', startdate, enddate)
    pass

