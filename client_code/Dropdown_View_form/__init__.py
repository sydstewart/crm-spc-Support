from ._anvil_designer import Dropdown_View_formTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date
from ..AddRow import AddRow
from .. selection import selection
from .. selection  import selectiondate
from .. selection import selectchart

class Dropdown_View_form(Dropdown_View_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     configure_mfa_with_form()
    anvil.users.login_with_form()
#     mfa_login_with_form()
    loggedinuser =  anvil.users.get_user()['email']
    self.loggedinuser.text = loggedinuser
    
    self.cases_arriving_button.visible = False
    self.waiting_on_4S_button.visible = False
    self.button_view_button.visible = False   
#     self.data_row_view.visible = True
#     self.data_row_edit.visible = False   
    self.chart_selection_dropdown.items = [row['Chart_Name'] for row in app_tables.charts.search(tables.order_by("order"), Active =True)]
    
  

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts')
    pass
  

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    selectiondate(self) 
    pass

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    selectiondate(self)
    pass

  def excluded_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    selection(self)
    pass

  def refresh_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    selection(self)
    pass

  def chart_selection_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    selection(self)
    pass


  def add_row_click(self,**event_args):
    """This method is called when the button is clicked"""
    new_test = {}
   
    # Open an alert displaying the 'ArticleEdit' Form
    save_clicked = alert(
      content=AddRow(item=new_test),
      title="Add Result",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
  
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      t = app_tables.charts.get(chartid = self.chartid_textbox.text)
      tablename =t['tablename']
      print('TableName', tablename) 
      anvil.server.call('add_test', tablename, new_test)

    open_form('Dropdown_View_form')
#     date_picker_1_change(self, **event_args)
    pass

  

  def show_excluded_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    t = app_tables.charts.get(chartid = self.chartid_textbox.text)
    tablename =t['tablename']
    self.repeating_panel_1.items = getattr(app_tables, tablename).search(exclude_point=True,  Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )

  def show_included_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    t = app_tables.charts.get(chartid = self.chartid_textbox.text)
    tablename =t['tablename']
    self.repeating_panel_1.items = getattr(app_tables, tablename).search(exclude_point=False,  Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
    pass



  def cases_arriving_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Button_view_form')
    selectchart(self, 2)
    pass

  def waiting_on_4S_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Button_view_form')
    selectchart(self, 4)
    pass

  def dropdown_view_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.cases_arriving_button.visible = False
    self.waiting_on_4S_button.visible = False
    self.button_view_button.visible = False
    pass

  def button_view_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.cases_arriving_button.visible = True
    self.waiting_on_4S_button.visible = True
    open_form('Button_view_form')
    pass



  def sign_out_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Dropdown_View_form')
    pass
































