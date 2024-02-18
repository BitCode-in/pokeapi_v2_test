import pytest

@pytest.mark.abilities
@pytest.mark.pokeathlon_stat_endpoint
@pytest.mark.parametrize("pokeathlon_stat_id_or_name", [1, "speed", "invalid_pokeathlon_stat"])
def test_pokeathlon_stat_endpoint(api_client, fixinstance, pokeathlon_stat_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/pokeathlon-stat/{pokeathlon_stat_id_or_name}/")
	if pokeathlon_stat_id_or_name == "invalid_pokeathlon_stat":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)

		fixinstance(data, "affecting_natures", dict)
		affecting_natures = data["affecting_natures"]
		assert isinstance(affecting_natures, dict)
		
		if "increase" in affecting_natures:
			fixinstance(affecting_natures, "increase", list)
			for affect in affecting_natures["increase"]:
				fixinstance(affect, "max_change", int)
				if fixinstance(affect, "nature", dict):
					NamedAPIResource(affect["nature"])
		
		if "decrease" in affecting_natures:
			fixinstance(affecting_natures, "decrease", list)
			for affect in affecting_natures["decrease"]:
				fixinstance(affect, "max_change", int)
				if fixinstance(affect, "nature", dict):
					NamedAPIResource(affect["nature"])