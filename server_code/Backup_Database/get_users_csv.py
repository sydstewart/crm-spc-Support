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
def get_users_csv():
  user_csv = app_tables.users.search().to_csv()
  return user_csv
 

@anvil.server.callable
def get_charts_csv():
  charts_csv = app_tables.charts.search().to_csv()
  return charts_csv


@anvil.server.callable
def get_cases_arriving_csv():
  cases_arriving_csv = app_tables.cases_arriving.search().to_csv()
  return cases_arriving_csv