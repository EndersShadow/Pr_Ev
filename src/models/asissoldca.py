#Comparable Analysis: As is Sold comparable.
from src.common.database import Database

class AsIsSold(object):
    def __init__(self, soldprice,
                 dateofsale,
                 mls,
                 totalsqft,
                 cstsqft,
                 dinrm,
                 fmlyrm,
                 bathrm,
                 fireplc,
                 aircond,
                 age,
                 patiodck,
                 garcrpt,
                 lotsize,
                 comments):
        self.soldprice = soldprice
        self.dateofsale = dateofsale
        self.mls = mls
        self.totalsqft = totalsqft
        self.cstsqft = cstsqft
        self.dinrm = dinrm
        self.fmlyrm = fmlyrm
        self.bathrm = bathrm
        self.fireplc = fireplc
        self.aircond = aircond
        self.age = age
        self.patiodck = patiodck
        self.garcrpt = garcrpt
        self.lotsize = lotsize
        self.comments = comments

    def save_to_mongo(self):
        Database.insert(collection= 'asissoldca', data = self.json())

    def json(self):
        return {
            "Sold Price": self.soldprice,
            "Date of Sale": self.dateofsale,
            "MLS": self.mls,
            "Total Sq Ft": self.totalsqft,
            "Cost Sq Ft": self.cstsqft,
            "Dinning Room": self.dinrm,
            "Family Room": self.fmlyrm,
            "Bathroom": self.bathrm,
            "Fireplace": self.fireplc,
            "Air Conditioner": self.aircond,
            "Age": self.age,
            "Patio Deck": self.patiodck,
            "Gar CRPT": self.garcrpt,
            "Lot Size": self.lotsize,
            "Comments": self.comments
        }

    @classmethod
    def from_mongo(cls, id):
        asissoldca_data = Database.find_one(collection='asissoldca',
                                      query={'_id:id]'})
        return cls(**asissoldca_data)

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='asissoldca',
                                 query={'_id': id})