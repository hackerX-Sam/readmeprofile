import sys
import re

# Sans-Serif Bold mapping
bold_map = {
    'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜',
    'J': '𝗝', 'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥',
    'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭'
}

def to_bold(text):
    return ''.join(bold_map.get(c, c) for c in text)

replacements = {
    "WHO AM I": to_bold("WHO AM I"),
    "TECH STACK": to_bold("TECH STACK"),
    "PROGRAMMING LANGUAGES": to_bold("PROGRAMMING LANGUAGES"),
    "FRONTEND DEVELOPMENT": to_bold("FRONTEND DEVELOPMENT"),
    "BACKEND DEVELOPMENT": to_bold("BACKEND DEVELOPMENT"),
    "DATABASES": to_bold("DATABASES"),
    "TOOLS & PLATFORMS": to_bold("TOOLS & PLATFORMS"),
    "CONTRIBUTION CALENDAR": to_bold("CONTRIBUTION CALENDAR"),
    "THE NUMBERS": to_bold("THE NUMBERS"),
    "FEATURED MASTERPIECES": to_bold("FEATURED MASTERPIECES"),
    "CYBERSHIELDPRO V1.3": to_bold("CYBERSHIELDPRO V1.3"),
    "OBSERVEX": to_bold("OBSERVEX"),
    "EVENTRA": to_bold("EVENTRA"),
    "SAVYA PRAJAPATI": to_bold("SAVYA PRAJAPATI")
}

files = ['README.md', r'C:\Users\samir\.gemini\antigravity-ide\brain\ba25574a-12df-4162-ab8b-5d03b7fb930f\github-profile-readme.md']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Font updated successfully.")
