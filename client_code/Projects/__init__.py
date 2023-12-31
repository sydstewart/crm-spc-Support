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
    rows = len(app_tables.projects.search())
    if rows == 0:
        projects, total_rows = anvil.server.call('listprojects')
    else:
    
        projectslist = app_tables.projects.search()
        total_rows = len(projectslist)
        print (projectslist)
        print('Total Rows = ', total_rows)
        self.total_rows_text.text = total_rows
        self.repeating_panel_1.items = projectslist

  def multi_select_drop_down_1_change(self, **event_args):
    """This method is called when the selected values change"""
    selectedlist = self.multi_select_drop_down_1.selected
    projectslist = app_tables.projects.search(boardname=(q.any_of(*selectedlist)))
    total_rows = len(projectslist)
    print (projectslist)
    print('Total Rows = ', total_rows)
    self.total_rows_text.text = total_rows
    self.repeating_panel_1.items = projectslist
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    selectedlist = self.multi_select_drop_down_1.selected
    projectslist = app_tables.projects.search(boardname=(q.any_of(*selectedlist)))
    df = pd.Dataframe(projectslist)
    df.to_excel(r'Path of excel\Projects.xlsx', sheet_name='projects', index=False)
#     result = anvil.server.call("export_to_excel", projectslist)
#     anvil.media.download(result)
    pass


