import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pymysql

def connect():
  connection = pymysql.connect(host='51.141.236.29',
                               port=3306,
                               user='CRMReadOnly',
                               password=anvil.secrets.get_secret('CRM'),
                               database = 'teamwork',
                               cursorclass=pymysql.cursors.DictCursor)
  return connection

@anvil.server.callable
def listprojects():
  conn = connect()
  with conn.cursor() as cur:
    cur.execute(
#                 "Select Date_Format(invoice.date_entered, '%Y/%m/%01') As YM \
#                       , Sum(invoice.amount_usdollar) As \
#                       NewandExisting_Invoice_total \
#                 From invoice Inner Join \
#                   invoice_cstm On invoice_cstm.id_c = invoice.id Inner Join \
#                   accounts On invoice.shipping_account_id = accounts.id \
#                 Where (invoice_cstm.newexistingormaintenance_c = 'New') Or \
#                   (invoice_cstm.newexistingormaintenance_c = 'Existing') \
#                 Group By YM \
#                 Order By Date_Format(Date(invoice.date_entered), '%Y/%m')")  
                  "Select * from projects where projectStatus LIKE 'active' AND projectStartDate iS NOT NULL")
    
#     return cur.fetchall() 
  dicts = [{'Name': r['projectname'],'Start Date':r['projectStartDate'], 'End Date':r['projectEndDate'], 'Status': r['projectStatus']}
            for r in cur.fetchall()]
  return dicts