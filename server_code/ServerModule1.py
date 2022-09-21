import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

def connect():
  connection = pymysql.connect(host='51.141.236.29',
                               port=3306,
                               user='CRMReadOnly',
                               password=anvil.secrets.get_secret('CrM'),
                               database = 'infoathand',
                               cursorclass=pymysql.cursors.DictCursor)
  return connection

@anvil.server.callable
def get_Sales_Existing_and_New():
  conn = connect()
  with conn.cursor() as cur:
    cur.execute(
"Select Date_Format(invoice.date_entered, '%01/%m/%Y') As YM \
      , Sum(invoice.amount_usdollar) As \
       NewandExisting_Invoice_total \
From invoice Inner Join \
  invoice_cstm On invoice_cstm.id_c = invoice.id Inner Join \
  accounts On invoice.shipping_account_id = accounts.id \
Where (invoice_cstm.newexistingormaintenance_c = 'New') Or \
  (invoice_cstm.newexistingormaintenance_c = 'Existing') \
Group By YM \
Order By YM")  
    
    return cur.fetchall()

  
