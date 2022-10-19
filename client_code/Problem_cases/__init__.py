from ._anvil_designer import Problem_casesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Problem_cases(Problem_casesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    chartid = 7
    
    t=app_tables.charts.get(chartid = chartid)
    tablename =t['tablename']
    
    waitinglist= getattr(app_tables, tablename).search()

    self.repeating_panel_1.items = waitinglist
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )

    

   
    for row in waitinglist:
          
          row.update(exclude_point = False)