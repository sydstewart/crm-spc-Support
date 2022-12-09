from ._anvil_designer import ProjectsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables.query as q
from anvil.tables import app_tables

class Projects(ProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    projects, total_rows = anvil.server.call('listprojects')
    print (projects)
    print('Total Rows = ', total_rows)
    self.total_rows_text.text = total_rows
    self.repeating_panel_1.items = projects