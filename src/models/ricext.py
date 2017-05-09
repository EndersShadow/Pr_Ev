#Renovation Inspection Checklist Exterior
import datetime

from src.common.database import Database

class ricext(object):
    def __init__(self,
                 estcost,
                 esttime,
                 contractor,
                 comments,
                 shinglesandunderlay,
                 underlay,
                 gutters,
                 alumsiding,
                 vinylsiding,
                 brick,
                 other,
                 glass,
                 screens,
                 framesandsills,
                 triphazards,
                 gravel,
                 asphalt,
                 concrete,
                 backyard,
                 frontandsideyard,
                 storms,
                 entdoorsandframes,
                 frporchandstairs,
                 bckporchandstairs,
                 wooddeck,
                 garoof,
                 gasiding,
                 gagutters,
                 gadoors,
                 gawindows,
                 gafoundation,
                 gafloors,
                 gaelectric,
                 gaheating,
                 gacooling,
                 gaplumbing,
                 created_date=datetime.datetime.now()):
        self.estcost = estcost,
        self.esttime = esttime,
        self.contractor = contractor,
        self.comments = comments,
        self.shinglesandunderlay = shinglesandunderlay,
        self.underlay = underlay,
        self.gutters = gutters,
        self.alumsiding = alumsiding,
        self.vinylsiding = vinylsiding,
        self.brick = brick,
        self.other = other,
        self.glass = glass,
        self.screens = screens,
        self.framesandsills = framesandsills,
        self.triphazards = triphazards,
        self.gravel = gravel,
        self.asphalt = asphalt,
        self.concrete = concrete,
        self.backyard = backyard,
        self.frontandsideyard = frontandsideyard,
        self.storms = storms,
        self.entdoorsandframes = entdoorsandframes,
        self.frporchandstairs = frporchandstairs,
        self.bckporchandstairs = bckporchandstairs,
        self.wooddeck = wooddeck,
        self.garoof = garoof,
        self.gasiding = gasiding,
        self.gagutters = gagutters,
        self.gadoors = gadoors,
        self.gawindows = gawindows,
        self.gafoundation = gafoundation,
        self.gafloors = gafloors,
        self.gaelectric = gaelectric,
        self.gaheating = gaheating,
        self.gacooling = gacooling,
        self.gaplumbing = gaplumbing,
        self.created_date = created_date

    def save_to_mongo(self):
        Database.insert(collection='ricext', data=self.json())

    def json(self):
        return {
            "Shingles and Underlayment":[
                {
                    "Estimated Cost":self.estcost,
                    "Estimated Time":self.esttime,
                    "Contractor":self.contractor,
                    "Comments":self.comments
                }
            ],
            "Underlayment": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Missing or Damaged Gutters": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Aluminum Siding": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Vinyl Siding": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Brick": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Other": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Glass": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Screens": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Frames and Sills": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Trip Hazards": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Gravel": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Asphalt": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Concrete": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Backyard": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Front and Side Yards": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Screen Doors": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Storm Doors": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Entry Doors and Frames": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Front Porch and Stairs": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Back Porch and Stairs": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Wood Decking": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Garage Roof Siding and Gutters": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Garage Doors and Windows": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Garage Foundation and Floors": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Garage Electric": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Garage Heating": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Garage Cooling": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Garage Plumbing": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
        }
    @classmethod
    def from_mongo(cls, id):
        ricext_data = Database.find_one(collection='ricext',
                                      query={'_id:id]'})
        return cls(**ricext_data)

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='ricext',
                                 query={'_id': id})