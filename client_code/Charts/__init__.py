from ._anvil_designer import ChartsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go
from datetime import datetime, time , date
import anvil.media

class Charts(ChartsTemplate):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.select_table_dropdown.items = [row['tablename'] for row in app_tables.charts.search(Active = True)]
  
  
  def getting_4S_Waiting_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.get_4S_Waiting.text = anvil.server.call('get_4S_Waiting')
    open_form('All_Cases_with_4S')
    pass

  def get_cases_arriving_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('get_Cases_Arriving_update')
    self.cases_arriving.text = anvil.server.call('get_Cases_Arriving')
    open_form('All_Cases_Arriving')
    pass

  def get_charts_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts_copy')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts_edit')
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    tablename ='waiting_on_4s'
    open_form('Cases_Waiting_on_4S_from_Table')
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    tablename = 'cases_arriving'
    open_form('Cases_Waiting_on_4S_from_Table')
    pass

  def import_waiting_on_4s_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('store_data',file)
    pass

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('store_data',file, self.select_table_dropdown.selected_value)
    pass

  def return_to_charts_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dropdown_View_form')
    pass










