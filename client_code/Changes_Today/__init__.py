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
      
        if len(app_tables.changes.search( tablename= table_name))  > 0 :
            changes = app_tables.changes.search(tables.order_by('change_date', ascending=False), tablename = table_name)
            latest = changes[0]
       
            self.repeating_panel_1.items = latest['change_date']
         
        
#            latest = changes[0]
        
#            print (latest['change_date'],latest['tablename'],latest['change_type'])
        
#         if changes:  
#            for row1 in changes: 
#               print (row1['change_date'],row1['tablename'],row1['change_type'])
#         else:
#             print('No changes detected in ', table_name)
    
  