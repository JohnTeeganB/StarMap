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
    except requests.exceptions.HTTPError:
        print("Invalid planet ID or API unavailable.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    planet_id = input("Enter a planet ID (1–60): ")
    get_planet(planet_id)