import requests

def get_zoom_status():
    url = "https://status.zoom.us/api/v2/summary.json"
    response = requests.get(url)
    data = response.json()
    print("=== ZOOM Service STATUS === \n")

    for component in data["components"]:
        name = component["name"]
        status = component["status"]
        if status == "operational":
            icon = "✅"
        else:
            icon = "❌"
        print(f"{icon} {name}: {status}")

get_zoom_status()
