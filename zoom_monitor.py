import requests
import sys

def get_zoom_status():
    url = "https://status.zoom.us/api/v2/summary.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception:
        print("Failed to fetch Zoom status\n")
        sys.exit(2)

    print("=== ZOOM Service STATUS ===\n")

    all_operational = True

    for component in data.get("components", []):
        name = component.get("name", "Unknown")
        status = component.get("status", "unknown")
        if status == "operational":
            icon = "✅"
        else:
            icon = "❌"
            all_operational = False
        print(f"{icon} {name}: {status}")
    if all_operational:
        sys.exit(0)
    else:
        sys.exit(1)

get_zoom_status()
