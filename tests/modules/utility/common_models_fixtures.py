import pytest

@pytest.fixture
def APIResource(fixinstance):
	def check(apiresource):
		fixinstance(apiresource, "url", str)
	return check

@pytest.fixture
def Description(fixinstance, NamedAPIResource):
	def check(description):
		assert isinstance(description, dict)
		fixinstance(description, "description", str)
		if fixinstance(description, "language", dict):
			NamedAPIResource(description['language'])
	return check

@pytest.fixture
def Effect(fixinstance, NamedAPIResource):
	def check(effect):
		fixinstance(effect, "effect", str)
		if fixinstance(effect, "language", dict):
			NamedAPIResource(effect['language'])
	return check

@pytest.fixture
def Encounter(fixinstance, NamedAPIResource):
	def check(encounter):
		fixinstance(encounter, "min_level", int)
		fixinstance(encounter, "max_level", int)
		fixinstance(encounter, "condition_values", list)
		for condition_values in encounter['condition_values']:
			NamedAPIResource(condition_values)
		fixinstance(encounter, "chance", int)
		if fixinstance(encounter, "method", dict):
			NamedAPIResource(encounter['method'])
	return check

@pytest.fixture
def FlavorText(fixinstance, NamedAPIResource):
	def check(flavortext):
		fixinstance(flavortext, "flavor_text", str)
		fixinstance(flavortext, "language", dict)
		if fixinstance(flavortext, "language", dict):
			NamedAPIResource(flavortext['language'])
		if fixinstance(flavortext, "version", dict):
			NamedAPIResource(flavortext['version'])
	return check

@pytest.fixture
def GenerationGameIndex(fixinstance, NamedAPIResource):
	def check(generationgameindex):
		fixinstance(generationgameindex, "game_index", int)
		if fixinstance(generationgameindex, "generation", dict):
			NamedAPIResource(generationgameindex['generation'])
	return check

@pytest.fixture
def MachineVersionDetail(NamedAPIResource, APIResource):
	def check(machineversiondetail):
		APIResource(machineversiondetail['machine'])
		NamedAPIResource(machineversiondetail['version_group'])
	return check

@pytest.fixture
def Name(fixinstance, NamedAPIResource):
	def check(name):
		fixinstance(name, "name", str)
		fixinstance(name, "language", dict)
		if fixinstance(name, "language", dict):
			NamedAPIResource(name['language'])
	return check


@pytest.fixture
def NamedAPIResource(fixinstance):
	def check(namedapiresource):
		fixinstance(namedapiresource, "name", str)
		fixinstance(namedapiresource, "url", str)
	return check

@pytest.fixture
def VerboseEffect(fixinstance, NamedAPIResource):
	def check(verboseeffect):
		fixinstance(verboseeffect, "effect", str)
		fixinstance(verboseeffect, "short_effect", str)
		if fixinstance(verboseeffect, "language", dict):
			NamedAPIResource(verboseeffect['language'])
	return check

@pytest.fixture
def VersionEncounterDetail(NamedAPIResource, Encounter, fixinstance):
	def check(versionencounterdetail):
		if fixinstance(versionencounterdetail, "version", dict):
			NamedAPIResource(versionencounterdetail['version'])
		fixinstance(versionencounterdetail, "max_chance", int)
		fixinstance(versionencounterdetail, "encounter_details", list)
		for encounter_details in versionencounterdetail['encounter_details']:
			Encounter(encounter_details)
	return check

@pytest.fixture
def VersionGameIndex(NamedAPIResource, fixinstance):
	def check(versiongameindex):
		fixinstance(versiongameindex, "game_index", int)
		if fixinstance(versiongameindex, "version", dict):
			NamedAPIResource(versiongameindex['version'])
	return check

@pytest.fixture
def VersionGroupFlavorText(fixinstance, NamedAPIResource):
	def check(flavor_text):
		fixinstance(flavor_text, "text", str)
		if fixinstance(flavor_text, "version_group", dict):
			NamedAPIResource(flavor_text['version_group'])
		if fixinstance(flavor_text, "language", dict):
			NamedAPIResource(flavor_text['language'])
	return check