## PyTest Configuration

### Base URL

The base URL for API requests is set to `"https://pokeapi.co/api/v2/"`.

```python
pytest.BASE_URL = "https://pokeapi.co/api/v2/"
```

### PyTest Plugins

The following plugins are included in the PyTest configuration:

```python
pytest_plugins = [
    'tests.modules.fixtures',
    'tests.modules.utility.common_models_fixtures',
]
```

## PyTest Markers

- **Pagination**: Testing the functionality of Resource Lists/Pagination (group)
- **Berries**: Testing the functionality of Berries (group)
    - **Berry Endpoint**: Testing the functionality of Berries (endpoint)
    - **Berry Firmness Endpoint**: Testing the functionality of Berry Firmnesses (endpoint)
    - **Berry Flavor Endpoint**: Testing the functionality of Berry Firmnesses (endpoint)
- **Contests**: Testing the functionality of Contests (group)
    - **Contest Type Endpoint**: Testing the functionality of Contest Types (endpoint)
    - **Contest Effect Endpoint**: Testing the functionality of Contest Effects (endpoint)
    - **Super Contest Effect Endpoint**: Testing the functionality of Contest Effects (endpoint)
- **Encounters**: Testing the functionality of Encounters (group)
    - **Encounter Methods Endpoint**: Testing the functionality of Encounter Methods (endpoint)
    - **Encounter Conditions Endpoint**: Testing the functionality of Encounter Conditions (endpoint)
    - **Encounter Condition Values Endpoint**: Testing the functionality of Encounter Condition Values (endpoint)
- **Evolution**: Testing the functionality of Evolution (group)
    - **Evolution Triggers Endpoint**: Testing the functionality of Evolution Triggers (endpoint)
    - **Evolution Chains Endpoint**: Testing the functionality of Evolution Chains (endpoint)
- **Games**: Marking tests related to Games (group)
    - **Generations Endpoint**: Marking tests related to Generations (endpoint)
    - **Pokedexes Endpoint**: Marking tests related to Pokedexes (endpoint)
    - **Version Endpoint**: Testing the functionality of Versions (endpoint)
    - **Version Group Endpoint**: Testing the functionality of Version Groups (endpoint)
- **Items**: Testing the functionality of Items (group)
    - **Item Endpoint**: Testing individual Item functionality
    - **Item Attribute Endpoint**: Testing the functionality of Item Attributes (endpoint)
    - **Item Category Endpoint**: Testing the functionality of Item Categories (endpoint)
    - **Item Fling Effect Endpoint**: Testing the functionality of Item Fling Effects (endpoint)
    - **Item Fling Pocket Endpoint**: Testing the functionality of Item Pockets (endpoint)
- **Locations**: Testing the functionality of Item Location (group)
    - **Location Endpoint**: Testing the functionality of Location (endpoint)
    - **Location Area Endpoint**: Testing the functionality of Location Area (endpoint)
    - **Pal Park Area Endpoint**: Testing the functionality of Pal Park Area (endpoint)
    - **Region Endpoint**: Testing the functionality of Region (endpoint)
- **Machines**: Testing the functionality of Machines (group)
    - **Machine Endpoint**: Testing the functionality of Machine (endpoint)
- **Moves**: Testing the functionality of Moves (group)
    - **Move Endpoint**: Testing the functionality of Move (endpoint)
    - **Move Ailment Endpoint**: Testing the functionality of Move ailment (endpoint)
    - **Move Battle Style Endpoint**: Testing the functionality of Move battle style (endpoint)
    - **Move Category Endpoint**: Testing the functionality of Move category (endpoint)
    - **Move Damage Class Endpoint**: Testing the functionality of Move damage class (endpoint)
    - **Move Learn Method Endpoint**: Testing the functionality of Move learn method (endpoint)
    - **Move Targets Endpoint**: Testing the functionality of Move targets (endpoint)
- **Abilities**: Testing the abilities functionality
    - **Ability Endpoint**: Testing the ability endpoints
    - **Stats Endpoint**: Testing the stats endpoint
    - **Characteristic Endpoint**: Testing the functionality of Characteristics (endpoint)
    - **Egg Group Endpoint**: Testing the functionality of Egg Groups (endpoint)
    - **Gender Endpoint**: Testing the functionality of Genders (endpoint)
    - **Growth Rate Endpoint**: Testing the functionality of Growth Rates (endpoint)
    - **Location Area Encounters Endpoint**: Testing the functionality of Location Area Encounters (endpoint)
    - **Nature Endpoint**: Testing the functionality of Natures (endpoint)
    - **Pokeathlon Stat Endpoint**: Testing the functionality of Pokeathlon Stats (endpoint)
    - **Pokemon Endpoint**: Testing the functionality of Pokemon (endpoint)
    - **Pokemon Colors Endpoint**: Testing the functionality of Pokemon Colors (endpoint)
    - **Pokemon Forms Endpoint**: Testing the functionality of Pokemon Forms (endpoint)
    - **Pokemon Habitats Endpoint**: Testing the functionality of Pokemon Habitats (endpoint)
    - **Pokemon Shapes Endpoint**: Testing the functionality of Pokemon Shapes (endpoint)
    - **Pokemon Species Endpoint**: Testing the functionality of Pokemon Species (endpoint)
    - **Type Endpoint**: Testing the functionality of Ability Type (endpoint)
- **Utility**: Testing the functionality of Utility (group)
    - **Language Endpoint**: Testing the functionality of Language (endpoint)
