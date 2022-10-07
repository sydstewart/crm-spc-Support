import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.graph_objects as go

def outofcontrol9below(df, pointdate, pointname, total_rows, pointmean, sd, showmeans):

            import pandas as pd

            print()
            print ('Nine or more Points on low side of the mean')
            print ('-------------------------------------------')
            print()
            print(df)
            print('pointmean=',pointmean)
            print('total_rows=', total_rows)
            outofcontrol9below = pd.DataFrame()
            for i in range(8,total_rows):
                countx = 0
                print(df[pointname].iloc[i],i)
                if (df[pointname].iloc[i]  < (pointmean)):
                    countx = 1
                   
                if (df[pointname].iloc[i-1]  < (pointmean)):
                        countx = countx + 1
                       
                if (df[pointname].iloc[i-2]  < (pointmean)):
                        countx = countx + 1
                       
                if (df[pointname].iloc[i-3]  < (pointmean)):
                        countx = countx + 1
                        
                if (df[pointname].iloc[i-4]  < (pointmean)):
                        countx = countx + 1

                if (df[pointname].iloc[i - 5]  < (pointmean)):
                        countx = countx + 1
                   
                if (df[pointname].iloc[i-6]  < (pointmean)):
                        countx = countx + 1
                        
                if (df[pointname].iloc[i-7]  < (pointmean)):
                        countx = countx + 1
                        
                if (df[pointname].iloc[i-8]  < (pointmean)):
                        countx = countx + 1
                print ('countx=',countx)
                 
                
                if countx == 9:

                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-8],pointname:df[pointname].iloc[i-8]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-7],pointname:df[pointname].iloc[i-7]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-6],pointname:df[pointname].iloc[i-6]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
                        outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
#                         Mean9below =outofcontrol9below[pointname].mean()
#                         outofcontrol9below['Mean9below'] = Mean9below
#                         print ('outofcontrol9below', outofcontrol9below)                                              
                        countx = 0

            if not outofcontrol9below.empty: 
                #Filter out  below (9 below mean)
                outofcontrol9belowfilter =  outofcontrol9below[pointname] < (pointmean)
                outofcontrol9below =  outofcontrol9below[outofcontrol9belowfilter] 
                print('outofcontrol9below with 9 consequtive measures below mean')
                Mean9below =outofcontrol9below[pointname].mean()
                outofcontrol9below['Mean9below'] = Mean9below
                print ('outofcontrol9below', outofcontrol9below)      
            
            print('outofcontrol9below',outofcontrol9below)
            
            
            
            if outofcontrol9below.empty:  
                    ninebelow = go.Scatter(
                    visible='legendonly',
                    name='9 consecutively below mean')
                    if showmeans == False:
                        mean9belowline = go.Scatter(
                        visible='legendonly',
                        name='New Mean')
            else:
                ninebelow = go.Scatter(
                    x=outofcontrol9below[pointdate],
                    y=outofcontrol9below[pointname],
                    mode='markers',
                    name='9 consecutively below mean',
                    marker=dict(
                        color='red',
                        size=5,
                        line=dict(
                            color='pink',
                            width=8
                        ))
                ) 
                if showmeans == False:
                      mean9belowline = go.Scatter(  # x=df[pointdate],
                            # y=df[pointname],
                            x=outofcontrol9below[pointdate],
                            y=outofcontrol9below['Mean9below'],
                            mode='markers + lines',
                            name='New Mean',
                            marker=dict(
                                color='white',
                                size=5,
                                line=dict(
                                    color='black',
                                    width=2
                                )) )
            return  ninebelow, mean9belowline
