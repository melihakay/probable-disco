c_mile   = 1609.344 #1mil = 1609.34m
c_feet   = 3.2808399 #1m = 3.2808399f
c_mf     = c_mile*c_feet #1mil = c_mile m = c_mile*c_feet f
v_meter1 = 21000


print(f"One mile is equal to {c_mile} meters.")
print(f"As calculated {v_meter1} meters is equal to",v_meter1/c_mile,"miles and",c_feet*v_meter1,"foots.")
print(f"1 mile is equal to", c_mf,"feets.")
