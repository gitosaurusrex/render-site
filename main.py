from flask import Flask, render_template
import os

import psycopg2

app = Flask(__name__)

###########################################
#Route
#########################################


@app.route('/')
def index():
  conn = None
  rowResults = None
  #2.
  try:
    conn = psycopg2.connect(database=os.environ['db_name'],
                            user=os.environ['db_user'],
                            password=os.environ['db_password'],
                            host=os.environ['db_host'],
                            port=os.environ['db_port'])

    cur = conn.cursor()
    order_statement = 'SELECT * FROM movies;'
    cur.execute(order_statement)
    rowResults = cur.fetchall()
    print(rowResults)
  except (Exception, psycopg2.Error) as error:
    print(error)

  finally:
    if conn is not None:
      cur.close()
      conn.close()
      print("database connection is now closed")
  return render_template('index.html', movies=rowResults)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
