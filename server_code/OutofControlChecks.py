import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.graph_objects as go

def outofcontrol1above(df, pointdate, pointname, total_rows, pointmean, sd ):
        import pandas as pd

        print()
        print ('Find 1 above 3 sd')
        print ('-------------------------------------------')
        print()

        outofcontrol1above = pd.DataFrame()
        for i in range(0,total_rows):
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

def outofcontrol1below(df, pointdate, pointname, total_rows, pointmean, sd ):
        import pandas as pd
        print()
        print ('Find 1 below 3 sd')
        print ('-------------------------------------------')
        print()

        outofcontrol1below = pd.DataFrame()
        for i in range(0,total_rows):
            countx = 0
            if (df[pointname].iloc[i]  < ( pointmean - (3 * sd) )):
                countx = 1

            if countx == 1:
                   outofcontrol1below = outofcontrol1below.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)

        if outofcontrol1below.empty:
            print('Empty')


        return outofcontrol1below

# def outofcontrol9above(df, pointdate, pointname, total_rows, pointmean, sd ):

#             import pandas as pd

#             print()
#             print ('Nine or more Points on high side of the mean')
#             print ('-------------------------------------------')
#             print()
#             print(df)

#             outofcontrol9above = pd.DataFrame() 
#             for i in range(8,total_rows):
#                 countx = 0
#                 print('point=', df[pointname].iloc[i])
#                 if (df[pointname].iloc[i]  > (pointmean)):
#                     countx = 1
                    
#                 if (df[pointname].iloc[i-1]  > (pointmean)):
#                         countx = countx + 1
                        
#                 if (df[pointname].iloc[i-2]  > (pointmean)):
#                         countx = countx + 1
                       
#                 if (df[pointname].iloc[i-3]  > (pointmean)):
#                         countx = countx + 1
                        
#                 if (df[pointname].iloc[i-4]  > (pointmean)):
#                         countx = countx + 1

#                 if (df[pointname].iloc[i - 5]  > (pointmean)):
#                         countx = countx + 1
                      
#                 if (df[pointname].iloc[i-6]  > (pointmean)):
#                         countx = countx + 1
                       
#                 if (df[pointname].iloc[i-7]  > (pointmean)):
#                         countx = countx + 1
                   
#                 if (df[pointname].iloc[i-8]  > (pointmean)):
#                         countx = countx + 1

#                 if countx == 9:
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-8],pointname:df[pointname].iloc[i-8]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-7],pointname:df[pointname].iloc[i-7]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-6],pointname:df[pointname].iloc[i-6]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
#                         outofcontrol9above = outofcontrol9above.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
#                         countx = 0
#             print('outofcontrol9above',outofcontrol9above)

#             if outofcontrol9above.empty:
#                     nineabove = go.Scatter(
#                     visible='legendonly',
#                     name='9 consecutively above mean')
#             else:
#                 nineabove = go.Scatter(
#                     x=outofcontrol9above[pointdate],
#                     y=outofcontrol9above[pointname],
#                     mode='markers',
#                     name='9 consecutively above mean',
#                     marker=dict(
#                         color='red',
#                         size=5,
#                         line=dict(
#                             color='orange',
#                             width=8
#                         ))
#                 ) 
#             return  nineabove

        

# def outofcontrol9below(df, pointdate, pointname, total_rows, pointmean, sd ):

#             import pandas as pd

#             print()
#             print ('Nine or more Points on low side of the mean')
#             print ('-------------------------------------------')
#             print()
#             print(df)
#             print('pointmean=',pointmean)
#             print('total_rows=', total_rows)
#             outofcontrol9below = pd.DataFrame()
#             for i in range(8,total_rows):
#                 countx = 0
#                 print(df[pointname].iloc[i],i)
#                 if (df[pointname].iloc[i]  < (pointmean)):
#                     countx = 1
                   
#                 if (df[pointname].iloc[i-1]  < (pointmean)):
#                         countx = countx + 1
                       
#                 if (df[pointname].iloc[i-2]  < (pointmean)):
#                         countx = countx + 1
                       
#                 if (df[pointname].iloc[i-3]  < (pointmean)):
#                         countx = countx + 1
                        
#                 if (df[pointname].iloc[i-4]  < (pointmean)):
#                         countx = countx + 1

#                 if (df[pointname].iloc[i - 5]  < (pointmean)):
#                         countx = countx + 1
                   
#                 if (df[pointname].iloc[i-6]  < (pointmean)):
#                         countx = countx + 1
                        
#                 if (df[pointname].iloc[i-7]  < (pointmean)):
#                         countx = countx + 1
                        
#                 if (df[pointname].iloc[i-8]  < (pointmean)):
#                         countx = countx + 1
#                 print ('countx=',countx)
                 
                
#                 if countx == 9:

#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-8],pointname:df[pointname].iloc[i-8]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-7],pointname:df[pointname].iloc[i-7]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-6],pointname:df[pointname].iloc[i-6]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
#                         outofcontrol9below = outofcontrol9below.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
# #                         Mean9below =outofcontrol9below[pointname].mean()
# #                         outofcontrol9below['Mean9below'] = Mean9below
# #                         print ('outofcontrol9below', outofcontrol9below)                                              
#                         countx = 0

#             if not outofcontrol9below.empty: 
#                 #Filter out  below (9 below mean)
#                 outofcontrol9belowfilter =  outofcontrol9below[pointname] < (pointmean)
#                 outofcontrol9below =  outofcontrol9below[outofcontrol9belowfilter] 
#                 print('outofcontrol9below with 9 consequtive measures below mean')
#                 Mean9below =outofcontrol9below[pointname].mean()
#                 outofcontrol9below['Mean9below'] = Mean9below
#                 print ('outofcontrol9below', outofcontrol9below)      
            
#             print('outofcontrol9below',outofcontrol9below)
            
            
            
#             if outofcontrol9below.empty:
#                     ninebelow = go.Scatter(
#                     visible='legendonly',
#                     name='9 consecutively below mean')
#                     mean9belowline = go.Scatter(
#                     visible='legendonly',
#                     name='New Mean')
#             else:
#                 ninebelow = go.Scatter(
#                     x=outofcontrol9below[pointdate],
#                     y=outofcontrol9below[pointname],
#                     mode='markers',
#                     name='9 consecutively below mean',
#                     marker=dict(
#                         color='red',
#                         size=5,
#                         line=dict(
#                             color='pink',
#                             width=8
#                         ))
#                 ) 
#                 mean9belowline = go.Scatter(  # x=df[pointdate],
#                       # y=df[pointname],
#                       x=outofcontrol9below[pointdate],
#                       y=outofcontrol9below['Mean9below'],
#                       mode='markers + lines',
#                       name='New Mean',
#                       marker=dict(
#                           color='white',
#                           size=8,
#                           line=dict(
#                               color='black',
#                               width=2
#                           )) )
#             return  ninebelow, mean9belowline
          
          
def outofcontrol6fall(df, pointdate, pointname, total_rows, pointmean, sd ):
  import pandas as pd


  print()
  print ('Find six points falling in succession')
  print ('-------------------------------------------')
  print()

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
              print('countx',countx)
              countx = 0
  print('outofcontrol6fall',outofcontrol6fall)
      
  if outofcontrol6fall.empty:
        down6 = go.Scatter(
        visible='legendonly')

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
#   if outofcontrol6fall.empty:
#       print('Empty')

  return down6

# def outofcontrol6rise(df, pointdate, pointname, total_rows, pointmean, sd ):
#             import pandas as pd


#             print()
#             print ('Find six points rising in succession')
#             print ('-------------------------------------------')
#             print()
            
#             outofcontrol6rise = pd.DataFrame() 
#             for i in range(6,total_rows):
#                 countx = 0
#                 if (df[pointname].iloc[i]  > df[pointname].iloc[i-1]):
#                         countx = 1
# #                         print(df[pointname].iloc[i],df[pointdate].iloc[i],i,countx)
#                 if (df[pointname].iloc[i-1]  > df[pointname].iloc[i-2]):
#                         countx = countx + 1
# #                         print(df[pointname].iloc[i-1],df[pointdate].iloc[i-1], i-1, countx)
#                 if (df[pointname].iloc[i-2]  > df[pointname].iloc[i-3]):
#                         countx = countx + 1
# #                         print(df[pointname].iloc[i-2],df[pointdate].iloc[i-2],i-2, countx)
#                 if (df[pointname].iloc[i-3]  > df[pointname].iloc[i-4] ):
#                         countx = countx + 1
# #                         print(df[pointname].iloc[i-3],df[pointdate].iloc[i-3], i-3, countx)
#                 if (df[pointname].iloc[i-4]  > df[pointname].iloc[i - 5]):
#                         countx = countx + 1
# #                         print(df[pointname].iloc[i-4],df[pointdate].iloc[i-4], i-4,countx)
#                 if (df[pointname].iloc[i - 5]  > df[pointname].iloc[i-6] ):
#                         countx = countx + 1
# #                         print(df[pointname].iloc[i-5],df[pointdate].iloc[i-5], i-5, countx)    
# #                 print('countx', countx)
#                 if countx == 6:
#                         outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
#                         outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
#                         outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
#                         outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
#                         outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
#                         outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
#                         print('outofcontrol6rise', outofcontrol6rise)
#                         countx =0
#                         Mean6rise =outofcontrol6rise[pointname].mean()
#                         outofcontrol6rise['Mean6rise'] = Mean6rise
#                         print ('outofcontrol6rise', outofcontrol6rise)
#                         print('countx', countx)

#             if outofcontrol6rise.empty:
#                 up6 = go.Scatter(
#                     visible='legendonly')
#                 mean6riseline = go.Scatter(
#                 visible='legendonly',
#                 name='New Mean')
#             else:
#                 up6 = go.Scatter(  # x=df[pointdate],
#                     # y=df[pointname],
#                     x=outofcontrol6rise[pointdate],
#                     y=outofcontrol6rise[pointname],
#                     mode='markers',
#                     name='6 rising in sucession',
#                     marker=dict(
#                         color='red',
#                         size=2,
#                         line=dict(
#                             color='olive',
#                             width=8
        
#                         ))
#                 )
#                 mean6riseline = go.Scatter(  # x=df[pointdate],
#                       # y=df[pointname],
#                       x=outofcontrol6rise[pointdate],
#                       y=outofcontrol6rise['Mean6rise'],
#                       mode='lines',
#                       name='New Mean',
#                       marker=dict(
#                           color='white',
#                           size=8,
#                           line=dict(
#                               color='black',
#                               width=2
#                           )) )
#             return up6, mean6riseline
        


def outofcontrol23above(df, pointdate, pointname, total_rows, pointmean, sd ):

        import pandas as pd

        print()
        print ('Find 2 out 3 above 2 sd')
        print ('-------------------------------------------')
        print()

        outofcontrol23above = pd.DataFrame()
        for i in range(2,total_rows):
            countx = 0
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

        if not outofcontrol23above.empty: 
                #Filter out Orders below (2 * sd + pointmean)
                outofcontrol23abovefilter =  outofcontrol23above[pointname] > (2 * sd + pointmean)
                outofcontrol23above =  outofcontrol23above[outofcontrol23abovefilter] 
                print('outofcontrol23above with orders below 2 * SD filtered out')

        if outofcontrol23above.empty:
             two3above = go.Scatter(
             visible='legendonly',
             name='2 out 3 above 2 X SD')

        else:
            two3above = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol23above[pointdate],
            y=outofcontrol23above[pointname],
            mode='markers',
            name='2 out 3 above 2 X SD',
            marker=dict(
                color='yellow',
                size=2,
                line=dict(
                    color='yellow',
                    width=8
                ))
        )        
        return two3above

    
def outofcontrol23below(df, pointdate, pointname, total_rows, pointmean, sd ):
        import pandas as pd   

        print()
        print ('Find 2 out 3 above 2 sd')
        print ('-------------------------------------------')
        print()
        outofcontrol23below = pd.DataFrame()
        for i in range(2,total_rows):
            countx = 0
            if (df[pointname].iloc[i]  < (pointmean - 2 * sd)):
                countx = 1
                #print(df[pointname].iloc[i],i)
            if (df[pointname].iloc[i-1]  < (pointmean - 2 * sd)):
                    countx = countx + 1
                    #print(df[pointname].iloc[i -1], i-1)
            if (df[pointname].iloc[i-2]  < (pointmean - 2 * sd)):
                    countx = countx + 1
                    #print(df[pointname].iloc[i - 2],1-2)
            if countx == 2:

                    outofcontrol23below = outofcontrol23below.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
                    outofcontrol23below = outofcontrol23below.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
                    outofcontrol23below = outofcontrol23below.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)

        if not outofcontrol23below.empty:  
                    #Filter out Orders above (pointmean - 2 * sd)
                    outofcontrol23belowfilter =  outofcontrol23below[pointname] < (pointmean - 2 * sd)
                    outofcontrol23below =  outofcontrol23below[outofcontrol23belowfilter] 
                    print('outofcontrol23below with orders below/below 2 * SD filtered out')

        return outofcontrol23below
def outofcontrol45above(df, pointdate, pointname, total_rows, pointmean, sd):
    import pandas as pd
    import datetime

    print()
    print('Find 4 out 5 above One sd')
    print('-------------------------------------------')
    print()
    outofcontrol45above = pd.DataFrame()
    for i in range(5, total_rows):
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
            
            mean45line = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol45above[pointdate],
            y=outofcontrol45above['Mean45'],
            mode='lines',
            name='New Mean',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='orange',
                    width=8
                ))
                               )
        #print (outofcontrol45above)
    return four5above,mean45line


def outofcontrol45below(df, pointdate, pointname, total_rows, pointmean, sd):
    import pandas as pd
    import datetime
    # Find 4 out of 5 below exceeding one sd
    print()
    print('Find 4 out 5 below 1 sd')
    print('-------------------------------------------')
    print()
    outofcontrol45below = pd.DataFrame()
    for i in range(6, total_rows):
        countx = 0
        if (df[pointname].iloc[i] < (pointmean - sd)):
            countx = 1
            # print(df[pointname].iloc[i],i)
        if (df[pointname].iloc[i-1] < (pointmean - sd)):
            countx = countx + 1
            #print(df[pointname].iloc[i -1], i-1)
        if (df[pointname].iloc[i-2] < (pointmean - sd)):
            countx = countx + 1
            #print(df[pointname].iloc[i - 2],1-2)
        if (df[pointname].iloc[i-3] < (pointmean - sd)):
            countx = countx + 1
            #print(df[pointname].iloc[i -1], i-1)
        if (df[pointname].iloc[i-4] < (pointmean - sd)):
            countx = countx + 1
            #print(df[pointname].iloc[i -1], i-1)

        if countx == 4:

            outofcontrol45below = outofcontrol45below.append({pointdate: df[pointdate].iloc[i-4], pointname: df[pointname].iloc[i-4]}, ignore_index=True)
            outofcontrol45below = outofcontrol45below.append({pointdate: df[pointdate].iloc[i-3], pointname: df[pointname].iloc[i-3]}, ignore_index=True)
            outofcontrol45below = outofcontrol45below.append({pointdate: df[pointdate].iloc[i - 2], pointname: df[pointname].iloc[i - 2]}, ignore_index=True)
            outofcontrol45below = outofcontrol45below.append({pointdate: df[pointdate].iloc[i-1], pointname: df[pointname].iloc[i-1]}, ignore_index=True)
            outofcontrol45below = outofcontrol45below.append({pointdate: df[pointdate].iloc[i], pointname: df[pointname].iloc[i]}, ignore_index=True)

        if not outofcontrol45below.empty:
            # Filter out Orders below (pointmean - sd)
            outofcontrol45belowfilter = outofcontrol45below[pointname] < (pointmean - sd)
            outofcontrol45below = outofcontrol45below[outofcontrol45belowfilter]
            print()
            print('outofcontrol45below with orders below one SD filtered out')
            print('-------------------------------------------')
            print()
            #print (outofcontrol45below)
        else:
            print('Empty')

    return outofcontrol45below