import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.graph_objects as go

def outofcontrol1above(df, pointdate, pointname, total_rows, pointmean, sd, showexluded ):
        import pandas as pd

        print()
        print ('Find 1 above 3 sd')
        print ('-------------------------------------------')
        print()

        outofcontrol1above = pd.DataFrame()
        for i in range(0,total_rows +1):
            countx = 0
            if (df[pointname].iloc[i]  > ((3 * sd) + pointmean)):
                countx = 1

            if countx == 1:
                   outofcontrol1above = outofcontrol1above.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)

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
            name='One above 3 X SD',
            marker=dict(
                                 color='red',
                                 size=2,
                                 line=dict(
                                     color='red',
                                     width=8
                                 ))
            )

        return oneabove3
