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
            print('Empty')

        return outofcontrol1above

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

def outofcontrol9above(df, pointdate, pointname, total_rows, pointmean, sd ):

            import pandas as pd

            print()
            print ('Nine or more Points on high side of the mean')
            print ('-------------------------------------------')
            print()


            outofcontrol9above = pd.DataFrame() 
            for i in range(8,total_rows):
                countx = 0
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
            print()

            if outofcontrol9above.empty:
                print('Empty')
               
            return outofcontrol9above

        

def outofcontrol9below(df, pointdate, pointname, total_rows, pointmean, sd ):

            import pandas as pd

            print()
            print ('Nine or more Points on low side of the mean')
            print ('-------------------------------------------')
            print()
            
            outofcontrol9below = pd.DataFrame()
            for i in range(8,total_rows):
                countx = 0
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
                #print (countx)       
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
                                                                     

            if outofcontrol9below.empty:
                print('Empty')

            return outofcontrol9below
          
          
def outofcontrol6fall(df, pointdate, pointname, total_rows, pointmean, sd ):
  import pandas as pd


  print()
  print ('Find six points falling in succession')
  print ('-------------------------------------------')
  print()

  outofcontrol6fall = pd.DataFrame() 
  for i in range(5,total_rows):
      countx = 0
      if (df[pointname].iloc[i]  < df[pointname].iloc[i-1]):
              countx = 1
              print(df[pointname].iloc[i], i, countx)
      if (df[pointname].iloc[i-1]  < df[pointname].iloc[i-2]):
              countx = countx + 1
              print(df[pointname].iloc[i-1], i-1, countx)
      if (df[pointname].iloc[i-2]  < df[pointname].iloc[i-3]):
              countx = countx + 1
              print(df[pointname].iloc[i-2],i-2, countx)
      if (df[pointname].iloc[i-3]  < df[pointname].iloc[i-4] ):
              countx = countx + 1
              print(df[pointname].iloc[i-3], i-3, countx)
      if (df[pointname].iloc[i-4]  < df[pointname].iloc[i - 5]):
              countx = countx + 1
              print(df[pointname].iloc[i-4], i-4, countx)
      if (df[pointname].iloc[i - 5]  < df[pointname].iloc[i-6] ):
              countx = countx + 1
              print(df[pointname].iloc[i-5], i-5, countx)
##                if (df[pointname].iloc[i - 6]  < df[pointname].iloc[i-7] ):
##                        countx = countx + 1
      print(countx)
      if countx == 6:
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
              outofcontrol6fall = outofcontrol6fall.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
  

  if outofcontrol6fall.empty:
      print('Empty')

  return outofcontrol6fall

def outofcontrol6rise(df, pointdate, pointname, total_rows, pointmean, sd ):
            import pandas as pd


            print()
            print ('Find six points rising in succession')
            print ('-------------------------------------------')
            print()
            
            outofcontrol6rise = pd.DataFrame() 
            for i in range(5,total_rows):
                countx = 0
                if (df[pointname].iloc[i]  > df[pointname].iloc[i-1]):
                        countx = 1
                        print(df[pointname].iloc[i],df[pointdate].iloc[i],i,countx)
                if (df[pointname].iloc[i-1]  > df[pointname].iloc[i-2]):
                        countx = countx + 1
                        print(df[pointname].iloc[i-1],df[pointdate].iloc[i-1], i-1, countx)
                if (df[pointname].iloc[i-2]  > df[pointname].iloc[i-3]):
                        countx = countx + 1
                        print(df[pointname].iloc[i-2],df[pointdate].iloc[i-2],i-2, countx)
                if (df[pointname].iloc[i-3]  > df[pointname].iloc[i-4] ):
                        countx = countx + 1
                        print(df[pointname].iloc[i-3],df[pointdate].iloc[i-3], i-3, countx)
                if (df[pointname].iloc[i-4]  > df[pointname].iloc[i - 5]):
                        countx = countx + 1
                        print(df[pointname].iloc[i-4],df[pointdate].iloc[i-4], i-4,countx)
                if (df[pointname].iloc[i - 5]  > df[pointname].iloc[i-6] ):
                        countx = countx + 1
                        print(df[pointname].iloc[i-5],df[pointdate].iloc[i-5], i-5, countx)       
                if countx == 6:
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-5],pointname:df[pointname].iloc[i-5]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-4],pointname:df[pointname].iloc[i-4]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-3],pointname:df[pointname].iloc[i-3]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-2],pointname:df[pointname].iloc[i-2]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i-1],pointname:df[pointname].iloc[i-1]}, ignore_index=True)
                        outofcontrol6rise = outofcontrol6rise.append({pointdate: df[pointdate].iloc[i],pointname:df[pointname].iloc[i]}, ignore_index=True)
            

            if outofcontrol6rise.empty:
                print('Empty')

            return outofcontrol6rise


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
