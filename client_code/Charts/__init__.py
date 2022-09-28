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



