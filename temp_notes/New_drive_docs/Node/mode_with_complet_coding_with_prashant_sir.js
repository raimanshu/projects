const react = require("react")

// NodeJs Features (Added)
Non-blocking I/O 
Networking Support
File System Access
Server Side Capabilities 
Modules 

// NodeJs Features (Removd)
Window Object 
DOM Manipulation
BOM (Browser Object Model)
Web specific API's

// Javascript on Client
Displays web page 
User Clicks 
Updates Content 
Loads file 

// Javascript on Server
Database Management
Authentication 
Authorization
Input Validation
Session Management 
API Management 
Error Handling
Security measures 
Data Encryption 
Logging and Monitoring

// Client code vs Server code
Environment access 
Security 
Performance 
Resource Utilization 
Data Handling 
Asynchronous Operations 
Session Management 
Scalability 

// Other uses of NodeJs
Local Utility Scripts 
Internet of Things
Scripting for Automation
Real Time Applications
Desktop Applications
Build tools like webpack, grunt, gulp, etc 

// Server Architecture with NodeJs


// Installation of NodeJs
What is IDE 
Need of IDE 
what is REPL 

// First Node Server
How DNS Works? - Domain Name Entry, DNS Query, DNS Server, Browser Connects , DNS Resolver, Root DNS,   Top level domain DNS, Authoritative DNS, Browser Connects
How Web works? - Client Request Initiation, DNS Resolution, TCP Connection, HTTP Request, Server Processing, HTTP Response, Network Transmission, Client Recieves Response, Rendering  
What are protocols? - HTTP, HTTPS, TCP
Node Core Modules ? - built in modules, (fs, http, https, path, path.os, events, crypto, url)
Require Kwyword
Creating first node server 

// Request and Response in NodeJs 
Node Life Cycle and event loop
How to exit event loop  - proces.exit()
Understand Request Object - req.url, req.method, req.headers, req.body, 
Sending Response - res.setHeader(), res.write(), res.end(), res.writeHead()
Routing Requests 
taking user Input - res.write(), res.end()
Redirecting Requests - res.statusCode

// Parsing Requests 
Streams - stream of chunks, Duplex Stream, read buffer, write buffer, 
Chunks - smallest unit of stream of data
Buffers - maintaing sequence of chunks
Reading Chunks - res.on("data", (chunk) => {...})
Buffering Chunks - store and sequencing the chunks for processing, res.on("end", () => {Buffer.concat(chunks).toString()})
Parsing Requests - new URLSearchParams(bufferData)
Using Modules - moduleRunnerTransform.exports 


// Event Loop 
Event Driven - event queue, event loop
Single Threaded - main thread, worker thread,  trigger callback, register callback, 
V8 vs libuv - IMPORTANT
Node Runtime - v8, libuv, event queue, event loop,
Event Loop - timers, pending callbacks, idle prepare, poll, check, close callbacks 
Async Code - 
Blocking Code - writeFileSync() vs writeFile

// NPM & Tools
install material icons 
npm init 
npm scripts - npm init 
npm packages - npm, package, package.json, package-lock.json, versioning, local/global, registry, examples - express, react, lodash
installing packages - --save, --save-dev, -g, --save-exact, --force, 
installing nodemon
using nodemon 

// Errors and Debugging 
types of error - 
syntax error -
runtime error -
logical error -
using the debugger - 
debugger with async code -
restart debug with noemon - modify launch.json

// Starting with Express.json 
What is express.js - minimal and flexible web application framework, 
Need of express.js -
installing of express.js - 
adding middleware - const app = express(), app.use((req, res, next) => {...}), 
sending response - app.use((req, res, next) => {res.send() })
express deep dive - 
handling routes - app.get(), app.post(), app.put(), app.delete(), app.patch(), app.all(), app.use()

// Express.js Deep dive 
Parsing Requests - body-parser, bodyParser.urlencoded()
Express Router - express.Router(), express.urlencoded(), 
Adding 404 - res.status().send("...")
common paths - userRouter("/admin", adminRoutes)
adding html files - 
serving html files - require('path'), res.sendFile(path.join(__dirname, 'views', 'index.html'))
using file helper - utils, module.exports = path.dirname(require.main.filename)

// Styling using tailwind css 
serving static files - public folder for css and assets, app.use(express.static(path.join(__dirname, 'public')))    
introduction to tailwind css - responsive mobile first, utility first, highly customizeable, responsive design, no pre-defined components, purge css, fast development
utility classes - 
installing extension - tailwind css intellisense, npm install -D tailwindcss postcss autoprefixer 
including tailwind css - 
installing tailwind css -
using tailwind css -

// Dynamic UI using EJS (Embeded JavaScript)
Need of dynamic Ui - personalized content, dynamic data delivery, security and access control, localization and internationalization, API versatility 
sharing using global variables - req.body
what is EJS - HTML with JS, simple syntax, easy to learn, template reuse, flexible logic, .html -> .ejs 
installing EJS - npm install ejs --save
using EJS templates - app.set('view-engine', 'ejs'), app.set('views', 'views'), res.render('index', {title: 'Home'}),<% pure_js %>   <%= variable_data %>
working with partials - <%- include('partials/header') %>

// Model View Controller 
Separation of concerns - Model, View, Controller 
Adding first controller -
Adding all Controllers - 
Adding 404 Contents - 
Adding Models - 
Writting data to files -
Nodemon causing problems -
Reading files from files -

// Dynamic Path & Model Deep Dive 
What are dynamic paths - path parameters, query parameters
Addding Home details paths - 
Showing Real Home Data - 
Adding favourites feature -
Adding favourites model - 
Edit Home: Adding feature skelton - 
Edit Home: Showing existing data -
Edit Home: handling existing request -
Adding delete feature - 
Removing Home from favourites - 

// Introduction to SQL 
What is Database - store data, enable data management, facilitate quick access, ensure data integrity, Support multiple useResolvedPath, secure data
Introduction to SQl DB - vertical scalability, relationships, relational model, fixed schema, Relational model use of SQl, ACID Complience, complex Queries,
Introduction to NoSQL DB - Flexible Schema, Duplicacy over relations, horizontal scalability, performance, key-value, graph, wide column, document
SQL vs NoSQL - 
Installing MySQL -
Connecting App to DB - cosnt mysql = require('mysql2'), mysql.createPool({...}), pool.promise(), 
Creating homes to Tables -
Querying homes in App - const db = require('../util/database'), db.execute('SELECT * FROM homes'),
Adding DB in Models -
Adding Home in Model - 
Implementing Model using Where - 


// Introduction to mongoDB
what is mongoDB - mongoDB, the name, NoSQL document database, Dynamic schema, high performance, scalability, high availability, rich query capabilities, Geospatial and text search, cross-platform campatibility, easy integration,  
setting up MongoDB - const mongodb = require('mongodb'), const mongoClient = mongodb.MongoClient,
Installing MongoDB Driver - 
Creating MongoDB Connection - 
Saving a Home - 
Installing MongoDB Compass - 
Install MongoDB for VS code - 
Fetching all Homes - 
fetching one home - 
Support editing and delete - 
Adding mongo DB to favourite - 

// Introduction to mongoose 
what is mongoose - ODM/ORM, schema based solution, data validation, easy interaction with mongoDB, supports middleware, helps manage relationships
setting up mongoose - 
create home schema - const mongoose = require('mongoose'), const homeSchema = new mongoose.Schema({...}), mongoose.model('Home', homeSchema),
saving home using mongoose -
fetching homes -
fetching one home -
editing a home -
deleate a home -
using mongoose for favourite -
fetching relations -

// Cookies and Sessions 
what are cookies - 
adding login functionality -
checking login functionality -
using a cookie -
define the logout feature -
problem with cookies -
what are sessions - server side storage mechanisms, express-session, 
installing session package -
creating a sessions - cosnt session = require('express-session'), app.use(session({...})),
saving sessions in DB - const MongoDBStore = require('connect-mongodb-session')(session), const store = new MongoDBStore({...}),

// Authentication and Authorization
what is authentication - 
what is authorization -
Session based authentication -
authentication vs authorization -
signup UI - 
using express validator -
addding user model -
encrypting password - bycryptjs
implementing login -
adding user functions -

// File upload and download 
adding a file picker - multer
creating a multipart form -
handling multipart form data -
saving image file -
custom file name -
restricting upload file types - 
handling edits - 
serving saved data - 
serving files after auth - 
deleting files -

// REST API / JSON Requests 
What are async requests -
what are REST APIs -
Decoupling frontend and backend -
routes and http methods -
REST core concepts -
First API todo app -
API for fetch items -
API for deleating items -
Improving UI elements - 
adding complete item functionality - 
Deploying React app - 
