from ._anvil_designer import All_Cases_with_4STemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class All_Cases_with_4S(All_Cases_with_4STemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    waitinglist  = anvil.server.call('get_Waiting_on_4S')
    self.repeating_panel_1.items = waitinglist
    self.plot_1.data = go.Scatter(x = [x['Date_Entered'] for x in waitinglist],
                            y = [x['All_Cases_with_4S'] for x in waitinglist],
                            marker=dict(color='#2196f3'))