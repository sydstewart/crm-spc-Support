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
from datetime import datetime, time , date , timedelta

def outofcontrol1above(df, pointdate, pointname, total_rows, pointmean, sd, showexluded , tablename, chartid):
        import pandas as pd

        print()
        print ('Find 1 above 3 sd')
        print ('-------------------------------------------')
        print()

        t = app_tables.charts.get(chartid = chartid)
        
        chartname = t['Chart_Name']
        
        outofcontrol1above = pd.DataFrame()
        for i in range(0,total_rows +1):
            countx = 0
            if (df[pointname].iloc[i]  > ((3 * sd) + pointmean)):
                countx = 1

            if countx == 1:
                   outofcontrol1above = outofcontrol1above.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
                   print('1 above 3 sd:' ,tablename,' at', (df[pointdate].iloc[i].strftime("%b %d, %Y")))
                        
                   row = app_tables.changes.get(
                            change_type="1 above 3 sd",
                            chartid = chartid,
                            change_date= df[pointdate].iloc[i])

                   if not row:
                          row = app_tables.changes.add_row(
                                change_type="1 above 3 sd",
                                chartid = chartid,
                                change_date= df[pointdate].iloc[i],
                                new_mean=df[pointname].iloc[i],
                                short_date = df[pointdate].iloc[i].date(),
                                chartname=chartname
                          )

        if outofcontrol1above.empty:
            oneabove3 = go.Scatter(
            visible='legendonly',
            name='One above 3 X SD')
        else:
            oneabove3 = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol1above[pointdate],
            y=outofcontrol1above[pointname],
            mode='markers',
            name='1 above 3 X SD',
            marker=dict(
                                 color='red',
                                 size=2,
                                 line=dict(
                                     color='red',
                                     width=8
                                 ))
            )

        return oneabove3
