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

def outofcontrol9above(df, pointdate, pointname, total_rows, pointmean, sd, showmeans ):

            import pandas as pd

            print()
            print ('Nine or more Points on high side of the mean')
            print ('-------------------------------------------')
            print()
#             print(df)

            outofcontrol9above = pd.DataFrame() 
            for i in range(8,total_rows):
                countx = 0
#                 print('point=', df[pointname].iloc[i])
                if (df[pointname].iloc[i]  > (pointmean)):
                    countx = 1
                    
                if (df[pointname].iloc[i-1]  > (pointmean)):
                        countx = countx + 1
                        
                if (df[pointname].iloc[i-2]  > (pointmean)):
                        countx = countx + 1
                       
                if (df[pointname].iloc[i-3]  > (pointmean)):
                        countx = countx + 1
                        
                if (df[pointname].iloc[i-4]  > (pointmean)):
                        countx = countx + 1

                if (df[pointname].iloc[i - 5]  > (pointmean)):
                        countx = countx + 1
                      
                if (df[pointname].iloc[i-6]  > (pointmean)):
                        countx = countx + 1
                       
                if (df[pointname].iloc[i-7]  > (pointmean)):
                        countx = countx + 1
                   
                if (df[pointname].iloc[i-8]  > (pointmean)):
                        countx = countx + 1

                if countx == 9:
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-8],pointname:df[pointname].iloc[i-8]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-7],pointname:df[pointname].iloc[i-7]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-6],pointname:df[pointname].iloc[i-6]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
                        outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
                        countx = 0
                        Mean9above =outofcontrol9above[pointname].mean()
                        outofcontrol9above['Mean9above'] = Mean9above
#                         print('outofcontrol9above',outofcontrol9above)

            if outofcontrol9above.empty:
                    nineabove = go.Scatter(
                    visible='legendonly',
                    name='9 above mean')
#                     if showmeans == False:
                    mean9aboveline = go.Scatter(
                    visible='legendonly',
                    name='New Mean')
            else:
                
#                  if showmeans == False:
                    mean9aboveline = go.Scatter(  # x=df[pointdate],
                          # y=df[pointname],
                          x=outofcontrol9above[pointdate],
                          y=outofcontrol9above['Mean9above'],
                          mode='markers',
                          marker_symbol = 'line-ew',
                          name='New Mean 9 above',
                          
                           marker=dict(
                              color='pink',
                              size=7,
                              line=dict(
                                  color='pink',
                                  width=2
                              )) )
              
        
              
                    nineabove = go.Scatter(
                        x=outofcontrol9above[pointdate],
                        y=outofcontrol9above[pointname],
                        mode='markers',
                        name='9 in succesion above mean',
#                         marker_symbol = 'line-ew',
                        marker=dict(
                            color='pink',
                            size=7,
                            line=dict(
                                color='pink',
                                width=8
                            ))
              ) 
            return  nineabove, mean9aboveline