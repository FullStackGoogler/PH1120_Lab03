C1 = #Capcitor 1
C1DEV = #Capcitor 1 Uncertainty
C2 = #Capcitor 2
C2DEV = #Capcitor 2 Uncertainty

#Capacitors in Series
Cseries = (C1*C2) / (C1+C2)
CseriesDEV = (C1DEV * ((C2/(C1+C2)) ** 2)) + (C2DEV * ((C1/(C1+C2)) ** 2))

#Capacitors in Parallel
Cparallel = C1 + C2
CparallelDEV = C1DEV + C2DEV

print(f'Total capacitance (parallel): {Cparallel} ± {CparallelDEV} F')
print(f'Total capacitance (series): {Cseries} ± {CseriesDEV} F')
