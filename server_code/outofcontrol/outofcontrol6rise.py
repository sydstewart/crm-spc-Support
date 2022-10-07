import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.graph_objects as go

def outofcontrol6rise(df, pointdate, pointname, total_rows, pointmean, sd ):
            import pandas as pd


            print()
            print ('Find six points rising in succession')
            print ('-------------------------------------------')
            print()
            
            outofcontrol6rise = pd.DataFrame() 
            for i in range(6,total_rows):
                countx = 0
                if (df[pointname].iloc[i]  > df[pointname].iloc[i-1]):
                        countx = 1
#                         print(df[pointname].iloc[i],df[pointdate].iloc[i],i,countx)
                if (df[pointname].iloc[i-1]  > df[pointname].iloc[i-2]):
                        countx = countx + 1
#                         print(df[pointname].iloc[i-1],df[pointdate].iloc[i-1], i-1, countx)
                if (df[pointname].iloc[i-2]  > df[pointname].iloc[i-3]):
                        countx = countx + 1
#                         print(df[pointname].iloc[i-2],df[pointdate].iloc[i-2],i-2, countx)
                if (df[pointname].iloc[i-3]  > df[pointname].iloc[i-4] ):
                        countx = countx + 1
#                         print(df[pointname].iloc[i-3],df[pointdate].iloc[i-3], i-3, countx)
                if (df[pointname].iloc[i-4]  > df[pointname].iloc[i - 5]):
                        countx = countx + 1
#                         print(df[pointname].iloc[i-4],df[pointdate].iloc[i-4], i-4,countx)
                if (df[pointname].iloc[i - 5]  > df[pointname].iloc[i-6] ):
                        countx = countx + 1
#                         print(df[pointname].iloc[i-5],df[pointdate].iloc[i-5], i-5, countx)    
#                 print('countx', countx)
                if countx == 6:
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
                        print('outofcontrol6rise', outofcontrol6rise)
                        countx =0
                        Mean6rise =outofcontrol6rise[pointname].mean()
                        outofcontrol6rise['Mean6rise'] = Mean6rise
                        print ('outofcontrol6rise', outofcontrol6rise)
                        print('countx', countx)

            if outofcontrol6rise.empty:
                up6 = go.Scatter(
                    visible='legendonly')
                mean6riseline = go.Scatter(
                visible='legendonly',
                name='New Mean')
            else:
                up6 = go.Scatter(  # x=df[pointdate],
                    # y=df[pointname],
                    x=outofcontrol6rise[pointdate],
                    y=outofcontrol6rise[pointname],
                    mode='markers',
                    name='6 rising in sucession',
                    marker=dict(
                        color='red',
                        size=2,
                        line=dict(
                            color='olive',
                            width=8
        
                        ))
                )
                mean6riseline = go.Scatter(  # x=df[pointdate],
                      # y=df[pointname],
                      x=outofcontrol6rise[pointdate],
                      y=outofcontrol6rise['Mean6rise'],
                      mode='markers + lines',
                      name='New Mean',
                      marker=dict(
                          color='white',
                          size=5,
                          line=dict(
                              color='black',
                              width=2
                          )) )
            return up6, mean6riseline