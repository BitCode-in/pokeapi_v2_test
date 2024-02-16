import pytest

pytest.BASE_URL = "https://pokeapi.co/api/v2/"

pytest_plugins = [
	'tests.modules.fixtures',
]

def pytest_configure(config):
	config.addinivalue_line('markers', 'pagination: Testing the functionality of Resource Lists/Pagination (group)')
	config.addinivalue_line('markers', 'berries: Testing the functionality of Berries (group)')
	config.addinivalue_line('markers', 'berry_endpoint: Testing the functionality of Berries (endpoint)')
	config.addinivalue_line('markers', 'berry_firmness_endpoint: Testing the functionality of Berry Firmnesses (endpoint)')
	config.addinivalue_line('markers', 'berry_flavor_endpoint: Testing the functionality of Berry Firmnesses (endpoint)')
	config.addinivalue_line('markers', 'contests: Testing the functionality of Contests (group)')
	config.addinivalue_line('markers', 'contest_type_endpoint: Testing the functionality of Contest Types (endpoint)')
	config.addinivalue_line('markers', 'contest_effect_endpoint: Testing the functionality of Contest Effects (endpoint)')
	config.addinivalue_line('markers', 'super_contest_effect_endpoint: Testing the functionality of Contest Effects (endpoint)')
	config.addinivalue_line('markers', 'encounters: Testing the functionality of Encounters (group)')
	config.addinivalue_line('markers', 'encounter_methods_endpoint: Testing the functionality of Encounter Methods (endpoint)')
	config.addinivalue_line('markers', 'encounter_conditions_endpoint: Testing the functionality of Encounter Conditions (endpoint)')
	config.addinivalue_line('markers', 'encounter_condition_values_endpoint: Testing the functionality of Encounter Condition Values (endpoint)')
	config.addinivalue_line('markers', 'evolution: Testing the functionality of Evolution (group)')
	config.addinivalue_line('markers', 'evolution_triggers_endpoint: Testing the functionality of Evolution Triggers (endpoint)')
	config.addinivalue_line('markers', 'evolution_chains_endpoint: Testing the functionality of Evolution Chains (endpoint)')
	config.addinivalue_line('markers', 'games: Marking tests related to Games (group)')
	config.addinivalue_line('markers', 'generations_endpoint: Marking tests related to Generations (endpoint)')
	config.addinivalue_line('markers', 'pokedexes_endpoint: Marking tests related to Pokedexes (endpoint)')
	config.addinivalue_line('markers', 'version_endpoint: Testing the functionality of Versions (endpoint)')
	config.addinivalue_line('markers', 'version_group_endpoint: Testing the functionality of Version Groups (endpoint)')
	config.addinivalue_line('markers', 'items: Testing the functionality of Items (group)')
	config.addinivalue_line('markers', 'item_endpoint: Testing individual Item functionality')
	config.addinivalue_line('markers', 'item_attribute_endpoint: Testing the functionality of Item Attributes (endpoint)')
	config.addinivalue_line('markers', 'item_category_endpoint: Testing the functionality of Item Categories (endpoint)')
	config.addinivalue_line('markers', 'item_fling_effect_endpoint: Testing the functionality of Item Fling Effects (endpoint)')
	config.addinivalue_line('markers', 'item_fling_pocket_endpoint: Testing the functionality of Item Pockets (endpoint)')
	config.addinivalue_line('markers', 'locations: Testing the functionality of Item Location (group)')
	config.addinivalue_line('markers', 'location_endpoint: Testing the functionality of Location (endpoint)')
	config.addinivalue_line('markers', 'location_area_endpoint: Testing the functionality of Location Area (endpoint)')
	config.addinivalue_line('markers', 'pal_park_area_endpoint: Testing the functionality of Pal Park Area (endpoint)')
	config.addinivalue_line('markers', 'region_endpoint: Testing the functionality of Region (endpoint)')
	config.addinivalue_line('markers', 'machines: Testing the functionality of Machines (group)')
	config.addinivalue_line('markers', 'machine_endpoint: Testing the functionality of Machine (endpoint)')
	config.addinivalue_line('markers', 'moves: Testing the functionality of Moves (group)')
	config.addinivalue_line('markers', 'move_endpoint: Testing the functionality of Move (endpoint)')
	config.addinivalue_line('markers', 'move_ailment_endpoint: Testing the functionality of Move ailment (endpoint)')
	config.addinivalue_line('markers', 'move_battle_style_endpoint: Testing the functionality of Move battle style (endpoint)')
	config.addinivalue_line('markers', 'move_category_endpoint: Testing the functionality of Move category (endpoint)')
	config.addinivalue_line('markers', 'move_damage_class_endpoint: Testing the functionality of Move damage class (endpoint)')
	config.addinivalue_line('markers', 'move_learn_method_endpoint: Testing the functionality of Move learn method (endpoint)')
	config.addinivalue_line('markers', 'move_targets_endpoint: Testing the functionality of Move targets (endpoint)')
	
	

