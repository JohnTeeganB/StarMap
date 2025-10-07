# StarMap (SWAPI-planets)
## Overview
SWAPI-planets (codenamed: StarMap) is a Python app that uses SWAPI (Star Wars API) to provide the user information on 50+ planets in the Star Wars universe. StarMap makes a request to the API for JSON data, parses said data, and displays it to the user.
## How It Works
1. The user is prompted to enter a planet ID (1–60).
2. The program constructs the request URL: `https://swapi.dev/api/planets/{id}/`.
3. A GET request is sent using the `requests` library.
4. The JSON response is parsed and displayed.
5. If the ID is invalid or the API is down, an error message is shown.
## Successes
 - Tested the {id} being put inside the URL itself and it worked perfectly.
 - Added main.py to the repository.
## Issues
 - Repository created and app verified to connect with SWAPI.
 - Realized error handling was not robust enough, added multiple exception handling techniques using the `requests` library.
