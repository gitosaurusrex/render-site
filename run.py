from flask import Flask, render_template
#1.
from config import config
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
    params = config()
    conn = psycopg2.connect(**params)
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
  return render_template('index.html', recentRecords=rowResults)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
