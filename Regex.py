import re

# https://anyflipdownload.com/njbp/ired/#pages
# https://anyflipdownload.com/njbp/ired/mobile/#pages
# https://online.anyflip.com/njbp/ired/files/mobile/1.jpg
# https://anyflip.com/njbp/ired

# https://anyflipdownload.com/nlqlf/gizt/#pages

# example URLs
url = input()

before = "https://online.anyflip.com"
after = "/files/mobile/"

# pattern to extract the desired substring
pattern = r"/\w+/\w+/?"

# extract substring from URL 1
match = re.search(pattern, url)
substring = match.group()
print(substring)

# check if string ends with slash
if substring.endswith("/"):
    substring = substring.rstrip(substring[-1])
    full_url = before + substring + after
else:
    full_url = before + substring + after

print(full_url)
