import initialise_logging
from actions import action, raise_temperature_for, message, wait_until_temperature_has_fallen_to

MASH_TEMPERATURE = 65
MASH_OUT_TEMPERATURE = 77
BOILING_TEMPERATURE = 98
PITCHING_TEMPERATURE = 30

WATER_TREATMENT_MINUTES = 10
MASH_MINUTES = 60
PRE_HOP_BOIL_MINUTES = 15
POST_HOP_BOIL_MINUTES = 45

action('Add water treatment salts')
raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=WATER_TREATMENT_MINUTES)

message('Cooling liquor to mashing temperature')
wait_until_temperature_has_fallen_to(MASH_TEMPERATURE)

action('Add Grain')
raise_temperature_for(target_temperature=MASH_TEMPERATURE, target_minutes=MASH_MINUTES)

message('Mash Out')
raise_temperature_for(target_temperature=MASH_OUT_TEMPERATURE)

action('Remove Grain')

message('Bring to boiling point')
raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=60)

action('Add t-30 min  Hops')
raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=15)

action('Add t-15 min  Hops')
raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=15)

action('Add Post Boil  Hops and cool')

message('Cooling to fermentation temperature')
wait_until_temperature_has_fallen_to(PITCHING_TEMPERATURE)
action('Remove hops and pitch yeast')
