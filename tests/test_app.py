from app import home
from app import db
def test_home():
   cur = db()
   cur.execute('SELECT * FROM blog limit 1;')
   rows = cur.fetchone()
   assert home() == rows 