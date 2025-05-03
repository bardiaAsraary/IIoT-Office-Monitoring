---- MODULE OfficeSpec ----
EXTENDS Integers, TLC

CONSTANTS MaxTemp, MinTemp, MaxHumidity, MinHumidity

VARIABLES temperature, humidity, occupancy

Init == 
    /\ temperature \in MinTemp..MaxTemp
    /\ humidity \in MinHumidity..MaxHumidity
    /\ occupancy \in {0, 1}

TypeInvariant == 
    /\ temperature \in MinTemp..MaxTemp
    /\ humidity \in MinHumidity..MaxHumidity
    /\ occupancy \in {0, 1}

SafetyProperties ==
    /\ temperature >= MinTemp
    /\ temperature <= MaxTemp
    /\ humidity >= MinHumidity
    /\ humidity <= MaxHumidity
    /\ (occupancy = 1) => (temperature >= 18)

Next ==
    \/ /\ LET tSet == {temperature + d : d \in {-2, -1, 0, 1, 2}}
           IN temperature' \in {t \in tSet : MinTemp <= t /\ t <= MaxTemp}
       /\ LET hSet == {humidity + d : d \in {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}}
           IN humidity' \in {h \in hSet : MinHumidity <= h /\ h <= MaxHumidity}
       /\ UNCHANGED occupancy
    \/ /\ UNCHANGED <<temperature, humidity>>
       /\ occupancy' = 1 - occupancy


Spec == Init /\ [][Next]_<<temperature, humidity, occupancy>>

====