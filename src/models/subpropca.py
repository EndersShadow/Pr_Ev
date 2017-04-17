#Comparable Analysis: Subject Property
from src.common.database import Database

class SPCA(object):
    def __init__(self, contprice,
                 rent,
                 dom,
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
        self.contprice = contprice
        self.rent = rent
        self.dom = dom
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
        Database.insert(collection= 'subpropca', data = self.json())

    def json(self):
        return {
            "Contract Price": self.contprice,
            "Rent": self.rent,
            "DOM": self.dom,
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
        subpropca_data = Database.find_one(collection='subpropca',
                                      query={'_id:id]'})
        return cls(**subpropca_data)

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='subpropca',
                                 query={'_id': id})