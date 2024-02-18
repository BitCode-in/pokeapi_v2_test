import pytest

@pytest.mark.abilities
@pytest.mark.location_area_encounters_endpoint
@pytest.mark.parametrize("pokemon_id_or_name", ["pikachu", "bulbasaur", "invalid_pokemon"])
def test_location_area_encounters_endpoint(api_client, fixinstance, pokemon_id_or_name, NamedAPIResource, VersionEncounterDetail):
    response = api_client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}/encounters")
    if pokemon_id_or_name == "invalid_pokemon":
        assert response.status_code == 404
    else:
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for location_area_encounter in data:
            fixinstance(location_area_encounter, "location_area", dict)
            NamedAPIResource(location_area_encounter["location_area"])
            fixinstance(location_area_encounter, "version_details", list)
            for version_detail in location_area_encounter["version_details"]:
                VersionEncounterDetail(version_detail)