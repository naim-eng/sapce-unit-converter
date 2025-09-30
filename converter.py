# converter.py

# Gravity ratios relative to Earth (almost)
MARS = 0.38
MOON = 0.165
JUPITER = 2.64   # simple approximation for this project

#  Distance constants
LIGHT_YEAR_KM = 9.46e12          # kilometers in one light-year (approx)
AU_KM = 149_597_870.7            # kilometers in one AU

#  Weight conversion 
weight = float(input("Enter your Earth weight (kg): ")) 
print("\n Weight Conversions")
print(f"Your weight on Mars:   {weight * MARS:.1f} kg")
print(f"Your weight on Moon:   {weight * MOON:.1f} kg")
print(f"Your weight on Jupiter:{weight * JUPITER:.1f} kg")

# -Light-year to km 
ly = float(input("\nEnter distance in light years: "))
print(f"{ly} light years = {ly * LIGHT_YEAR_KM:.2e} km")

#  AU to km 
au = float(input("\nEnter distance in AU: "))
print(f"{au} AU = {au * AU_KM:.2e} km")
print("\nConversion complete. Thanks for using Space Unit Converter!") 
