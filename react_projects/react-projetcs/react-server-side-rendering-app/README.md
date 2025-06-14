# Step-by-Step: React SSR with Express (Professional Setup) ❌❌❌ NOT WORKING

---

## 1. Setup project directory

<pre class="overflow-visible!" data-start="249" data-end="309"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">bash</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>mkdir</span><span> react-ssr-app
</span><span>cd</span><span> react-ssr-app
npm init -y
</span></span></code></div></div></pre>

---

## 2. Install dependencies

<pre class="overflow-visible!" data-start="344" data-end="494"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">bash</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>npm install react react-dom express
npm install @babel/core @babel/preset-env @babel/preset-react @babel/register ignore-styles --save-dev
</span></span></code></div></div></pre>

* `react`, `react-dom`: React libraries
* `express`: Node.js server framework
* Babel packages: To transpile JSX and modern JavaScript on server side
* `ignore-styles`: To prevent errors when importing CSS on the server

---

## 3. Configure Babel

Create a `.babelrc` file for Babel config:

<pre class="overflow-visible!" data-start="789" data-end="862"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">json</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"presets"</span><span>:</span><span></span><span>[</span><span>"@babel/preset-env"</span><span>,</span><span></span><span>"@babel/preset-react"</span><span>]</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

---

## 4. Create React component (e.g., `App.jsx`)

<pre class="overflow-visible!" data-start="917" data-end="1129"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">jsx</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-jsx"><span><span>// src/App.jsx</span><span>
</span><span>import</span><span></span><span>React</span><span></span><span>from</span><span></span><span>'react'</span><span>;

</span><span>const</span><span></span><span>App</span><span> = (</span><span></span><span>) => {
  </span><span>return</span><span> (
    </span><span><span class="language-xml"><div</span></span><span>>
      </span><span><h1</span><span>>React SSR Example</span><span></h1</span><span>>
      </span><span><p</span><span>>This is rendered on the server.</span><span></p</span><span>>
    </span><span></div</span><span>>
  );
};

</span><span>export</span><span></span><span>default</span><span></span><span>App</span><span>;
</span></span></code></div></div></pre>

---

## 5. Create server entry point (`server.js`)

<pre class="overflow-visible!" data-start="1183" data-end="2236"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">js</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-js"><span><span>// server.js</span><span>
</span><span>require</span><span>(</span><span>'@babel/register'</span><span>)({
  </span><span>ignore</span><span>: [</span><span>/node_modules/</span><span>],
  </span><span>presets</span><span>: [</span><span>'@babel/preset-env'</span><span>, </span><span>'@babel/preset-react'</span><span>],
});
</span><span>require</span><span>(</span><span>'ignore-styles'</span><span>);

</span><span>const</span><span> express = </span><span>require</span><span>(</span><span>'express'</span><span>);
</span><span>const</span><span></span><span>React</span><span> = </span><span>require</span><span>(</span><span>'react'</span><span>);
</span><span>const</span><span></span><span>ReactDOMServer</span><span> = </span><span>require</span><span>(</span><span>'react-dom/server'</span><span>);
</span><span>const</span><span></span><span>App</span><span> = </span><span>require</span><span>(</span><span>'./src/App'</span><span>).</span><span>default</span><span>;

</span><span>const</span><span> app = </span><span>express</span><span>();

app.</span><span>use</span><span>(express.</span><span>static</span><span>(</span><span>'public'</span><span>)); </span><span>// for static assets like CSS, JS</span><span>

app.</span><span>get</span><span>(</span><span>'*'</span><span>, </span><span>(req, res</span><span>) => {
  </span><span>const</span><span> appString = </span><span>ReactDOMServer</span><span>.</span><span>renderToString</span><span>(</span><span>React</span><span>.</span><span>createElement</span><span>(</span><span>App</span><span>));

  </span><span>const</span><span> html = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>React SSR</title>
    </head>
    <body>
      <div id="root"></span><span>${appString}</span><span></div>
      <script src="/client.js"></script> <!-- client bundle -->
    </body>
    </html>
  `;

  res.</span><span>send</span><span>(html);
});

</span><span>const</span><span></span><span>PORT</span><span> = process.</span><span>env</span><span>.</span><span>PORT</span><span> || </span><span>3000</span><span>;

app.</span><span>listen</span><span>(</span><span>PORT</span><span>, </span><span>() =></span><span> {
  </span><span>console</span><span>.</span><span>log</span><span>(</span><span>`SSR server running on http://localhost:${PORT}</span><span>`);
});
</span></span></code></div></div></pre>

---

## 6. Client-side hydration (`client.js`)

Create a client entry file to hydrate the React app in the browser:

<pre class="overflow-visible!" data-start="2355" data-end="2538"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">jsx</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-jsx"><span><span>// src/client.js</span><span>
</span><span>import</span><span></span><span>React</span><span></span><span>from</span><span></span><span>'react'</span><span>;
</span><span>import</span><span> { hydrateRoot } </span><span>from</span><span></span><span>'react-dom/client'</span><span>;
</span><span>import</span><span></span><span>App</span><span></span><span>from</span><span></span><span>'./App'</span><span>;

</span><span>hydrateRoot</span><span>(</span><span>document</span><span>.</span><span>getElementById</span><span>(</span><span>'root'</span><span>), </span><span><span class="language-xml"><App</span></span><span> />);
</span></span></code></div></div></pre>

---

## 7. Bundle client-side code with Webpack

Install webpack and loaders:

<pre class="overflow-visible!" data-start="2619" data-end="2709"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">bash</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>npm install webpack webpack-cli webpack-node-externals babel-loader --save-dev
</span></span></code></div></div></pre>

Create `webpack.client.config.js`:

<pre class="overflow-visible!" data-start="2747" data-end="3169"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">js</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-js"><span><span>// webpack.client.config.js</span><span>
</span><span>const</span><span> path = </span><span>require</span><span>(</span><span>'path'</span><span>);

</span><span>module</span><span>.</span><span>exports</span><span> = {
  </span><span>entry</span><span>: </span><span>'./src/client.js'</span><span>,
  </span><span>output</span><span>: {
    </span><span>path</span><span>: path.</span><span>resolve</span><span>(__dirname, </span><span>'public'</span><span>),
    </span><span>filename</span><span>: </span><span>'client.js'</span><span>,
  },
  </span><span>module</span><span>: {
    </span><span>rules</span><span>: [
      {
        </span><span>test</span><span>: </span><span>/\.jsx?$/</span><span>,
        </span><span>exclude</span><span>: </span><span>/node_modules/</span><span>,
        </span><span>use</span><span>: </span><span>'babel-loader'</span><span>,
      },
    ],
  },
  </span><span>resolve</span><span>: {
    </span><span>extensions</span><span>: [</span><span>'.js'</span><span>, </span><span>'.jsx'</span><span>],
  },
  </span><span>mode</span><span>: </span><span>'development'</span><span>,
};
</span></span></code></div></div></pre>

---

## 8. Add scripts to `package.json`

<pre class="overflow-visible!" data-start="3213" data-end="3376"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">json</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>"scripts"</span><span>:</span><span></span><span>{</span><span>
  </span><span>"build:client"</span><span>:</span><span></span><span>"webpack --config webpack.client.config.js"</span><span>,</span><span>
  </span><span>"start"</span><span>:</span><span></span><span>"node server.js"</span><span>,</span><span>
  </span><span>"dev"</span><span>:</span><span></span><span>"npm run build:client && npm start"</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

---

## 9. Build and run

<pre class="overflow-visible!" data-start="3404" data-end="3446"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">bash</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>npm run build:client
npm start
</span></span></code></div></div></pre>

Visit `http://localhost:3000` to see server-side rendered React app.
