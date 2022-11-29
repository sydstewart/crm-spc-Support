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
    chartid = properties['chartid']
    self.changes_repeating_panel_1.items = app_tables.changes.search(chartid = chartid)
    self.changes_repeating_panel_1.items = sorted([r for r in self.changes_repeating_panel_1.items], key = lambda x: x['change_date'], reverse=True )


  def Return_to_Main_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dropdown_View_form')
    pass



