import folium

# Create the base map centered in the US
anthrax_map = folium.Map(location=[37.8, -96], zoom_start=5)

# List of all locations and events
event_locations = [
    {"name": "10 Nassau Street, Princeton, NJ", "coords": [40.3487, -74.6598],
     "event": "2001-09-18: The first letters containing anthrax are mailed."},
    {"name": "Boca Raton, FL", "coords": [26.3587, -80.0831],
     "event": "2001-09-19: Robert Stevens handled an anthrax-contaminated letter.<br>2001-09-28: Stevens hospitalized.<br>2001-10-05: Stevens died."},
    {"name": "New York City, NY", "coords": [40.7128, -74.0060],
     "event": "2001-09-21: Johanna Huden noticed symptoms.<br>2001-10-10: NBC employee tested positive.<br>2001-10-12: Erin O’Connor developed anthrax."},
    {"name": "NBC Office, New York City, NY", "coords": [40.755, -73.984],
     "event": "2001-09-25: Erin O’Connor handled a threatening letter postmarked from Trenton."},
    {"name": "Hamilton Township, NJ", "coords": [40.2116, -74.6963],
     "event": "2001-09-26: Postal worker Richard Morgano developed cutaneous anthrax."},
    {"name": "American Media Inc., Boca Raton, FL", "coords": [26.3571, -80.0831],
     "event": "2001-10-08: FBI launched a criminal investigation; anthrax found in the building."},
    {"name": "The Hart Senate Office Building, Washington, D.C.", "coords": [38.8903, -77.0091],
     "event": "2001-10-16: Senator Tom Daschle’s office received a letter containing anthrax spores."},
    {"name": "Brentwood Mail Facility, Washington, D.C.", "coords": [38.9276, -76.9939],
     "event": "2001-10-19: Workers developed inhalation anthrax.<br>2001-10-22: Facility closed after two deaths."},
    {"name": "Fort Detrick, MD", "coords": [39.6243, -77.4163],
     "event": "2002-04-01: Spores traced to Bruce Ivins’ office.<br>2010-04-01: FBI confirmed spores originated here."},
    {"name": "Oxford, CT", "coords": [41.4334, -73.1168],
     "event": "2001-11-21: Ottilie Lundgren, 94, became the fifth person to die from inhalation anthrax."},
]

# Add markers for all locations
for loc in event_locations:
    folium.Marker(
        location=loc["coords"],
        popup=f"<b>{loc['name']}</b><br>{loc['event']}",
        tooltip=loc["name"]
    ).add_to(anthrax_map)

# Save the initial map as HTML
map_file = "anthrax_events_map.html"
anthrax_map.save(map_file)

# Define the timeline iframe code
timeline_code = """
<div style="display: flex; height: 100vh;">
    <!-- Map container -->
    <div id="map" style="flex: 3;"></div>

    <!-- Timeline container -->
    <div style="flex: 1; background: white; overflow-y: auto; padding: 10px; border-left: 2px solid black;">
        <iframe src='https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1BPnam7nVGZlzx7PPaF6rij3jbN6m2c7qr2p7JbKeGk4&font=Default&lang=en&initial_zoom=2&height=650'
                width='100%' height='100%' webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0'>
        </iframe>
    </div>
</div>
"""

# Inject the timeline code into the HTML map file
with open(map_file, "r") as file:
    map_html = file.read()

# Replace the <body> tag to include the timeline layout
map_html = map_html.replace('<body>', f'<body>{timeline_code}')

# Save the final file with the timeline integrated
final_map_file = "INT200_NGist_anthrax_events_map_with_timeline.html"
with open(final_map_file, "w") as file:
    file.write(map_html)

print(f"Map with timeline integrated created! Open '{final_map_file}' in your browser to view.")
