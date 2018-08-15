
import logging
logging.basicConfig(level=logging.DEBUG)

from actions import manual_action, raise_temperature_for, message, wait_until_temperature_has_fallen_to

MASH_TEMPERATURE = 65
MASH_OUT_TEMPERATURE = 77
BOILING_TEMPERATURE = 98
PITCHING_TEMPERATURE = 30


WATER_TREATMENT_MINUTES = 10
MASH_MINUTES = 60
PRE_HOP_BOIL_MINUTES = 15
POST_HOP_BOIL_MINUTES = 45

#WATER_TREATMENT_MINUTES = MASH_MINUTES = PRE_HOP_BOIL_MINUTES = POST_HOP_BOIL_MINUTES = 0
#MASH_TEMPERATURE=MASH_OUT_TEMPERATURE=BOILING_TEMPERATURE=PITCHING_TEMPERATURE=65

# manual_action('Add water treatment salts')
# raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=WATER_TREATMENT_MINUTES)
#
# message('Cooling liquor to mashing temperature')
# wait_until_temperature_has_fallen_to(MASH_TEMPERATURE)
# raise_temperature_for(target_temperature=MASH_TEMPERATURE)
#
# manual_action('Add Grain')
# raise_temperature_for(target_temperature=MASH_TEMPERATURE, target_minutes=MASH_MINUTES)
#
#
# message('Mash Out')
# raise_temperature_for(target_temperature=MASH_OUT_TEMPERATURE)
#
# manual_action('Remove Grain')

message('Bring to boiling point')
raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=60)

manual_action('Add t-30 min  Hops')
raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=15)

manual_action('Add t-15 min  Hops')
raise_temperature_for(target_temperature=BOILING_TEMPERATURE, target_minutes=15)

manual_action('Add Post Boil  Hops and cool')


message('Cooling to fermentation temperature')
wait_until_temperature_has_fallen_to(PITCHING_TEMPERATURE)
manual_action('Remove hops')

manual_action('Pitch Yeast')