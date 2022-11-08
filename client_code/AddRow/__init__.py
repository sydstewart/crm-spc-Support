from ._anvil_designer import AddRowTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date

class AddRow(AddRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.check_box_1.checked = False
    self.date_picker_1.format = '%Y-%m-%d'
    self.date_picker_1.pick_time = True
    self.item['Date_Entered'] =  datetime.now()
    self.refresh_data_bindings()
    print('self.date_picker_1.date=',self.date_picker_1.date)
    # Any code you write here will run when the form opens.