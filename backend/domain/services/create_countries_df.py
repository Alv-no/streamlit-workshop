import pandas as pd


def prepare_country_data(countries: list[dict]) -> pd.DataFrame:
    """Prepares country data for visualization.

    Args:
        countries (List[Dict]): A list of dictionaries containing country data.

    Returns:
        pd.DataFrame: A DataFrame with the following columns:
            - 'Name': Common name of the country.
            - 'Population': Population of the country.
            - 'Area': Area of the country (default to 0 if missing).
            - 'Languages': List of languages spoken in the country (empty list if missing).
            - 'Capital': Capital city of the country.
            - 'CapitalLatLng': Latitude and longitude of the capital city.
            - 'FlagPNG': URL to the PNG representation of the country's flag.
            - 'FlagEmoji': Emoji representation of the country's flag.
            - 'Currency': Currency used in the country.
            - 'Continents': List of continents where the country is located.
            - 'Timezones': List of timezones in the country.

    Example:
        prepare_country_data([
            {
                'name': {'common': 'Andorra', 'official': 'Principality of Andorra', ...},
                'population': 77265,
                'area': 468.0,
                'languages': {'cat': 'Catalan'},
                'capital': ['Andorra la Vella'],
                'capitalInfo': {'latlng': [42.5, 1.52]},
                'flags': {'png': 'https://flagcdn.com/w320/ad.png'},
                'flag': '🇦🇩',
                'currencies': {'EUR': {'name': 'Euro', 'symbol': '€'}},
                'continents': ['Europe'],
                'timezones': ['UTC+01:00']
            },
            {
                'name': {'common': 'Country2', 'official': 'Official Name2', ...},
                # Other data for Country2...
            },
            # Additional country data...
        ])

    Note:
        - If some data is missing in the input dictionaries, appropriate defaults or empty lists are provided.
    """
    data = []
    for country in countries:
        capital_info = country.get("capitalInfo", {})
        data.append(
            {
                "Name": country["name"]["common"],
                "Population": country["population"],
                "Area": country.get("area", 0),
                "Languages": list(country["languages"].values())
                if "languages" in country
                else [],
                "Capital": country.get("capital", []),
                "CapitalLatLng": capital_info.get("latlng", []),
                "FlagPNG": country.get("flags", {}).get("png", ""),
                "FlagEmoji": country.get("flag", ""),
                "Currency": list(country["currencies"].keys())[0]
                if "currencies" in country
                else "",
                "Continents": country.get("continents", []),
                "Timezones": country.get("timezones", []),
            }
        )
    return pd.DataFrame(data)
