"""Basketbal Vlaanderen API Client."""

import requests


class BvlDataFetcher:
    endpoint_url = "https://vblapi481.wisseq.eu/VBL_API_481"

    @staticmethod
    def get_games_for_team(team_guid: str) -> list[dict]:
        """Fetches games for a specific team by its GUID."""
        ## https://vblapi481.wisseq.eu/VBL_API_481/data/TeamMatchesByGuid?teamGuid=BVBL1237G12%20%202

        url = f"{BvlDataFetcher.endpoint_url}/data/TeamMatchesByGuid"

        params = {
            "teamGuid": team_guid,
        }

        res = requests.get(url, params=params)
        res.raise_for_status()
        games = res.json()

        return games

    @staticmethod
    def get_game_details(game_guid: str) -> dict:
        """Fetches details for a specific game by its GUID."""
        url = f"{BvlDataFetcher.endpoint_url}/data/MatchByWedGuid"

        params = {
            "issguid": game_guid,
        }

        res = requests.get(url, params=params)
        res.raise_for_status()
        game_details = res.json()[0]

        return game_details

    @staticmethod
    def get_clubs() -> list[dict]:
        """Fetches a list of clubs affiliated with BVL"""
        url = "https://vblcb.wisseq.eu/VBLCB_WebService/data/OrgList?p=1"
        res = requests.get(url)
        res.raise_for_status()
        clubs = res.json()

        return clubs

    @staticmethod
    def get_club_teams(club_guid: str) -> list[dict]:
        """Fetches teams for a specific club by its GUID."""
        ## https://vblapi481.wisseq.eu/VBL_API_481/data/OrgDetailByGuid?issguid=BVBL1237
        url = f"{BvlDataFetcher.endpoint_url}/data/OrgDetailByGuid"

        params = {
            "issguid": club_guid,
        }

        res = requests.get(url, params=params)
        res.raise_for_status()
        club_info = res.json()[0]
        teams_json = club_info.get("teams", [])

        return teams_json

    @staticmethod
    def get_club_details(club_guid: str) -> dict:
        """Fetches detailed information about a specific club by its GUID."""
        url = f"{BvlDataFetcher.endpoint_url}/data/OrgDetailByGuid"

        params = {
            "issguid": club_guid,
        }

        res = requests.get(url, params=params)
        res.raise_for_status()
        club_info = res.json()[0]

        return club_info

    @staticmethod
    def get_poule_games(poule_guid: str) -> list[dict]:
        """Fetches games for a specific poule by its GUID."""
        url = f"{BvlDataFetcher.endpoint_url}/data/PouleMatchesByGuid"

        params = {
            "issguid": poule_guid,
        }

        res = requests.get(url, params=params)
        res.raise_for_status()
        games = res.json()

        return games
