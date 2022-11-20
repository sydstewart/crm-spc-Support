from ._anvil_designer import changes_gridTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. selection import selection


class changes_grid(changes_gridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.changes.search()
    
    self.select_table_dropdown.items = [row['tablename'] for row in app_tables.charts.search(tables.order_by("order"), Active =True)]

#     self.repeating_panel_1.items = app_tables.changes.search(tablename = self.select_table_dropdown.selected_value)
    # Any code you write here will run when the form opens.

  def Return_to_Main_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dropdown_View_form')
    pass

  def select_table_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.repeating_panel_1.items = app_tables.changes.search(tablename = self.select_table_dropdown.selected_value)
    pass


