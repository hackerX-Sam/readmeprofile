import sys
import re

# We will read the current file and replace the existing Unicode Bold font with the new font.
# Current Bold Sans-Serif
bold_sans = [
    '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', 
    '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭'
]
# ASCII
ascii_upper = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
# Monospace
mono = [
    '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', 
    '𝙽', '𝙾', '𝙿', '𝚀', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉'
]
# Double Struck
double = [
    '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 
    'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ'
]

# We will apply Double Struck this time (it's very "aesthetic" and popular for portfolios)
font_to_apply = double

# Map current characters in README to new characters
bold_to_new = dict(zip(bold_sans, font_to_apply))

files = ['README.md', r'C:\Users\samir\.gemini\antigravity-ide\brain\ba25574a-12df-4162-ab8b-5d03b7fb930f\github-profile-readme.md']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace character by character
    new_content = ""
    for char in content:
        new_content += bold_to_new.get(char, char)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Font updated successfully to Double Struck.")
