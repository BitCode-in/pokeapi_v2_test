import pytest

@pytest.fixture
def TypeRelations(fixinstance, NamedAPIResource):
	def check(relations):
		fixinstance(relations, "no_damage_to", list)
		fixinstance(relations, "half_damage_to", list)
		fixinstance(relations, "double_damage_to", list)
		fixinstance(relations, "no_damage_from", list)
		fixinstance(relations, "half_damage_from", list)
		fixinstance(relations, "double_damage_from", list)
		for relation_list in relations.values():
			for relation in relation_list:
				NamedAPIResource(relation)
	return check

@pytest.mark.abilities
@pytest.mark.type_endpoint
@pytest.mark.parametrize("type_id_or_name", [5, "ground", "invalid_type"])
def test_type_endpoint(api_client, fixinstance, type_id_or_name, NamedAPIResource, TypeRelations, GenerationGameIndex, Name):
	response = api_client.get(f"https://pokeapi.co/api/v2/type/{type_id_or_name}/")
	if type_id_or_name == "invalid_type":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		if fixinstance(data, "damage_relations", dict):
			TypeRelations(data['damage_relations'])
			

		fixinstance(data, "past_damage_relations", list)
		for past_relation in data["past_damage_relations"]:
			if fixinstance(past_relation , "generation", dict):
				NamedAPIResource(past_relation ["generation"])
			if fixinstance(past_relation , "damage_relations", dict):
				TypeRelations(past_relation ['damage_relations'])

		fixinstance(data, "game_indices", list)
		for game_index in data["game_indices"]:
			GenerationGameIndex(game_index)

		if fixinstance(data, "generation", dict):
			NamedAPIResource(data["generation"])

		if fixinstance(data, "move_damage_class", dict):
			NamedAPIResource(data["move_damage_class"])

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			Name(name_info)

		fixinstance(data, "pokemon", list)
		for pokemon_info in data["pokemon"]:
			fixinstance(pokemon_info, "slot", int)
			if fixinstance(pokemon_info, "pokemon", dict):
				NamedAPIResource(pokemon_info["pokemon"])

		fixinstance(data, "moves", list)
		for moves_info in data["moves"]:
			NamedAPIResource(moves_info)


	