from flask import Flask, request, render_template
import os
import psycopg2
import json

# This is how you use Postgress Direct in Flask

app = Flask(__name__)

class database_postgre:
    def __init__(self):
        self.conn = psycopg2.connect("host='127.0.0.1' dbname='postgres' user='postgres' password='pass'")
        self.cur = self.conn.cursor()

    def query_sales(self):
        self.cur.execute ("select place, market, count(cust) as cust from market.shop")
        columns = ('place', 'market', 'cust')
        hasil = []
        for row in self.cur.fetchall():
            hasil.append(dict(zip(columns, row)))
        return hasil

@app.route('/')
def sales():
    def db_query():
        db = database_postgre()
        customer = db.query_sales()
        return customer
    res = db_query()
    return render_template('customer.html', result=res, content_type='application/json')

if __name__ == '__main__':
    app.run()
