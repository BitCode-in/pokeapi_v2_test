import pytest

@pytest.mark.contests
@pytest.mark.super_contest_effect_endpoint
@pytest.mark.parametrize("super_contest_effect_id", [1, 2, -1, 'none_effect'])
def test_super_contest_effect_endpoint(api_client, super_contest_effect_id, fixinstance, NamedAPIResource, FlavorText):
    response = api_client.get(f"{pytest.BASE_URL}/super-contest-effect/{super_contest_effect_id}/")
    if super_contest_effect_id in (-1, 'none_effect'):
        assert response.status_code == 404
    else:
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        fixinstance(data, "id", int)
        fixinstance(data, "appeal", int)
        fixinstance(data, "flavor_text_entries", list)
        assert len(data["flavor_text_entries"]) > 0
        for flavor_text_entry in data["flavor_text_entries"]:
            assert isinstance(flavor_text_entry, dict)
            FlavorText(flavor_text_entry)
        fixinstance(data, "moves", list)
        assert len(data["moves"]) > 0
        for move in data["moves"]:
            assert isinstance(move, dict)
            NamedAPIResource(move)