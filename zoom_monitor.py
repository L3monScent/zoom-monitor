import requests
import sys

def get_zoom_status():
    url = "https://status.zoom.us/api/v2/summary.json"
    response = requests.get(url)
    data = response.json()
    print("=== ZOOM Service STATUS === \n")

    all_operational = True

    for component in data["components"]:
        name = component["name"]
        status = component["status"]
        if status == "operational":
            icon = "✅"
        else:
            icon = "❌"
            all_operational = False
        print(f"{icon} {name}: {status}")
    if all_operational:
        SystemExit(0)
    else:
        SystemExit(1)
        
get_zoom_status()
