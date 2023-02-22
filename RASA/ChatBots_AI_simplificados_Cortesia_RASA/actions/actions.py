# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

CRIC_API_URL = "https://api.cricapi.com/v1/"
CRIC_API_KEY = "36af0021-25ef-4d9c-a39e-ae6eaf9a9a56" # "<UPDATE_API_KEY_HERE>"

SHOW_RECENT_MATCHES = 5

class ActionGetRecentMatches(Action):
	def name(self):
		return 'action_get_recent_matches'

	def run(self, dispatcher, tracker, domain):
		res = requests.get(CRIC_API_URL + "currentMatches" + "?apikey=" + CRIC_API_KEY + "&offset=0")
		if res.status_code == 200:
			matches_data = res.json()["data"]
			matches_data.sort(key=lambda x: x["date"], reverse=True)
			matches_data = [x for x in matches_data if "matchType" in x]
			recent_matches = matches_data[:SHOW_RECENT_MATCHES]
			dispatcher.utter_message(f'Showing the status of {len(recent_matches)} recent matches\n')
			msg = ''
			for index, match in enumerate(recent_matches):
				msg = msg + f'{index+1}. {match["matchType"].upper()} match between ' \
					  f'{match["teams"][0]} and {match["teams"][1]} \n' \
					  f'Date: {match["date"]}, Match Status: {match["status"]}\n'
			dispatcher.utter_message(msg)
		else:
			dispatcher.utter_message(f'Unable to fetch the recent matches details. Please try with some other query!!')
		return []

class ActionGetUpcomingMatches(Action):
	def name(self):
		return 'action_get_upcoming_matches'

	def run(self, dispatcher, tracker, domain):
		res = requests.get(CRIC_API_URL + "matches" + "?apikey=" + CRIC_API_KEY + "&offset=0")
		if res.status_code == 200:

			matches_data = res.json()["data"]
			matches_data.sort(key=lambda x: x["date"], reverse=True)
			team_name = tracker.get_slot('team')
			if team_name is None:
				dispatcher.utter_message(f"Team not set. Showing the results for all the upcoming matches.")
				team_name = "All Teams"
			else:
				matches_data = [x for x in matches_data if team_name in x["teams"]]
			if len(matches_data):
				dispatcher.utter_message(f'Showing the upcoming matches ({len(matches_data)}) for team: {team_name}\n')
				msg = ''
				for index, match in enumerate(matches_data):
					msg = msg + f'{index+1}. {match["matchType"].upper() if "matchType" in match else "A"} match between {match["teams"][0]} and {match["teams"][1]}. ' \
						f'Date: {match["date"]}, Venue: {match["venue"]}\n'
				dispatcher.utter_message(msg)
			else:
				dispatcher.utter_message(f'No upcoming matches for team: {team_name}\n')
		else:
			dispatcher.utter_message(f'Unable to fetch the upcoming matches details. Please try with some other query!!')

		return [SlotSet('team',None)]
        