import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.graph_objects as go

def outofcontrol6fall(df, pointdate, pointname, total_rows, pointmean, sd, showmeans , tablename, chartid  ):
  import pandas as pd


  print()
  print ('Find six points falling in succession')
  print ('-------------------------------------------')
  print()
  t = app_tables.charts.get(chartid = chartid)
        
  chartname = t['Chart_Name']

  outofcontrol6fall = pd.DataFrame() 
  for i in range(6,total_rows):
      countx = 0
      if (df[pointname].iloc[i]  < df[pointname].iloc[i-1]):
              countx = 1
#               print(df[pointname].iloc[i], i, countx)
      if (df[pointname].iloc[i-1]  < df[pointname].iloc[i-2]):
              countx = countx + 1
#               print(df[pointname].iloc[i-1], i-1, countx)
      if (df[pointname].iloc[i-2]  < df[pointname].iloc[i-3]):
              countx = countx + 1
#               print(df[pointname].iloc[i-2],i-2, countx)
      if (df[pointname].iloc[i-3]  < df[pointname].iloc[i-4] ):
              countx = countx + 1
#               print(df[pointname].iloc[i-3], i-3, countx)
      if (df[pointname].iloc[i-4]  < df[pointname].iloc[i - 5]):
              countx = countx + 1
#               print(df[pointname].iloc[i-4], i-4, countx)
      if (df[pointname].iloc[i - 5]  < df[pointname].iloc[i-6] ):
              countx = countx + 1
#               print(df[pointname].iloc[i-5], i-5, countx)
#       if (df[pointname].iloc[i - 6]  < df[pointname].iloc[i-7] ):
#                        countx = countx + 1
      
      if countx == 6:
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
#               print('countx',countx)
              
              
              stagemean = (df[pointname].iloc[i - 5] + df[pointname].iloc[i-4] + df[pointname].iloc[i-3] + df[pointname].iloc[i-2] + df[pointname].iloc[i])/6
              stagemeandict = pd.DataFrame() 
              stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i-5],pointmean:stagemean}, ignore_index=True)
              stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i-4],pointmean:stagemean}, ignore_index=True)
              stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i-3],pointmean:stagemean}, ignore_index=True)
              stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i-2],pointmean:stagemean}, ignore_index=True)
              stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i-1],pointmean:stagemean}, ignore_index=True)
              stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i],pointmean:stagemean}, ignore_index=True)
              print ('stagemeandict',stagemeandict)

              countx = 0
              Mean6fall =outofcontrol6fall[pointname].mean()
              outofcontrol6fall['Mean6fall'] = Mean6fall  
#               print('outofcontrol6fall',outofcontrol6fall)
              print(' 6 falling' ,tablename,' at', (df[pointdate].iloc[i].strftime("%b %d, %Y")), 'with New Mean=',round(Mean6fall,0))
                        
              row = app_tables.changes.get(
                    change_type="6 falling",
                    chartid = chartid,
                    change_date= df[pointdate].iloc[i])

              if not row:
                    row = app_tables.changes.add_row(
                          change_type="6 falling",
                          chartid = chartid,
                          change_date= df[pointdate].iloc[i],
                          new_mean=df[pointname].iloc[i],
                          short_date = df[pointdate].iloc[i].date(),
                          chartname=chartname
                    )

  if outofcontrol6fall.empty:
        down6 = go.Scatter(
        visible='legendonly')
        mean6fallline  = go.Scatter(
        visible='legendonly',
        name='New Mean')

  else:
        down6 = go.Scatter(  # x=df[pointdate],
        # y=df[pointname],
        x=outofcontrol6fall[pointdate],
        y=outofcontrol6fall[pointname],
        mode='markers',
        name='6 falling in sucession',
        marker=dict(
                          color='red',
            size=2,
            line=dict(
                color='green',
                width=8
            ))
    )
        mean6fallline = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=stagemeandict[pointdate],
            y=stagemeandict[pointmean],
                      mode='lines',
                      name='New Mean from 6 falling =' + str(round(Mean6fall, 1)),
                      marker=dict(
                          color='green',
                          size=7,
                          line=dict(
                              color='black',
                              width=2
                ))
                               )
#   if outofcontrol6fall.empty:
#       print('Empty')
         
  return down6, mean6fallline 

