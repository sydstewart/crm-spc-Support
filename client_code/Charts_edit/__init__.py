from ._anvil_designer import Charts_editTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Invite_Users import Invite_Users
from ..Charts_Grid import Charts_Grid


class Charts_edit(Charts_editTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    self.repeating_panel_1.items = app_tables.charts.search(Active = True)

  def charts_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dropdown_View_form')
    pass

  def setup_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    anvil.server.call('store_data',file)
    
    pass

  def user_management_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Invite_Users')
    pass

  def chart_table_link_click(self, **event_args):
    """This method is called when the link is clicked"""
#     self.reset_links()
#     self.chart_table_link.role = 'selected'
    self.content_panel.clear()
    self.content_panel.add_component(Charts_Grid(), full_width_row=True)
    open_form('Charts_edit')
    pass

  def user_table_link_click(self, **event_args):
    """This method is called when the link is clicked"""
#     self.reset_links()
#     self.user_table_link.role = 'selected'
    self.content_panel.clear()
    self.content_panel.add_component(Invite_Users(), full_width_row=True)
    pass
  
  def reset_links(self, **event_args):
    self.user_table_link.role = ''
    self.chart_table_link.role = ''      





