from ._anvil_designer import Users_GridTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Users_Grid(Users_GridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.users.search()
    # Any code you write here will run before the form opens.
    

  def maintenance_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts_edit')
    pass

