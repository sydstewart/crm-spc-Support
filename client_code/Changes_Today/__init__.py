from ._anvil_designer import Changes_TodayTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date , timedelta
from ..Dropdown_View_form import Dropdown_View_form

class Changes_Today(Changes_TodayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.repeating_panel_1.items = app_tables.changes.search(tables.order_by('short_date', ascending=False))
    today = date.today()

#     current_date =  today.strftime("%Y-%m-%d")
    
#     self.repeating_panel_1.items  = app_tables.changes.search(tables.order_by('short_date', ascending=False), short_date= today)
#     today = date.today()
    threedays = today - timedelta(days =3)
    self.last_three_days_button.background = 'theme:Gray 300'
    self.last_seven_days_button.background = 'White'
    self.repeating_panel_1.items  = app_tables.changes.search(tables.order_by('short_date', ascending=False), short_date=q.greater_than_or_equal_to(threedays ))    
#     t = app_tables.charts.search(Active= True)
#     for row in t:
#         table_name= row['tablename']
#         print(table_name)
      
#         if len(app_tables.changes.search( tablename= table_name))  > 0 :
#             changes = app_tables.changes.search(tables.order_by('short_date', ascending=False), tablename = table_name)
#             latest = changes[0]
       
# #             self.repeating_panel_1.items = latest['short_date']
         
        
#             latest = changes[0]
        
#             print (latest['short_date'],latest['tablename'],latest['change_type'])
        
#         if changes:  
#            for row1 in changes: 
#               print (row1['change_date'],row1['tablename'],row1['change_type'])
#         else:
#             print('No changes detected in ', table_name)

  def last_seven_days_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    today = date.today()
    sevendays = today - timedelta(days =7)
    
    self.last_three_days_button.background = 'White'
    self.last_seven_days_button.background = 'theme:Gray 300'
    self.today_button.background = 'White'
    
    self.repeating_panel_1.items  = app_tables.changes.search(tables.order_by('short_date', ascending=False), short_date=q.greater_than_or_equal_to(sevendays ))
    
    
    pass

  def return_to_main_menu_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dropdown_View_form')
    pass

  def last_three_days_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    today = date.today()
    threedays = today - timedelta(days =3)
      
    self.last_three_days_button.background = 'theme:Gray 300'
    self.last_seven_days_button.background = 'White'
    self.today_button.background = 'White'
    self.repeating_panel_1.items  = app_tables.changes.search(tables.order_by('short_date', ascending=False), short_date=q.greater_than_or_equal_to(threedays ))
    pass

  def today_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    today = date.today()
    self.last_three_days_button.background = 'White'
    self.last_seven_days_button.background = 'White'
    self.today_button.background = 'theme:Gray 300'
    
    self.repeating_panel_1.items  = app_tables.changes.search(tables.order_by('short_date', ascending=False), short_date=today)
    pass




