from ._anvil_designer import All_Cases_ArrivingTemplate
from anvil import *
import anvil.users
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date

class All_Cases_Arriving(All_Cases_ArrivingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    waitinglist  = anvil.server.call('get_Cases_Arriving')
    self.repeating_panel_1.items = waitinglist
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
    self.plot_1.data = go.Scatter(x = [x['Date_Entered'] for x in waitinglist],
                            y = [x['Cases_Arriving'] for x in waitinglist],
                            mode ='markers+lines',
                            name= ' All_Cases Arriving',
                            marker=dict(
                                        color='green',
                                        size=7),
                            line=dict(
                                        color='blue',
                                        width=2
                                        ))
    self.plot_1.layout.title = ' All_Cases_Arriving' + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('All_Cases_with_4S')
    pass

  def Cases_with_4S_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('All_Cases_with_4S')
    pass


