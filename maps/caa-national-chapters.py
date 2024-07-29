import folium
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

France = [46.2276, 2.2137]
m = folium.Map(location=[France[0], France[1]], zoom_start=5)

locations = {
    'Australasie': (-25.2744, 133.7751),
    'Brésil': (-14.2350, -51.9253),
    'Tchéquie': (49.8175, 15.4730),
    'Slovaquie': (48.6690, 19.6990),
    'Danemark': (56.2639, 9.5018),
    'Allemagne': (51.1657, 10.4515),
    'Grèce': (39.0742, 21.8243),
    'Hongrie': (47.1625, 19.5033),
    'Inde': (20.5937, 78.9629),
    'Amérique Latine & les Caraïbes': (-8.7832, -55.4915),
    'Pays-Bas': (52.1326, 5.2913),
    'Flandres': (51.0100, 4.0000),
    'Mexique': (23.6345, -102.5528),
    'Amérique du Nord': (37.0902, -95.7129),
    'Norvège': (60.4720, 8.4689),
    'Pologne': (51.9194, 19.1451),
    'Suède': (60.1282, 18.6435),
    'Suisse': (46.8182, 8.2275),
    'Royaume-Uni': (55.3781, -3.4360)
}

for name, (lat, lon) in locations.items():
    folium.Marker([lat, lon], popup=name, icon=folium.Icon(color='blue')).add_to(m)
folium.Marker(France, popup='France', icon=folium.Icon(color='red')).add_to(m)

# Save the map to an HTML file
m.save(dir_path + '/caa-national-chapter.html')
