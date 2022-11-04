from ._anvil_designer import RowTemplate5Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# from .. import Cases_Waiting_on_4S_from_Table
class RowTemplate5(RowTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 
    # Any code you write here will run when the form opens.