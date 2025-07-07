'''
✅ - okay need to read onece
❌ - need to understand
⭐ - asked in interview 
'''

cookies vs local storage vs session storage
promise vs async await
Debounce vs Throttle

prototype, prototype chain, 
call, apply, bind
web workers vs service worker
Document and window 
Node vs javascript
callback in callback vs callback hell

*********

# ✅ Javascript
'''JavaScript is a high-level, dynamic, untyped, and interpreted programming language that is widely used for creating interactive and dynamic web applications. It is an essential part of web development, enabling developers to manipulate the Document Object Model (DOM), handle events, and perform asynchronous operations. JavaScript is known for its versatility, allowing it to be used on both the client-side (in web browsers) and server-side (with environments like Node.js).'''
# ✅ Is JavaScript a compiled or interpreted language
'''JavaScript is primarily an interpreted language, meaning that it is executed line by line by the JavaScript engine in the browser or server environment. However, modern JavaScript engines use Just-In-Time (JIT) compilation techniques to optimize performance by compiling frequently executed code into machine code at runtime.'''
# ✅ Is JavaScript a case-sensitive language
'''Yes, JavaScript is a case-sensitive language. This means that variable names, function names, and other identifiers must be used with consistent casing. For example, "myVariable" and "myvariable" would be considered two different identifiers in JavaScript.'''
# ✅ Is there any relation between Java and JavaScript
'''No, there is no direct relation between Java and JavaScript. Despite the similar names, they are distinct programming languages with different syntax, features, and use cases. Java is a statically typed, compiled language primarily used for building large-scale applications, while JavaScript is a dynamically typed, interpreted language primarily used for web development. The name "JavaScript" was chosen for marketing reasons when it was first introduced, but the two languages are not related in terms of design or functionality.'''
# ✅ Why do we call javascript as dynamic language
'''JavaScript is called a dynamic language because it allows for dynamic typing, meaning that variables can hold values of any type and can change types at runtime. It also supports dynamic object creation, where objects can be created and modified on the fly, enabling flexible and adaptable code. This dynamic nature allows developers to write code that can respond to changing conditions and user interactions in real-time.'''
# ✅ Who created javascript
'''JavaScript was created by Brendan Eich while working at Netscape Communications Corporation in 1995. It was initially developed under the name "Mocha," later renamed to "LiveScript," and finally became known as JavaScript. The language was designed to enable interactive web pages and has since evolved into a powerful programming language used for both client-side and server-side development.'''
# ✅ Why is JavaScript treated as Single threaded
'''JavaScript is treated as single-threaded because it executes code in a single sequence, meaning that only one piece of code can run at a time. This design simplifies the programming model and avoids issues related to concurrent execution and shared state. However, JavaScript can handle asynchronous operations using callbacks, promises, and async/await, allowing it to perform non-blocking tasks while still maintaining a single-threaded execution model. This is achieved through the event loop, which manages the execution of asynchronous code without blocking the main thread.'''
# ✅ ways to create objects - 
'''Object literal syntax, Object constructor, Object's create method, Function constructor, Function constructor with prototype, Object's assign method, ES6 Class syntax, Singleton pattern'''
# ❌ prototype chain - 
'''The prototype chain enables inheritance in JavaScript.
If a property isn’t found on an object, JavaScript looks up its prototype chain.
The prototype of an object instance can be accessed with Object.getPrototypeOf(obj) or __proto__.
The prototype of a constructor function is available via Constructor.prototype.
The chain ends when the prototype is null.'''
# ❌ call - 
'''invokes a function immediately, allowing you to specify the value of this and pass arguments individually (comma-separated)'''
# ❌ apply - 
'''it takes the function arguments as an array (or array-like object) instead of individual arguments.'''
# ❌ bind -
''' returns a new function that you can call later'''
# ❌ call vs apply vs bind
# ✅ JSON (JavaScript Object Notation) and it's operation
''' lightweight, text-based data format that uses JavaScript object syntax for  transmitting data between a server and a client in web applications'''
# ✅ slice - '''extract a section of an array, returning a new array'''
# ✅ splice - '''used to add, remove, or replace elements within an array, modify the original array'''
# ✅ splice vs slice 
'''
slice() : Does not modify the original array (immutable), Returns a shallow copy (subset) of selected elements, Used to extract elements from an array, Syntax: array.slice(start, end)
splice(): Modifies the original array (mutable), Returns an array of the removed elements, 	Used to add, remove, or replace elements in an array, Syntax: array.splice(start, deleteCount, ...items)'''
# ✅ object and map
'''
Object : 
Map :
- Key types: Object keys are strings or symbols, while Map keys can be of any type (objects, functions, primitives)
- Key Order: Object Keys are unordered, while Map keys maintains insertion order
- Performance: Map is generally more efficient for frequent additions and removals of key-value pairs, while Object is better for static key-value pairs
- Size: Object requires Object.keys(obj).length to determine size while Map has a size property, 
- Iterability: Objects are not directly iterable; must use Object.keys, Object.values, or Object.entries while maps are directly iterable with for...of, .keys(), .values(), .entries()
- Prototype chain: Objects have a prototype chain, which can lead to unexpected behavior when using inherited properties, while Maps do not have a prototype chain and do not inherit properties from Object.prototype
- Performance: Objects are less efficient for frequent additions and removals of key-value pairs, while Maps are optimized for such operations
- Serialization: Objects can be serialized to JSON using JSON.stringify(), while Maps require conversion to an array or object before serialization
- Methods: Map provides methods like set(), get(), has(), and delete() for key-value operations, while Object uses bracket notation or dot notation for property access and manipulation
- Use cases: Object is suitable for simple key-value pairs, while Map is preferred for complex key-value pairs, frequent updates, and when key types are not limited to strings or symbols.'''
# ✅ == vs ===
'''
Loose equality (==, !=): Performs type conversion if the types differ, comparing values after converting them to a common type.
Strict equality (===, !==): Compares both value and type, without any type conversion.
0 == false            // true      (loose equality, type coercion)
0 === false           // false     (strict equality, different types)
1 == "1"              // true      (string converted to number)
1 === "1"             // false     (different types)
null == undefined     // true      (special case)
null === undefined    // false     (different types)
'0' == false          // true      ('0' is converted to 0)
'0' === false         // false     (different types)
NaN == NaN            // false     (NaN is never equal to itself)
NaN === NaN           // false
[] == []              // false     (different array objects)
[] === []             // false
{} == {}              // false     (different object references)
{} === {}             // false'''



# ❌ lambda expressions or arrow functions
'''concise syntax for writing function expressions,
- Arrow functions do not have their own this, arguments, super, or new.target bindings. They inherit these from their surrounding (lexical) context.
- They are best suited for non-method functions, such as callbacks or simple computations.
- Arrow functions cannot be used as constructors and do not have a prototype property.
- They also cannot be used with new, yield, or as generator functions.'''
# ✅ first class function''' 
''' functions are treated like any other variable'''
# ✅ first order function -
'''function that doesn’t accept another function as an argument and doesn’t return a function as its return value'''
# ✅ higher order function - 
'''function that either accepts another function as an argument, returns a function as its result, or both'''
# ✅ unary function or monadic function - 
'''function that accepts exactly one argument'''
# ✅ currying function - 
'''process of transforming a function with multiple arguments into a sequence of nested functions, each accepting only one argument at a time'''
# ❌ pure function 
'''function whose output depends only on its input arguments and produces no side effects.'''
# ❌ pure vs impure functions
# ✅ let
'''block-scoped local variable, No Hoisting Issues, No Redeclaration'''
# ✅ const
'''block-scoped local variable, No Hoisting Issues, No Redeclaration, Must be initialized at the time of declaration, Cannot be reassigned but can be mutated if it is an object or array'''
# ✅ var
'''function-scoped or globally scoped variable, Hoisting Issues, Redeclaration Allowed'''
# ❌ let, const and var
# ✅ Temporal Dead Zone
'''period between the start of a block and the point where a variable declared with let or const is initialized. During this time, the variable exists in scope but cannot be accessed, and attempting to do so results in a ReferenceError'''
# ✅ IIFE (Immediately Invoked Function Expression)
'''function that is defined and executed immediately, often used to create a private scope for variables and avoid polluting the global namespace.'''
# ✅ decode or encode a URL - decodeURI(uri) or encodeURI(encoded_uri)
# memoization
'''optimization technique that stores the results of expensive function calls and returns the cached result when the same inputs occur again.'''
# ✅ Hoisting
'''JavaScript's behavior of moving variable and function declarations to the top of their containing scope during compilation, allowing you to use variables and functions before they are declared in the code.'''
# ✅ classes in ES6
'''syntactic sugar over JavaScript's existing prototype-based inheritance, providing a more familiar and structured way to define classes, constructors, and inheritance. Classes in ES6 use the `class` keyword and support features like constructors, methods, static methods, and inheritance through the `extends` keyword. They also provide a clearer syntax for defining object-oriented code compared to the traditional prototype-based approach.'''
# ❌ closures
'''function that retains access to its lexical scope, even when the function is executed outside of that scope. This allows the function to remember variables from its surrounding context, enabling powerful patterns like data encapsulation and partial application.'''
# ✅ modules
'''independednt, reusable pieces of code that can be exported from one file and imported into another, allowing for better organization, encapsulation, and reusability of code.'''
# ✅ scope in javascript
'''context in which variables and functions are defined and accessed, determining the visibility and lifetime of those variables and functions. JavaScript has function scope, block scope (with let and const), and global scope.'''
# ✅ service worker
'''script that runs in the background, separate from a web page, allowing for features that don't need a web page or user interaction like caching, push notifications, and background synchronization. It can intercept network requests and manage offline capabilities.'''
 
 
 
# service worker -
# ❌ postMessage()
'''allows communication between the main thread and the service worker, enabling the exchange of messages and data between them. This is essential for implementing features like push notifications and background sync.'''
# onfetch()
'''event handler that intercepts network requests made by the web page, allowing the service worker to respond with cached resources or perform custom actions before the request is sent to the network. This is crucial for implementing offline capabilities and caching strategies.'''
# ❌ onmessage()
'''event handler that listens for messages sent from the main thread or other contexts, allowing the service worker to respond to those messages and perform actions based on the received data. This is important for implementing features like push notifications and background sync.'''
# ❌ IndexedDB
'''a low-level API for client-side storage of large amounts of structured data, including files and blobs. It allows for asynchronous access to a database, enabling complex queries and transactions. IndexedDB is useful for building offline-capable web applications that require persistent storage.'''
# ✅ web storage / Web Storage API
'''a mechanism for storing key-value pairs in a web browser, providing a way to persist data across sessions. It includes localStorage (for long-term storage) and sessionStorage (for temporary storage during a session). Web storage is useful for maintaining user preferences, caching data, and improving performance in web applications.'''
# ✅ post message
'''a method used to send messages between different browsing contexts, such as between a web page and an iframe, or between a web page and a service worker. It allows for cross-origin communication and is essential for implementing features like postMessage-based messaging systems and cross-origin resource sharing (CORS).'''



# ✅ Cookie - options with cookie, delete a cookie 
'''small pieces of data stored by the web browser on the user's device, used to remember user preferences, session information, and other data across requests. Cookies can be set with various attributes like expiration time, path, domain, and secure flag. They are useful for maintaining user sessions and personalizing web experiences.'''
# ✅ session storage -  methods
'''a type of web storage that allows you to store data for the duration of a page session. Data stored in sessionStorage is cleared when the page session ends, making it suitable for temporary data storage during a user's interaction with a web application. It is accessible only within the same tab or window.'''
# ✅ local storage - methods
'''a type of web storage that allows you to store data persistently in the user's browser. Data stored in localStorage remains available even after the browser is closed and reopened, making it suitable for long-term data storage. It is accessible across different tabs and windows of the same origin.'''
# ✅ access web storage - window.localStorage, window.sessionStorage
# ✅ cookie vs local storage vs session storage
'''
client side or server side: Cookies are saved on both server-side & client-side, while localStorage and sessionStorage are client-side only.
Expiry: Cookies can have an expiration date, while localStorage data persists until explicitly deleted, and sessionStorage data is cleared when the page session ends.
SSL support: Cookies can be marked as secure and sent only over HTTPS, while localStorage and sessionStorage do not have this feature.
Maximum size: Cookies have a size limit of around 4KB, while localStorage and sessionStorage can store up to 5-10MB of data, depending on the browser.
Accesible from: Cookies and local storage are accesible in any window while session storage is only accessible in the same tab or window.
Sent with requests: Cookies are sent with every HTTP request, while localStorage and sessionStorage data are not sent to the server.
Methods: Cookies have methods like document.cookie, while localStorage and sessionStorage have methods like setItem(), getItem(), removeItem(), and clear().
'''
# ✅ storage event and its event handler
'''event that is triggered when a change is made to the web storage (localStorage or sessionStorage) in one window or tab, allowing other windows or tabs of the same origin to respond to the change. The event provides access to the key, old value, new value, and storage area where the change occurred. window.onstorage = function(event) { ... } is used to handle this event.'''
# check web storage browser support - typeof Storage !== "undefined"
# 
# ❌ Web Workers
'''a JavaScript feature that allows you to run scripts in background threads, enabling concurrent execution of tasks without blocking the main thread. Web workers are useful for performing computationally intensive tasks, such as data processing or image manipulation, without affecting the responsiveness of the user interface. They can communicate with the main thread using the postMessage() method.'''
# ✅ check web workers browser support - typeof Worker !== "undefined"
# ❌ example of a web worker
# ✅ restrictions of web workers on DOM - Window object, Document object, Parent object
# ❌ web workers vs service workers
# 
# 
# ✅ callback function
'''a function that is passed as an argument to another function and is invoked inside the outer function to complete an action. Callbacks are commonly used in asynchronous programming to handle the result of an operation once it is completed, allowing for non-blocking execution. They are essential for handling events, making API calls, and managing asynchronous tasks in JavaScript.'''
# ✅ need callbacks
'''Handle asynchronous operations.'''
# ✅ callback in callback
'''a situation where a callback function is passed as an argument to another function, which in turn calls the first callback function after completing its own operation. This can lead to nested callbacks, making the code harder to read and maintain. It is often seen in asynchronous programming, where multiple callbacks are used to handle different stages of an operation.'''
# ✅ callback hell
'''a situation in asynchronous programming where multiple nested callbacks lead to deeply indented and hard-to-read code. It occurs when callbacks are used extensively, making the code difficult to maintain and understand. To avoid callback hell, developers can use techniques like promises, async/await, or modularizing code into smaller functions.'''
# ✅ promise
'''a JavaScript object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. Promises provide a cleaner and more manageable way to handle asynchronous code compared to traditional callback functions, allowing for better error handling and chaining of operations.'''
# ✅ need a promise
'''Handle asynchronous operations.
Provide a cleaner alternative to callbacks.
Avoid callback hell.
Make code more readable and maintainable.'''
# ✅ states of promise - pending, fulfilled, rejected
# ✅ methods used with promise - .then(), .catch(), and .finally() are used to handle success, errors, and cleanup respectively.
# ✅ main rules of promise
'''A promise can be in one of three states: pending, fulfilled, or rejected.
A promise can only transition from pending to fulfilled or rejected once.
Once a promise is fulfilled or rejected, it cannot change its state again.
A promise can have multiple then() and catch() handlers attached to it, allowing for chaining of operations.
A promise can be resolved with a value or another promise, allowing for nested promises.
A promise can be rejected with an error or reason, which can be handled using catch() or then() with a rejection handler.'''
# ✅ promise chaining
'''the process of linking multiple promises together in a sequence, where the output of one promise is passed as input to the next promise. This allows for cleaner and more readable asynchronous code, as each promise can handle its own success and failure cases without nesting callbacks. Promise chaining is achieved using the then() method, which returns a new promise.'''
# ✅ promise.all([...])
'''a method that takes an array of promises and returns a single promise that resolves when all the promises in the array have resolved, or rejects if any of the promises reject. It allows you to run multiple asynchronous operations in parallel and wait for all of them to complete before proceeding.'''
# ✅ promise.race([...])
'''a method that takes an array of promises and returns a single promise that resolves or rejects as soon as one of the promises in the array resolves or rejects. It allows you to handle the first completed promise, regardless of whether it is fulfilled or rejected.'''
# ❌ pros and cons of promises over callbacks
# promise vs callbacks
# ❌ promise vs async await



# ✅ server-sent events
'''a technology that allows a server to push real-time updates to a web page over a single HTTP connection. It enables the server to send events to the client as they occur, without the need for the client to continuously poll the server for updates. Server-sent events are useful for applications that require real-time data updates, such as live notifications, stock prices, or social media feeds.'''
# ✅ receive server-sent event notifications
'''
if (typeof EventSource !== "undefined") {
  var source = new EventSource("sse_generator.js");
  source.onmessage = function (event) {
    document.getElementById("output").innerHTML += event.data + "<br>";
  };
}
'''
# check browser support for server-sent events - typeof EventSource !== "undefined"
# events available for server sent events - onopen(), onmessage(), onerror()


# ✅ strict mode in javascript
'''a way to opt-in to a restricted variant of JavaScript that eliminates some of the language's more problematic features and behaviors. It is used to write "secure" JavaScript by notifying "bad syntax" into real errors. It helps catch common coding errors, prevents the use of certain unsafe features, and improves performance by enabling optimizations. Strict mode is enabled by adding "use strict"; at the beginning of a script or function.'''
# ✅ purpose of double exclamation (!!) operator
'''used to convert a value to its boolean equivalent. It is a shorthand way of checking if a value is truthy or falsy in JavaScript. The first exclamation mark negates the value, converting it to a boolean, and the second exclamation mark negates it again, resulting in the original boolean value. This is often used to ensure that a value is explicitly treated as a boolean.'''
# ✅ purpose of the delete operator
'''used to remove a property from an object.'''
# ✅ typeof <variable> operator
'''used to determine the type of a variable or expression in JavaScript. It returns a string indicating the type of the operand, such as "undefined", "object", "boolean", "number", "string", "function", or "symbol".'''
# ✅ undefined property
'''a property that has been declared but has not been assigned a value.'''
# ✅ null value
'''a special value in JavaScript that represents the intentional absence of any object value. It is often used to indicate that a variable or property is empty or has no value.'''
# ✅ null vs undefined
'''
Assignment value: null is an assigned value that represents no value, while undefined means a variable has been declared but not assigned a value.
typeof: typeof null returns "object", while typeof undefined returns "undefined".
Absence of value: null indicates the absence of a value for a variable while undefined Indicates absence of variable itself.
Primitive operation: null converted to zero (0) while performing primitive operations while undefined converted to NaN (Not-a-Number) when performing primitive operations.
'''
# ✅ eval
'''a built-in JavaScript function that evaluates a string as JavaScript code and executes it. It can be used to dynamically execute code at runtime, but it is generally discouraged due to security risks and performance issues. Using eval can lead to code injection vulnerabilities and makes debugging more difficult.'''
# ❌ window vs document
'''
- window is the root level element in any web page while document is the direct child of the window object. This is also known as Document Object Model (DOM)
- By default window object is available implicitly in the page while document You can access it via window.document or document.
- window has methods like alert(), confirm() and properties like document, location etc. while document has methods like getElementById(), getElementsByClassName() and properties like body, head, etc.
'''
# ✅ access history in javascript - window.history.back(), window.history.forward();
# ✅ caps lock key turned on or not - mouseEvent  getModifierState("CapsLock")
# ✅ isNaN(<variable>)
'''a global function that determines whether a value is NaN (Not-a-Number).'''
# ✅ undeclared vs undefined variables
'''
- Undeclared variables do not exist in a program and are not declared whereas undefined variables declared in the program but have not assigned any value.
- If you try to read the value of an undeclared variable, then a runtime error is encountered while reading the value of an undefined variable does not throw an error. '''
# ✅ global variables - problems with global variables
'''variables that are available throughout the length of the code without any scope, regardless of where they are defined. They can lead to naming conflicts, unintended side effects, and difficulties in maintaining code.'''
# ✅ NaN property
'''a special value in JavaScript that represents a value that is not a valid number. It is the result of operations that cannot produce a meaningful numeric result, such as dividing zero by zero or attempting to parse a non-numeric string as a number. NaN is of type "number" and is not equal to any other value, including itself.'''
# ✅ isFinite(<variable>) function
'''a global function that determines whether a value is a finite number.  It returns false if the value is +infinity, -infinity, or NaN (Not-a-Number), otherwise it returns true.'''


# ✅ events
'''Events are actions or occurrences that happen in the browser, such as user interactions (clicks, key presses), changes in the DOM, or network requests. JavaScript can respond to these events by executing specific functions or code blocks when the event occurs. This allows developers to create interactive and dynamic web applications.'''
# ✅ event flow
'''The event flow in JavaScript refers to the order in which events are propagated through the DOM. There are three phases: capturing phase (from the root to the target), target phase (when the event reaches the target element), and bubbling phase (from the target back up to the root). Developers can listen for events at different phases using event listeners.'''
# ✅ event capturing
'''phase of event propagation in which an event is first intercepted by the outermost ancestor element, then travels downward through the DOM hierarchy until it reaches the target (innermost) element. Event capturing is enabled by setting the third argument of addEventListener() to true.'''
# ✅ event bubbling
'''phase of event propagation in which an event starts at the target (innermost) element and bubbles up through its ancestor elements until it reaches the outermost ancestor element. Event bubbling is the default behavior in JavaScript, and it allows developers to handle events at a higher level in the DOM hierarchy.'''
# ✅ submit a form using JavaScript - document.forms[0].submit();
# ✅ find operating system details - console.log(navigator.platform);
# ✅ document load vs DOMContentLoaded events -
'''The DOMContentLoaded event is fired when the initial HTML document has been completely loaded and parsed, without waiting for assets(stylesheets, images, and subframes) to finish loading. Whereas The load event is fired when the whole page has loaded, including all dependent resources(stylesheets, images).''' 
# ✅ native vs host vs user objects
'''Native objects are built-in JavaScript objects provided by the language, such as Object, Array, Function, and Date. Host objects are provided by the environment in which JavaScript runs, such as the browser's Document Object Model (DOM) and the Window object. User objects are custom objects created by developers to represent specific data or functionality in their applications.'''
# ✅ tools or techniques used for debugging JavaScript code - Chrome Devtools, debugger statement, console.log statement
# ✅ attribute vs property
'''Attributes are defined in the HTML markup and represent the initial state of an element, while properties are JavaScript representations of those attributes that can be manipulated dynamically. Attributes are accessed using the getAttribute() and setAttribute() methods, while properties are accessed directly through the DOM element's properties.''' 
# ✅ same-origin policy
'''a security measure implemented by web browsers that restricts how documents or scripts loaded from one origin can interact with resources from another origin. It prevents malicious scripts from accessing sensitive data on other domains, ensuring that web applications can only interact with resources from the same origin (protocol, domain, and port).'''
# ✅ purpose of void 0 - used to prevent the page from refreshing
# ✅ preventDefault method
'''used in event handlers to stop the default behavior of elements, such as preventing a form submission or stopping a link from navigating to a new page.'''
# ✅ stopPropagation method
'''used in event handlers to stop the propagation of an event through the DOM, preventing it from reaching parent elements. This is useful when you want to handle an event at a specific level without triggering any parent event handlers.'''
# steps involved in return false usage


# ✅ BOM
'''Browser Object Model (BOM) is a collection of objects provided by the browser that allows JavaScript to interact with the browser window and its components, such as the history, location, and navigator. It provides methods and properties to manipulate the browser environment, enabling developers to create dynamic and interactive web applications.'''
# ✅ setTimeout
'''used to call a function or evaluate an expression after a specified number of milliseconds. The setTimeout function returns a unique identifier that can be used to cancel the timeout using clearTimeout().'''
# ✅ setInterval
'''used to call a function or evaluate an expression at specified intervals (in milliseconds). The setInterval function returns a unique identifier that can be used to cancel the interval using clearInterval().'''
# ✅ event delegation
'''a technique in JavaScript where a single event listener is attached to a parent element instead of multiple listeners on child elements.'''
# ✅ ECMAScript
'''a standardized scripting language specification that JavaScript is based on. It defines the core features and syntax of the language, ensuring consistency across different implementations. ECMAScript versions are released periodically, introducing new features and improvements to the language.'''
# ❌ PWAs (Progressive Web Apps)
'''Progressive Web Apps (PWAs) are web applications that use modern web capabilities to deliver an app-like experience to users. They can be installed on a user's device, work offline, and provide features like push notifications and background sync. PWAs are designed to be fast, reliable, and engaging, making them a popular choice for developers looking to create cross-platform applications.'''
# ✅ clearTimeout method -  used in javascript to clear the timeout which has been set by setTimeout() function
# ✅ clearInterval method - used in javascript to clear the interval which has been set by setInterval() function
# ✅ redirect new page in javascript - window.location.href = "https://example.com";
# ✅ check whether a string contains a substring - str.includes(substring), str.indexOf(substring) !== -1, str.search(substring) !== -1
# ✅ validate an email in javascript - using regex
# ✅ get the current url with javascript - window.location.href, document.URL
# ✅ various url properties of location object - href, protocol, host, hostname, port, pathname, search, hash
# ✅ get query string values in javascript - new URLSearchParams(window.location.search)
# ✅ check if a key exists in an object - 'key' in object, obj.hasOwnProperty('key'), user.name !== undefined
# ✅ loop through or enumerate javascript object - for (const key in obj) { console.log(key, obj[key]); }
# ✅ test for an empty object - Object.keys(obj).length === 0, Object.entries(obj).length === 0
# ✅ arguments object
'''an array-like object available within functions that contains the arguments passed to the function. It allows access to the function's arguments even if they are not explicitly defined in the function parameters. However, it is not a true array, so methods like forEach() cannot be used directly on it.'''
# ✅ make first letter of the string in an uppercase - str.charAt(0).toUpperCase() + str.slice(1);
# pros and cons of for loops
'''
Pros : Works on every environment, can use break and continue flow control statements
Cons : Too verbose, Imperative, You might face off-by-one errors.'''
# ✅ display the current date in javascript - new Date()
# ✅ compare two date objects - d1.getTime() === d2.getTime() ✅ d1 === d2 ❌
# ✅ check if a string starts with another string - str.startsWith(substring), str.indexOf(substring) === 0
# ✅ trim a string in javascript - str.trim()
# ✅ add a key value pair in javascript - obj.key = value, obj[key] = value, Object.assign(obj, { key: value }), Object.defineProperty(obj, key, { value: value })
# ✅ Is the !-- notation represents a special operator - No ! and --
# ✅ assign default values to variables - var a = b || c; (falsy values - null, false, undefined, 0, empty string, or NaN)
# ✅ define multiline strings - using '\n' or template literals (backticks)
# ❌ app shell model
'''a design pattern for building Progressive Web Apps (PWAs) that separates the application shell (the static parts of the app) from the dynamic content. The app shell is loaded once and cached, allowing for fast loading and smooth user experience, while dynamic content is fetched and updated as needed. This approach improves performance and provides a native app-like experience.'''
# ✅ Can we define properties for functions
# ✅ way to find the number of parameters expected by a function - <function_name>.length
# ❌ polyfill
'''a piece of code used to provide modern functionality on older browsers that do not natively support it. For example, Silverlight plugin polyfill can be used to mimic the functionality of an HTML Canvas element on Microsoft Internet Explorer 7.
There are two main polyfill libraries available,
Core.js: It is a modular javascript library used for cutting-edge ECMAScript features.
Polyfill.io: It provides polyfills that are required for browser needs.'''
# ✅ break vs continue
'''break' is used to exit a loop or switch statement immediately, while 'continue' is used to skip the current iteration of a loop and move to the next iteration based on some condition.'''
# ✅ js labels
'''a way to assign a name to a statement in JavaScript, allowing you to break out of or continue a specific loop or block of code. Labels are defined using the labelName: syntax and can be used with break and continue statements to control the flow of execution.'''
# ✅ benefits of keeping declarations at the top - Gives cleaner code, provides a single place to look for local variables, Easy to avoid unwanted global variables, reduces the possibility of unwanted re-declarations
# ✅ benefits of initializing variables - gives cleaner code, provides a single place to initialize variables, Avoid undefined values in the code
# ✅ recommendations to create new object
# ✅ define JSON arrays - arrays are written inside square brackets and arrays contain javascript objects, <var_name> = [{key: value}, {key: value}]
# ✅ generate random integers - Math.floor(Math.random() * 10) + 1; 
# ✅ random integers function to print integers within a range
'''
function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
'''
# ✅ tree shaking - need of tree shaking
'''Tree shaking is a technique used in modern JavaScript build tools to eliminate unused code from the final bundle. It helps reduce the size of the JavaScript files by removing functions, variables, and modules that are not referenced or used in the application. This results in faster load times and improved performance for web applications. Tree shaking is particularly effective when using ES6 modules, as it allows for static analysis of imports and exports.'''
# ✅ Is it recommended to use eval 
'''No, it is generally not recommended to use eval in JavaScript due to security risks and performance issues. Eval can execute arbitrary code, which can lead to code injection vulnerabilities if user input is not properly sanitized. Additionally, using eval can make debugging more difficult and hinder performance optimizations by the JavaScript engine. Instead, developers are encouraged to use safer alternatives like JSON.parse() for parsing JSON data or other methods for dynamic code execution.'''

# ✅ Regular Expression
'''a sequence of characters that forms a search pattern, used for matching and manipulating strings based on specific criteria. Regular expressions are powerful tools for tasks like validation, searching, and replacing text in strings.'''
# ✅ string methods that accept Regular expression - search(), replace(), replaceAll(), test(), exec(), match(), matchAll(), and split().
# ✅ modifiers in regular expression
'''Modifiers are flags that can be added to a regular expression to change its behavior. Common modifiers include:
- g (global): Searches for all matches in the string, not just the first one.
- i (case-insensitive): Makes the search case-insensitive, allowing matches regardless of letter case.
- m (multiline): Changes the behavior of ^ and $ to match the start and end of each line within a string, rather than just the start and end of the entire string.'''
# ❌ regular expression syntax
# ❌ regular expression patterns -
'''
Brackets: These are used to find a range of characters. For example, below are some use cases,
[abc]: Used to find any of the characters between the brackets(a,b,c)
[0-9]: Used to find any of the digits between the brackets
(a|b): Used to find any of the alternatives separated with |
Metacharacters: These are characters with a special meaning. For example, below are some use cases,
\d: Used to find a digit
\s: Used to find a whitespace character
\b: Used to find a match at the beginning or ending of a word
Quantifiers: These are useful to define quantities. For example, below are some use cases,
n+: Used to find matches for any string that contains at least one n
n*: Used to find matches for any string that contains zero or more occurrences of n
n?: Used to find matches for any string that contains zero or one occurrences of n'''
# ✅ RegExp object
'''a built-in JavaScript object that provides methods for working with regular expressions. It allows you to create, test, and manipulate regular expressions using various methods like test(), exec(), and toString(). The RegExp constructor can be used to create a new regular expression object from a pattern and optional modifiers.'''
# ✅ search a string for a pattern - /pattern/.test("How are you?"), return true or false depending on the result
# exec() method
'''The purpose of exec method is similar to test method but it executes a search for a match in a specified string and returns a result array, or null instead of returning true/false.'''
# ✅ change the style of a HTML element - document.getElementById("title").style.fontSize = "30px";, document.getElementById("title").className = "custom-title";
# ✅ debugger statement
'''a built-in JavaScript statement that can be used to pause the execution of code and invoke the debugging functionality of the browser's developer tools. When the debugger statement is encountered, the execution stops, allowing developers to inspect variables, step through code, and analyze the program's state at that point. It is useful for debugging and troubleshooting issues in JavaScript code.'''
# ✅ purpose of breakpoints in debugging
'''Breakpoints are markers set in the code that pause execution at a specific line, allowing developers to inspect the program's state, variables, and call stack. They are essential for debugging, as they help identify issues by providing a way to analyze the code step-by-step. Breakpoints can be set in browser developer tools or IDEs, enabling developers to control the flow of execution and examine the behavior of their code.'''
# ✅ Can I use reserved words as identifiers - No will throw Uncaught SyntaxError: Unexpected token else
# ✅ detect a mobile browser - using regex
# ✅ detect a mobile browser without regexp - navigator.userAgent
# ✅ get the image width and height using JS
'''
var img = new Image();
img.onload = function () {
  console.log(this.width + "x" + this.height);
};
img.src = "http://www.google.com/intl/en_ALL/images/logo.gif";
'''
# ❌ make synchronous HTTP request
'''
function httpGet(theUrl) {
  var xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.open("GET", theUrl, false); // false for synchronous request
  xmlHttpReq.send(null);
  return xmlHttpReq.responseText;
}
'''
# ❌ make asynchronous HTTP request
'''
function httpGetAsync(theUrl, callback) {
  var xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.onreadystatechange = function () {
    if (xmlHttpReq.readyState == 4 && xmlHttpReq.status == 200)
      callback(xmlHttpReq.responseText);
  };
  xmlHttpReq.open("GET", theUrl, true); // true for asynchronous
  xmlHttpReq.send(null);
}'''
# ✅ convert date to another timezone in javascript- console.log(new Date().toLocaleString("en-GB", { timeZone: "UTC" })); //29/06/2019, 09:56:00
# ✅ properties used to get size of window - window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
# ✅ conditional or ternary operator - expression ? value_if_true : value_if_false;
# ✅ Can you apply chaining on conditional operator - yes expression ? value_if_true : (expression2 ? value_if_true2 : value_if_false2);
# ✅ ways to execute javascript after a page load - window.onload = function ..., document.onload = function ..., <body onload="script();">
# ❌ proto vs prototype
# ❌ Can you give an example of when you really need a semicolon
# ✅ freeze method - purpose
'''The freeze method is used to make an object immutable, preventing any changes to its properties or values. Once an object is frozen, you cannot add, delete, or modify its properties. It is useful for creating constant objects that should not be altered during the execution of the program. It is only applied to the top-level properties in objects but not for nested objects.'''
# ✅ detect a browser language preference
'''
var language =
  (navigator.languages && navigator.languages[0]) || // Chrome / Firefox
  navigator.language || // All browsers
  navigator.userLanguage; // IE <= 10

console.log(language);'''
# ✅ convert a string to title case with javascript - txt.charAt(0).toUpperCase() + txt.substring(1).toLowerCase()
# ✅ detect if javascript is disabled on the page - <noscript> gets executed when JavaScript is disabled, and is typically used to display alternative content when the page generated in JavaScript.
# ✅ operators supported by javascript - arithmetic, assignment, comparison, logical, bitwise, identity, membership, conditional (ternary), and typeof operators.
# ✅ rest parameter
'''a feature in JavaScript that allows a function to accept an multiple number of arguments as an array. It is denoted by three dots (...) before the parameter name in the function definition. The rest parameter collects all remaining arguments passed to the function into an array, making it easier to work with variable-length argument lists.'''
# ✅ What happens if you do not use rest parameter as a last argument - will throw an error
# ✅ bitwise operators - Bitwise AND ( & ), Bitwise OR ( | ), Bitwise XOR ( ^ ), Bitwise NOT ( ~ ), Left Shift ( << ), Sign Propagating Right Shift ( >> ), Zero fill Right Shift ( >>> )
# ✅ spread operator 
'''a feature in JavaScript that allows an iterable (like an array or string) to be expanded into individual elements. It is denoted by three dots (...) before the iterable in the function call or array literal. The spread operator is useful for creating shallow copies of arrays, merging arrays, and passing multiple arguments to functions.'''
# ✅ determine whether object is frozen or not - Object.isFrozen(obj)
# ✅ determine two values same or not using object - Object.is(value1, value2)
'''
both undefined
both null
both true or both false
both strings of the same length with the same characters in the same order
both the same object (means both object have same reference)
both numbers and both +0 both -0 both NaN both non-zero and both not NaN and both have the same value.'''
# ✅ purpose of using object is method - comparison of two strings/numbers/objects/polarity
# ✅ copy properties from one object to other - Object.assign(target, ...sources);
# ✅ assign method - used for cloning an object or merging multiple objects into one.
# ✅ proxy object
'''a built-in JavaScript object that allows you to create a proxy for another object, enabling you to intercept and redefine fundamental operations for that object, such as property access, assignment, enumeration, and function invocation. A proxy is created with two parameters: a target object which you want to proxy and a handler object which contains methods to intercept fundamental operations.  var p = new Proxy(target, handler);'''
# ✅ seal method
'''a built-in JavaScript method used to seal an object, by preventing new properties from being added to it and marking all existing properties as non-configurable. But values of present properties can still be changed as long as they are writable. '''
# ❌ freeze vs seal methods
'''seal() prevents new properties from being added to an object and marks existing properties as non-configurable, while freeze() makes an object immutable by preventing any changes to its properties or values. In other words, seal() allows modification of existing property values, while freeze() does not.'''
# ✅ determine if an object is sealed or not - Object.isSealed(obj)
# ✅ get enumerable key and value pairs - Object.entries()
# ✅ Object.values vs Object.entries method
# ✅ get the list of keys of any object - Object.keys(keys)
# ❌ create an object with a prototype - Object.create()
# ✅ WeakSet 
'''A WeakSet is a collection of objects that allows you to store unique values of any type, but unlike a regular Set, it does not prevent garbage collection of its elements. This means that if there are no other references to an object in a WeakSet, it can be garbage collected, making WeakSet memory-efficient for managing collections of objects.'''
# ❌ WeakSet vs Set
'''
- Set can store any value whereas WeakSet can store only collections of objects
- WeakSet does not have size property unlike Set
- WeakSet does not have methods such as clear, keys, values, entries, forEach.
- WeakSet is not iterable.'''
# ✅ methods on WeakSet - add(), delete(), has()
# ✅ WeakMap  
'''A WeakMap is similar to a Map, but it allows you to store key/value pairs where the keys are objects and the values can be any type. The keys in a WeakMap are weakly referenced, meaning that if there are no other references to a key object, it can be garbage collected, making WeakMap memory-efficient for managing collections of objects. In this case, keys must be objects and the values can be arbitrary values.''' 
# ❌ WeakMap vs Map
'''
- Map can store any key type whereas WeakMap can store only collections of key objects
- WeakMap does not have size property unlike Map
- WeakMap does not have methods such as clear, keys, values, entries, forEach.
- WeakMap is not iterable.'''
# ✅ methods on WeakMap - get(), set(), has(), delete()
# ✅ uneval -  used to create a string representation of the source code of an Object. It is a top-level function and is not associated with any object. uneval() function has been deprecated. It is recommended to use toString() for functions and JSON.stringify() for other cases.
# ✅ print the contents of web page - window.print()
# u❌ uneval vs eval
# ✅ anonymous function
'''a function that does not have a name and is often used as an argument to other functions or as a callback.'''
# ✅ precedence order between local and global variables - local variable takes precedence over a global variable
# ❌ javascript accessors
'''special methods that allow you to define custom behavior for getting and setting the values of object properties. They are defined using the get and set keywords within an object literal or class. Accessors provide a way to encapsulate property access and validation logic, making it easier to manage and control how properties are accessed and modified.'''
# define property on Object constructor
'''a method that allows you to define a new property or modify an existing property on an object. It takes three arguments: the object to define the property on, the property name, and a property descriptor that specifies the property's attributes (such as value, writable, enumerable, and configurable). This method provides fine-grained control over how properties behave in JavaScript objects.
Object.defineProperty(obj, prop, descriptor)'''
# ❌ get vs defineProperty
# ❌ Getters vs Setters
# ✅ Can I add getters and setters using defineProperty method - yes, you can add getters and setters using the defineProperty method by specifying the get and set functions in the property descriptor.
# ✅ switch-case
'''a control flow statement in JavaScript that allows you to execute different blocks of code based on the value of an expression. It is an alternative to using multiple if-else statements and provides a cleaner way to handle multiple conditions. The switch statement evaluates an expression and compares its value against multiple case labels, executing the corresponding block of code when a match is found. If no match is found, the default block (if provided) is executed.'''
# ✅ What are the conventions to be followed for the usage of switch case
'''expression can be of type either number or string
Duplicate values are not allowed for the expression.
default statement is optional.
break statement is used inside the switch to terminate a statement sequence.
break statement is optional. But if it is omitted, the execution will continue on into the next case.'''
# ✅ primitive data types - string, number, boolean, null, undefined, bigint, symbol
# ✅ ways to access object properties - objectName.property;, objectName["property"];, objectName[expression];, Object.getOwnPropertyDescriptor(objectName, "property");
# ✅ function parameter rules - do not specify data types for parameters, Do not perform type checking on the passed arguments., Do not check the number of arguments received.
# ✅ error object
'''a built-in JavaScript object that represents an error that occurs during the execution of a script. It provides information about the error, such as its name, message, and stack trace. The Error object can be used to create custom error types and handle exceptions in a structured way. It is commonly used in try-catch blocks to catch and handle errors gracefully.'''
# ✅ When do you get a syntax error - eval("greeting('welcome)"); // Missing ' will produce an error
# ✅ error names from error object - AggregateError, EvalError, RangeError, ReferenceError, SyntaxError, TypeError, URIError
# ✅ various statements in error handling
'''try: This statement is used to test a block of code for errors
catch: This statement is used to handle the error
throw: This statement is used to create custom errors.
finally: This statement is used to execute code after try and catch regardless of the result.'''
# ✅ types of loops in javascript - Entry Controlled loops, Exit Controlled loops

# ✅ nodejs
'''a JavaScript runtime built on Chrome's V8 engine that allows developers to run JavaScript code on the server side. It provides an event-driven, non-blocking I/O model, making it suitable for building scalable and high-performance applications. Node.js is commonly used for creating web servers, APIs, and real-time applications.'''
# ✅ Intl object
'''a built-in JavaScript object that provides language-sensitive string comparison, number formatting, and date and time formatting. It is part of the ECMAScript Internationalization API and allows developers to create applications that can adapt to different languages and regions. The Intl object includes constructors like Intl.Collator, Intl.NumberFormat, and Intl.DateTimeFormat for various localization tasks.'''
# ✅ perform language specific date and time formatting
'''var date = new Date(Date.UTC(2019, 07, 07, 3, 0, 0));
console.log(new Intl.DateTimeFormat("en-GB").format(date)); // 07/08/2019'''
# ❌ Iterator
'''an object that defines a sequence and potentially a return value upon its completion.  It implements the Iterator protocol with a next() method which returns an object with two properties: value (the next value in the sequence) and done (which is true if the last value in the sequence has been consumed). In JavaScript, iterators are used with the for...of loop and can be created using the Symbol.iterator method.'''
# ❌ How does synchronous iteration works
'''Synchronous iteration in JavaScript allows you to iterate over a collection of elements one at a time, blocking the execution until the current element is processed before moving to the next one. This is typically done using a for loop or the for...of loop, which automatically handles the iteration process by calling the next() method on the iterator object until all elements have been processed.'''
# ✅ event loop
'''
The event loop is a process that continuously monitors both the call stack and the event queue and checks whether or not the call stack is empty. If the call stack is empty and there are pending events in the event queue, the event loop dequeues the event from the event queue and pushes it to the call stack. The call stack executes the event, and any additional events generated during the execution are added to the end of the event queue.
a fundamental concept in JavaScript that manages the execution of asynchronous code. It allows JavaScript to perform non-blocking operations by using a single thread to handle events and callbacks. The event loop continuously checks the call stack for pending tasks and processes them in the order they were added, ensuring that the main thread remains responsive while handling asynchronous operations like timers, network requests, and user interactions.'''
# ✅ call stack
'''a data structure that stores the execution context of functions in JavaScript. It follows the Last In, First Out (LIFO) principle, meaning that the last function called is the first one to be executed. The call stack keeps track of function calls, allowing JavaScript to manage the flow of execution and handle nested function calls. When a function is called, its execution context is pushed onto the stack, and when it returns, the context is popped off the stack.'''
# ❌ event queue or Callback Queue or Macrotask Queue
'''a data structure that holds events and messages that are waiting to be processed by the event loop in JavaScript. When an event occurs, it is added to the event queue, and the event loop processes these events one by one, executing their associated callback functions. The event queue ensures that events are handled in the order they occur, allowing for asynchronous processing of tasks without blocking the main thread.'''
# ❌ decorator
'''an expression that allows you to modify or enhance the behavior of a function or class without changing its original code. Decorators are typically implemented as higher-order functions that take a function or class as an argument and return a new function or class with additional functionality. They are commonly used for logging, validation, and other cross-cutting concerns in applications.'''
# ✅ properties of the Intl object - Collator, DateTimeFormat, ListFormat, Locale, NumberFormat, PluralRules, RelativeTimeFormat
# ✅ Unary operator
'''used to convert a variable to a number.If the variable cannot be converted, it will still become a number but with the value NaN.'''
# ✅ sort elements in an array - array.sort(compareFunction)
# ✅ purpose of compareFunction while sorting arrays - 
''' used to define the sort order. If omitted, the array elements are converted to strings, then sorted according to each character's Unicode code point value.'''
# ✅ reverse an array - array.reverse()
# ✅ find the min and max values in an array - Math.min(...array), Math.max(...array)
# ❌ find the min and max values without Math functions - write a program
# ✅ empty statement and purpose of it
'''The empty statement is a semicolon (;) indicating that no statement will be executed, even if JavaScript syntax requires one. Since there is no action with an empty statement you might think that it's usage is quite less, but the empty statement is occasionally useful when you want to create a loop that has an empty body. '''
# ✅ get the metadata of a module - import.meta
# ✅ comma operator - advantage
''' used to evaluate each of its operands from left to right and returns the value of the last operand. This is totally different from comma usage within arrays, objects, and function arguments and parameters'''


# ✅ typescript
'''a superset of JavaScript that adds static typing and other features to the language. It allows developers to catch errors at compile time, provides better tooling support, and enhances code maintainability. TypeScript code is transpiled to standard JavaScript, making it compatible with existing JavaScript codebases. It is widely used in large-scale applications and frameworks like Angular.'''
# ✅ javascript vs typescript
'''
Language paradigm: typescript support object oriented programming language	while javascript supports multi-paradigm language
Typing support:	ts supports static typing while js supports	dynamic typing
Modules: ts supported	bu js not supported
Interface:	ts has interfaces concept	but js doesn't support interfaces
Optional parameters:	ts functions support optional parameters. No support of optional parameters for functions in js'''
# ✅ advantages of typescript over javascript
# ✅ object initializer
'''a way to create and initialize objects in JavaScript using a concise syntax. It allows you to define properties and methods directly within curly braces, making it easier to create complex objects without the need for constructor functions or classes. Object initializers are commonly used to create configuration objects, data structures, and other types of objects in JavaScript applications.'''
# ✅ literal notation
'''a way to define objects, arrays, and other data structures in JavaScript using a concise syntax. It allows you to create complex data structures without the need for constructor functions or classes. Literal notation is commonly used for creating configuration objects, data structures, and other types of objects in JavaScript applications.'''
# ✅ constructor method
'''special method for creating and initializing an object created within a class. If you do not specify a constructor method, a default constructor is used. '''
# ✅ What happens if you write constructor more than once in a class -  throw a SyntaxError
# ✅ call the constructor of a parent class - super() must be called before using this reference. Otherwise it will cause a reference error. 
# ✅ get the prototype of an object - 
'''Object.getPrototypeOf(obj) method to return the prototype of the specified object. i.e. The value of the internal prototype property. If there are no inherited properties then null value is returned.'''
# ✅ What happens If I pass string type for getPrototype method - 
'''In ES5, it will throw a TypeError exception if the obj parameter isn't an object. Whereas in ES2015, the parameter will be coerced to an Object.'''
# ✅ set the prototype of one object to another
'''Object.setPrototypeOf(Square.prototype, Rectangle.prototype);
Object.setPrototypeOf({}, null);'''
# ✅ check whether an object can be extended or not - Object.isExtensible(obj)
# ✅ prevent an object from being extend - Object.preventExtensions(obj)
# ✅ ways to make an object non-extensible - Object.preventExtensions, Object.seal, Object.freeze
# ✅ define multiple properties on an object
'''Object.defineProperties(obj, {
  newProperty1: {
    value: "John",
    writable: true,
  },
  newProperty2: {},
});'''
# ✅ MEAN stack
'''a popular web development stack that combines four technologies: MongoDB (a NoSQL database), Express.js (a web application framework for Node.js), Angular (a front-end framework), and Node.js (a JavaScript runtime). The MEAN stack allows developers to build full-stack web applications using a single programming language, JavaScript, across both the client and server sides.'''
# ✅ Obfuscation
'''deliberate act of creating obfuscated javascript code(i.e, source or machine code) that is difficult for humans to understand. It is something similar to encryption, but a machine can understand the code and execute it.'''
# ✅ obsfuscation advantages - Code size will be reduced. So data transfers between server and client will be fast., hides the business logic from outside, Reverse engineering is highly difficult, download time will be reduced
# ✅ Minification - advantages - 
'''process of removing all unnecessary characters(empty spaces are removed) and variables will be renamed without changing it's functionality. It is also a type of obfuscation .'''
# ✅ obfuscation vs Encryption
'''
Definition:	Obfuscation is hanging the form of any data in any other form while	Encryption ishanging the form of information to an unreadable format by using a key
A key to decode: Obfuscation can be decoded without any key. Key is required encryption
Target data format:	Obfuscation will be converted to a complex form	Encryption is converted into an unreadable format'''
# ✅ tools used for minification - Google's Closure Compiler, UglifyJS2, jsmin, javascript-minifier.com/, prettydiff.com
# ✅ form validation using javascript
'''a process of checking user input in a web form to ensure it meets specific criteria before submission. JavaScript can be used to validate form fields, such as checking for required fields, valid email formats, and password strength. This helps improve user experience by providing immediate feedback and preventing invalid data from being submitted to the server.'''
# ✅ form validation without javascript - using attributes like required, pattern, minlength, maxlength, and type in HTML5 forms.
# ✅ DOM methods available for constraint validation - checkValidity(), setCustomValidity()
# ✅ available constraint validation DOM properties - validity, validationMessage, willValidate
# ✅ validity properties - customError, patternMismatch, rangeOverflow, rangeUnderflow, stepMismatch, tooLong, tooShort, typeMismatch, valid, valueMissing
# ✅ rangeOverflow property
# ✅ Are enums available in javascript
'''No, javascript does not natively support enums. But there are different kinds of solutions to simulate them even though they may not provide exact equivalents. For example, you can use freeze or seal on object,'''
# ✅ enum
'''a special data type that allows you to define a set of named constants. Enums are used to represent a collection of related values, making code more readable and maintainable. In JavaScript, enums can be simulated using objects or by using TypeScript, which provides built-in support for enums.'''
# ✅ list all properties of an object - Object.getOwnPropertyNames() or Object.keys()
# ✅ get property descriptors of an object - Object.getOwnPropertyDescriptors()
# ✅ What are the attributes provided by a property descriptor - value, writable, configurable, enumerable, set, get
# ✅ How do you extend classes - class ChildClass extends ParentClass { ... }
# ✅ modify the url without reloading the page - history.pushState() and history.replaceState()
# ✅ check whether or not an array includes a particular value - arr.includes(<value>), arr.indexOf(<value>) !== -1, arr.findIndex(<callback>) !== -1
# ✅ compare scalar arrays
'''console.log(
  arrayFirst.length === arraySecond.length &&
    arrayFirst.every((value, index) => value === arraySecond[index])
);'''
# ✅ get the value from get parameters
'''let urlString = "http://www.some-domain.com/about.html?x=1&y=2&z=3"; //window.location.href
let url = new URL(urlString);
let parameterZ = url.searchParams.get("z");
console.log(parameterZ); // 3'''
# ✅ print numbers with commas as thousand separators - Number.prototype.toLocaleString()
# java vs javascript
'''| Feature     | Java                             | JavaScript                                |
|-------------|----------------------------------|--------------------------------------------|
| Typed       | It's a strongly typed language   | It's a dynamic typed language              |
| Paradigm    | Object oriented programming      | Prototype based programming                |
| Scoping     | Block scoped                     | Function-scoped, block scoped since ES6    |
| Concurrency | Thread based                     | Event based                                |'''
# ✅ Does JavaScript support namespaces - JavaScript doesn’t support namespaces by default. It always calls the second function definition. In this case, namespaces will solve the name collision problem.
# ❌ declare a namespace - Using Object Literal Notation, Using IIFE, Using a block and a let/const declaration
# ✅ invoke javascript code in an iframe from the parent page - 
'''document.getElementById("targetFrame").contentWindow.targetFunction();
window.frames[0].frameElement.contentWindow.targetFunction(); // Accessing iframe this way may not work in latest versions chrome and firefox'''
# ✅ get the timezone offset of a date object - var offset = new Date().getTimezoneOffset();
# ✅ load CSS and JS files dynamically - using createElement() and setAttribute() methods
# ✅ methods to find HTML elements in DOM - document.getElementById(id), document.getElementsByTagName(name), document.getElementsByClassName(name), document.querySelector(cssSelector), document.querySelectorAll(cssSelector)
# 
# ✅ jQuery
'''a fast and feature-rich JavaScript library that simplifies HTML document traversal, manipulation, event handling, and animation. It provides an easy-to-use API for working with the DOM, making it easier to create dynamic and interactive web applications. jQuery is widely used for its cross-browser compatibility and extensive plugin ecosystem.'''
# ✅ V8 JavaScript engine
'''an open-source JavaScript engine developed by Google, used in the Chrome browser and Node.js. It compiles JavaScript code to native machine code for improved performance and efficiency. V8 is known for its speed and ability to handle large-scale applications, making it a popular choice for web developers. It also supports modern JavaScript features and provides a powerful runtime environment for executing JavaScript code.'''
# ✅ void operator
'''a unary operator in JavaScript that evaluates an expression and returns undefined. It is often used to execute a function without returning a value or to create a placeholder for a function that does not need to return anything. The void operator can also be used to prevent the default behavior of links or form submissions by returning undefined., void expression;'''
# ✅ set the cursor to wait - window.document.body.style.cursor = "wait";
# ✅ create an infinite loop - for (;;) {}, while (true) {}
# ✅  Why do you need to avoid with statement
'''The with statement is used to extend the scope chain for a statement. However, it is generally discouraged in JavaScript because it can lead to confusion and performance issues. The with statement makes code harder to read and maintain, as it can create ambiguity about variable resolution. It also prevents certain optimizations by JavaScript engines, leading to slower execution. As a result, the use of the with statement is considered bad practice and is not recommended in modern JavaScript development.'''
# ✅ ES6 - 
'''ES6, also known as ECMAScript 2015, is the sixth edition of the ECMAScript language specification. It introduced significant improvements and new features to JavaScript, making it more powerful and easier to work with. Some of the key features of ES6 include arrow functions, classes, template literals, destructuring assignment, modules, deafault parameters, promises, and enhanced object literals. ES6 has become the standard for modern JavaScript development and is widely supported by browsers and JavaScript engines.'''
# ✅ Can I redeclare let and const variables - No, throw SyntaxError
# ✅ Does the const variable make the value immutable - No, the const variable doesn't make the value immutable. But it disallows subsequent assignments
# ✅ default parameters -
'''feature allows parameters to be initialized with default values if no value or undefined is passed.'''
# ✅ template literals 
'''a feature in ES6 that allows you to create multi-line strings and embed expressions within strings using backticks (`) instead of single or double quotes. Template literals can contain placeholders for variables and expressions, making it easier to construct dynamic strings. They also support multi-line formatting without the need for concatenation or escape characters.'''
# ✅ write multi-line strings in template literals
'''console.log("This is string sentence 1\n" + "This is string sentence 2");
console.log(`This is string sentence
'This is string sentence 2`);'''
# ✅ nesting templates
'''a feature in ES6 that allows you to embed template literals within other template literals. This enables you to create complex strings with multiple levels of interpolation and formatting. You can use backticks (`) to define the outer template literal and then use `${}` to insert inner template literals or expressions.'''
# ✅ tagged templates
'''Tagged templates are the advanced form of templates in which tags allow you to parse template literals with a function. The tag function accepts the first parameter as an array of strings and remaining parameters as expressions. This function can also return manipulated strings based on parameters.'''
# ✅ raw strings
'''a feature in ES6 that allows you to access the raw string content of a template literal, including escape sequences. The raw strings are obtained using the `String.raw` tag function, which returns a string with the original escape sequences intact. This is useful when you want to preserve the exact formatting of a template literal without interpreting escape characters.'''
# ✅ destructuring assignment
'''a feature in ES6 that allows you to unpack values from arrays or properties from objects into distinct variables. It provides a concise syntax for extracting values, making code more readable and easier to work with. Destructuring can be used with arrays, objects, and function parameters, enabling developers to access and assign values in a more intuitive way.
var { name, age } = { name: "John", age: 32 };
var [one, two, three] = ["JAN", "FEB", "MARCH"];'''
# ✅ default values in destructuring assignment
'''a feature in ES6 that allows you to assign default values to variables when destructuring arrays or objects. If the value being destructured is undefined, the default value will be used instead. This helps avoid errors and provides a fallback value when the expected data is not present. Default values can be specified using the assignment operator (=) in the destructuring syntax.
var x, y, z;
[x = 2, y = 4, z = 6] = [10];'''
# ✅ swap variables in destructuring assignment - [x, y] = [y, x];
# ✅ enhanced object literals
''' Object literals make it easy to quickly create objects with properties inside the curly braces.
//ES6
var x = 10,
  y = 20;
obj = { x, y };
console.log(obj); // {x: 10, y:20}
//ES5
var x = 10,
  y = 20;
obj = { x: x, y: y };
console.log(obj); // {x: 10, y:20}'''
# ✅ dynamic imports
'''a feature in ES2020 that allows you to load modules dynamically at runtime using the import() function. This enables you to split your code into smaller chunks and load them on demand, improving performance and reducing initial load times. Dynamic imports return a promise that resolves to the module object, allowing you to access its exports once the module is loaded.
import("./Module").then((Module) => Module.method());'''
# ✅ typed arrays
'''a feature in JavaScript that provides a way to work with binary data in a more efficient manner. Typed arrays are array-like objects that allow you to read and write binary data directly, using specific data types such as Int8Array, Uint8Array, Float32Array, etc. They are useful for handling large amounts of binary data, such as images, audio, and video, and provide better performance compared to regular arrays when dealing with binary data.'''
# ✅ module loaders
'''a mechanism in JavaScript that allows you to load and manage modules in your application. Module loaders enable you to define dependencies between modules, load them asynchronously, and handle their execution order. Common module loaders include RequireJS, SystemJS, and Webpack. They help organize code into reusable modules, improving maintainability and scalability of applications.'''
# ❌ collation
'''a process of comparing and sorting strings based on specific rules, such as language or locale. In JavaScript, collation is typically handled using the Intl.Collator object, which provides methods for comparing strings according to the rules of a particular locale. This is useful for tasks like sorting lists of strings in a way that respects language-specific rules and character ordering.'''
# ✅ for...of statement
'''creates a loop iterating over iterable objects or elements such as built-in String, Array, Array-like objects (like arguments or NodeList), TypedArray, Map, Set, and user-defined iterables. '''
# ✅ Is PostMessage secure - Yes, postMessages can be considered very secure as long as the programmer/developer is careful about checking the origin and source of an arriving message. But if you try to send/receive a message without verifying its source will create cross-site scripting attacks.
# ✅ problems with postmessage target origin as wildcard
'''Using a wildcard (*) as the target origin in postMessage can lead to security vulnerabilities, as it allows any domain to receive the message. This can expose sensitive data to malicious websites and increase the risk of cross-site scripting (XSS) attacks. It is recommended to specify the exact origin of the target window to ensure that messages are only sent to trusted domains.
targetWindow.postMessage(message, "*");'''
# ✅ How do you avoid receiving postMessages from attackers - message.origin
# ✅ Can I avoid using postMessages completely - 
'''You cannot avoid using postMessages completely(or 100%). Even though your application doesn’t use postMessage considering the risks, a lot of third party scripts use postMessage to communicate with the third party service. So your application might be using postMessage without your knowledge.'''
# ✅ Is postMessages synchronous - 
'''No, postMessages are asynchronous. The message is sent to the target window, and the sender continues executing without waiting for a response. The target window can then handle the message at its own pace.'''
# ✅ What paradigm is Javascript
'''multi-paradigm programming language that supports various programming styles, including imperative, functional, and object-oriented programming..'''
# ✅ internal vs external javascript
'''Internal JavaScript: It is the source code within the script tag. External JavaScript: The source code is stored in an external file(stored with .js extension) and referred with in the tag.'''
# ✅ Is JavaScript faster than server side script - Yes because JavaScript is a client-side script it does not require any web server’s help for its computation or calculation.
# ✅ get the status of a checkbox - console.log(document.getElementById(‘checkboxname’).checked); 
# ✅ purpose of double tilde operator (~~  double NOT bitwise operator) - slightly quicker substitute for Math.floor()
# ✅ convert character to ASCII code
'''
"ABC".charCodeAt(0); // returns 65
String.fromCharCode(65, 66, 67); // returns "ABC" '''
# ✅ ArrayBuffer
'''used to represent a generic, fixed-length raw binary data buffer.
let buffer = new ArrayBuffer(16); // create a buffer of length 16
//Create a DataView referring to the buffer
let view = new DataView(buffer);
'''
# ✅ purpose of Error object
'''a built-in JavaScript object that represents an error that occurs during the execution of a script. It provides information about the error, such as its name, message, and stack trace. The Error object can be used to create custom error types and handle exceptions in a structured way. It is commonly used in try-catch blocks to catch and handle errors gracefully., new Error([message[, fileName[, lineNumber]]])'''
# ✅ purpose of EvalError object
'''a built-in JavaScript object that represents an error that occurs when the eval() function is used incorrectly. It is a subclass of the Error object and is thrown when there is a problem with the evaluation of a string as JavaScript code. EvalError is rarely used in modern JavaScript development, as the use of eval() is generally discouraged due to security and performance concerns., new EvalError([message[, fileName[, lineNumber]]])'''
# ❌ What are the list of cases error thrown from non-strict mode to strict mode
# ✅ Do all objects have prototypes - No, Object.prototype itself and Objects created with **Object.create(null)**
# ✅ parameter vs argument - Parameter is the variable name of a function definition whereas an argument represents the value given to a function when it is invoked.
# ✅ some() method
'''a built-in JavaScript array method that tests whether at least one element in the array passes the test implemented by the provided callback function. It returns true if any element satisfies the condition, otherwise it returns false. The some() method does not modify the original array and is often used for checking conditions on array elements without iterating through all of them., array.some(callback(element[, index[, array]])[, thisArg])''' 
# ✅ combine two or more arrays - array1.concat(array2, array3, ..., arrayX)
# ✅ Shallow vs Deep copy
# ✅ create specific number of copies of a string - "Hello".repeat(4); // 'HelloHelloHelloHello'
# ✅ return all matching strings against a regular expression - let greetingList = [...greeting.matchAll(regexp)];
# ✅ trim a string at the beginning or ending - trimStart/trimLeft and trimEnd/trimRight
# ✅ Does javascript uses mixins
'''
JavaScript does not have built-in support for mixins as a formal language feature. However, developers commonly implement mixins using various patterns to enable code reuse and composition.
A mixin is a way to add reusable functionality from one or more objects into a class or another object, without using classical inheritance. It promotes object composition by combining behaviors or properties from different sources into a single destination.'''
# Mixin Example using Object composition - Avoids deep inheritance hierarchies, Encourages composition over inheritance, Promotes reusable and modular code
# ✅ thunk function
'''a higher-order function which delays the evaluation of the value. It doesn’t take any arguments but gives the value whenever you invoke the thunk. i.e, It is used not to execute now but it will be sometime in the future.'''
# ✅ asynchronous thunks
'''asynchronous thunks are useful to make network requests.'''
# ✅ reflow vs repaint
'''Reflow is the process of recalculating the layout of a web page when changes are made to the DOM or CSS that affect the size or position of elements. Repaint, on the other hand, is the process of redrawing elements on the screen without changing their layout. Reflow is more expensive in terms of performance compared to repaint, as it requires recalculating positions and sizes of elements.'''
# ✅ What happens with negating an array - console.log(![]); // false because an array is truthy
# ✅ What happens if we add two arrays
'''console.log(["a"] + ["b"]); // "ab"
console.log([] + []); // ""
console.log(![] + []); // "false", because ![] returns false.'''
# ✅ output of prepend additive operator on falsy values
'''console.log(+null); // 0
console.log(+undefined); // NaN
console.log(+false); // 0
console.log(+NaN); // NaN
console.log(+""); // 0'''
# ❌ create self string using special characters
# ✅ remove falsy values from an array
'''const myArray = [false, null, 1, 5, undefined];
myArray.filter(Boolean); // [1, 5] // is same as myArray.filter(x => x);'''
# ✅ get unique values of an array - console.log([...new Set([1, 2, 4, 4, 3])]); // [1, 2, 4, 3]
# ✅ destructuring aliases
'''const obj = { x: 1 };
// Grabs obj.x as as { otherName }
const { x: otherName } = obj;'''
# ✅ map the array values without using map method
'''const countries = [
  { name: "India", capital: "Delhi" },
  { name: "US", capital: "Washington" },
  { name: "Russia", capital: "Moscow" },
  { name: "Singapore", capital: "Singapore" },
  { name: "China", capital: "Beijing" },
  { name: "France", capital: "Paris" },
];
const cityNames = Array.from(countries, ({ capital }) => capital);
console.log(cityNames); // ['Delhi, 'Washington', 'Moscow', 'Singapore', 'Beijing', 'Paris']'''
# ✅ How do you empty an array - cities.length = 0; // cities becomes []
# ✅ How do you round numbers to certain decimals - pie = pie.toFixed(3); // 3.142
# ✅ easiest way to convert an array to an object
'''var fruits = ["banana", "apple", "orange", "watermelon"];
var fruitsObject = { ...fruits };
console.log(fruitsObject); // {0: "banana", 1: "apple", 2: "orange", 3: "watermelon"}'''
# ✅ create an array with some data
'''var newArray = new Array(5).fill("0");
console.log(newArray); // ["0", "0", "0", "0", "0"]'''
# ✅ placeholders from console object - %o, %s, %d
'''const user = { name: "John", id: 1, city: "Delhi" };
console.log(
  "Hello %s, your details %o are available in the object form",
  "John",
  user
); // Hello John, your details {name: "John", id: 1, city: "Delhi"} are available in object'''
# ✅ Is it possible to add CSS to console messages
'''console.log(
  "%c The text has blue color, with large font and red background",
  "color: blue; font-size: x-large; background: red"
);'''
# ✅ dir method of console object - console.dir(obj);, used to display an interactive list of the properties of the specified JavaScript object as JSON.
# ✅ Is it possible to debug HTML elements in console
'''const element = document.getElementsByTagName("body")[0];
console.log(element);'''
# ✅ display data in a tabular format using console object
'''const users = [
  { name: "John", id: 1, city: "Delhi" },
  { name: "Max", id: 2, city: "London" },
  { name: "Rod", id: 3, city: "Paris" },
];
console.table(users);'''
# ✅ verify that an argument is a Number or not - !isNaN(parseFloat(n)) && isFinite(n);
# ✅ create copy to clipboard button
'''document.querySelector("#copy-button").onclick = function () {
  // Select the content
  document.querySelector("#copy-input").select();
  // Copy to the clipboard
  document.execCommand("copy");
};'''
# ✅ shortcut to get timestamp
'''console.log(new Date().getTime());
console.log(+new Date());
console.log(Date.now());'''
# ✅ flattening multi dimensional arrays - arr.flat(Infinity);
# ✅ What is the easiest multi condition checking
'''// Verbose approach
if (
  input === "first" ||
  input === 1 ||
  input === "second" ||
  input === 2
) {
  someFunction();
}
// Shortcut
if (["first", 1, "second", 2].indexOf(input) !== -1) {
  someFunction();
}'''
# ✅ capture browser back button
'''window.addEventListener("beforeunload", () => {
  console.log("Clicked browser back button");
});
window.addEventListener("popstate", () => {
  console.log("Clicked browser back button");
  box.style.backgroundColor = "white";
});
'''
# ✅ disable right click in the web page - <body oncontextmenu="return false;"></body>
# ❌ wrapper objects
'''a feature in JavaScript that allows you to create objects that wrap primitive values, providing additional methods and properties for manipulating those values. Wrapper objects are created automatically when you access properties or methods on primitive values, such as strings, numbers, and booleans. They allow you to treat primitive values as objects, enabling you to use methods like toUpperCase() on strings or toFixed() on numbers.'''

# ✅ AJAX
'''Asynchronous JavaScript and XML (AJAX) is a technique used in web development to create asynchronous web applications. It allows web pages to send and receive data from a server asynchronously, without requiring a full page reload. AJAX uses JavaScript to make HTTP requests to the server, retrieve data (often in JSON or XML format), and update the web page dynamically based on the response. This results in a more interactive and responsive user experience.'''
# ✅ ways to deal with Asynchronous Code - Callbacks, Promises, Async/await, Third-party libraries such as async.js,bluebird etc
# ✅ How to cancel a fetch request - new AbortController();
# ❌ web speech API
'''a browser API that enables web applications to incorporate speech recognition and synthesis capabilities. It allows developers to convert spoken language into text (speech recognition) and generate spoken language from text (speech synthesis). The Web Speech API provides a way to create voice-controlled applications, enhance accessibility, and improve user interaction through natural language processing., window.SpeechRecognition and new SpeechSynthesisUtterance("Hello World!");'''
# ✅ minimum timeout throttling
'''Both browser and NodeJS javascript environments throttles with a minimum delay that is greater than 0ms. That means even though setting a delay of 0ms will not happen instantaneously. Browsers: They have a minimum delay of 4ms. This throttle occurs when successive calls are triggered due to callback nesting(certain depth) or after a certain number of successive intervals.'''
# ✅ implement zero timeout in modern browsers - You can't
# ✅ tasks in event loop
'''A task is any javascript code/program which is scheduled to be run by the standard mechanisms such as initially starting to run a program, run an event callback, or an interval or timeout being fired. All these tasks are scheduled on a task queue. '''
# ✅ microtask
'''A microtask is a type of JavaScript callback that is scheduled to run immediately after the currently executing script and before the next event loop tick. Microtasks are executed after the current task completes and before any new tasks (macrotasks) are run.'''
# ✅ What are different event loops - Browser Event Loop, Node.js Event Loop
# ❌ queueMicrotask
'''a method in JavaScript that allows you to schedule a microtask to be executed after the current task completes. It is used to add a function to the microtask queue, ensuring that it runs before the next event loop tick. This is useful for handling asynchronous operations and ensuring that certain tasks are executed in a specific order without blocking the main thread.'''
# ❌ use javascript libraries in typescript file - declare var customLibrary;
# ❌ promises vs observables
'''
- promises emits only a single value at a time while observables can emit multiple values over time(stream of values ranging from 0 to multiple).
- promises are eager in nature; they are going to be called immediately while observables are lazy in nature; they are not going to be called until you subscribe to them.
- Promise is always asynchronous even though it resolved immediately whereas Observable can be synchronous or asynchronous.
- promises doesn't provide any operators while observables provides operators such as map, forEach, filter, reduce, retry, and retryWhen etc
- promises cannot be canceled while observables can be canceled using unsubscribe() method.'''
# ✅ heap
'''a region of a computer's memory where dynamically allocated objects are stored. In JavaScript, the heap is used for storing objects, arrays, and functions that are created at runtime.'''
# ✅ event table
'''a data structure used in JavaScript to manage event listeners and their associated callbacks. It maps event types to their corresponding listeners, allowing the event loop to efficiently dispatch events to the appropriate handlers when they occur. The event table is an essential part of the event-driven architecture in JavaScript, enabling asynchronous programming and responsive user interfaces.'''
#  ❌ microTask queue
'''a queue in JavaScript that holds microtasks, which are tasks that need to be executed after the current task completes but before the next event loop tick. Microtasks are typically used for handling promises and other asynchronous operations. The microTask queue is processed after the current task finishes, ensuring that microtasks are executed in a timely manner without blocking the main thread.'''
# ✅ shim vs polyfill
'''A shim is a piece of code that provides compatibility for a feature that is not natively supported in a particular environment. It allows developers to use modern features in older browsers or environments by providing a fallback implementation. A polyfill, on the other hand, is a specific type of shim that implements a missing feature in JavaScript, allowing developers to use newer language features in older environments. Polyfills are often used to ensure cross-browser compatibility and provide a consistent API across different platforms.'''
# ✅ detect primitive or non primitive value type - primitive types include boolean, string, number, BigInt, null, Symbol and undefined. Whereas non-primitive types include the Objects.

# ✅ babel
'''a JavaScript compiler that allows developers to use the latest JavaScript features and syntax while ensuring compatibility with older browsers. It transforms modern JavaScript code into a version that can run in environments that do not support the latest features. Babel is widely used in web development to enable the use of ES6+ features, JSX syntax, and other experimental language features.'''
# ✅ Is Node.js completely single threaded
'''No, Node.js is not completely single-threaded. While the main event loop runs on a single thread, Node.js uses a thread pool (libuv) to handle I/O operations asynchronously. This allows Node.js to perform non-blocking I/O operations efficiently, enabling it to handle multiple requests concurrently without blocking the main thread. However, CPU-intensive tasks may still block the event loop, so developers need to be cautious about performance when using synchronous code in Node.js.'''
# ✅ use cases of observables - web sockets with push notifications, user input changes, repeating intervals, etc
# ✅ RxJS (Reactive Extensions for JavaScript)
'''a library for composing asynchronous and event-based programs using observable sequences. It provides a powerful set of operators for transforming, filtering, and combining streams of data, making it easier to work with asynchronous events and manage complex data flows in JavaScript applications. RxJS is widely used in modern web development, especially in frameworks like Angular, to handle reactive programming patterns.'''
# ❌ Function constructor vs function declaration
'''Function constructor: It creates a new function object from a string of code. It is less commonly used and can lead to security issues if not handled properly. 
Function declaration: It defines a named function that can be called later in the code. It is the preferred way to define functions in JavaScript due to its readability and maintainability.'''
# ✅ Short circuit condition - condensed way of writing simple if statements., authenticate && loginToPorta();
# ✅ easiest way to resize an array
'''var array = [1, 2, 3, 4, 5];
console.log(array.length); // 5

array.length = 2;
console.log(array.length); // 2
console.log(array); // [1,2]'''
# ✅ observable
'''function that can return a stream of values either synchronously or asynchronously to an observer over time. The consumer can get the value by calling subscribe() method.'''
# ❌ function vs class declarations
'''Function declarations are hoisted, meaning they can be called before they are defined in the code. Class declarations are not hoisted, so they must be defined before they are used. Function declarations use the function keyword, while class declarations use the class keyword. Functions can be invoked directly, while classes need to be instantiated using the new keyword.'''
# ✅ async function
'''a function that allows you to write asynchronous code using the async/await syntax. It returns a promise and can contain await expressions, which pause the execution of the function until the awaited promise is resolved. Async functions make it easier to work with asynchronous operations, improving code readability and maintainability.'''
# ✅ prevent promises swallowing errors - Add catch block at the end of each chain:, Add done method:, Extend ES6 Promises by Bluebird
# ✅ deno
'''simple, modern and secure runtime for JavaScript and TypeScript that uses V8 JavaScript engine and the Rust programming language. It solves the inherent problems of Node.Js and has been officially released in May 2018. Unlike Node.JS, by default Deno executes the code in a sandbox, which means that runtime has no access to below areas: The file system, The network, Execution of other scripts, The environment variables'''
# ❌ make an object iterable in javascript - Symbol.iterator
# ❌ Proper Tail Call
'''A tail call is a subroutine or function call performed as the final action of a calling function. Whereas Proper tail call(PTC) is a technique where the program or code will not create additional stack frames for a recursion when the function call is a tail call.'''
# ✅ check an object is a promise or not - Promise && Promise.resolve, value && typeof value.then === "function
# ✅ detect if a function is called as constructor - new.target
# ✅ arguments object vs rest parameter
'''The arguments object is an array-like object that contains the arguments passed to a function. It is available within the function scope and can be used to access the arguments dynamically. The rest parameter, on the other hand, is a syntax that allows you to represent an indefinite number of arguments as an array. It is defined using the ... syntax in the function parameter list. The rest parameter provides a more concise and readable way to handle variable-length argument lists compared to the arguments object.
- The arguments object is an array-like but not an array. Whereas the rest parameters are array instances.
- The arguments object does not support methods such as sort, map, forEach, or pop. Whereas these methods can be used in rest parameters.
- The rest parameters are only the ones that haven’t been given a separate name, while the arguments object contains all arguments passed to the function'''
# ✅ spread operator vs rest parameter
'''The spread operator (...) is used to expand an iterable (like an array) into individual elements, while the rest parameter (...) is used to collect multiple arguments into a single array parameter in a function definition. The spread operator is typically used in function calls or array literals, whereas the rest parameter is used in function declarations to handle variable-length argument lists.'''
# ❌ different kinds of generators
'''Generators are functions that can be paused and resumed, allowing for the generation of a sequence of values over time. There are several types of generators in JavaScript:
1. **Function Generators**: Defined using the `function*` syntax, these generators use the `yield` keyword to produce values one at a time.
2. **Async Generators**: Defined using the `async function*` syntax, these generators allow for asynchronous iteration using the `await` keyword with `yield`.
3. **Generator Expressions**: Similar to array comprehensions, these are concise ways to create generators using the `yield` keyword within an expression.
4. **Custom Generators**: You can create custom generator functions that implement specific logic for generating values based on your requirements.'''
# ✅ built-in iterables - Arrays, Strings, Maps, Sets, Typed Arrays, NodeLists, Arguments object
# ✅ for...of vs for...in statements - for..in iterates over all enumerable property keys of an object and for..of iterates over the values of an iterable object.
# ❌ How do you define instance and non-instance properties - Instance properties must be defined inside of class methods. But Static(class) and prototype data properties must be defined outside of the ClassBody declaration
# ✅ isNaN vs Number.isNaN?
'''isNaN: The global function isNaN converts the argument to a Number and returns true if the resulting value is NaN.
Number.isNaN: This method does not convert the argument. But it returns true when the type is a Number and value is NaN.'''
# ❌ invoke an IIFE without any extra brackets?
'''
(function (dt) {
  console.log(dt.toLocaleTimeString());
})(new Date());'''
# ✅ Is that possible to use expressions in switch cases? - yes
# ✅ easiest way to ignore promise errors? - await promise.catch((e) => void e);
# ✅ style the console output using CSS? - console.log("%cThis is a red text", "color:red");
# ✅ nullish coalescing operator (??)? 
'''logical operator that returns its right-hand side operand when its left-hand side operand is null or undefined, and otherwise returns its left-hand side operand.'''
# ✅ ?? vs || operator?
'''The ?? operator returns the right-hand side operand only when the left-hand side operand is null or undefined, while the || operator returns the right-hand side operand when the left-hand side operand is falsy (null, undefined, false, 0, NaN, or an empty string). This means that ?? is more specific in its behavior compared to ||.'''
# ✅ How do you group and nest console output? - console.group("User Details");, console.groupEnd();, console.groupCollapsed()
# ✅ dense vs sparse arrays
'''An array contains items at each index starting from first(0) to last(array.length - 1) is called as Dense array. Whereas if at least one item is missing at any index, the array is called as sparse.'''
# ✅ ways to create sparse arrays? - Array literal, Array() constructor, Delete operator, Increase length property
# ❌ setTimeout, setImmediate and process.nextTick?
'''setTimeout: Schedules a function to be executed after a specified delay (in milliseconds). It is used for delaying the execution of code.
setImmediate: Schedules a function to be executed immediately after the current event loop cycle, allowing other I/O operations to complete first. It is specific to Node.js and is not available in browsers.
process.nextTick: Schedules a function to be executed in the next iteration of the event loop, before any I/O operations. It is also specific to Node.js and allows for immediate execution of code after the current operation completes.'''
# ✅ reverse an array without modifying original array? - newArray = [...originalArray].reverse();
# ✅ create custom HTML element? - customElements.define("custom-element", CustomElement);
# ✅ global execution context?
'''The global execution context is the default context in which JavaScript code runs. It is created when a script is loaded and contains the global object (window in browsers, global in Node.js), as well as any variables and functions defined in the global scope. The global execution context is the outermost context and serves as the foundation for all other execution contexts created during the execution of JavaScript code.'''
# ✅ function execution context?
'''The function execution context is created whenever a function is invoked. It contains information about the function's parameters, local variables, and the value of the `this` keyword within that function. Each time a function is called, a new execution context is created, allowing for isolated variable scopes and enabling recursion and nested function calls. The function execution context is pushed onto the call stack when the function is invoked and popped off when the function completes execution.'''
# ❌ debouncing?
'''Debouncing is a technique used to limit the rate at which a function is executed. It ensures that a function is only called after a specified delay has passed since the last time it was invoked. This is particularly useful for handling events that can trigger multiple times in quick succession, such as scrolling, resizing, or typing in an input field. By debouncing, you can improve performance and reduce unnecessary function calls.'''
# ❌ throttling?
'''Throttling is a technique used to control the frequency at which a function is executed. It ensures that a function is called at most once within a specified time interval, regardless of how many times it is triggered. This is useful for limiting the rate of execution for events that can occur frequently, such as scrolling or resizing. Throttling helps improve performance by preventing excessive function calls and reducing resource consumption.'''
# ✅ optional chaining?
'''Optional chaining is a feature in JavaScript that allows you to safely access deeply nested properties of an object without having to check if each property in the chain exists. It uses the `?.` operator to short-circuit the evaluation if any property in the chain is `null` or `undefined`, returning `undefined` instead of throwing an error. This makes it easier to work with complex objects and reduces the need for repetitive null checks.'''
# environment record?
'''An environment record is a data structure in JavaScript that stores the variables and their values in a specific scope. It is used to manage the execution context of functions and blocks, allowing for variable lookups and scoping rules. Each execution context has its own environment record, which keeps track of the variables defined within that context, including function parameters, local variables, and any outer variables that are accessible through closures.'''
# ✅ verify if a variable is an array? - isArray(<variable>), <variable> instanceof Array, <variable>.constructor === Array
# ❌ pass by value vs pass by reference?
'''In JavaScript, primitive values (like numbers, strings, booleans, null, undefined, and symbols) are passed by value, meaning that when you assign a primitive value to a variable or pass it to a function, a copy of the value is created. Non-primitive values (like objects and arrays) are passed by reference, meaning that when you assign an object or array to a variable or pass it to a function, the variable holds a reference to the original object or array in memory. This means that changes made to the object or array will affect the original value.'''
# ✅ primitives vs non-primitives?
'''| Feature        | Primitives                 | Non-primitives         |
| -------------- | -------------------------- | ---------------------- |
| Definition     | These types are predefined | Created by developer   |
| Mutability     | Immutable                  | Mutable                |
| Comparison     | Compare by value           | Compare by reference   |
| Memory Storage | Stored in Stack            | Stored in Heap         |
| Value          | Contain certain value      | Can contain `null` too |'''
# ❌ How do you create your own bind method using either call or apply method?
# ✅ pure vs impure functions
'''| Feature                 | Pure Function                                 | Impure Function                                          |
| ----------------------- | --------------------------------------------- | -------------------------------------------------------- |
| Side Effects            | Has no side effects                           | Causes side effects                                      |
| Return Consistency      | Always returns the same result for same input | May return different results for same input              |
| Debugging & Readability | Easy to read and debug                        | Difficult to read and debug due to external dependencies |'''
# ✅ referential transparency?
'''An expression in javascript that can be replaced by its value without affecting the behaviour of the program is called referential transparency. Pure functions are referentially transparent.'''
# ✅ What are the possible side-effects in javascript?
'''Making an HTTP request. Asynchronous functions such as fetch and promise are impure.
DOM manipulations
Mutating the input data
Printing to a screen or console: For example, console.log() and alert()
Fetching the current time
Math.random() calls: Modifies the internal state of Math object'''
# ❌ compose and pipe functions?
'''Compose and pipe functions are higher-order functions used to combine multiple functions into a single function. 
- **Compose**: Takes multiple functions as arguments and returns a new function that applies the functions from right to left. It is often used to create a pipeline of transformations.
- **Pipe**: Takes multiple functions as arguments and returns a new function that applies the functions from left to right. It is often used to create a sequence of operations on data.
Both compose and pipe functions are useful for functional programming and can help improve code readability and maintainability by allowing you to build complex operations from simpler functions.'''
# ✅ module pattern?
'''designed pattern used to wrap a set of variables and functions together in a single scope returned as an object. JavaScript doesn't have access specifiers similar to other languages(Java, Python, etc) to provide private scope. It uses IIFE (Immediately invoked function expression) to allow for private scopes. i.e., a closure that protect variables and methods.'''
# ✅ Function Composition?
'''approach where the result of one function is passed on to the next function, which is passed to another until the final function is executed for the final result.'''
# ✅ How to use await outside of async function prior to ES2022?
'''(async function () {
  await Promise.resolve(console.log("Hello await")); // Hello await
})();'''
# ❌ purpose of the this keyword in JavaScript?
''' refers to the object that is executing the current function. Its value is determined by how a function is called, not where it is defined. this is essential for writing object-oriented and event-driven code, as it allows methods to interact with the data of the object they belong to.'''
# ❌ uses of closures?
'''allow functions to retain access to variables from their containing (enclosing) scope even after the outer function has finished executing. This means that a function defined within another function can access variables from the outer function, even if the outer function has already returned.'''
# ✅ phases of execution context? - Creation phase and Execution phase
# ✅ possible reasons for memory leaks?
'''
- execessive usage of global variables or omitting the var keyword in local scope.
- Forgetting to clear the timers set up by setTimeout or setInterval.
- Closures retain references to variables from their parent scope, which leads to variables might not garbage collected even they are no longer used.'''
# ✅ optimization techniques of V8 engine? - Inline expansion, Copy elision, Inline caching
# ✅ examples of built-in higher order functions? - arrays, DOM, Strings
# ✅ benefits higher order functions? - Abstraction, Reusability, Immutability, Modularity
# ❌ How do you create polyfills for map, filter and reduce methods?
# ✅ map vs forEach functions?
'''
- `map` method returns a new array with transformed elements whereas `forEach` method returns `undefined` eventhough both of them are doing the same job.
- `map` method is chainable. i.e, It can be attached with `reduce`, `filter`, `sort` and other methods as well. Whereas `forEach` cannot be attached with any other methods because it returns `undefined` value.
 - `map` method doesn't mutate the original array by returning new array. Whereas `forEach` method also doesn't mutate the original array but it's callback is allowed to mutate the original array.
'''
# ✅ Give an example of statements affected by automatic semicolon insertion? - An empty statement, var statement, An expression statement, do-while statement, continue statement, break statement, return statement, throw statement
# ✅ event phases of a browser? - Capturing phase, Target phase, Bubbling phase
# ✅ real world use cases of proxy?
'''
Vue3 used proxy concept to implement reactive state
SolidJS implemented reactive stores
Immerjs built upon proxy to track updates to immutable updates
ZenStack improved Prisma ORM for access control layer'''
# ✅ hidden classes?
'''Hidden classes are internal data structures used by JavaScript engines (like V8) to optimize object property access. When an object is created, the engine assigns it a hidden class based on its properties and their order. If properties are added or removed, the hidden class may change, allowing the engine to optimize property access for better performance. This mechanism helps improve the speed of property lookups and method calls in JavaScript objects.'''
# ✅ inline caching?
'''optimization technique based on the observation that repeated calls to same function tends to occur on same type of objects. The V8 compiler stores a cache of the type of objects that were passed as a parameter in recent method calls. Upon next time when same function is called, compiler can directly search for the type in cache.
- Monomorphic: This is a optimized caching technique in which there can be always same type of objects passed.
- Polymorphic: This ia slightly optimized caching technique in which limited number of different types of objects can be passed.
- Megamorphic: It is an unoptimized caching in which any number of different objects can be passed.
'''
# ❌ different ways to execute external scripts? - async, defer, and normal script loading
# ✅ Lexical Scope?
'''Lexical scope is a scoping mechanism in JavaScript that determines the visibility and accessibility of variables based on their position in the source code. It means that a variable defined in a certain scope is accessible only within that scope and its nested scopes. This allows for better organization of code and prevents variable name collisions, as each function or block has its own scope. Lexical scope is fundamental to understanding closures and how variables are resolved in JavaScript.'''
# ✅ detect system dark mode in javascript? -  window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
# ✅ purpose of requestAnimationFrame method? 
'''requestAnimationFrame() method in JavaScript is used to schedule a function to be called before the next repaint of the browser window, allowing you to create smooth, efficient animations. It's primarily used for animations and visual updates, making it an essential tool for improving performance when you're animating elements on the web.'''
# ✅ substring vs substr methods? - substring(start, end) and substr(start, length) (Deprecated)
# ✅ find the number of parameters expected by a function? - console.log(multiply.length); 
# ❌ globalThis, and what is the importance of it?
'''globalThis is a standard way to access the global object in JavaScript, regardless of the environment (browser, Node.js, etc.). It provides a consistent way to refer to the global scope, allowing developers to write code that works across different platforms without worrying about the specific global object name (like window in browsers or global in Node.js). This is particularly useful for libraries and frameworks that need to operate in various JavaScript environments.'''
# ✅ array mutation methods? - push, pop, unshift, shift, splice, sort, reverse, fill, copyWithIn
# ✅ module scope in JavaScript?
'''Module scope in JavaScript refers to the scope created by a module, which is a self-contained unit of code that can export and import functionality. In module scope, variables, functions, and classes defined within the module are not accessible from the global scope or other modules unless explicitly exported. This encapsulation helps prevent naming conflicts and promotes better organization of code. Modules can be imported into other modules, allowing for code reuse and separation of concerns.'''
# ✅ shadowing and illegal shadowing?
'''Shadowing occurs when a variable in a local scope has the same name as a variable in an outer scope, effectively hiding the outer variable within the local scope. This can lead to confusion and bugs if not managed carefully. 
let a = 10;
function func() {
  let a = 20; // Shadows the outer 'a'
  console.log(a); // 20
}
func();
console.log(a); // 10
Illegal shadowing refers to situations where a variable is declared in a way that conflicts with existing variables or reserved keywords, leading to syntax errors or unexpected behavior. It is important to avoid shadowing and illegal shadowing to maintain code clarity and prevent unintended consequences.'''
# ✅ Why is it important to remove event listeners after use?
'''Removing event listeners after use is important to prevent memory leaks and improve performance. When an event listener is added, it creates a reference to the function that handles the event. If the listener is not removed, it can keep the function and any associated data in memory, even if they are no longer needed. This can lead to increased memory usage and slow down the application over time. By removing event listeners when they are no longer needed, you help ensure that resources are released and the application runs efficiently.'''













