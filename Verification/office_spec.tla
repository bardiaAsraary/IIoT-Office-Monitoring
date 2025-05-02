---- MODULE OfficeSpec ----
EXTENDS Integers, TLC
CONSTANTS MaxTemp = 30, MinTemp = 15
CONSTANTS MaxHumidity = 80, MinHumidity = 30

(*--algorithm office_system
variables 
    temperature \in MinTemp..MaxTemp,
    humidity \in MinHumidity..MaxHumidity,
    occupancy \in {0, 1}

define
    TypeInvariant == 
        /\ temperature \in MinTemp..MaxTemp
        /\ humidity \in MinHumidity..MaxHumidity
        /\ occupancy \in {0, 1}
    
    SafetyProperties ==
        /\ temperature >= MinTemp
        /\ temperature <= MaxTemp
        /\ (occupancy = 1) => (temperature >= 18)
end define

fair process sensor \in {"temp", "humidity", "motion"}
begin
    SensorUpdate:
        either
            \/ /\ temperature' \in {t \in MinTemp..MaxTemp : Abs(t - temperature) <= 2}
               /\ humidity' = humidity
               /\ occupancy' = occupancy
        or
            \/ /\ humidity' \in {h \in MinHumidity..MaxHumidity : Abs(h - humidity) <= 5}
               /\ temperature' = temperature
               /\ occupancy' = occupancy
        or
            \/ /\ occupancy' = 1 - occupancy
               /\ temperature' = temperature
               /\ humidity' = humidity
        end either;
    goto SensorUpdate
end process
====