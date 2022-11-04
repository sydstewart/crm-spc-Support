import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.graph_objects as go


def outofcontrol23above(df, pointdate, pointname, total_rows, pointmean, sd, showmeans ):

        import pandas as pd

        print()
        print ('Find 2 out 3 above 2 sd')
        print ('-------------------------------------------')
        print()

        outofcontrol23above = pd.DataFrame()
        stagemeandict = pd.DataFrame() 
        meanline =pd.DataFrame()
#         numberfound = 0
        for i in range(2,total_rows + 1):
            countx = 0
            numberfound = 0
            if (df[pointname].iloc[i]  > (2 * sd + pointmean)):
                countx = 1
                #print(df[pointname].iloc[i],i)
            if (df[pointname].iloc[i-1]  > (2 * sd + pointmean)):
                    countx = countx + 1
                    #print(df[pointname].iloc[i -1], i-1)
            if (df[pointname].iloc[i-2]  > (2 * sd + pointmean)):
                    countx = countx + 1
                    #print(df[pointname].iloc[i - 2],1-2)
            if countx == 2:
                    outofcontrol23above = outofcontrol23above.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
                    outofcontrol23above = outofcontrol23above.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
                    outofcontrol23above = outofcontrol23above.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
                    
#                     if numberfound > 1:
#                       stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i-3],pointmean:stagemean}, ignore_index=True)
                    
                    stagemean = (df[pointname].iloc[i-2] + df[pointname].iloc[i-1] + df[pointname].iloc[i])/3
                    
                    stagemeandict  = stagemeandict.append({pointdate: df[pointdate].iloc[i-2],pointmean:stagemean}, ignore_index=True)
                    stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i-1],pointmean:stagemean}, ignore_index=True)
                    stagemeandict = stagemeandict.append({pointdate: df[pointdate].iloc[i],pointmean:stagemean}, ignore_index=True)
#                     print ('stagemeandict',stagemeandict)
                    numberfound = 1 + numberfound
        if not outofcontrol23above.empty: 
                #Filter out Orders below (2 * sd + pointmean)
#                 outofcontrol23abovefilter =  outofcontrol23above[pointname] > (2 * sd + pointmean)
#                 outofcontrol23above =  outofcontrol23above[outofcontrol23abovefilter] 
#                 print('outofcontrol23above with orders below 2 * SD filtered out')
                
                
                Mean23above =outofcontrol23above[pointname].mean()
                outofcontrol23above['Mean23above'] = Mean23above
#                 meanline = outofcontrol23above
#                 print ('outofcontrol23above', outofcontrol23above)  

        if outofcontrol23above.empty:
             two3above = go.Scatter(
             visible='legendonly',
             name='2 out 3 above 2 X SD')
#              if showmeans == False:
             mean23aboveline = go.Scatter(
             visible='legendonly',
             name='New Mean')
             stagemeandictline = go.Scatter(
             visible='legendonly',
             name='New Mean')
        else:
            two3above = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol23above[pointdate],
            y=outofcontrol23above[pointname],
            mode='markers',
            name='2 out 3 above 2 X SD',
            marker=dict(
                color='blue',
                size=2,
                line=dict(
                    color='blue',
                    width=8
                ))
        )
#             if showmeans == False:
#             mean23aboveline = go.Scatter(  # x=df[pointdate],
#                   # y=df[pointname],
#                   x=outofcontrol23above[pointdate],
#                   y=outofcontrol23above['Mean23above'],
#                   mode='lines',
#                   name='New Mean from 2 3 above='+str(round(Mean23above,1)),
#                   marker=dict(
#                       color='blue',
#                       size=7,
#                       line=dict(
#                           color='black',
#                           width=1
#                       )) )
            stagemeandictline = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=stagemeandict[pointdate],
            y=stagemeandict[pointmean],
            mode='markers',
            name='New Mean from 2 3 above',
            marker_symbol = 'line-ew',
            
#             text= str(round(pointmean,1)),
#             textposition='top left',
#             textfont=dict(
#                       family="sans serif",
#                       size=11,
#                       color="black"),
            marker=dict(
                color='green',
                size=7,
                line=dict(
                    color='green',
                    width=3
                )) )
        return two3above, stagemeandictline 


