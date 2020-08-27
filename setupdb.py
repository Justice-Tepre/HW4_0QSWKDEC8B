from app import db, CountryReport

db.create_all()

Ghana = CountryReport("Ghana",256,135,2000,32)
Togo = CountryReport("Togo",300,130,21,32)
Algeria = CountryReport("Algeria",342,124,57,24)
Spain = CountryReport("Spain",23141,1234,35,3436)
Italy = CountryReport("Italy",8436,3256,1234,63)


db.session.add_all([Ghana, Togo, Algeria, Spain, Italy])

db.session.commit()

firstcountry =CountryReport.query.get(1)
db.session.delete(firstcountry)
db.session.commit()
