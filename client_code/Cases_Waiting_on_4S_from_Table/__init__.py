from ._anvil_designer import Cases_Waiting_on_4S_from_TableTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date
from 

class Cases_Waiting_on_4S_from_Table(Cases_Waiting_on_4S_from_TableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    chartid = 5
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    showmeans = self.check_box_1.checked
#     total_rows = anvil.server.call('get_total_rows',tablename, columnname)

    Scatter, total_rows = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showmeans)
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
    t = app_tables.charts.get(chartid = chartid)
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    showmeans = self.check_box_1.checked
    Scatter , total_rows = anvil.server.call('get_Waiting_on_4S',    tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showmeans)
    
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
    t = app_tables.charts.get(chartid = chartid)
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    showmeans = self.check_box_1.checked
    Scatter, total_rows = anvil.server.call('get_Waiting_on_4S',  tablename,columnname,  self.date_picker_1.date,  self.date_picker_2.date, showmeans)
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
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showmeans = self.check_box_1.checked
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
   
#     print(self.plot_1.layout.title)
#     print(columnname )
    Scatter, total_rows = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showmeans)
    print(columnname )
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
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showmeans = self.check_box_1.checked
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
#     print(self.plot_1.layout.title)
#     print(columnname )
    Scatter = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showmeans)
    print(columnname )
    self.plot_1.data = Scatter
#     print(columnname )
#     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
#     print(self.plot_1.layout.title)
    pass
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.drop_down_2.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.drop_down_2.selected_value == 'Cases Arriving':
         chartid = 2
    if self.drop_down_2.selected_value == 'Test':
         chartid = 5
#     self.plot_1.layout.title = ""
    t = app_tables.charts.get(chartid = chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showmeans = self.check_box_1.checked
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
   
#     print(self.plot_1.layout.title)
#     print(columnname )
    Scatter, total_rows = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showmeans)
    print(columnname )
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
      content=Form1(item=new_new_test),
      title="Add Result",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    print(new_article)
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      anvil.server.call('add_test', new_test)

    self.refresh_articles()

    pass
    pass









