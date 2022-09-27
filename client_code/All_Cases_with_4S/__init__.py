from ._anvil_designer import All_Cases_with_4STemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class All_Cases_with_4S(All_Cases_with_4STemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    self.repeating_panel_1.items = app_tables.Waiting_on_4S.search()
   