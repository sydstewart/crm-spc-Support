from ._anvil_designer import Changes_TodayTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date 

class Changes_Today(Changes_TodayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
   
    self.repeating_panel_1.items = app_tables.changes.search(tables.order_by('change_date', ascending=False))[0]