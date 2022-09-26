import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server

def plotAllandRangepoints(df, date_col, name_col):
    # #import plotly.plotly as py
    import plotly.graph_objs as go

    allpoints = go.Scatter(x=df[date_col],
                           y=df[name_col],
                           mode='markers+lines',
                           name='All Points',
                           visible = True,
                           # yxis ='y0',
                           # yxis0  = dict(title='No. of Arriving Calls',overlaying='y',side='left'),
                           line=dict(color='firebrick', width=1)
                           )

    rangepoints = go.Scatter(x=df[date_col],
                             y=df['Range'],
                             mode='markers+lines',
                             name='Ranges',
                             visible=False,
                             line=dict(color='blue', width=1,
                             dash='dot')
                             )
    move8points = go.Scatter(x=df[date_col],
                               y=df['Mov_avg8'],
                               mode='lines',
                               name='Moving8Avg',
                               visible=False,
                               line=dict(color='green', width=2)
                              )


    rangecusum = go.Scatter(x=df[date_col],
                                  y=df['Range_Cusum'],
                                  mode='lines',
                                  name='Range_Cusum',
                                  visible=False,
                                  line=dict(color='darkcyan', width=2)
                                  )
    seriescusum = go.Scatter(x=df[date_col],
                                y=df['Series_Cusum'],
                                mode='lines',
                                name='Series_Cusum',
                                visible=False,
                                line=dict(color='blue', width=2),
                                yaxis = 'y2',
                                # y2  = dict(title='No. of Arriving Calls Cusum',overlaying='y',side='right')
                                )




    return allpoints, rangepoints, move8points, rangecusum, seriescusum



def plotoutofcontrol9(pointdate, pointname, outofcontrol9above1, outofcontrol9below1):
    # #import plotly.plotly as py
    import plotly.graph_objs as go

    if outofcontrol9above1.empty:
        nineabove = go.Scatter(
            visible='legendonly',
            name='9 consecutively below mean')
    else:
        nineabove = go.Scatter(
            x=outofcontrol9above1[pointdate],
            y=outofcontrol9above1[pointname],
            mode='markers',
            name='9 consecutively above mean',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='powderblue',
                    width=8
                ))
        )

    if outofcontrol9below1.empty:
        ninebelow = go.Scatter(
            visible='legendonly',
            name='9 consecutively below mean')
    else:
        ninebelow = go.Scatter(
            x=outofcontrol9below1[pointdate],
            y=outofcontrol9below1[pointname],
            mode='markers',
            name='9 consecutively below mean',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='pink',
                    width=8
                ))
        )
    return nineabove, ninebelow


def plotoutofcontrol45(pointdate, pointname, outofcontrol45above1, outofcontrol45below1):

    # #import plotly.plotly as py
    import plotly.graph_objs as go

    if outofcontrol45above1.empty:
        four5above = go.Scatter(
            visible='legendonly',
            name='4 out 5 above SD')
    else:
        four5above = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol45above1[pointdate],
            y=outofcontrol45above1[pointname],
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
    if outofcontrol45below1.empty:
        four5below = go.Scatter(
            visible='legendonly',
            name='4 out 5 above SD')
    else:
        four5below = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol45below1[pointdate],
            y=outofcontrol45below1[pointname],
            mode='markers',
            name='4 out 5 below lower one SD',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='orange',
                    width=8
                ))
        )
    return four5above, four5below


def plotoutofcontrol23(pointdate, pointname, outofcontrol23above1, outofcontrol23below1):

    # #import plotly.plotly as py
    import plotly.graph_objs as go

    if outofcontrol23above1.empty:
        two3above = go.Scatter(
            visible='legendonly')

    else:
        two3above = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol23above1[pointdate],
            y=outofcontrol23above1[pointname],
            mode='markers',
            name='2 out 3 above 2 X SD',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='yellow',
                    width=8
                ))
        )

    if outofcontrol23below1.empty:
        two3below = go.Scatter(
            visible='legendonly')

    else:
        two3below = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol23below1[pointdate],
            y=outofcontrol23below1[pointname],
            mode='markers',
            name='2 out 3 below 2 X SD',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='yellow',
                    width=8
                ))
        )
    return two3above, two3below


def plotoutofcontrol1(pointdate, pointname, outofcontrol1above1, outofcontrol1below1):

    # #import plotly.plotly as py
    import plotly.graph_objs as go

    if outofcontrol1below1.empty:
        onebelow3 = go.Scatter(
            visible='legendonly',
            name='One below 3 X SD')
    else:
        onebelow3 = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol1below1[pointdate],
            y=outofcontrol1below1[pointname],
            mode='markers',
            name='One below 3 X SD',
            marker=dict(
                                 color='red',
                                 size=2,
                                 line=dict(
                                     color='red',
                                     width=8
                                 ))
        )

    if outofcontrol1above1.empty:
        oneabove3 = go.Scatter(
            visible='legendonly',
            name='One above 3 X SD')
    else:
        oneabove3 = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol1above1[pointdate],
            y=outofcontrol1above1[pointname],
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
    return oneabove3, onebelow3


def plotoutofcontroltrend(pointdate, pointname, outofcontrol6fall1, outofcontrol6rise1):

    # #import plotly.plotly as py
    import plotly.graph_objs as go

    if outofcontrol6fall1.empty:
        down6 = go.Scatter(
            visible='legendonly')

    else:
        down6 = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol6fall1[pointdate],
            y=outofcontrol6fall1[pointname],
            mode='markers',
            name='6 rising in sucession',
            marker=dict(
                             color='red',
                size=2,
                line=dict(
                    color='lavender',
                    width=8
                ))
        )
    if outofcontrol6rise1.empty:
        up6 = go.Scatter(
            visible='legendonly')

    else:
        up6 = go.Scatter(  # x=df[pointdate],
            # y=df[pointname],
            x=outofcontrol6rise1[pointdate],
            y=outofcontrol6rise1[pointname],
            mode='markers',
            name='6 falling in sucession',
            marker=dict(
                color='red',
                size=2,
                line=dict(
                    color='olive',
                    width=8

                ))
        )
    return down6, up6
