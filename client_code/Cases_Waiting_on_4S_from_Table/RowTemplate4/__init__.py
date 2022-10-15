from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...AddRow import AddRow
from .. import Cases_Waiting_on_4S_from_Table

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.data_row_panel_view.visible = True
    self.data_row_panel_edit.visible = False
#     self.parent.raise_event('x-delete-article', article=self.item)
#     self.repeating_panel_1.set_event_handler('x-refresh-test', self.refresh_test)
#     # Any code you write here will run when the form opens.
#     def refresh_test(self, **event_args):
#         self.repeating_panel_1.items = app_tables.test.search()

  def edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
#     self.data_row_panel_read_view.visible = True
#     self.data_row_panel_write_view.visible = False
#     result_copy = dict(list(self.item))
#     # Open an alert displaying the 'ArticleEdit' Form
#     # set the `self.item` property of the ArticleEdit Form to a copy of the article to be updated
#     save_clicked = alert(
#       content=AddRow(item=result_copy),
#       title="Update Result",
#       large=True,
#       buttons=[("Save", True), ("Cancel", False)]
#     )
#     # Update the article if the user clicks save
#     if save_clicked:
#       anvil.server.call('update_result', self.item, result_copy)

#       # Now refresh the page
#       self.refresh_data_bindings()
#     pass

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if confirm("Are you sure you want to delete {}?".format(self.item['Date_Entered'])):
  
 
        anvil.server.call('delete_test', self.item)
        self.parent.raise_event('x-delete-test', test=self.item)
        self.parent.raise_event(RepeatingPanel())  
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_view.visible = False
    self.data_row_panel_edit.visible = True
    pass

  def Save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_view.visible = True
    self.data_row_panel_edit.visible = False

    anvil.server.call('update_result', self.item)
    self.refresh_data_bindings()
    pass




