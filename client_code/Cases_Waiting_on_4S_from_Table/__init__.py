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
    t = app_tables.charts.get(chartid = 4)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    Scatter = anvil.server.call('get_Waiting_on_4S',  self.date_picker_1.date,  self.date_picker_2.date)

    self.plot_1.data = Scatter
    self.plot_1.layout.title = ' All_Cases_with_4S' + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts')
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    Scatter = anvil.server.call('get_Waiting_on_4S',  self.date_picker_1.date,  self.date_picker_2.date)
    self.plot_1.data = Scatter
    self.plot_1.layout.title = ' All_Cases_with_4S' + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    t = app_tables.charts.get(chartid = 4)
    t['StartDate'] = self.date_picker_1.date
    t['EndDate'] = self.date_picker_2.date
    
    
    pass

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    Scatter = anvil.server.call('get_Waiting_on_4S',  self.date_picker_1.date,  self.date_picker_2.date)
    self.plot_1.data = Scatter
    self.plot_1.layout.title = ' All_Cases_with_4S' + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    t = app_tables.charts.get(chartid = 4)
    t['StartDate'] = self.date_picker_1.date
    t['EndDate'] = self.date_picker_2.date
    
    pass



