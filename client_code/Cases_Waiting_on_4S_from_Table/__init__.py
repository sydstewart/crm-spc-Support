from ._anvil_designer import Cases_Waiting_on_4S_from_TableTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date
from ..AddRow import AddRow
class Cases_Waiting_on_4S_from_Table(Cases_Waiting_on_4S_from_TableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
#     self.data_row_view.visible = True
#     self.data_row_edit.visible = False   
    

  
    chartid = 5
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    showexcluded = self.check_box_1.checked
#     total_rows = anvil.server.call('get_total_rows',tablename, columnname)
    
    Scatter, total_rows, total_excluded, mean, stdev = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    self.number_excluded.text = total_excluded
    self.mean.text = round(mean,2)
    self.SD.text = round(stdev,2)
    if total_rows <=10:
          alert('10 or more data points needed to produce a chart')
    else:
    
        self.plot_1.data = Scatter
        self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    
    self.repeating_panel_1.items = app_tables.test.search()
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Charts')
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    if self.drop_down_2.selected_value == 'Test':
         chartid = 5
    if self.drop_down_2.selected_value == 'Problem Cases':
         chartid = 6
    t = app_tables.charts.get(chartid = chartid)
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    showexcluded = self.check_box_1.checked
    Scatter , total_rows, total_excluded, mean, stdev = anvil.server.call('get_Waiting_on_4S',    tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    self.number_excluded.text = total_excluded
    self.mean.text = round(mean,2)
    self.SD.text = round(stdev,2)
    if total_rows < 10:
        alert('10 or more data points needed to produce a chart')
    
    else: 
    
        self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        self.plot_1.data = Scatter 

        t = app_tables.charts.get(chartid = chartid)
        t['StartDate'] = self.date_picker_1.date
        t['EndDate'] = self.date_picker_2.date
    
    
    pass

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    if self.drop_down_2.selected_value == 'Test':
         chartid = 5
    if self.drop_down_2.selected_value == 'Problem Cases':
         chartid = 6
    t = app_tables.charts.get(chartid = chartid)
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    showexcluded = self.check_box_1.checked
    Scatter, total_rows, total_excluded, mean, stdev = anvil.server.call('get_Waiting_on_4S',  tablename,columnname,  self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    self.number_excluded.text = total_excluded
    self.mean.text = round(mean,2)
    self.SD.text = round(stdev,2)
    
    
    if total_rows < 10:
                    alert('10 or more data points needed to produce a chart')
    
    else: 
    
      self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
      self.plot_1.data = Scatter
  
      t = app_tables.charts.get(chartid = chartid)
      t['StartDate'] = self.date_picker_1.date
      t['EndDate'] = self.date_picker_2.date
    
    pass


  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    if self.drop_down_2.selected_value == 'Test':
         chartid = 5
    if self.drop_down_2.selected_value == 'Problem Cases':
         chartid = 6
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showexcluded = self.check_box_1.checked
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
   
#     print(self.plot_1.layout.title)
    print(columnname )
    print(t['Date_Column_Name'])
    Scatter, total_rows ,total_excluded, mean, stdev= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    print(columnname )
    self.number_excluded.text = total_excluded
    self.mean.text = round(mean,2)
    self.SD.text = round(stdev,2)
    if total_rows < 10:
                    alert('10 or more data points needed to produce a chart')
    
    else: 
       self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
       self.plot_1.data = Scatter
#     print(columnname )
#     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
#     print(self.plot_1.layout.title)
    pass

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    if self.drop_down_2.selected_value == 'Test':
         chartid = 5
    if self.drop_down_2.selected_value == 'Problem Cases':
         chartid = 6
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showexcluded = self.check_box_1.checked
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
#     print(self.plot_1.layout.title)
#     print(columnname )
    Scatter,total_rows ,total_excluded, mean, stdev = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    print(columnname )
    self.number_excluded.text = total_excluded
    self.mean.text = round(mean,2)
    self.SD.text = round(stdev,2)
    self.plot_1.data = Scatter
#     print(columnname )
#     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
#     print(self.plot_1.layout.title)
    pass
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
#     open_form('Cases_Waiting_on_4S_from_Table')
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    if self.drop_down_2.selected_value == 'Test':
         chartid = 5
    if self.drop_down_2.selected_value == 'Problem Cases':
         chartid = 6
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showexcluded = self.check_box_1.checked
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
   
#     print(self.plot_1.layout.title)
#     print(columnname )
    Scatter,total_rows ,total_excluded, mean, stdev = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    print(columnname )
    self.number_excluded.text = total_excluded
    self.mean.text = round(mean,2)
    self.SD.text = round(stdev,2)
    if total_rows < 10:
                    alert('10 or more data points needed to produce a chart')
    
    else: 
       self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
       self.plot_1.data = Scatter
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
      # Initialise an empty dictionary to store the user inputs


  def add_row_click(self, **event_args):
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
      anvil.server.call('add_test', new_test)

    open_form('Cases_Waiting_on_4S_from_Table')
#     date_picker_1_change(self, **event_args)
    pass

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

   

  def show_excluded_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = app_tables.test.search(exclude_point=True, Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )

  def show_included_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = app_tables.test.search(exclude_point=False,  Date_Entered = q.between(self.date_picker_1.date,self.date_picker_2.date))
    self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
    pass

  def refresh_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    if self.drop_down_2.selected_value == 'Test':
         chartid = 5
    if self.drop_down_2.selected_value == 'Problem Cases':
         chartid = 6
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showexcluded = self.check_box_1.checked
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    pass
















