import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.graph_objects as go

def outofcontrol45above(df, pointdate, pointname, total_rows, pointmean, sd , showmeans):
    import pandas as pd
    import datetime

    print()
    print('Find 4 out 5 above One sd')
    print('-------------------------------------------')
    print()
    outofcontrol45above = pd.DataFrame()
    for i in range(5, total_rows + 1):
        countx = 0
        if (df[pointname].iloc[i] > (sd + pointmean)):
            countx = 1
            # print(df[pointname].iloc[i],i)
        if (df[pointname].iloc[i-1] > (sd + pointmean)):
            countx = countx + 1
            #print(df[pointname].iloc[i -1], i-1)
        if (df[pointname].iloc[i-2] > (sd + pointmean)):
            countx = countx + 1
            #print(df[pointname].iloc[i - 2],1-2)
        if (df[pointname].iloc[i-3] > (sd + pointmean)):
            countx = countx + 1
            #print(df[pointname].iloc[i -1], i-1)
        if (df[pointname].iloc[i-4] > (sd + pointmean)):
            countx = countx + 1
            #print(df[pointname].iloc[i -1], i-1)
            print('countx', i, countx)
        if countx == 4:
            outofcontrol45above = outofcontrol45above.append({pointdate: df[pointdate].iloc[i-4], pointname: df[pointname].iloc[i-4]}, ignore_index=True)
            outofcontrol45above = outofcontrol45above.append({pointdate: df[pointdate].iloc[i-3], pointname: df[pointname].iloc[i-3]}, ignore_index=True)
            outofcontrol45above = outofcontrol45above.append({pointdate: df[pointdate].iloc[i - 2], pointname: df[pointname].iloc[i - 2]}, ignore_index=True)
            outofcontrol45above = outofcontrol45above.append({pointdate: df[pointdate].iloc[i-1], pointname: df[pointname].iloc[i-1]}, ignore_index=True)
            outofcontrol45above = outofcontrol45above.append({pointdate: df[pointdate].iloc[i], pointname: df[pointname].iloc[i]}, ignore_index=True)
            countx = 0
            Mean45 =outofcontrol45above[pointname].mean()
            outofcontrol45above['Mean45'] = Mean45
            print ('outofcontrol45above', outofcontrol45above)
#     if not outofcontrol45above.empty:
#         # Filter out Orders below (sd + pointmean)
#         outofcontrol45abovefilter = outofcontrol45above[pointname] > (sd + pointmean)
#         outofcontrol45above = outofcontrol45above[outofcontrol45abovefilter]
#         print('outofcontrol45above with points below one SD filtered out')
#         print()
#         print('-------------------------------------------')
#         print()
        if outofcontrol45above.empty:
            four5above = go.Scatter(
            visible='legendonly',
            name='4 out 5 above 1SD')
#             if showmeans == False:
            mean45line = go.Scatter(
            visible='legendonly',
            name='New Mean')
      
        else:
            four5above = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol45above[pointdate],
            y=outofcontrol45above[pointname],
            mode='markers',
            name='4 out 5 above upper one SD',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='orange',
                    width=8
                ))
                          )
#             if showmeans == False:
            
            mean45line = go.Scatter(  # x=df[pointdate],
        # y=df[pointname],
                              x=outofcontrol45above[pointdate],
                              y=outofcontrol45above['Mean45'],
                                        mode='lines',
                                        name='New Mean from 45 above =' + str(round(Mean45, 1)),
                                        marker=dict(
                                            color='orange',
                                            size=7,
                                            line=dict(
                                                color='black',
                                                width=2
            ))
                          )
              #print (outofcontrol45above)
    return four5above,mean45line
