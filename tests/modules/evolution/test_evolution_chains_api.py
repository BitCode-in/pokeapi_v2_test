import pytest

@pytest.mark.evolution
@pytest.mark.evolution_chains_endpoint
@pytest.mark.parametrize("evolution_chain_id", [1, 7, 20, "invalid_evolution_chain"])
def test_evolution_chain_endpoint(api_client, evolution_chain_id, fixinstance, NamedAPIResource, ChainLink):
	response = api_client.get(f"{pytest.BASE_URL}/evolution-chain/{evolution_chain_id}/")
	if evolution_chain_id == "invalid_evolution_chain":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		assert "baby_trigger_item" in data
		fixinstance(data, "chain", dict)
		ChainLink(data["chain"])
		assert "evolution_details" in data["chain"]
		fixinstance(data["chain"], "evolves_to", list)
		evolves_to = data["chain"]["evolves_to"]
		for evolve_link in evolves_to:
			ChainLink(evolve_link)
			fixinstance(evolve_link, "evolution_details", list)
			for detail in evolve_link["evolution_details"]:
				if fixinstance(detail, "item", dict):
					NamedAPIResource(detail["item"])
				if fixinstance(detail, "trigger", dict):
					NamedAPIResource(detail["trigger"])
				fixinstance(detail, "gender", int)
				if fixinstance(detail, "held_item", dict):
					NamedAPIResource(detail["held_item"])
				if fixinstance(detail, "known_move", dict):
					NamedAPIResource(detail["known_move"])
				if fixinstance(detail, "known_move_type", dict):
					NamedAPIResource(detail["known_move_type"])
				if fixinstance(detail, "location", dict):
					NamedAPIResource(detail["location"])
				fixinstance(detail, "min_level", int)
				fixinstance(detail, "min_happiness", int)
				fixinstance(detail, "min_beauty", int)
				fixinstance(detail, "min_affection", int)
				fixinstance(detail, "needs_overworld_rain", bool)
				if fixinstance(detail, "party_species", dict):
					NamedAPIResource(detail["party_species"])
				if fixinstance(detail, "party_type", dict):
					NamedAPIResource(detail["party_type"])
				fixinstance(detail, "relative_physical_stats", int)
				fixinstance(detail, "time_of_day", str)
				if fixinstance(detail, "trade_species", dict):
					NamedAPIResource(detail["trade_species"])
				fixinstance(detail, "turn_upside_down", bool)