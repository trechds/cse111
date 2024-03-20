from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def calculate_distance(customer_city):
    # Localização de Marau-RS (exemplo)
    marau_location = (-28.4481, -52.1996)

    # Inicialize o geolocalizador do Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Obtenha as coordenadas da cidade do cliente
    customer_location = geolocator.geocode(customer_city)

    # Verifique se a cidade foi encontrada
    if customer_location:
        customer_coords = (customer_location.latitude, customer_location.longitude)
        print(f"Your location is: {customer_coords}")
    else:
        print(f"We didn't find your location")
        return None

    # Calcula a distância entre Marau-RS e a cidade do cliente
    distance = geodesic(marau_location, customer_coords).kilometers

    return distance

# Exemplo de uso
customer_city = input("Enter the customer's city-state: ")
try:
    distance = calculate_distance(customer_city)
    if distance:
        print(f"The distance between Marau-RS and {customer_city} is {distance:.2f} km.")
except ValueError as e:
    print(e)