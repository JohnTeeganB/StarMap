import requests

def get_planet(id):
    url = f"https://swapi.dev/api/planets/{id}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("\n--- Planet Information ---")
        print(f"Name: {data['name']}")
        print(f"Climate: {data['climate']}")
        print(f"Terrain: {data['terrain']}")
        print(f"Population: {data['population']}")
        print("---------------------------")
    except requests.exceptions.Timeout:
        print("Request timed out. The SWAPI server may be busy — please try again.")
    except requests.exceptions.ConnectionError:
        print("Network error: Could not connect to SWAPI. Check your internet connection.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("Planet not found. Please enter a valid planet ID.")
        else:
            print(f"HTTP error occurred: {e}")
    except ValueError:
        print("Error: Received unexpected data format from API.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    while True:
        planet_id = input("\nEnter a planet ID (1–60): ")
        get_planet(planet_id)

        again = input("\nWould you like to look up another planet? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThe Force will be with you, always...")
            break

