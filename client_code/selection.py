import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date



def selection(self, **event_args):
    if self.chart_selection_dropdown.selected_value == 'All_Cases_with_4S':
         chartid = 4
    if self.chart_selection_dropdown.selected_value == 'Cases Arriving':
         chartid = 2
    if self.chart_selection_dropdown.selected_value == 'Test':
         chartid = 5
    if self.chart_selection_dropdown.selected_value == 'Problem Cases':
         chartid = 6
    if self.chart_selection_dropdown.selected_value == 'Printing Problems':
         chartid = 7

    t = app_tables.charts.get(chartid = chartid)
#     self.date_picker_1.date =t['StartDate']
#     self.date_picker_2.date =t['EndDate']
    showexcluded = self.excluded_checkbox.checked 
    tablename =t['tablename']
    columnname = t['Measure_Column_Name']
     
#     print(self.plot_1.layout.title)
    print(columnname )
    print(t['Date_Column_Name'])
    
        
    total_rows = anvil.server.call('get_total_rows',tablename,columnname,  self.date_picker_1.date, self.date_picker_2.date, showexcluded)
    if total_rows < 10:
                    alert('10 or more data points needed to produce a chart')
                    self.total_rows_text.text = str(total_rows)
    else: 
        Scatter, total_rows ,total_excluded, mean, stdev= anvil.server.call('get_Waiting_on_4S',tablename, columnname, self.date_picker_1.date,  self.date_picker_2.date, showexcluded)
        print(columnname )
        self.number_excluded.text = total_excluded
        self.mean.text = round(mean,2)
        self.SD.text = round(stdev,2)
               
    
        self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
        self.plot_1.data = Scatter
        
        t = app_tables.charts.get(chartid = chartid)
        t['StartDate'] = self.date_picker_1.date
        t['EndDate'] = self.date_picker_2.date
      #     print(columnname )
    #     self.plot_1.layout.title = columnname + " "  +  " created at " + datetime.now().strftime('%d %B %c %Y %H:%M')
    #     print(self.plot_1.layout.title)
        pass
