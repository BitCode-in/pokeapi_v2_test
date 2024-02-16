import pytest
import requests
import warnings
import inspect

@pytest.fixture(scope="session")
def api_client():
	session = requests.Session()
	yield session
	session.close()

@pytest.fixture
def fixinstance():
	def check(object_dict, object_name, _type):
		assert object_name in object_dict and isinstance(object_dict[object_name], (_type, type(None)))
		if object_dict[object_name] is None:
			caller_frame = inspect.currentframe().f_back
			caller_module = caller_frame.f_globals['__file__']
			warnings.warn_explicit(
				f"{object_name} является None. А должен быть {_type}",
				category=UserWarning,
				filename=caller_module,
				lineno=caller_frame.f_lineno
			)
			return False
		return True
		
	return check


@pytest.fixture
def NamedAPIResource(fixinstance):
	def check(named):
		fixinstance(named, "name", str)
		fixinstance(named, "url", str)
	return check

@pytest.fixture
def APIResource(fixinstance):
	def check(named):
		fixinstance(named, "url", str)
	return check

@pytest.fixture
def MachineVersionDetail(NamedAPIResource, APIResource):
	def check(named):
		APIResource(named['machine'])
		NamedAPIResource(named['version_group'])
	return check

@pytest.fixture
def Encounter(NamedAPIResource, fixinstance):
	def check(named):
		fixinstance(named, "min_level", int)
		fixinstance(named, "max_level", int)
		fixinstance(named, "condition_values", list)
		for condition_values in named['condition_values']:
			NamedAPIResource(condition_values)
		fixinstance(named, "chance", int)
		if fixinstance(named, "method", dict):
			NamedAPIResource(named['method'])
	return check

@pytest.fixture
def VersionEncounterDetail(NamedAPIResource, Encounter, fixinstance):
	def check(named):
		if fixinstance(named, "version", dict):
			NamedAPIResource(named['version'])
		fixinstance(named, "max_chance", int)
		fixinstance(named, "encounter_details", list)
		for encounter_details in named['encounter_details']:
			Encounter(encounter_details)
	return check

@pytest.fixture
def Name(fixinstance):
	def check(named):
		fixinstance(named, "name", str)
		fixinstance(named, "language", dict)
		language = named["language"]
		fixinstance(language, "name", str)
		fixinstance(language, "url", str)
	return check

@pytest.fixture
def ChainLink(fixinstance):
	def check(chain):
		fixinstance(chain, "is_baby", bool)
		fixinstance(chain, "species", dict)
		species = chain["species"]
		fixinstance(species, "name", str)
		fixinstance(species, "url", str)
	return check

@pytest.fixture
def Effect(fixinstance):
	def check(named):
		fixinstance(named, "effect", str)
		fixinstance(named, "language", dict)
		language = named["language"]
		fixinstance(language, "name", str)
		fixinstance(language, "url", str)
	return check

@pytest.fixture
def FlavorText(fixinstance):
	def check(named):
		fixinstance(named, "flavor_text", str)
		fixinstance(named, "language", dict)
		language = named["language"]
		fixinstance(language, "name", str)
		fixinstance(language, "url", str)
	return check

@pytest.fixture
def Description(fixinstance):
	def check(description):
		assert isinstance(description, dict)
		fixinstance(description, "description", str)
		fixinstance(description, "language", dict)
		fixinstance(description["language"], "name", str)
		fixinstance(description["language"], "url", str)
	return check

@pytest.fixture
def PokemonEntry(fixinstance):
	def check(entry):
		assert isinstance(entry, dict)
		fixinstance(entry, "entry_number", int)
		fixinstance(entry, "pokemon_species", dict)
		species = entry["pokemon_species"]
		fixinstance(species, "name", str)
		fixinstance(species, "url", str)
	return check

@pytest.fixture
def VerboseEffect(fixinstance):
	def check(effect):
		fixinstance(effect, "effect", str)
		fixinstance(effect, "short_effect", str)
		fixinstance(effect, "language", dict)
		language = effect["language"]
		fixinstance(language, "name", str)
		fixinstance(language, "url", str)
	return check

@pytest.fixture
def VersionGroupFlavorText(fixinstance):
	def check(flavor_text):
		fixinstance(flavor_text, "text", str)
		fixinstance(flavor_text, "version_group", dict)
		version_group = flavor_text["version_group"]
		fixinstance(version_group, "name", str)
		fixinstance(version_group, "url", str)
		fixinstance(flavor_text, "language", dict)
		language = flavor_text["language"]
		fixinstance(language, "name", str)
		fixinstance(language, "url", str)
	return check

@pytest.fixture
def GenerationGameIndex(fixinstance):
	def check(game_index):
		fixinstance(game_index, "game_index", int)
		fixinstance(game_index, "generation", dict)
		generation = game_index["generation"]
		fixinstance(generation, "name", str)
		fixinstance(generation, "url", str)
	return check


