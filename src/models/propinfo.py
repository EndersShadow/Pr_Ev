import datetime
import uuid

from src.common.database import Database


class Prop(object):
    def __init__(self,
                 propaddr,
                 streetnum,
                 streetname,
                 zip,
                 city,
                 state,
                 purchprice,
                 owner,
                 attorney,
                 taxid,
                 listagent,
                 buyersagent,
                 annproptax,
                 anninsur,
                 lender,
                 created_date=datetime.datetime.now(), _id=None):
        self.propaddr = propaddr
        self.streetnum = streetnum
        self.streetnam = streetname
        self.zip = zip
        self.city = city
        self.state = state
        self.purchprice = purchprice
        self.owner = owner
        self.attorney = attorney
        self.taxid = taxid
        self.listagent = listagent
        self.buyersagent = buyersagent
        self.annproptax = annproptax
        self.anninsur = anninsur
        self.lender  = lender
        self.created_date = created_date
        self._id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection= 'property', data = self.json())

    def json(self):
        return {
            "Property":[
                {
                    "Street Number":self.streetnum,
                    "Street Name":self.streetnam,
                    "Zip Code":self.zip,
                    "City":self.city
                }
            ],
            "Purchase Price": self.purchprice,
            "Owner": self.owner,
            "Attorney": self.attorney,
            "Tax ID": self.taxid,
            "List Agent": self.listagent,
            "Buyers Agent": self.buyersagent,
            "Annual Property Tax" : self.annproptax,
            "Annual Insurance": self.anninsur,
            "Lender": self.lender,
            "Creation Date": self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        prop_data = Database.find_one(collection='property',
                                      query={'_id:id]'})
        return cls(**prop_data)

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='property',
                                 query={'_id': id})

