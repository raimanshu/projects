
# https://www.simplilearn.com/tutorials/nodejs-tutorial/nodejs-interview-questions
# https://www.turing.com/interview-questions/node-js
# https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/

'''
✅ - okay need to read onece
❌ - need to understand
⭐ - asked in interview 
👉 - important may be
🤔 - Not understand
'''

# What is Node.js and Where can you use it?
'''open-source, cross-platform JavaScript runtime environment engine used for executing JavaScript code outside the browser. It is built on Google Chrome's V8 JavaScript engine.'''
# Why use Node.js?
'''Fast Performance, NPM Ecosystem, Real-Time Applications, Unified Codebase, Easy for JavaScript Developers'''
# 👉How does Node.js work?

# Why is Node.js Single-threaded?
'''NodeJS is single-threaded because it's based on the asynchronous, non-blocking nature of JavaScript.'''
# 👉If Node.js is single-threaded, then how does it handle concurrency?
'''NodeJS is single-threaded, but it can handle concurrency efficiently through its asnchronous, event-driven, non-blocking I/O model. While the event loop in NodeJS runs on a single thread, it doesn’t block the execution of other tasks when waiting for I/O operations, such as file reads or database queries. Instead, NodeJS delegates these I/O tasks to the system's kernel, allowing it to continue processing other requests. Once the I/O operation is complete, the corresponding callback is added to a queue and processed by the event loop. This non-blocking approach enables NodeJS to handle multiple concurrent tasks without waiting for each one to finish sequentially.'''
# 👉Explain the difference between NodeJS and server-side scripting languages like Python - https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/

# Explain callback in Node.js.
# What are the advantages of using promises instead of callbacks?
'''A promise is an advancement of callbacks in NodeJS. In other words, a promise is a JavaScript object that is used to handle all the asynchronous data operations. While developing an application, you may encounter that you are using a lot of nested callback functions, which causes a problem of callback hell. Promises solve this problem of callback hell. '''
# How would you define the term I/O? 
# How is Node.js most frequently used?
# Explain the difference between frontend and backend development?
# What is NPM?
''' It is the package manager for the NodeJS environment. It is used to install, share, and manage dependencies (libraries, tools, or packages) in JavaScript applications.
- NPM uses a package.json file in NodeJS projects to track project dependencies, versions, scripts, and metadata like the project's name and version.
- NPM is accessed by a command-line interface (CLI). Common commands include npm install to install packages, npm update to update them, and npm uninstall to remove them.'''
# 👉What are the modules in Node.js?
'''In a NodeJS Application, a Module can be considered as a block of code that provides a simple or complex functionality that can communicate with external application. Modules can be organized in a single file or a collection of multiple files/folders. They are useful because of their reusability and ability to reduce the complexity of code into smaller pieces. Examples of modules are. http, fs, os, path, etc.'''
# What is the purpose of the 'require' keyword in NodeJS? -  used to include and import modules
# What is the purpose of the module.Exports?
# Why is Node.js preferred over other backend technologies like Java and PHP?
# What is the difference between Angular and Node.js?
'''
| Key          | NodeJS                                    | Angular                                              |
|--------------|-------------------------------------------|------------------------------------------------------|
| Type         | Server-side runtime env                   | Front-end framework                                  |
| Language     | JavaScript / TypeScript                   | TypeScript (mainly), supports JavaScript            |
| Runs on      | Server                                     | Client (browser)                                     |
| Purpose      | Handle requests & responses               | Build user interfaces                                |
| Performance  | Non-blocking, I/O efficient               | Optimized for large SPAs                             |
| Use          | Backend services, server-side JS          | Dynamic, responsive front-end apps                   |'''
# Which database is more popularly used with Node.js?
# What are some of the most commonly used libraries in Node.js?
'''
- ExpressJS: ExpressJS is a minimal and flexible web application framework for building robust APIs and web apps. It simplifies routing, middleware handling, and request/response management.
- Mongoose: An Object Data Modeling (ODM) library for MongoDB and NodeJS, it helps in managing data relationships, schema validation, and business logic.'''
# What are the pros and cons of Node.js?
# What is the command used to import external libraries? - const express = require('express');
# What does event-driven programming mean?
'''Event-driven programming is used to synchronize the occurrence of multiple events and to make the program as simple as possible. The basic components of an Event-Driven Program are:
- A callback function ( called an event handler) is called when an event is triggered.
- An event loop that listens for event triggers and calls the corresponding event handler for that event.'''
# What is an Event Loop in Node.js?
'''The event loop in NodeJS is a mechanism that allows it to handle multiple asynchronous tasks concurrently within a single thread. It continuously listens for events and executes associated callback functions.'''
# Differentiate between process.nextTick() and setImmediate()? - https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/
# What is an EventEmitter in Node.js?
'''an Event Emitteris a class that allows objects to emit events and register listeners (callbacks) to handle those events. It is part of the events module and is commonly used to handle asynchronous events and to implement an observer pattern, where an object (the emitter) triggers events, and other objects (listeners) respond to those events.
Key Concepts of EventEmitter:
- Emitting Events: Objects can emit custom events by calling the .emit() method. This triggers all listeners that are registered for that event.
- Listening to Events: You can listen for specific events using the .on() or .once() methods. .on() will listen for the event indefinitely, while .once() will listen for the event only once.
- Event Handling: Event listeners (callbacks) are executed when the corresponding event is emitted. These listeners are often used to handle asynchronous operations like HTTP requests or file I/O.'''
# What is a cluster in NodeJS?
'''Due to a single thread in NodeJS, it handles memory more efficiently because there are no multiple threads due to which no thread management is needed. Now, to handle workload efficiently and to take advantage of computer multi-core systems, cluster modules are created that provide us the way to make child processes that run simultaneously with a single parent process.'''
# What are the two types of API functions in Node.js?
'''
- Asynchronous, non-blocking functions - mostly I/O operations which can be fork out of the main loop.
- Synchronous, blocking functions - mostly operations that influence the process running in the main loop.'''
# What is the package.json file?
'''package.json in NodeJS is a metadata file that contains project-specific information such as dependencies, scripts, version, author details, and other configuration settings required for managing and building the project.'''
# How would you use a URL module in Node.js?
# What is the Express.js package?
# How do you create a simple Express.js application?
# What are streams in Node.js?
'''streams are a powerful way to handle data in chunks rather than loading the entire data into memory. Streams allow for the efficient processing of large volumes of data, especially in situations where the data size is too large to fit into memory all at once.'''
# How to read command line arguments in NodeJS?
'''
Command-line arguments (CLA) are strings of text used to pass additional information to a program when an application is running through the command line interface of an operating system. 
let arguments = process.argv ; 
console.log(arguments) ;
'''
# Explain the NodeJS Redis module.
'''Redis is an Open Source store for storing data structures. It is used in multiple ways. It is used as a database, cache, and message broker. It can store data structures such as strings, hashes, sets, sorted sets, bitmaps, indexes, and streams. Redis is very useful for NodeJS developers as it reduces the cache size which makes the application more efficient. However, it is very easy to integrate Redis with NodeJS applications.'''
# How do you install, update, and delete a dependency?
# How do you create a simple server in Node.js that returns Hello World?
'''
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello, World!');
});
server.listen(3000, () => {
  console.log('Server is running at http://localhost:3000/');
});'''
# Explain asynchronous and non-blocking APIs in Node.js.
'''Asynchronous APIs in Node.js allow for non-blocking operations, enabling concurrent execution of tasks without blocking the main thread. Non-blocking APIs enable efficient handling of multiple requests and asynchronous operations, improving overall application performance.'''
# How do we implement async in Node.js?
# What is a callback function in Node.js?
# What is REPL in Node.js?
''' Read, Evaluate, Print, and Loop. It is a computer environment similar to the shell which is useful for writing and debugging code as it executes the code in on go.'''
# What is control flow in NodeJS?
'''refers to the sequence in which statements and functions are executed. It manages the order of execution, handling asynchronous operations, callbacks, and error handling to ensure smooth program flow.'''
# What is the control flow function?
# How does control flow manage the function calls?
# What is the difference between fork() and spawn() methods in Node.js? - https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/
'''
| Key           | spawn()                                         | fork()                                                       |
|---------------|--------------------------------------------------|---------------------------------------------------------------|
| Purpose       | Launch any process with a given command         | Spawn new NodeJS process                                      |
| IPC Support   | No built-in IPC (needs setup)                   | Built-in IPC for parent-child messaging                       |
| Returns       | ChildProcess object                             | ChildProcess object (with IPC support)                        |
| Usage         | Run external cmds or scripts (e.g., shell)      | Run NodeJS scripts with messaging                             |
| Example       | `spawn('ls', ['-lh', '/usr'])`                  | `fork('child.js')`                                            |'''
# What is the buffer class in Node.js?
'''Buffer class in NodeJS is used to perform operations on raw binary data. Generally, Buffer refers to the particular memory location in memory. Buffer and array have some similarities, but the difference is that array can be any type, and it can be resizable. Buffers only deal with binary data, and it can not be resizable. Each integer in a buffer represents a byte. console.log() function is used to print the Buffer instance.'''
# What is piping in Node.js?
'''process of passing the output of one stream directly into another stream. It allows data to flow through multiple streams without needing to store it in memory or temporarily write it to disk. This is a common pattern used in file handling, HTTP requests, and other I/O operations in NodeJS.'''
# What are some of the flags used in the read/write operations in files?
# How do you open a file in Node.js?
# What is callback hell?
'''Callback hell is an issue caused by a nested callback. This causes the code to look like a pyramid and makes it unable to read To overcome this situation, we use promises.'''
# What are the three methods to avoid callback hell? - Using async/await(), Using promises, Using generators
# What is a reactor pattern in Node.js?
# What is a test pyramid in Node.js?
'''The Test Pyramid is a strategy for structuring tests in a software project to ensure efficiency, maintainability, and good coverage. It consists of three levels:
- Unit Tests (Base): Test individual components or functions in isolation. These tests are fast and numerous. Example: Testing a single function like add(1, 2).
- Integration Tests (Middle): Test interactions between components to ensure they work together. These are slower than unit tests but cover more functionality. Example: Testing API routes to ensure they connect properly with the database.
- End-to-End Tests (Top): Test the entire application flow from the user interface to the backend. These are slow and fewer in number. Example: Simulating user login and navigating the application.'''
# For Node.js, why does Google use the V8 engine?
'''
- High Performance: V8 is a highly optimized JavaScript engine designed for speed. It compiles JavaScript directly into machine code, which makes it much faster than interpreted JavaScript.
- Just-In-Time (JIT) Compilation: V8 uses JIT compilation, which translates JavaScript code into machine code during execution, enabling faster execution compared to traditional interpretation.
- Cross-platform Compatibility: V8 is cross-platform due to which the NodeJS application can run on that platforms.
- Integration with Google Chrome: The Google Chrome by using the V8 engine in the NodeJS ensures consistency in performance and features.
- Asynchronous I/O Efficiency: The V8 engine can handle the non-blocking, asynchronous I/O operations which is important for handling the multiple tasks in NodeJS.'''
# Describe Node.js exit codes.
# Explain the concept of middleware in Node.js.
'''function that works between the request and the response cycle. Middleware gets executed after the server receives the request and before the controller sends the response.'''
# What is a .body-parser in NodeJS?
'''Body-parser is the NodeJS body-parsing middleware. It is responsible for parsing the incoming request bodies in a middleware before you handle it. It is an NPM module that processes data sent in HTTP requests.'''
# What is CORS in NodeJS?
'''“Cross-Origin Resource Sharing”. Cross-Origin Resource Sharing is an HTTP-header based mechanism implemented by the browser which allows a server or an API to indicate any origins (different in terms of protocol, hostname, or port) other than its origin from which the unknown origin gets permission to access and load resources. The cors package available in the npm registry is used to tackle CORS errors in a NodeJS application.'''
# Explain the tls module in NodeJS..
'''The tls module provides an implementation of the Transport Layer Security (TLS) and Secure Socket Layer (SSL) protocols that are built on top of OpenSSL. It helps to establish a secure connection on the network.'''
# What are the different types of HTTP requests?
'''
GET: Retrieve data.
POST: Create new resource.
PUT: Update an entire resource.
PATCH: Partially update a resource.
DELETE: Remove a resource.'''
# How would you connect a MongoDB database to Node.js?
'''
const mongoose = require("mongoose");
mongoose.connect("DATABASE_URL_HERE", {
   useNewUrlParser: true,
   useUnifiedTopology: true
});'''
# What is the purpose of NODE_ENV?
'''The NODE_ENV environment variable in NodeJS is used to specify the environment in which the NodeJS application is running. It helps in distinguishing between different stages of the application's lifecycle, such as development, testing, or production, and allows you to customize the behavior of the application based on that environment.'''
# List the various Node.js timing features.
# What is WASI, and why is it being introduced?
# What is a first-class function in Javascript?
# How do you manage packages in your Node.Js project? - using NPM
# How is Node.js better than other frameworks?
# What is a fork in node JS?
'''Fork is a method in NodeJS that is used to create child processes. It helps to handle the increasing workload. It creates a new instance of the engine which enables multiple processes to run the code.'''
# List down the two arguments that async. First, does the queue take as input?
# What is the purpose of the module.exports?
# What tools can be used to assure consistent code style?
#  What is the difference between JavaScript and Node.js?
#  What is the difference between asynchronous and synchronous functions?
'''
| **Synchronous Functions**                                                  | **Asynchronous Functions**                                                           |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Blocks execution until the task completes.                                 | Does not block; other tasks proceed concurrently.                                   |
| Executes tasks sequentially.                                               | Initiates tasks and continues with others.                                          |
| Returns result immediately after completion.                               | Returns a promise, uses callbacks or events.                                        |
| Errors caught easily with try-catch.                                       | Error handling involves callbacks, promises, or async/await.                        |
| Best for simple, predictable execution flows.                              | Ideal for I/O tasks, network calls, parallel operations.                            |
'''
# What are the asynchronous tasks that should occur in an event loop?
# What is the order of execution in control flow statements?
'''
- Execution and queue handling
- Collection of data and storing it
- Handling concurrency
- Executing the next lines of code'''
# What are the input arguments for an asynchronous queue?
#  Are there any disadvantages to using Node.js?
'''
- Single-threaded nature: It may not fully utilize multi-core CPUs, limiting performance.
- NoSQL preference: Relational databases like MySQL aren't commonly used.
- Rapid API changes: Frequent updates can introduce instability and compatibility issues.'''
# What is the primary reason for using the event-based model in Node.js?
#  What is the difference between Node.js and Ajax?
# What is the advantage of using Node.js?
# Does Node run on Windows?
# Can you access DOM in Node?
'''No, you cannot access the DOM in NodeJS because NodeJS is a server-side environment, while the DOM (Document Object Model) is a client-side concept used in browsers to interact with HTML and XML documents.'''
# Why is Node.JS quickly gaining attention from JAVA programmers?
# What are the Challenges with Node.js?
# What is "non-blocking" in node.js?
# How does Node.js overcome the problem of blocking I/O operations?
# How can we use async await in node.js?
# Why should you separate the Express app and server?
# Explain the concept of stub in Node.js.
# What is the framework that is used majorly in Node.js today?
# What are the security implementations that are present in Node.js?
# What is Libuv?
# What are global objects in Node.js?
# Why is assert used in Node.js?
# Why is ExpressJS used?
# How to manage sessions in NodeJS?
'''express-session module. It helps in saving the data in the key-value form. In this module, the session data is not saved in the cookie itself, just the session ID.'''
# What is the use of the connect module in Node.js?
# What's the difference between 'front-end' and 'back-end' development?
# What are LTS releases of Node.js?
# What do you understand about ESLint?
# Define the concept of the test pyramid. Please explain the process of implementing them in terms of HTTP APIs.
# How does Node.js handle the child threads?
# Explain some of the cluster methods in NodeJS
'''
- Fork(): It creates a new child process from the master. The isMaster returns true if the current process is master or else false.
- isWorker: It returns true if the current process is a worker or else false.
- process: It returns the child process which is global.
- send(): It sends a message from worker to master or vice versa. 
- kill(): It is used to kill the current worker.'''
# How to Enhance Node.js Performance through Clustering?
# What is a thread pool, and which library handles it in Node.js?
# How are worker threads different from clusters?
# How to measure the duration of async operations?
# How to measure the performance of async operations?
# What are the types of streams available in Node.js?
'''
- Readable Streams: These streams allow you to read data. For example, reading data from a file or receiving HTTP request data. Example:
fs.createReadStream() or http.IncomingMessage.
- Writable Streams: These streams allow you to write data. For example, writing data to a file or sending HTTP response data. Example:
fs.createWriteStream() or http.ServerResponse.
- Duplex Streams: These are both readable and writable. You can both read and write data using the same stream. Example: A TCP socket.
- Transform Streams: These are a type of duplex stream where the data is transformed as it is read and written. Example: A zlib stream to compress or decompress data.'''
# What is meant by tracing in Node.js?
# Where is package.json used in Node.js?
# What is the difference between readFile and create Read Stream in Node.js?
# What is the use of the crypto module in Node.js?
'''used for encrypting, decrypting, or hashing any type of data. This encryption and decryption basically help to secure and add a layer of authentication to the data. The main use case of the crypto module is to convert the plain readable text to an encrypted format and decrypt it when required.'''
#  How can we implement authentication and authorization in NodeJS?
'''Authentication is the process of verifying a user’s identity while authorization is determining what actions can be performed. We use packages like Passport and JWT to implement authentication and authorization.'''
# What is a passport in Node.js?
'''used for adding authentication features to our website or web app. It implements authentication measure which helps to perform sign-in operations.'''
# Explain the packages used for file uploading in NodeJS.the
'''Multer. The file can be uploaded to the server using this module. There are other modules in the market but Multer is very popular when it comes to file uploading. Multer is a NodeJS middleware that is used for handling multipart/form-data, which is a mostly used library for uploading files.'''
# How to get information about a file in Node.js?
# How does the DNS lookup function work in Node.js?
# Explain the use of the timers module in NodeJS.
'''The Timers module in NodeJS contains various functions that allow us to execute a block of code or a function after a set period. The Timers module is global, we do not need to use require() to import it. 

1. setTimeout() method
The setTimeout() function is used to execute a function once after a specified delay (in milliseconds).
setTimeout(callback, delay, [arg1, arg2, ...]);
callback: The function to be executed after the delay.
delay: The time in milliseconds after which the function is executed.
[arg1, arg2, ...]: Optional arguments that can be passed to the callback function.

2. setImmediate() method
The setImmediate() function is used to execute a callback function immediately after the current event loop cycle, i.e., after the I/O events in the NodeJS event loop have been processed. It is similar to setTimeout() with a delay of 0 milliseconds, but it differs in terms of when the function is executed.
setImmediate(callback, [arg1, arg2, ...]);
callback: The function to be executed.
[arg1, arg2, ...]: Optional arguments to pass to the callback function.

3. setInterval() method
The setInterval() function is used to execute a function repeatedly, with a fixed time delay between each call.
setInterval(callback, delay, [arg1, arg2, ...]);
callback: The function to be executed repeatedly.
delay: The time in milliseconds between each execution.
[arg1, arg2, ...]: Optional arguments that can be passed to the callback function.'''
# What is the difference between setImmediate() and setTimeout()? - https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/
# What is the difference between setImmediate() and process.nextTick()?
'''
| Key               | setImmediate()                                               | process.nextTick()                                               |
|------------------|--------------------------------------------------------------|------------------------------------------------------------------|
| Timing           | After current event loop, before I/O tasks                   | Immediately after current operation, before I/O or timers        |
| Execution Order  | After I/O, before timers                                     | Before I/O, timers, and even setImmediate()                      |
| Stack Behavior   | Safer, queued after event loop phase                         | Risk of stack overflow if overused                               |
| Use Case         | Defer execution to next phase of event loop                  | Run code before any I/O/timers in current phase                  |
| Example          | `setImmediate(() => { console.log('Immediate'); });`         | `process.nextTick(() => { console.log('Next Tick'); });`         |'''
# Explain the concept of Punycode in Node.js.
# Does Node.js provide any Debugger?
# Is cryptography supported in Node.js?
# Why do you think you are the right fit for this Node.js role?
# Do you have any past Node.js work experience?
# Do you have any experience working in the same industry as ours?
# What is web socket?
'''Web Socket is a protocol that provides full-duplex (multiway) communication i.e. allows communication in both directions simultaneously. Web Socket is a modern web technology in which there is a continuous connection between the user’s browser (client) and the server. In this type of communication, between the web server and the web browser, both of them can send messages to each other at any point in time.'''
# Explain the util module in NodeJS
'''
- OS Module: Operating System-based utility modules for NodeJS are provided by the OS module. 
- Path Module: The path module in NodeJS is used for transforming and handling various file paths. 
- DNS Module: DNS Module enables us to use the underlying Operating System name resolution functionalities. The actual DNS lookup is also performed by the DNS Module. 
- Net Module: Net Module in NodeJS is used for the creation of both client and server. Similar to DNS Module this module also provides an asynchronous network wrapper.'''
# How to handle environment variables in NodeJS?
'''We use process.env to handle environment variables in NodeJS. We can specify environment configurations as well as keys in the .env file. To access the variable in the application, we use the “process.env.VARIABLE_NAME” syntax.'''
# Explain DNS module in NodeJS
'''DNS is a node module used to do name resolution facility which is provided by the operating system as well as used to do an actual DNS lookup. Its main advantage is that there is no need for memorizing IP addresses – DNS servers provide a nifty solution for converting domain or subdomain names to IP addresses.'''

