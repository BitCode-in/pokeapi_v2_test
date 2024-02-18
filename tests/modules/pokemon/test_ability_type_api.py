# import pytest

# @pytest.mark.abilities
# @pytest.mark.type_endpoint
# @pytest.mark.parametrize("type_id_or_name", [5, "ground"])
# def test_type_endpoint(api_client, fixinstance, type_id_or_name, NamedAPIResource, TypeRelations):
# 	response = api_client.get(f"https://pokeapi.co/api/v2/type/{type_id_or_name}/")
# 	assert response.status_code == 200
# 	data = response.json()
# 	assert isinstance(data, dict)
# 	fixinstance(data, "id", int)
# 	fixinstance(data, "name", str)
# 	if fixinstance(data, "damage_relations", dict):
# 		fixinstance(data["damage_relations"], "no_damage_to", list)
# 		fixinstance(data["damage_relations"], "half_damage_to", list)
# 		fixinstance(data["damage_relations"], "double_damage_to", list)
# 		fixinstance(data["damage_relations"], "no_damage_from", list)
# 		fixinstance(data["damage_relations"], "half_damage_from", list)
# 		fixinstance(data["damage_relations"], "double_damage_from", list)
# 		for relation_list in data["damage_relations"].values():
# 			for relation in relation_list:
# 				NamedAPIResource(relation)
				
# 	if fixinstance(data, "generation", dict):
# 		NamedAPIResource(data["generation"])
# 	if fixinstance(data, "move_damage_class", dict):
# 		NamedAPIResource(data["move_damage_class"])
# 	fixinstance(data, "names", list)
# 	assert len(data["names"]) > 0
# 	for name_info in data["names"]:
# 		assert isinstance(name_info, dict)
# 		NamedAPIResource(name_info)
	