from ._anvil_designer import Button_view_formTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date
from .AddRow import AddRow
# from .. selection import selection
from . selection  import selectiondate
from . selection import selectchart
from .selection import selection
from .selection import selectchartdate

class Button_view_form(Button_view_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
#     self.data_row_view.visible = True
#     self.data_row_edit.visible = False   
#     self.chart_selection_dropdown.items = [row['Chart_Name'] for row in app_tables.charts.search(Active = True)]
    
  
#     chartid = 5
#     t = app_tables.charts.get(chartid = chartid)
#     self.date_picker_1.date =t['StartDate']
#     self.date_picker_2.date =t['EndDate']
#     tablename =t['tablename']
#     columnname = t['Measure_Column_Name']
#     chartname =t['Chart_Name']
#     showexcluded = self.excluded_checkbox.checked  
# #     total_rows = anvil.server.call('get_total_rows',tablename, columnname)
    
#     Scatter, total_rows, total_excluded, mean, stdev, waitinglist = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
#     self.number_excluded.text = total_excluded
#     self.total_rows_text.text = str(total_rows)
#     print('total rows =',total_rows)
#     self.mean.text = round(mean,2)
#     self.SD.text = round(stdev,2)
#     if total_rows <=10 or total_rows > 400:
#           alert('10 or more data points and not not more than 400 - please adjust the search dates')
#     else:
    
#         self.plot_1.data = Scatter
#         self.plot_1.layout.title = chartname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    
#     self.repeating_panel_1.items = waitinglist
#     self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts')
    pass
  

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    selectchartdate(self, self.chartid_textbox.text)
    pass

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    selectchartdate(self, self.chartid_textbox.text)
    pass

  def excluded_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    selectchart(self, self.chartid_textbox.text)
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

    open_form('Button_view_form')
#     date_picker_1_change(self, **event_args)
    pass


  

  def show_excluded_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    t = app_tables.charts.get(chartid = self.chartid_textbox.text)
    tablename =t['tablename']
    self.repeating_panel_1.items = getattr(app_tables, tablename).search(exclude_point=True,  Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
#     self.repeating_panel_1.items = app_tables.test.search(exclude_point=True, Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )

  def show_included_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    t = app_tables.charts.get(chartid = self.chartid_textbox.text)
    tablename =t['tablename']
    self.repeating_panel_1.items = getattr(app_tables, tablename).search(exclude_point=False,  Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
#     self.repeating_panel_1.items = app_tables.test.search(exclude_point=False,  Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
    pass



  def cases_arriving_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    selectchart(self, 2)
    pass

  def waiting_on_4S_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    selectchart(self, 4)
    pass

  def dropdown_view_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.cases_arriving_button.visible = False
    self.waiting_on_4S_button.visible = False
    open_form('Dropdown_View_form')
    pass

  def button_view_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.cases_arriving_button.visible = True
    self.waiting_on_4S_button.visible = True
    pass




























