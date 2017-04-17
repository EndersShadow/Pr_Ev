#Comparable Analysis: Rent comparable.
from src.common.database import Database

class ARVSold(object):
    def __init__(self, rent,
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
        self.rent = rent
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
        Database.insert(collection= 'rentca', data = self.json())

    def json(self):
        return {
            "Rent": self.rent,
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
        rentca_data = Database.find_one(collection='rentca',
                                      query={'_id:id]'})
        return cls(**rentca_data)

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='rentca',
                                 query={'_id': id})