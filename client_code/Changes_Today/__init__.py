from ._anvil_designer import Changes_TodayTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date 

class Changes_Today(Changes_TodayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    t = app_tables.charts.search(Active= True)
    for row in t:
        table_name = row['tablename']
      
        print(table_name)
      
        changes = app_tables.changes.search(tables.order_by('change_date', ascending=False), tablename = table_name)
        if changes:  
           for row1 in changes: 
              print (row1['change_date'],row1['tablename'],row1['change_type'])
        else:
            print('No changes detected in ', table_name)
    
  