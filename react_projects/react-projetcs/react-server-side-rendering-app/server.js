// server.js
require('@babel/register')({
  ignore: [/node_modules/],
  presets: ['@babel/preset-env', '@babel/preset-react'],
});
require('ignore-styles');

const express = require('express');
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const App = require('./src/App').default;

const app = express();

app.use(express.static('public')); // for static assets like CSS, JS

app.get('*', (req, res) => {
  const appString = ReactDOMServer.renderToString(React.createElement(App));

  const html = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>React SSR</title>
    </head>
    <body>
      <div id="root">${appString}</div>
      <script src="/client.js"></script> <!-- client bundle -->
    </body>
    </html>
  `;

  res.send(html);
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`SSR server running on http://localhost:${PORT}`);
});
