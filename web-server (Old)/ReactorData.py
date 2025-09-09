import requests
from tkinter import *
from fnmatch import fnmatch


class ReactorData:
    CoreTemp: float
    CoreTempMax: float
    CoreTempOperative: float
    CoreState: str
    Critical: str
    CriticalityCounter: int
    CoreWear: float
    CoreIntegrity: float
    CorePressure: float
    CorePressureMax: float
    CorePressureOperative: float

    def __init__(self, url):
        self.label = None
        self.root = None
        self.StartButton = None
        self.PauseButton = None
        self.TimeLabel = None
        self.CoreLabel = None
        self.CoreTempLabel = None
        self.CorePressLabel = None
        self.CoreCoolantLabel = None
        self.Pump0Label = None
        self.Pump1Label = None
        self.Pump2Label = None
        self.RodsLabel = None

        self.url = url
        self.data = {}
        self.vars = [
            "TIME", "TIME_STAMP", "CORE_TEMP", "CORE_TEMP_OPERATIVE", "CORE_TEMP_MAX",
            "CORE_TEMP_MIN", "CORE_TEMP_RESIDUAL", "CORE_PRESSURE", "CORE_PRESSURE_MAX",
            "CORE_PRESSURE_OPERATIVE", "CORE_INTEGRITY", "CORE_WEAR", "CORE_STATE",
            "CORE_STATE_CRITICALITY", "CORE_CRITICAL_MASS_REACHED",
            "CORE_CRITICAL_MASS_REACHED_COUNTER", "CORE_IMMINENT_FUSION",
            "CORE_READY_FOR_START", "CORE_STEAM_PRESENT", "CORE_HIGH_STEAM_PRESENT",
            "COOLANT_CORE_STATE", "COOLANT_CORE_PRESSURE", "COOLANT_CORE_MAX_PRESSURE",
            "COOLANT_CORE_VESSEL_TEMPERATURE", "COOLANT_CORE_QUANTITY_IN_VESSEL",
            "COOLANT_CORE_PRIMARY_LOOP_LEVEL", "COOLANT_CORE_FLOW_SPEED",
            "COOLANT_CORE_FLOW_ORDERED_SPEED", "COOLANT_CORE_FLOW_REACHED_SPEED",
            "COOLANT_CORE_QUANTITY_CIRCULATION_PUMPS_PRESENT",
            "COOLANT_CORE_QUANTITY_FREIGHT_PUMPS_PRESENT",
            "COOLANT_CORE_CIRCULATION_PUMP_0_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_1_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_2_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_0_DRY_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_1_DRY_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_2_DRY_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_0_OVERLOAD_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_1_OVERLOAD_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_2_OVERLOAD_STATUS",
            "COOLANT_CORE_CIRCULATION_PUMP_0_ORDERED_SPEED",
            "COOLANT_CORE_CIRCULATION_PUMP_1_ORDERED_SPEED",
            "COOLANT_CORE_CIRCULATION_PUMP_2_ORDERED_SPEED",
            "COOLANT_CORE_CIRCULATION_PUMP_0_SPEED",
            "COOLANT_CORE_CIRCULATION_PUMP_1_SPEED",
            "COOLANT_CORE_CIRCULATION_PUMP_2_SPEED",
            "RODS_STATUS", "RODS_MOVEMENT_SPEED",
            "RODS_MOVEMENT_SPEED_DECREASED_HIGH_TEMPERATURE",
            "RODS_DEFORMED", "RODS_TEMPERATURE", "RODS_MAX_TEMPERATURE",
            "RODS_POS_ORDERED", "RODS_POS_ACTUAL", "RODS_POS_REACHED",
            "RODS_QUANTITY", "RODS_ALIGNED"
        ]
        self.translations = {
            "CORE_STATE": {
                "NOREACTIVO": "NOT_REACTIVE",
                "REACTIVO": "REACTIVE"
            },
            "CORE_STATE_CRITICALITY": {
                "SUBCRITICO": "SUBCRITICAL",
                "CRITICO": "CRITICAL"
            },
            "COOLANT_CORE_STATE": {
                "INMOVIL": "IMMOBILE",
                "CIRCULANDO": "CIRCULATING"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_0_STATUS": {
                "0": "NOT_ACTIVE",
                "1": "ACTIVE_AND_NOT_REACHED_SET_VELOCITY",
                "2": "ACTIVE_AND_REACHED_SET_VELOCITY",
                "3": "ACTIVE_AND_REQUIRES_MAINTENANCE",
                "4": "INACTIVE_OR_NOT_OPERATIONAL",
                "5": "ACTIVATION_REQUESTED_BUT_INSUFFICIENT_POWER"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_1_STATUS": {
                "0": "NOT_ACTIVE",
                "1": "ACTIVE_AND_NOT_REACHED_SET_VELOCITY",
                "2": "ACTIVE_AND_REACHED_SET_VELOCITY",
                "3": "ACTIVE_AND_REQUIRES_MAINTENANCE",
                "4": "INACTIVE_OR_NOT_OPERATIONAL",
                "5": "ACTIVATION_REQUESTED_BUT_INSUFFICIENT_POWER"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_2_STATUS": {
                "0": "NOT_ACTIVE",
                "1": "ACTIVE_AND_NOT_REACHED_SET_VELOCITY",
                "2": "ACTIVE_AND_REACHED_SET_VELOCITY",
                "3": "ACTIVE_AND_REQUIRES_MAINTENANCE",
                "4": "INACTIVE_OR_NOT_OPERATIONAL",
                "5": "ACTIVATION_REQUESTED_BUT_INSUFFICIENT_POWER"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_0_DRY_STATUS": {
                "1": "ACTIVE_AND_DRY",
                "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_1_DRY_STATUS": {
                "1": "ACTIVE_AND_DRY",
                "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_2_DRY_STATUS": {
                "1": "ACTIVE_AND_DRY",
                "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_0_OVERLOAD_STATUS": {
                "1": "ACTIVE_AND_OVERLOADED",
                "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_1_OVERLOAD_STATUS": {
                "1": "ACTIVE_AND_OVERLOADED",
                "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
            },
            "COOLANT_CORE_CIRCULATION_PUMP_2_OVERLOAD_STATUS": {
                "1": "ACTIVE_AND_OVERLOADED",
                "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
            },
            "RODS_STATUS": {
                "INMOVIL": "IMMOBILE",
                "AJUSTANDO": "ADJUSTING"
            }
        }
        self.Time = ""

        self.CoreState = ""
        # self.Critical = float()
        self.CriticalityReached = bool()
        self.CriticalityCounter = int()
        self.CoreWear = 0.0
        self.CoreIntegrity = 0.0
        self.Steam = bool()
        self.HighSteam = bool()
        self.ImminentFusion = bool()
        self.ReadyStart = bool()

        self.CoreTemp = 0.0
        self.CoreTempOperative = 0.0
        self.CoreTempMax = 0.0
        self.CoreTempMin = 0.0

        self.CorePressure = 0.0
        self.CorePressureMax = 0.0
        self.CorePressureOperative = 0.0

        self.CoreCoolant = {'State': '', 'Pressure': 0.0, 'Max Pressure': 0.0, 'Vessel Temp': 0.0, 'Quantity': 0.0, 'Primary Loop Level': 0.0, 'Flow': 0, 'Ordered Flow': 0, 'Flow Reached': '', 'Circ Pumps': 0, 'Freight Pumps': 0}
        self.Pumps = {
            'Pump0': {'Status': '', 'Flow': 0, 'Ordered Flow': 0, 'Flow Reached': bool(), 'Overload': bool(), 'Dry': bool()},
            'Pump1': {'Status': '', 'Flow': 0, 'Ordered Flow': 0, 'Flow Reached': bool(), 'Overload': bool(), 'Dry': bool()},
            'Pump2': {'Status': '', 'Flow': 0, 'Ordered Flow': 0, 'Flow Reached': bool(), 'Overload': bool(), 'Dry': bool()}
        }

        self.RodsState = ''
        self.RodsMoveSpd = 0.0
        self.RodsSpdReduced = bool()
        self.RodsDeformed = bool()
        self.RodsTemp = 0.0
        self.RodsTempMax = 0.0
        self.RodsPosActual = 0.0
        self.RodsPosOrdered = 0.0
        self.RodsPosReached = bool()
        self.RodsNum = 0
        self.RodsAligned = bool()

        self.init_display()


    def init_display(self):
        self.root = Tk()
        self.root.geometry('450x900')
        self.label = Label(self.root, text="Reactor Data\n\n\n")
        self.StartButton = Button(self.root, text="Start", command=self.display)
        self.PauseButton = Button(self.root, text="Pause", command=self.pause_display)
        self.UpdateButton = Button(self.root, text="Update", command=self.update)

        self.TimeLabel = Label(self.root)
        self.CoreLabel = Label(self.root)
        self.CoreCoolantLabel = Label(self.root)
        self.Pump0Label = Label(self.root)
        self.Pump1Label = Label(self.root)
        self.Pump2Label = Label(self.root)
        self.RodsLabel = Label(self.root)

        self.label.pack()
        self.StartButton.pack()
        self.PauseButton.pack()
        self.UpdateButton.pack()
        
        self.TimeLabel.pack()
        self.CoreLabel.pack()
        self.CoreCoolantLabel.pack()
        self.Pump0Label.pack()
        self.Pump1Label.pack()
        self.Pump2Label.pack()
        self.RodsLabel.pack()
        
        self.display()

    def pause_display(self):
        import sys
        sys.exit()

    def update(self):
        for var in self.vars:
            holder = self.get_variable(var)
            if not fnmatch(holder, "*Error*"):
                self.data[var] = self.translate_variable(var, holder)
            else:
                self.data[var] = holder

        try:
            # Core Data
            self.Time = self.data["TIME"]
            self.CoreState = self.data["CORE_STATE"]
            # self.Critical = float(self.data["CORE_STATE_CRITICALITY"])
            self.CoreWear = float(self.data["CORE_WEAR"])
            self.CoreIntegrity = float(self.data["CORE_INTEGRITY"])
            self.CriticalityCounter = int(self.data["CORE_CRITICAL_MASS_REACHED_COUNTER"])
            self.ReadyStart = True if self.data["CORE_READY_FOR_START"] == "TRUE" else False
            self.CriticalityReached = True if self.data["CORE_CRITICAL_MASS_REACHED"] == "TRUE" else False

            # Major Issues
            self.ImminentFusion = True if self.data["CORE_IMMINENT_FUSION"] == "TRUE" else False
            self.Steam = True if self.data["CORE_STEAM_PRESENT"] == "TRUE" else False
            self.HighSteam = True if self.data["CORE_HIGH_STEAM_PRESENT"] == "TRUE" else False

            # Pressure
            self.CorePressure = float(self.data["CORE_PRESSURE"])
            self.CorePressureMax = float(self.data["CORE_PRESSURE_MAX"])
            self.CorePressureOperative = float(self.data["CORE_PRESSURE_OPERATIVE"])

            # Temp
            self.CoreTemp = float(self.data["CORE_TEMP"])
            self.CoreTempMax = float(self.data["CORE_TEMP_MAX"])
            self.CoreTempMin = float(self.data["CORE_TEMP_MIN"])
            self.CoreTempOperative = float(self.data["CORE_TEMP_OPERATIVE"])

            # Core Coolant
            self.CoreCoolant['State'] = self.data["COOLANT_CORE_STATE"]
            self.CoreCoolant['Pressure'] = float(self.data["COOLANT_CORE_PRESSURE"])
            self.CoreCoolant['Max Pressure'] = float(self.data["COOLANT_CORE_MAX_PRESSURE"])
            self.CoreCoolant['Vessel Temp'] = float(self.data["COOLANT_CORE_VESSEL_TEMPERATURE"])
            self.CoreCoolant['Quantity'] = round(float(self.data["COOLANT_CORE_QUANTITY_IN_VESSEL"]) / 120000, 2)
            self.CoreCoolant['Primary Loop Level'] = float(self.data["COOLANT_CORE_PRIMARY_LOOP_LEVEL"])
            self.CoreCoolant['Flow'] = float(self.data["COOLANT_CORE_FLOW_SPEED"])
            self.CoreCoolant['Ordered Flow'] = float(self.data["COOLANT_CORE_FLOW_ORDERED_SPEED"])
            self.CoreCoolant['Flow Reached'] = True if self.CoreCoolant['Flow'] == self.CoreCoolant['Ordered Flow'] else False
            self.CoreCoolant['Circ Pumps'] = self.data["COOLANT_CORE_QUANTITY_CIRCULATION_PUMPS_PRESENT"]
            self.CoreCoolant['Freight Pumps'] = self.data["COOLANT_CORE_QUANTITY_FREIGHT_PUMPS_PRESENT"]

            # Coolant Pumps
              # Pump 0
            self.Pumps['Pump0']['Status'] = self.data["COOLANT_CORE_CIRCULATION_PUMP_0_STATUS"]
            self.Pumps['Pump0']['Flow'] = int(self.data["COOLANT_CORE_CIRCULATION_PUMP_0_SPEED"])
            self.Pumps['Pump0']['Ordered Flow'] = int(self.data["COOLANT_CORE_CIRCULATION_PUMP_0_ORDERED_SPEED"])
            self.Pumps['Pump0']['Flow Reached'] = True if self.Pumps['Pump0']['Flow'] == self.Pumps['Pump0']['Ordered Flow'] else False
            self.Pumps['Pump0']['Overload'] = True if fnmatch(self.data["COOLANT_CORE_CIRCULATION_PUMP_0_OVERLOAD_STATUS"], "*OVERLOADED*") else False
            self.Pumps['Pump0']['Dry'] = True if fnmatch(self.data["COOLANT_CORE_CIRCULATION_PUMP_0_DRY_STATUS"], "*DRY*") else False

              # Pump 1
            self.Pumps['Pump1']['Status'] = self.data["COOLANT_CORE_CIRCULATION_PUMP_1_STATUS"]
            self.Pumps['Pump1']['Flow'] = int(self.data["COOLANT_CORE_CIRCULATION_PUMP_1_SPEED"])
            self.Pumps['Pump1']['Ordered Flow'] = int(self.data["COOLANT_CORE_CIRCULATION_PUMP_1_ORDERED_SPEED"])
            self.Pumps['Pump1']['Flow Reached'] = True if self.Pumps['Pump1']['Flow'] == self.Pumps['Pump1']['Ordered Flow'] else False
            self.Pumps['Pump1']['Overload'] = True if fnmatch(self.data["COOLANT_CORE_CIRCULATION_PUMP_1_OVERLOAD_STATUS"], "*OVERLOADED*") else False
            self.Pumps['Pump1']['Dry'] = True if fnmatch(self.data["COOLANT_CORE_CIRCULATION_PUMP_1_DRY_STATUS"], "*DRY*") else False

              # Pump 2
            self.Pumps['Pump2']['Status'] = self.data["COOLANT_CORE_CIRCULATION_PUMP_2_STATUS"]
            self.Pumps['Pump2']['Flow'] = int(self.data["COOLANT_CORE_CIRCULATION_PUMP_2_SPEED"])
            self.Pumps['Pump2']['Ordered Flow'] = int(self.data["COOLANT_CORE_CIRCULATION_PUMP_2_ORDERED_SPEED"])
            self.Pumps['Pump2']['Flow Reached'] = True if self.Pumps['Pump2']['Flow'] == self.Pumps['Pump2']['Ordered Flow'] else False
            self.Pumps['Pump2']['Overload'] = True if fnmatch(self.data["COOLANT_CORE_CIRCULATION_PUMP_2_OVERLOAD_STATUS"], "*OVERLOADED*") else False
            self.Pumps['Pump2']['Dry'] = True if fnmatch(self.data["COOLANT_CORE_CIRCULATION_PUMP_2_DRY_STATUS"], "*DRY*") else False

            # Control Rods
            self.RodsState = "NOMINAL" if self.data["RODS_STATUS"] == "IMMOBILE" else "ADJUSTING"
            self.RodsMoveSpd = float(self.data["RODS_MOVEMENT_SPEED"])
            self.RodsSpdReduced = True if self.data["RODS_MOVEMENT_SPEED_DECREASED_HIGH_TEMPERATURE"] == "TRUE" else False
            self.RodsDeformed = True if self.data["RODS_DEFORMED"] == "TRUE" else False
            self.RodsTemp = float(self.data["RODS_TEMPERATURE"])
            self.RodsTempMax = float(self.data["RODS_MAX_TEMPERATURE"])
            self.RodsPosActual = float(self.data["RODS_POS_ACTUAL"])
            self.RodsPosOrdered = float(self.data["RODS_POS_ORDERED"])
            self.RodsPosReached = True if self.RodsPosActual == self.RodsPosOrdered else False
            self.RodsNum = self.data["RODS_QUANTITY"]
            self.RodsAligned = True if self.data["RODS_ALIGNED"] == "TRUE" else False
        except TypeError as e:
            print("Error assigning variables")

        timeLabel = ""
        coreLabel = ""
        cCoolantLabel = ""
        p0Label = ""
        p1Label = ""
        p2Label = ""
        rodsLabel = ""

        timeLabel = f"""Time: ........... {self.Time}"""
        self.TimeLabel.config(text=timeLabel)

        if self.CoreTemp >= (self.CoreTempMax - 75):
            coreLabel += f"""            \n**** WARNING - HIGH TEMP - ****"""
        if self.CorePressure < 120:
            coreLabel += f"""\n**** WARNING - LOW CORE PRESSURE - ****"""
        if self.CoreIntegrity < 95.0:
            coreLabel += f"""\n**** WARNING - INTEGRITY: {self.CoreIntegrity} - ****"""
        if self.CoreWear > 40.0:
            coreLabel += f"""\n**** WARNING - HIGH WEAR: {self.CoreWear} - ****"""

        coreLabel += f"""\n\n\t\tCore State\nCore State ...... {self.CoreState}\nCore Temp ....... {round(self.CoreTemp, 2)}\nCore Press ...... {round(self.CorePressure)}"""

        cCoolantLabel = f"""\n\n\t\tCore Coolant\nStatus .......... {self.CoreCoolant['State']}\nCore Flow ....... {self.CoreCoolant['Flow']}\nVessel Level .... {self.CoreCoolant['Quantity']}"""

        # Pump 0
        if not fnmatch(self.Pumps['Pump0']['Status'], "*INACTIVE*") and not fnmatch(self.Pumps['Pump0']['Status'], "*NOT_ACTIVE*"):
            p0Label = f"""\n\n\t\tPump 0\nSpeed ........... """
            p0Label += str(self.Pumps['Pump0']['Flow']) if self.Pumps['Pump0']['Flow Reached'] else f"""{self.Pumps['Pump0']['Flow']} -> {self.Pumps['Pump0']['Ordered Flow']}"""
            p0Label += """\nRUNNING DRY""" if self.Pumps['Pump0']['Dry'] else ""
            p0Label += """\nPUMP OVERLOADED""" if self.Pumps['Pump0']['Overload'] else ""
        else:
            p0Label = ""

        # Pump 1
        if not fnmatch(self.Pumps['Pump1']['Status'], "*INACTIVE*") and not fnmatch(self.Pumps['Pump1']['Status'], "*NOT_ACTIVE*"):
            p1Label = f"""\n\n\t\tPump 1\nSpeed ........... """
            p1Label += str(self.Pumps['Pump1']['Flow']) if self.Pumps['Pump1']['Flow Reached'] else f"""{self.Pumps['Pump1']['Flow']} -> {self.Pumps['Pump1']['Ordered Flow']}"""
            p1Label += """\nRUNNING DRY""" if self.Pumps['Pump1']['Dry'] else ""
            p1Label += """\nPUMP OVERLOADED""" if self.Pumps['Pump1']['Overload'] else ""
        else:
            p1Label = ""

        # Pump 2
        if not fnmatch(self.Pumps['Pump2']['Status'], "*INACTIVE*") and not fnmatch(self.Pumps['Pump2']['Status'], "*NOT_ACTIVE*"):
            p2Label = f"""\n\n\t\tPump 2\nSpeed ........... """
            p2Label += str(self.Pumps['Pump2']['Flow']) if self.Pumps['Pump2']['Flow Reached'] else f"""{self.Pumps['Pump2']['Flow']} -> {self.Pumps['Pump2']['Ordered Flow']}"""
            p2Label += """\nRUNNING DRY""" if self.Pumps['Pump2']['Dry'] else ""
            p2Label += """\nPUMP OVERLOADED""" if self.Pumps['Pump2']['Overload'] else ""
        else:
            p2Label = ""


        rodsLabel = f"""
        
        RODS
Rods Status .... {self.RodsState}
Rods Temp ...... {self.RodsTemp}
Rods Position .. """
        rodsLabel += str(self.RodsPosActual) if self.RodsPosReached else f"{self.RodsPosActual} -> {self.RodsPosOrdered}"


        self.TimeLabel.config(text=timeLabel)
        self.CoreLabel.config(text=coreLabel)
        self.CoreCoolantLabel.config(text=cCoolantLabel)
        self.Pump0Label.config(text=p0Label)
        self.Pump1Label.config(text=p1Label)
        self.Pump2Label.config(text=p2Label)
        self.RodsLabel.config(text=rodsLabel)



        self.root.after(1000, self.update)
        # self.CoreLabel.pack()



    def display(self):
        #display_active = True
        #while display_active:
        self.update()
        self.root.mainloop()


    def get_variable(self, variable):
        try:
            response = requests.get(self.url, params={'variable': variable})
            if response.status_code == 200:
                return response.text
            else:
                return f"Error - Server responded with status code {response.status_code}"
        except requests.RequestException as e:
            return f"Request Error - {e}"

    def translate_variable(self, var, result):
        if var in self.translations.keys():
            try:
                return self.translations[var][result]
            except KeyError as e:
                # print(f"Error translating variable: {var} with value: {result}")
                return result
        else:
            return result
