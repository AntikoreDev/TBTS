import os
import time

import keyboard
import requests

from src.commons import *

# Clear the terminal
def clear():
	is_windows: bool = (os.name == "nt")
	os.system("cls" if is_windows else "clear")

# Get the index by the letter the player choose
def get_idx_by_letter(letter: str, list: list = TRIVIA_LETTERS) -> int:
	try:
		return list.index(letter.strip().upper())
	except:
		return -1

# Fetch data from some url
def fetch(url: str) -> dict:
	try:
		response = requests.get(url)
		
		# If response is OK
		if (response.status_code == 200):
			data = response.json()  
			return data
		return None
	
	except Exception as e:
		print("Error:", e)
		return None
	
# This function halts the game for
def halt_or_skip(text: str, max_time: float = 3, min_time: float = 0.5) -> bool:
	print(text)

	check_time: float = 0.1
	s: int = 0
	
	while s < max_time:
		time.sleep(check_time)
		s += check_time

		if (keyboard.is_pressed("enter") and s > min_time):
			return True
	return True

def format_number(n: int) -> str:
	return "{:,}".format(n)