from ._anvil_designer import Cases_Waiting_on_4S_from_TableTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date


class Cases_Waiting_on_4S_from_Table(Cases_Waiting_on_4S_from_TableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    chartid = 2
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']

    Scatter = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date)

    self.plot_1.data = Scatter
    self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts')
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    t = app_tables.charts.get(chartid = chartid)
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    Scatter = anvil.server.call('get_Waiting_on_4S',    tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date)
    self.plot_1.data = Scatter
    self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    t = app_tables.charts.get(chartid = 4)
    t['StartDate'] = self.date_picker_1.date
    t['EndDate'] = self.date_picker_2.date
    
    
    pass

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    t = app_tables.charts.get(chartid = chartid)
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    Scatter = anvil.server.call('get_Waiting_on_4S',  tablename,columnname,  self.date_picker_1.date,  self.date_picker_2.date)
    self.plot_1.data = Scatter
    self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    t = app_tables.charts.get(chartid = 4)
    t['StartDate'] = self.date_picker_1.date
    t['EndDate'] = self.date_picker_2.date
    
    pass


  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
#     print(self.plot_1.layout.title)
#     print(columnname )
    Scatter = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date)
    print(columnname )
    self.plot_1.data = Scatter
#     print(columnname )
#     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
#     print(self.plot_1.layout.title)
    pass





