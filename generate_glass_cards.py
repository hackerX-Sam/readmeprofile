import urllib.request, base64
import os

projects = [
    ("CyberShieldPro v1.3", "cybershieldpro-v1.3"),
    ("ObserveX", "observeX---realtime-desktop-monitoring-system"),
    ("Eventra", "EVENTRA-real-time-event-streaming-monitoring-platform-"),
    ("Savya Prajapati", "savyaprajapati")
]

os.makedirs('assets', exist_ok=True)

for i, (title, repo) in enumerate(projects):
    url = f'https://opengraph.githubassets.com/1/hackerX-Sam/{repo}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            img_data = response.read()
            b64 = base64.b64encode(img_data).decode('utf-8')
    except Exception as e:
        print(f"Error downloading {repo}: {e}")
        b64 = ""
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 420">
    <defs>
        <linearGradient id="glassGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255, 255, 255, 0.15)" />
            <stop offset="100%" stop-color="rgba(255, 255, 255, 0.02)" />
        </linearGradient>
        <linearGradient id="borderGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255, 255, 255, 0.6)" />
            <stop offset="100%" stop-color="rgba(255, 255, 255, 0.0)" />
        </linearGradient>
        <filter id="shadow">
            <feDropShadow dx="0" dy="10" stdDeviation="15" flood-color="#000000" flood-opacity="0.4" />
        </filter>
        <clipPath id="imageClip">
            <rect x="30" y="75" width="540" height="284" rx="15" />
        </clipPath>
    </defs>
    
    <!-- Shadow and Base Rect -->
    <rect x="15" y="15" width="570" height="390" rx="25" fill="url(#glassGradient)" filter="url(#shadow)" stroke="url(#borderGradient)" stroke-width="1.5" />
    
    <!-- Title -->
    <text x="300" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-weight="bold" font-size="22" fill="#ffffff" text-anchor="middle" letter-spacing="1">{title.upper()}</text>
    
    <!-- Embedded OpenGraph Image -->
    <image href="data:image/jpeg;base64,{b64}" x="30" y="75" width="540" height="284" preserveAspectRatio="xMidYMid slice" clip-path="url(#imageClip)" />
    
</svg>"""
    
    with open(f'assets/glass_card_{i+1}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

print("Generated all glassmorphic SVGs.")
