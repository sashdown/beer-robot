# desired profile

#  water treatment - bring to boiling, boil for 10 minutes

# mash - raise to 67C

# mashout - raise to 77 C

# cool to 28C
from time import sleep
from temperature import read_temp




manual_action('Add water treatment salts')
wait_until_temperature_has_risen_to(temperature=100, minutes=10)

message('Cooling liquor to mashing temperature')
wait_until_temperature_has_fallen_to(67)

manual_action('Add Grain')
wait_until_temperature_has_risen_to(temperature=67, minutes=60)


message('Mash Out')
wait_until_temperature_has_risen_to(temperature=77)

manual_action('Remove Grain')
wait_until_temperature_has_risen_to(temperature=100, minutes=45)

message('Bring to boiling point')
wait_until_temperature_has_risen_to(temperature=100, minutes=15)

manual_action('Add boiling Hops')
wait_until_temperature_has_risen_to(temperature=100, minutes=45)

message('Cooling to fermentation temperature')
wait_until_temperature_has_fallen_to(30)

manual_action('Pitch Yeast')