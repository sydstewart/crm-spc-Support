from ._anvil_designer import Charts_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go
from datetime import datetime, time , date
import anvil.media

class Charts_copy(Charts_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
 
    self.repeating_panel_1.items = anvil.server.call('get_Sales_Existing_and_New')
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['YM'], reverse=False )
    startdate = '2008-11-01'
    enddate = '2022-08-01'
    t = app_tables.charts.get(chartid = 2)
    self.date_picker_1.date = t['StartDate']
    self.date_picker_2.date = t['EndDate']
    
    t = app_tables.charts.get(chartid = 4)
    self.date_picker_3.date = t['StartDate']
    self.date_picker_4.date = t['EndDate']
    #     build_Sales_Existing_and_New_graph(self)
    
    t = app_tables.charts.get(chartid = 3)
    self.date_picker_5.date = t['StartDate']
    self.date_picker_6.date = t['EndDate']
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
#     self.plot_1.data = anvil.server.call('get_df_Sales_Existing_and_New', startdate, enddate)
#     self.plot_1.layout.title = ' New and Existing Monthly Sales' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

    # Daily Cases _ self.plot_2 ____________________________________________________________________________
    t = app_tables.charts.get(chartid = 2)
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chartid= t['chartid']
    chart_title =t['Chart_Name']
     
    self.plot_2.data =anvil.server.call('get_data',self.date_picker_1.date, self.date_picker_2.date, self.check_box_1.checked, chartid, Date_Column, Measure_Column )
    self.plot_2.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 
    
    self.plot_1.data =anvil.server.call('get_data',self.date_picker_1.date, self.date_picker_2.date, self.check_box_1.checked, chartid, Date_Column, Measure_Column )
    self.plot_1.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 
    
    
    #     self.plot_2.data = anvil.server.call('get_daily_cases_arriving',self.date_picker_1.date, self.date_picker_2.date, self.check_box_1.checked)
#     self.plot_2.layout.title = ' Daily Cases Arriving' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 
    self.plot_3.data = anvil.server.call('get_daily_cases_closed',self.date_picker_5.date, self.date_picker_6.date, self.check_box_1.checked)
    self.plot_3.layout.title = ' Daily Cases Closed' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 
    t = app_tables.charts.get(chartid = 2)
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chartid = t['chartid']
    self.plot_2.data =anvil.server.call('get_data',self.date_picker_1.date, self.date_picker_2.date, self.check_box_1.checked, chartid, Date_Column, Measure_Column)
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

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    startdate2 = self.date_picker_3.date
    enddate2 = self.date_picker_4.date
    
    self.plot_1.data = anvil.server.call('get_df_Sales_Existing_and_New', startdate2, enddate2)
    
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    startdate1 = self.date_picker_1.date
    enddate1 = self.date_picker_2.date
    show_dropped = self.check_box_1.checked
    self.plot_2.data = anvil.server.call('get_daily_cases_arriving', startdate1, enddate1, show_dropped)
    pass

  
  # Daily Cases   #____________________________________________________________________________________________________
  
  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    t = app_tables.charts.get(chartid = 2)
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chart_title =t['Chart_Name']
    chartid= t['chartid']
    self.plot_2.data =anvil.server.call('get_data',self.date_picker_1.date, self.date_picker_2.date, self.check_box_1.checked, chartid, Date_Column, Measure_Column)
    self.plot_2.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

    pass

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    t = app_tables.charts.get(chartid = 2)
    t['EndDate'] =  self.date_picker_2.date
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chart_title =t['Chart_Name']
    chartid= t['chartid']
    self.plot_2.data =anvil.server.call('get_data',self.date_picker_1.date, self.date_picker_2.date, self.check_box_1.checked, chartid, Date_Column, Measure_Column)
    self.plot_2.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

    pass

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    startdate1 = self.date_picker_1.date
    enddate1 = self.date_picker_2.date
    show_dropped = self.check_box_1.checked
    t = app_tables.charts.get(chartid = 2)
    chart_title =t['Chart_Name']
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chartid= t['chartid']
    self.plot_2.data =anvil.server.call('get_data',self.date_picker_1.date, self.date_picker_2.date, self.check_box_1.checked, chartid, Date_Column, Measure_Column)
    self.plot_2.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

    pass
#_______________________________________________________________________________________
  # Closed cases
   
  def date_picker_5_change(self, **event_args):
    """This method is called when the selected date changes"""
    t = app_tables.charts.get(chartid = 3)
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chart_title =t['Chart_Name']
    chartid= t['chartid']
    self.plot_3.data =anvil.server.call('get_data',self.date_picker_5.date, self.date_picker_6.date, self.check_box_2.checked, chartid, Date_Column, Measure_Column)
    self.plot_3.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

    pass

  def date_picker_6_change(self, **event_args):
    """This method is called when the selected date changes"""
    t = app_tables.charts.get(chartid = 3)
    t['EndDate'] =  self.date_picker_2.date
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chart_title =t['Chart_Name']
    chartid= t['chartid']
    self.plot_3.data =anvil.server.call('get_data',self.date_picker_5.date, self.date_picker_6.date, self.check_box_2.checked, chartid, Date_Column, Measure_Column)
    self.plot_3.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

    pass

  def check_box_2_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    startdate1 = self.date_picker_1.date
    enddate1 = self.date_picker_2.date
    show_dropped = self.check_box_1.checked
    t = app_tables.charts.get(chartid = 3)
    chart_title =t['Chart_Name']
    Date_Column = t['Date_Column_Name']
    Measure_Column = t['Measure_Column_Name']
    chartid= t['chartid']
    self.plot_3.data =anvil.server.call('get_data',self.date_picker_5.date, self.date_picker_6.date, self.check_box_2.checked, chartid, Date_Column, Measure_Column)
    self.plot_3.layout.title = chart_title + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 

    pass
#   def date_picker_5_change(self, **event_args):
#     """This method is called when the selected date changes"""
#     t = app_tables.charts.get(chartid = 3)
#     t['StartDate'] =  self.date_picker_5.date
   
#     self.plot_3.data = anvil.server.call('get_daily_cases_closed',self.date_picker_5.date, self.date_picker_6.date, self.check_box_1.checked)
#     self.plot_3.layout.title = ' Daily Cases Closed' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 
    
#     pass

#   def date_picker_6_change(self, **event_args):
#     """This method is called when the selected date changes"""
#     t = app_tables.charts.get(chartid = 3)
#     t['EndDate'] =  self.date_picker_6.date 
#     self.plot_3.data = anvil.server.call('get_daily_cases_closed',self.date_picker_5.date, self.date_picker_6.date, self.check_box_1.checked)
#     self.plot_3.layout.title = ' Daily Cases Closed' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 
#     pass

#   def check_box_2_change(self, **event_args):
#     """This method is called when this checkbox is checked or unchecked"""
    
#     startdate1 = self.date_picker_5.date
#     enddate1 = self.date_picker_6.date
#     show_dropped = self.check_box_1.checked
#     self.plot_3.data = anvil.server.call('get_daily_cases_closed',self.date_picker_5.date, self.date_picker_6.date, self.check_box_1.checked)
#     self.plot_3.layout.title = ' Daily Cases Closed' + " "  +  " created at " + datetime.now().strftime('%d %B %Y %H:%M') 
#     pass
    
    
 #____________________________________________________________  

  def import_waiting_on_4s_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('store_data',file)
    pass

  def getting_4S_Waiting_click(self, **event_args):
    """This method is called when the button is clicked"""


    self.get_4S_Waiting.text = anvil.server.call('get_4S_Waiting')
    open_form('All_Cases_with_4S')
    
    pass 

  def get_4S_Waiting_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def get_cases_arriving_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.cases_arriving.text = anvil.server.call('get_Cases_Arriving')
    open_form('All_Cases_Arriving')
    pass

  def get_charts_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts')
    pass




 


















