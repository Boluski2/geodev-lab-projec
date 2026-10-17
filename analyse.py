with open ("wards.csv") as f:
    lines = f.readlines()

for  line in lines[1:]:
     parts = line.strip().split(",")
     wards  = parts [0]
     area_km2 = float (parts[1])
    #  area_hectares = area_km2 * 100
     if area_km2 > 9:
       size = "large"
     else:
       size = "small"

     print(wards, "is", size)