import pytest

@pytest.mark.moves
@pytest.mark.move_endpoint
@pytest.mark.parametrize("move_id_or_name", [1, "pound", "invalid_move"])
def test_move_endpoint(api_client, fixinstance, move_id_or_name, NamedAPIResource, APIResource, VerboseEffect, Effect, MachineVersionDetail, Name):
	response = api_client.get(f"{pytest.BASE_URL}move/{move_id_or_name}/")
	if move_id_or_name == "invalid_move":
		assert response.status_code == 404
	else:
		assert response.status_code == 200
		data = response.json()
		assert isinstance(data, dict)
		fixinstance(data, "id", int)
		fixinstance(data, "name", str)
		fixinstance(data, "accuracy", int)
		fixinstance(data, "effect_chance", int)
		fixinstance(data, "pp", int)
		fixinstance(data, "priority", int)
		fixinstance(data, "power", int)

		fixinstance(data, "contest_combos", dict)
		contest_combos = data["contest_combos"]
		assert isinstance(contest_combos, dict)
		if fixinstance(contest_combos, "normal", dict):
			if fixinstance(contest_combos["normal"], "use_before", list):
				for use_before in contest_combos["normal"]["use_before"]:
					assert isinstance(use_before, dict)
					NamedAPIResource(use_before)
			if fixinstance(contest_combos["normal"], "use_after", list):
				for use_after in contest_combos["normal"]["use_after"]:
					assert isinstance(use_after, dict)
					NamedAPIResource(use_after)
		if fixinstance(contest_combos, "super", dict):
			if fixinstance(contest_combos["super"], "use_before", list):
				for use_before in contest_combos["super"]["use_before"]:
					assert isinstance(use_before, dict)
					NamedAPIResource(use_before)
			if fixinstance(contest_combos["super"], "use_after", list):
				for use_after in contest_combos["super"]["use_after"]:
					assert isinstance(use_after, dict)
					NamedAPIResource(use_after)

		if fixinstance(data, "contest_type", dict):
			NamedAPIResource(data["contest_type"])

		if fixinstance(data, "contest_effect", dict):
			APIResource(data["contest_effect"])

		if fixinstance(data, "damage_class", dict):
			NamedAPIResource(data["damage_class"])

		fixinstance(data, "effect_entries", list)
		for effect_entries in data["effect_entries"]:
			VerboseEffect(effect_entries)

		fixinstance(data, "effect_changes", list)
		for effect_changes in data["effect_changes"]:
			fixinstance(effect_changes, "effect_entries", list)
			for effect_entries_2 in effect_changes["effect_entries"]:
				Effect(effect_entries_2)
			if fixinstance(data, "version_group", dict):
				NamedAPIResource(data["version_group"])

		fixinstance(data, "learned_by_pokemon", list)
		for learned_by_pokemon in data["learned_by_pokemon"]:
			NamedAPIResource(learned_by_pokemon)

		fixinstance(data, "flavor_text_entries", list)
		for flavor_text_entries in data["flavor_text_entries"]:
			assert isinstance(flavor_text_entries, dict)
			fixinstance(flavor_text_entries, "flavor_text", str)
			if fixinstance(flavor_text_entries, "language", dict):
				NamedAPIResource(flavor_text_entries["language"])
			if fixinstance(flavor_text_entries, "version_group", dict):
				NamedAPIResource(flavor_text_entries["version_group"])

		if fixinstance(data, "generation", dict):
			NamedAPIResource(data["generation"])

		fixinstance(data, "machines", list)
		for machines in data["machines"]:
			assert isinstance(machines, dict)
			MachineVersionDetail(machines)

		if fixinstance(data, "meta", dict):
			if fixinstance(data["meta"], "category", dict):
				NamedAPIResource(data["meta"]["category"])
			if fixinstance(data["meta"], "ailment", dict):
				NamedAPIResource(data["meta"]["ailment"])
			fixinstance(data["meta"], "min_hits", int)
			fixinstance(data["meta"], "max_hits", int)
			fixinstance(data["meta"], "min_turns", int)
			fixinstance(data["meta"], "max_turns", int)
			fixinstance(data["meta"], "drain", int)
			fixinstance(data["meta"], "healing", int)
			fixinstance(data["meta"], "crit_rate", int)
			fixinstance(data["meta"], "ailment_chance", int)
			fixinstance(data["meta"], "flinch_chance", int)
			fixinstance(data["meta"], "stat_chance", int)

		fixinstance(data, "names", list)
		for name_info in data["names"]:
			assert isinstance(name_info, dict)
			Name(name_info)

		fixinstance(data, "past_values", list)
		for past_values in data["past_values"]:
			fixinstance(past_values, "accuracy", int)
			fixinstance(past_values, "effect_chance", int)
			fixinstance(past_values, "power", int)
			fixinstance(past_values, "pp", int)
			fixinstance(past_values, "effect_entries", list)
			for effect_entries in past_values["effect_entries"]:
				assert isinstance(effect_entries , dict)
				VerboseEffect(effect_entries)
			if fixinstance(past_values, "type", dict):
				NamedAPIResource(past_values["type"])				
			if fixinstance(past_values, "version_group", dict):
				NamedAPIResource(past_values["version_group"])

		fixinstance(data, "stat_changes", list)
		for stat_changes in data["stat_changes"]:
			fixinstance(stat_changes, "change", int)
			if fixinstance(stat_changes, "stat", dict):
				NamedAPIResource(stat_changes["stat"])

		if fixinstance(data, "super_contest_effect", dict):
			APIResource(data["super_contest_effect"])

		if fixinstance(data, "target", dict):
			NamedAPIResource(data["target"])

		if fixinstance(data, "type", dict):
			NamedAPIResource(data["type"])