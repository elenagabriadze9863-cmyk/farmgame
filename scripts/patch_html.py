import re
with open('android/app/src/main/assets/www/index.html', 'r') as f:
    content = f.read()
content = content.replace('https://unpkg.com/react@18/umd/react.production.min.js', 'react.js')
content = content.replace('https://unpkg.com/react-dom@18/umd/react-dom.production.min.js', 'react-dom.js')
content = content.replace('https://unpkg.com/lucide-react@0.383.0/dist/umd/lucide-react.js', 'lucide.js')
content = content.replace('https://cdn.tailwindcss.com', 'tailwind.js')
content = re.sub(r'<script src="[^"]*babel[^"]*"[^>]*></script>\n?', '', content)
start = content.find('<script type="text/babel"')
end = content.rfind('</script>') + len('</script>')
content = content[:start] + '<script src="game.js"></script>' + content[end:]
with open('android/app/src/main/assets/www/index.html', 'w') as f:
    f.write(content)
print("Done")
