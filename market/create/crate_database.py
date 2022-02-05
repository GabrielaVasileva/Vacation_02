from datetime import datetime, timedelta, date

from market import db

db.drop_all()
db.create_all()

from market.models import db

from market.models import User, Item, Vacation

u1=User(username='gabi',first_name='Gabriela',last_name='Vasileva',manager_id = 1, password_hash='123456', email_address='gabi@gabi.com')
u2=User(username='lily',first_name='Lili',last_name='Vasileva',manager_id = 1, password_hash='123456', email_address='lily@lily.com')
u3=User(username='koko',first_name='Koko',last_name='Vasilev',manager_id = 1, password_hash='123456', email_address='koko@koko.com')
u4=User(username='dan',first_name='Dan',last_name='Vasilev',manager_id = 1, password_hash='123456', email_address='dan@dan.com')
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.commit()


item1 = Item(name="Phone", price=500, description='Phone description', barcode='893212299897')
item2 = Item(name="Laptop", price=900, description='Laptop description', barcode='123985473165')
item3 = Item(name="Keyboard", price=150, description='Keyboard description', barcode='231985128446')

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.commit()
Item.query.all()

item1.owner = User.query.filter_by(username='gabi').first().id
db.session.add(item1)
db.session.commit()

i = Item.query.filter_by(name='Phone').first()


vacation1 = Vacation(start_date = date.today(), end_date = date.today()+ timedelta(days = 10), work_days = 7,reason = 'holiday',approved = True,comments = "fine",requester = 2)
vacation2 = Vacation(start_date = date.today()+ timedelta(days = 3), end_date = date.today()+ timedelta(days = 10), work_days = 5,reason = 'holiday',approved = True,comments = "fine",requester = 5)

db.session.add(vacation1)
db.session.add(vacation2)
db.session.commit()
Vacation.query.all()

# vacation2.requester = User.query.filter_by(username='gabi1').first().id
# db.session.add(vacation2)
# db.session.commit()



