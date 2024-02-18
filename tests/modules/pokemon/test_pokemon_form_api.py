import pytest

@pytest.mark.abilities
@pytest.mark.pokemon_forms_endpoint
@pytest.mark.parametrize("form_id_or_name", ["arceus-bug", "10041", "invalid_form"])
def test_pokemon_forms_endpoint(api_client, fixinstance, form_id_or_name, NamedAPIResource, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/pokemon-form/{form_id_or_name}/")
	if form_id_or_name == "invalid_form":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "order", int)
		fixinstance(data, "form_order", int)
		fixinstance(data, "is_default", bool)
		fixinstance(data, "is_battle_only", bool)
		fixinstance(data, "is_mega", bool)
		fixinstance(data, "form_name", str)
		if fixinstance(data, "pokemon", dict):
			NamedAPIResource(data["pokemon"])

		fixinstance(data, "types", list)
		for pokemon_form_type in data["types"]:
			fixinstance(pokemon_form_type, "slot", int)
			NamedAPIResource(pokemon_form_type["type"])

		if fixinstance(data, "sprites", dict):
			fixinstance(data["sprites"], "front_default", str)
			fixinstance(data["sprites"], "front_shiny", str)
			fixinstance(data["sprites"], "back_default", str)
			fixinstance(data["sprites"], "back_shiny", str)

		if fixinstance(data, "version_group", dict):
			NamedAPIResource(data["version_group"])

		for name_info in data["names"]:
			Name(name_info)

		for form_names_info in data["form_names"]:
			Name(form_names_info)
		