import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
# import plotly.io
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date, timedelta



def selection(self, **event_args):
  
#     if self.chart_selection_dropdown.selected_value == 'All_Cases_with_4S':
#          chartid = 4
#     if self.chart_selection_dropdown.selected_value == 'Cases Arriving':
#          chartid = 2
#     if self.chart_selection_dropdown.selected_value == 'Test':
#          chartid = 5
#     if self.chart_selection_dropdown.selected_value == 'Problem Cases per Week':
#          chartid = 6
#     if self.chart_selection_dropdown.selected_value == 'Printing Problems':
#          chartid = 7
    print('Start to find Chart Table '+str(datetime.now()))
    t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value)
      
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate'] + timedelta(days=1)
    showexcluded = self.excluded_checkbox.checked 
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    chartname = t['Chart_Name'] 
    chartid = t['chartid']
#     print(self.plot_1.layout.title)
    print(columnname )
    print(t['Date_Column_Name'])
    
    print('End to find Chart Table '+str(datetime.now()))
    print('Start to find Rows '+str(datetime.now()))    
    Scatter, total_rows ,total_excluded, mean, stdev, waitinglist= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded, chartid)
    print(columnname )
    print('total_rows=',total_rows)
    self.total_rows_text.text = str(total_rows)
    print('End to find Rows '+str(datetime.now())) 
    
    if total_rows <=10 or total_rows > 500:
          alert('10 or more data points and not not more than 500 - please adjust the search dates')
          
    else: 
#         print('Start to Create Scatter'+str(datetime.now())) 
#         Scatter, total_rows ,total_excluded, mean, stdev, waitinglist= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
#         print(columnname )
        
#         print('End to Create Scatter'+str(datetime.now())) 
        
        self.number_excluded.text = total_excluded
        self.mean.text = round(mean,2)
        self.SD.text = round(stdev,2)
        self.chartid_textbox.text = chartid         
    
        self.plot_1.layout.title = chartname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        self.plot_1.data = Scatter

        self.repeating_panel_1.items = waitinglist
        self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
  
#         t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value)
        t['StartDate'] = self.date_picker_1.date
        t['EndDate'] = self.date_picker_2.date
      #     print(columnname )
    #     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    #     print(self.plot_1.layout.title)
        print('End to Create Scatter'+str(datetime.now())) 
        
    pass
      
def selectiondate(self, **event_args):
#     if self.chart_selection_dropdown.selected_value == 'All_Cases_with_4S':
#          chartid = 4
#     if self.chart_selection_dropdown.selected_value == 'Cases Arriving':
#          chartid = 2
#     if self.chart_selection_dropdown.selected_value == 'Test':
#          chartid = 5
#     if self.chart_selection_dropdown.selected_value == 'Problem Cases per Week':
#          chartid = 6
#     if self.chart_selection_dropdown.selected_value == 'Printing Problems':
#          chartid = 7
    
    t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value, Active = True)
#     self.date_picker_1.date =t['StartDate']
#     self.date_picker_2.date =t['EndDate']
    showexcluded = self.excluded_checkbox.checked 
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    chartname = t['Chart_Name']
    chartid =t['chartid']
#     print(self.plot_1.layout.title)
    print(columnname )
    print(t['Date_Column_Name'])
    
        
    Scatter, total_rows ,total_excluded, mean, stdev, waitinglist = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded, chartid)
    print('total_rows=',total_rows)
    
    self.total_rows_text.text = str(total_rows)
    if total_rows <=10 or total_rows > 500:
          alert('10 or more data points and not not more than 500 - please adjust the search dates')
          
    else: 
#         Scatter, total_rows ,total_excluded, mean, stdev, waitinglist = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
        print(columnname )
        self.number_excluded.text = total_excluded
        self.mean.text = round(mean,2)
        self.SD.text = round(stdev,2)
        self.chartid_textbox.text = chartid        
    
        self.plot_1.layout.title = chartname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        self.plot_1.data = Scatter
       
        self.repeating_panel_1.items = waitinglist
        self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
  
#         t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value, Active = True)
        t['StartDate'] = self.date_picker_1.date
        t['EndDate'] = self.date_picker_2.date
      #     print(columnname )
    #     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    #     print(self.plot_1.layout.title)
        pass
    
    
def selectchart(self,chartid):
  
#     if self.chart_selection_dropdown.selected_value == 'All_Cases_with_4S':
#          chartid = 4
#     if self.chart_selection_dropdown.selected_value == 'Cases Arriving':
#          chartid = 2
#     if self.chart_selection_dropdown.selected_value == 'Test':
#          chartid = 5
#     if self.chart_selection_dropdown.selected_value == 'Problem Cases per Week':
#          chartid = 6
#     if self.chart_selection_dropdown.selected_value == 'Printing Problems':
#          chartid = 7
    print('Start to find Chart Table '+str(datetime.now()))
    t = app_tables.charts.get(chartid=chartid)
    self.date_picker_1.date =t['StartDate']
    self.date_picker_2.date =t['EndDate']
    showexcluded = self.excluded_checkbox.checked 
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    chartname = t['Chart_Name'] 
#     print(self.plot_1.layout.title)
    print(columnname )
    print(t['Date_Column_Name'])
    
    print('End to find Chart Table '+str(datetime.now()))
    print('Start to find Rows '+str(datetime.now()))    
    Scatter, total_rows ,total_excluded, mean, stdev, waitinglist= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    print(columnname )
    print('total_rows=',total_rows)
    self.total_rows_text.text = str(total_rows)
    print('End to find Rows '+str(datetime.now())) 
    
    if total_rows <=10 or total_rows > 500:
          alert('10 or more data points and not not more than 500 - please adjust the search dates')
          
    else: 
#         print('Start to Create Scatter'+str(datetime.now())) 
#         Scatter, total_rows ,total_excluded, mean, stdev, waitinglist= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
#         print(columnname )
        
#         print('End to Create Scatter'+str(datetime.now())) 
        
        self.number_excluded.text = total_excluded
        self.mean.text = round(mean,2)
        self.SD.text = round(stdev,2)
        self.chartid_textbox.text = chartid       
    
        self.plot_1.layout.title = chartname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        self.plot_1.data = Scatter

        self.repeating_panel_1.items = waitinglist
        self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
  
#         t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value)
        t['StartDate'] = self.date_picker_1.date
        t['EndDate'] = self.date_picker_2.date
      #     print(columnname )
    #     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    #     print(self.plot_1.layout.title)
        print('End to Create Scatter'+str(datetime.now())) 
        pass 
      
def selectchartdate(self, chartid):
#     if self.chart_selection_dropdown.selected_value == 'All_Cases_with_4S':
#          chartid = 4
#     if self.chart_selection_dropdown.selected_value == 'Cases Arriving':
#          chartid = 2
#     if self.chart_selection_dropdown.selected_value == 'Test':
#          chartid = 5
#     if self.chart_selection_dropdown.selected_value == 'Problem Cases per Week':
#          chartid = 6
#     if self.chart_selection_dropdown.selected_value == 'Printing Problems':
#          chartid = 7
    
    t = app_tables.charts.get(chartid=chartid, Active = True)
#     self.date_picker_1.date =t['StartDate']
#     self.date_picker_2.date =t['EndDate']
    showexcluded = self.excluded_checkbox.checked 
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
    chartname = t['Chart_Name'] 
#     print(self.plot_1.layout.title)
    print(columnname )
    print(t['Date_Column_Name'])
    
        
    Scatter, total_rows ,total_excluded, mean, stdev, waitinglist = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    print('total_rows=',total_rows)
    self.total_rows_text.text = str(total_rows)
    if total_rows <=10 or total_rows > 500:
          alert('10 or more data points and not not more than 500 - please adjust the search dates')
          
    else: 
#         Scatter, total_rows ,total_excluded, mean, stdev, waitinglist = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
        print(columnname )
        self.number_excluded.text = total_excluded
        self.mean.text = round(mean,2)
        self.SD.text = round(stdev,2)
               
    
        self.plot_1.layout.title = chartname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        self.plot_1.data = Scatter
       
        self.repeating_panel_1.items = waitinglist
        self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
  
#         t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value, Active = True)
        t['StartDate'] = self.date_picker_1.date
        t['EndDate'] = self.date_picker_2.date
      #     print(columnname )
    #     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    #     print(self.plot_1.layout.title)
        pass

    
def selection_from_change(self, chartid):
  
  
          print('Start to find Chart Table '+str(datetime.now()))
          t = app_tables.charts.get(chartid=chartid)
          self.date_picker_1.date =t['StartDate']
          self.date_picker_2.date =t['EndDate']
          showexcluded = self.excluded_checkbox.checked 
          tablename =t['tablename']
          columnname = t['Measure_Column_Name']
          chartname = t['Chart_Name'] 
      #     print(self.plot_1.layout.title)
          print(columnname )
          print(t['Date_Column_Name'])
              
      #         print('End to find Chart Table '+str(datetime.now()))
      #         print('Start to find Rows '+str(datetime.now()))    
          Scatter, total_rows ,total_excluded, mean, stdev, waitinglist= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded, chartid)
          print(columnname )
          print('total_rows=',total_rows)
          self.total_rows_text.text = str(total_rows)
          print('End to find Rows '+str(datetime.now())) 
          
          if total_rows <=10 or total_rows > 500:
                alert('10 or more data points and not not more than 500 - please adjust the search dates')
                
          else: 
#         print('Start to Create Scatter'+str(datetime.now())) 
#         Scatter, total_rows ,total_excluded, mean, stdev, waitinglist= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
#         print(columnname )
        
#         print('End to Create Scatter'+str(datetime.now())) 
            
            self.number_excluded.text = total_excluded
            self.mean.text = round(mean,2)
            self.SD.text = round(stdev,2)
            self.chartid_textbox.text = chartid         
        
            self.plot_1.layout.title = chartname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
            self.plot_1.data = Scatter
    
            self.repeating_panel_1.items = waitinglist
            self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
      
            t = app_tables.charts.get(chartid=chartid)
            t['StartDate'] = self.date_picker_1.date
            t['EndDate'] = self.date_picker_2.date
          #     print(columnname )
        #     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        #     print(self.plot_1.layout.title)
            print('End to Create Scatter'+str(datetime.now())) 
            
            pass
      
def selection_from_change_date(self, tablename, columnname, showexcluded, chartid, chartname):
#     if self.chart_selection_dropdown.selected_value == 'All_Cases_with_4S':
#          chartid = 4
#     if self.chart_selection_dropdown.selected_value == 'Cases Arriving':
#          chartid = 2
#     if self.chart_selection_dropdown.selected_value == 'Test':
#          chartid = 5
#     if self.chart_selection_dropdown.selected_value == 'Problem Cases per Week':
#          chartid = 6
#     if self.chart_selection_dropdown.selected_value == 'Printing Problems':
#          chartid = 7
    
#     t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value, Active = True)
# #     self.date_picker_1.date =t['StartDate']
# #     self.date_picker_2.date =t['EndDate']
#     showexcluded = self.excluded_checkbox.checked 
#     tablename =t['tablename']
#     columnname = t['Measure_Column_Name']
#     chartname = t['Chart_Name']
#     chartid =t['chartid']
# #     print(self.plot_1.layout.title)
#     print(columnname )
#     print(t['Date_Column_Name'])
    
        
    Scatter, total_rows ,total_excluded, mean, stdev, waitinglist = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
    print('total_rows=',total_rows)
    self.total_rows_text.text = str(total_rows)
    if total_rows <=10 or total_rows > 500:
          alert('10 or more data points and not not more than 500 - please adjust the search dates')
          
    else: 
#         Scatter, total_rows ,total_excluded, mean, stdev, waitinglist = anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
        print(columnname )
        self.number_excluded.text = total_excluded
        self.mean.text = round(mean,2)
        self.SD.text = round(stdev,2)
        self.chartid_textbox.text = chartid        
    
        self.plot_1.layout.title = chartname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        self.plot_1.data = Scatter
       
        self.repeating_panel_1.items = waitinglist
        self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x['Date_Entered'], reverse=True )
  
#         t = app_tables.charts.get(Chart_Name= self.chart_selection_dropdown.selected_value, Active = True)
        t['StartDate'] = self.date_picker_1.date
        t['EndDate'] = self.date_picker_2.date
      #     print(columnname )
    #     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    #     print(self.plot_1.layout.title)
        pass