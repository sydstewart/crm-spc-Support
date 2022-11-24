from ._anvil_designer import chart_from_changesTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..selection import selection_from_change

class chart_from_changes(chart_from_changesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.chart = properties['chart']
    self.text_box_1.text = self.chart['tablename']
    tablename = self.chart['tablename']
    open_form('Charts_from_Changes', chart =self.item )
    # Any code you write here will run when the form opens.