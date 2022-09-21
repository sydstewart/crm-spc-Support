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

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass



