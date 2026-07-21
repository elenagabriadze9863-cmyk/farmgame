const babel = require('@babel/core');
const fs = require('fs');

const jsx = fs.readFileSync('/tmp/game.jsx', 'utf8');
const result = babel.transformSync(jsx, {
  presets: ['@babel/preset-react', '@babel/preset-env'],
  filename: 'game.jsx'
});
fs.writeFileSync('android/app/src/main/assets/www/game.js', result.code);
console.log('Compiled OK, size:', result.code.length);
