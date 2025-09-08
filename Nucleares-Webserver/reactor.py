import read_variables


class Reactor:

    def __init__(self):
        self.Time = ''
        self.TimeStamp = ''
        self.Day = 0
        self.core = Core()


class Core:

    def __init__(self):
        self.TempCurrent = 0
        self.TempOperative = 0
        self.TempMax = 0

        self.PressCurrent = 0
        self.PressOperative = 0
        self.PressMax = 0

        self.State = ''
        self.Criticality = False
        self.CritMassReached = False
        self.CriticalityCounter = 0
        self.ImminentFusion = False
        self.ReadyStart = False
        self.SteamPresent = False
        self.HighSteam = False
        self.CoreDelta = 0

        self.rods = Rods()
        self.coolant = CoreCoolant()
        self.chem = {'DoseOrd': 0, 'DoseAct': 0, 'FiltOrd': 0, 'FiltAct': 0, 'BoronPPM': 0}
        self.MaxPotentialPower = 0
        self.ExternalReservoir = 0


class Rods:
    def __init__(self):
        self.Status = ''
        self.MoveSpeed = 0
        self.SpeedDecreased = False
        self.Deformed = False
        self.TempCurrent = 0
        self.TempMax = 0
        self.OrderedPosition = 0
        self.ActualPosition = 0
        self.PositionReached = False
        self.RodCount = 0
        self.RodsAligned = False


class CoreCoolant:
    def __init__(self):
        self.State = ''
        self.PressCurrent = 0
        self.PressMax = 0
        self.Temp = 0
        self.OverallQuantity = 0
        self.PrimaryLoopLevel = 0
        self.FlowSpeed = 0
        self.FlowIn = 0
        self.FlowOut = 0
        self.OrderedSpeed = 0
        self.SpeedReached = False
        self.FeedwaterTankLevel = 0


class SteamTurbine:
    def __init__(self, loopNum):
        self.Loop
        self.RPM = 0
        self.Temp = 0
        self.Pressure = 0


class ElectricTurbine:
    def __init__(self, loopNum):
        self.Loop = 0
        self.Power = 0
        self.Voltage = 0
        self.Amps = 0
        self.Freq = 0
        self.Breaker = False


class CoolantLoop:

    def __init__(self, loopNum):
        self.LoopNum = loopNum
        self.PrimPump = Pump(loopNum)
        self.SecPumpCapacity = 0
        self.SteamGen = Evaporator(loopNum)


class Pump:

    def __init__(self, loop=0, pumpNum=0):
        self.Status = ''
        self.Dry = False
        self.Overload = False
        self.OrderedSpeed = 0
        self.ActualSpeed = 0
        self.Capacity = 0

class Evaporator:
    def __init__(self, loopNum):
        self.ReturnFlowPlusCondensed = 0