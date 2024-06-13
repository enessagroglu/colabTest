import folium
import json
# Create a map centered around the average coordinates
latitude = (41.0189 + 40.9382 + 40.7852) / 3
longitude = (29.1275 + 29.1557 + 29.4961) / 3
map_istanbul = folium.Map(location=[latitude, longitude], zoom_start=12)

# Adding markers for Tepeüstü, Başibüyük, and Reşadiye
folium.Marker([41.016830, 29.130371], popup='Tepeüstü').add_to(map_istanbul)
folium.Marker([40.959255, 29.156509], popup='Başibüyük').add_to(map_istanbul)
folium.Marker([41.079010, 29.257734], popup='Reşadiye').add_to(map_istanbul)



def add_points_from_json(file_name, map_object):
    file_path = file_name
    with open(file_path, 'r', encoding='utf-8') as file:  # Ensure using utf-8 encoding
        data = json.load(file)
    
    for item in data:
        try:
            # Remove any extraneous whitespace or quotation marks
            latitude = float(item["longitude"].strip().strip('"'))
            longitude = float(item["latitude"].strip().strip('"'))

            popup_info = (f"Name: {item['name']}<br>"
                          f"Population: {item['population']}<br>"
                          f"Population Rate: {item['rate_of_population']}<br>"
                          f"Demand: {item['demand']}")
            folium.Marker([latitude, longitude], popup=folium.Popup(popup_info, max_width=250)).add_to(map_object)
        except ValueError as e:
            print(f"Error converting coordinates for {item['name']}: {e}")


# Load data from JSON files and add to map
add_points_from_json('resadiye.json', map_istanbul)
add_points_from_json('basibuyuk.json', map_istanbul)
add_points_from_json('tepeustu.json', map_istanbul)

# Save the map as an HTML file
map_istanbul.save('neighborhoods.html')




