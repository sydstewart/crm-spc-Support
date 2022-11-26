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

                  "Select projects.projectname, companies.companyName as Company, projects.projectStatus, \
                  projects.projectStartDate, projects.projectEndDate,\
                  projectcategories.projectCategoryName, projects.projectCompleted,\
                  portfolioboards.boardName as boardname, portfoliocards.boardId, portfoliocolumns.columnName\
                 From projects Inner Join\
                  companies On projects.companyId = companies.companyId Inner Join \
                  projectcategories On projects.projectCategoryId = \
                    projectcategories.projectCategoryId Inner Join \
                  portfoliocards On projects.projectId = portfoliocards.projectId Inner Join \
                  portfolioboards On portfoliocards.boardId = portfolioboards.boardId Inner Join \
                  portfoliocolumns On portfoliocards.columnId = portfoliocolumns.columnId \
                  Where companies.companyName Like '4S%'")
    
#     return cur.fetchall() 
  dicts = [{'Company': r['Company'],'Name': r['projectname'],'Start Date':r['projectStartDate'], 'End Date':r['projectEndDate'], 'Status': r['projectStatus'], 'Board Name': r['boardname']}
            for r in cur.fetchall()]
  total_rows = len(dicts)
  return dicts, total_rows