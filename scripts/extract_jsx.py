with open('android/app/src/main/assets/www/index.html', 'r') as f:
    content = f.read()
start_tag = '<script type="text/babel" data-presets="react">'
start = content.find(start_tag) + len(start_tag)
end = content.rfind('</script>')
jsx_code = content[start:end]
with open('/tmp/game.jsx', 'w') as f:
    f.write(jsx_code)
print(f"Extracted {len(jsx_code)} chars")
