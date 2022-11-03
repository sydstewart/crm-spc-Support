from ._anvil_designer import Charts_editTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Charts_edit(Charts_editTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    self.repeating_panel_1.items = app_tables.charts.search(Active = True)

  def charts_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dropdown_View_form')
    pass

  def setup_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts')
    pass


