from ._anvil_designer import RowTemplate11Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...selection import selection

class RowTemplate11(RowTemplate11Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def see_chart_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_1.clear()
  
    self.column_panel_1.add_component(Dropdown_View_Form)
    
    pass

