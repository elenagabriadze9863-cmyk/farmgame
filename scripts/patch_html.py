import re

with open('android/app/src/main/assets/www/index.html', 'r') as f:
    content = f.read()

print(f"Input size: {len(content)}")

# Replace CDN with local files
content = content.replace('https://unpkg.com/react@18/umd/react.production.min.js', 'react.js')
content = content.replace('https://unpkg.com/react-dom@18/umd/react-dom.production.min.js', 'react-dom.js')
content = content.replace('https://unpkg.com/lucide-react@0.383.0/dist/umd/lucide-react.js', 'lucide.js')
content = content.replace('https://cdn.tailwindcss.com', 'tailwind.js')

# Remove babel script tag
content = re.sub(r'<script src="[^"]*babel[^"]*"[^>]*></script>\n?', '', content)

# Find the babel script block — from opening tag to its closing </script>
start = content.find('<script type="text/babel"')
if start == -1:
    print("ERROR: babel block not found!")
else:
    # Find the closing tag AFTER the start position
    end = content.find('</script>', start) + len('</script>')
    print(f"Replacing babel block: chars {start} to {end}")
    content = content[:start] + '<script src="game.js"></script>' + content[end:]

print(f"Output size: {len(content)}")

with open('android/app/src/main/assets/www/index.html', 'w') as f:
    f.write(content)
print("Done")
