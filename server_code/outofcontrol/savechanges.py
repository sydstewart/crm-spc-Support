import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server

@anvil.server.callable
def savechanges(tablename,lastpointdate,mean, change_type ):
            print(change_type,tablename,' at', (lastpointdate.strftime("%b %d, %Y")), 'with New Mean=',round(mean,0))
                        
            row = app_tables.changes.get(
                        change_type=change_type,
                        tablename= tablename,
                        change_date= lastpointdate,
                        new_mean=round(mean,0))
#                         chartid = chartid)
#                         print(row['change_type'])
            if not row:

                    row = app_tables.changes.add_row(
                            change_type=change_type,
                            tablename= tablename,
                            change_date= lastpointdate,
                            new_mean=round(mean,0),
                            short_date = lastpointdate.date())
#                             chartid = chartid)
