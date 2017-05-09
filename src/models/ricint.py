#Renovation Inspection Checklist Interior
import datetime

from src.common.database import Database

class ricint(object):
    def __init__(self,
                 estcost,
                 esttime,
                 contractor,
                 comments,
                 fusescircbreak,
                 wiring,
                 switchandcov,
                 junctboxcov,
                 outletfcepltcovers,
                 waterpipes,
                 wastewaterpipes,
                 waterheater,
                 flrdrainsumppumpbsmt,
                 furnaceradiatboil,
                 ductwrkandvent,
                 filters,
                 aircond,
                 humidfrdehumidfr,
                 flooringcarpet,
                 walls,
                 ceiling,
                 bcksplash,
                 lightfix,
                 cabinets,
                 countertops,
                 sink,
                 stove,
                 refrig,
                 dishwasher,
                 disposal,
                 bedrmflrcarp,
                 bedrmwalls,
                 bedrmceiling,
                 bedrmclosets,
                 bathrmfloor,
                 bathrmwalls,
                 bathrmceiling,
                 bathrmtile,
                 bathrmcabinets,
                 bathrmcountertops,
                 bathrmmirror,
                 bathrmlightfixt,
                 bathrmtubshowerencl,
                 bathrmtoilet,
                 bathrmsinkandvanity,
                 bathrmgfi,
                 basemntstrairsandhandrail,
                 basemntwatertightfound,
                 basemntwindows,
                 basemntlightfixt,
                 basemntfinished,
                 atticinsulation,
                 atticvents,
                 created_date=datetime.datetime.now()):
        self.estcost = estcost,
        self.esttime = esttime,
        self.contractor = contractor,
        self.comments = comments,
        self.fusescircbreak = fusescircbreak,
        self.wiring = wiring,
        self.switchandcov = switchandcov,
        self.junctboxcov = junctboxcov,
        self.outletfcepltcovers = outletfcepltcovers,
        self.waterpipes = waterpipes,
        self.wastewaterpipes = wastewaterpipes,
        self.waterheater = waterheater,
        self.flrdrainsumppumpbsmt = flrdrainsumppumpbsmt,
        self.furnaceradiatboil = furnaceradiatboil,
        self.ductwrkandvent = ductwrkandvent,
        self.filters = filters,
        self.aircond = aircond,
        self.humidfrdehumidfr = humidfrdehumidfr,
        self.flooringcarpet = flooringcarpet,
        self.walls = walls,
        self.ceiling = ceiling,
        self.bcksplash = bcksplash,
        self.lightfix = lightfix,
        self.cabinets = cabinets,
        self.countertops = countertops,
        self.sink = sink,
        self.stove = stove,
        self.refrig = refrig,
        self.dishwasher = dishwasher,
        self.disposal = disposal,
        self.bedrmflrcarp = bedrmflrcarp,
        self.bedrmwalls = bedrmwalls,
        self.bedrmceiling = bedrmceiling,
        self.bedrmclosets = bedrmclosets,
        self.bathrmfloor = bathrmfloor,
        self.bathrmwalls = bathrmwalls,
        self.bathrmceiling = bathrmceiling,
        self.bathrmtile = bathrmtile,
        self.bathrmcabinets = bathrmcabinets,
        self.bathrmcountertops = bathrmcountertops,
        self.bathrmmirror = bathrmmirror,
        self.bathrmlightfixt = bathrmlightfixt,
        self.bathrmtubshowerencl = bathrmtubshowerencl,
        self.bathrmtoilet = bathrmtoilet,
        self.bathrmsinkandvanity = bathrmsinkandvanity,
        self.bathrmgfi = bathrmgfi,
        self.basemntstrairsandhandrail = basemntstrairsandhandrail,
        self.basemntwatertightfound = basemntwatertightfound,
        self.basemntwindows = basemntwindows,
        self.basemntlightfixt = basemntlightfixt,
        self.basemntfinished = basemntfinished,
        self.atticinsulation = atticinsulation,
        self.atticvents = atticvents,
        self.created_date = created_date

    def save_to_mongo(self):
        Database.insert(collection='ricint', data=self.json())

    def json(self):
        return {
            "Fuses Circuit Breakers":[
                {
                    "Estimated Cost":self.estcost,
                    "Estimated Time":self.esttime,
                    "Contractor":self.contractor,
                    "Comments":self.comments
                }
            ],
            "Wiring": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Switches and Covers": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Junction Box Covers": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Outlets and Faceplate Covers": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Water Pipes": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Waste Water Pipes": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Water Heater": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Floor Drains/Sump Pump Bsmt": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Furnace/Radiators/Boilers": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Duct Work and Vent": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Filters": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Air Conditioning": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Humidifier/Dehumidifier": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Floor Carpet": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Walls": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Ceiling": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Laundry Room Floor and Carpet": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Laundry Room Walls": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Laundry Room Ceiling": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Washer Connection": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Dryer Connection": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Laundry Tub/Sink": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Kitchen Floor": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Kitchen Walls": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Kitchen Ceiling": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Backsplash": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Light Fixtures": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Cabinets": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Countertops": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Sink": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Stove": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Refrigerator": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Dishwasher": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Disposal": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bedroom Floor/Carpet": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bedroom Ceiling": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bedroom Closets": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Floor": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Walls": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Ceiling": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Tile": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Cabinets": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Countertops": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Mirror": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Light Fixtures": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Tub/Shower Enclosure": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Toilet": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom Sink and Vanity": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Bathroom GFI": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Basement Stairs and Handrail": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Basement Watertight Foundationi": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Basement Windows": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Basement Light Fixtures": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Finished Basement": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Attic Insulation": [
                {
                    "Estimated Cost": self.estcost,
                    "Estimated Time": self.esttime,
                    "Contractor": self.contractor,
                    "Comments": self.comments
                }
            ],
            "Attic Vents": [
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
        ricint_data = Database.find_one(collection='ricint',
                                      query={'_id:id]'})
        return cls(**ricint_data)

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='ricint',
                                 query={'_id': id})