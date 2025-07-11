
http://youtube.com/watch?v=wIyHSOugGGw
https://www.youtube.com/watch?v=LOH1l-MP_9k


# sudheerj/react-interview-questions
✅ React - open-source front-end JavaScript library
major features - 
✅ JSX -
✅ rules of JSX
✅ state and props
key prop 
✅ children prop 
default props 
✅ Lifting State Up
class vs className 
✅ Fragments 
Keyed Fragments
Poprtals
✅ dangerouslySetInnerHTML 
How to enable production mode
use for loop instead map() in jsx
✅ React.version
Polymer
React vs Angular 
✅ render hijacking 
✅ registerServiceWorker 
React.memo()
React lazy function - lets you render a dynamic import as a regular component
code splitting
route based code splitting
Throttling vs Debouncing vs RequestAnimationFrame throttling
windowing technique
react-window and react-virtualized - libraries to implement windowing technique
windowing technique
Concurrent Rendering 
Imperative and Declarative in React?
JSX transform
props drilling
strict mode in react 
local mutation 
batching vs automatic batching in react 
updater function 
initializer function or lazy initialization
layout thrashing 


Hooks
Rules with hooks 
useEffect()
useRef() - forward ref
useEffect()
uselayoutEffect()
useContext()
useReducer()
useMemo()
useImperativeHandle()



✅ Components - 
✅ functional components
✅ class components
❌ pure components 
✅ stateful components - component is dependent of its state
✅ stateless components - component is independent of its state
✅ controlled components - fully manages the form element's state
✅ uncontrolled components - manage their own state internally via the DOM
✅ higher-order components
✅ switching component
loadable component 
suspense component
react server components
wrapper component



✅ HTML and React event
synthetic events
inline conditional expressions
✅ pointer events - unified way of handling all input events
✅ htmlFor vs for
defaultValue vs value
Diffing Algorithm
capture phase events


❌ Element vs Component -
✅ Virtual DOM - lightweight, in-memory representation of Real DOM
✅ How Virtual DOM works
Real DOM vs Virtual DOM  
Shadow DOM vs Virtual DOM
❌ createElement and cloneElement

✅ React Fiber
✅ Reconcilation
React.lazy

✅ prop-types - library for type checking
React.PropTypes.shape({...}) - pass an array of objects to a component with a particular shape 
✅ moize - library for memoization of component in another component.
React Transition Group and React Motion -  animation packages
✅ React Router - routing library 
react-router vs history
<Router> - <BrowserRouter>, <HashRouter>, <MemoryRouter>, <StaticRouter> 
✅ URLSearchParams - parse query strings
✅ React Intl - internationalization library
<FormattedMessage>
injectIntl()
formatDate()
redux-saga - library for managing side effects in React uses generators
call() vs put() in redux-saga - 
Redux thunk - library for managing side effects in React uses promises
redux-saga vs redux-thunk
React Dev-tools - debugging tool
Formik - library for handling forms in React
web components in react app 
MobX - library fro state management 
Reux vs MobX 
immer - library for immutable state management

✅ react-dom - 
❌ React vs ReactDOM
✅ Server Side Rendering - handle rendering on Node servers
React hydration 
ReactDOMServer - renderToString(), renderToStaticMarkup()
render()
hydrate()
unmountComponentAtNode()
findDOMNode()
createPortal()
flushSync() 

React Mixins

✅ Shallow Renderer
TestRenderer 
✅ ReactTestUtils 
✅ Jest - testing framework
Jest vs Jasmine

flux - application architecture  to manage data flow in React,
Action, Dispatcher, Store, View
Flux vs redux 
Redux - state management library  enabling easier debugging, testing, and maintenance of states 
core principles of  Redux -
mapStateToProps() vs mapDispatchToProps()
createStore()
connect()
Redux vs RxJs
React context vs Redux
Reducer
root reducer
component vs container in Redux -
ownProps 
selectors - 
Redux Form 
applyMiddleware()
Relay vs Redux 
Actions 

React vs React native

reselect - memoized inputs/outputs of redux reducers
✅ flow - static type checking
✅ flow vs prop-types

webpack and babel

styled-components - library for styling React components


# What is React?
'''open-source front-end JavaScript library for building user interfaces based on components. It's used for handling the view layer in web and mobile applications, and allows developers to create reusable UI components and manage the state of those components efficiently.'''
# What is the history behind React’s evolution?
''' XHP is a PHP extension which improved the syntax of the language such that XML document fragments become valid PHP expressions and the primary purpose was used to create custom and reusable HTML elements. It was  created by Jordan Walke, a software engineer at Facebook (now Meta). It was first deployed on Facebook's News Feed in 2011 and on Instagram in 2012.'''
# 👉 What are the major features of React?
'''Component-Based Architecture, Virtual DOM, JSX (JavaScript XML), Unidirectional Data Flow, Declarative UI, React Hooks, Context API, Error Boundaries, Server-Side Rendering (SSR), Concurrent Mode, React Server Components, Suspense'''
# What is JSX?
''' it just provides the syntactic sugar for the React.createElement(type, props, ...children) function, giving us expressiveness of JavaScript along with HTML like template syntax.'''
# 👉What is the difference between an Element and a Component?
'''
Element - A React Element is a plain JavaScript object that describes what you want to see on the UI. It represents a DOM node or a component at a specific point in time.
Component - A Component is a function or class that returns an element (or a tree of elements) to describe part of the UI. Components can accept inputs (called props) and manage their own state (in case of class or function components with hooks).
- Components allow you to split the UI into independent, reusable pieces, each isolated and composable.
- You can define a component using a function or a class'''
# 👉How do you create components in React?
'''
Function Components: Those are pure JavaScript functions that accept props object as the one and only one parameter and return React elements to render the output.
Class Components: You can also use ES6 class to define a component. The above function component can be written as a class component
'''
# When should you use a Class Component over a Function Component?
# What are Pure Components?
# What is state in React?
# What are props in React?
# What is the difference between state and props?
# What is the difference between HTML and React event handling?
# What are synthetic events in React?
# What are inline conditional expressions?
# What is the "key" prop and what is its benefit when used in arrays of elements?
# What is the Virtual DOM?
# How does the Virtual DOM work?
# What is the difference between Shadow DOM and Virtual DOM?
# What is React Fiber?
# What is the main goal of React Fiber?
# What are controlled components?
# What are uncontrolled components?
# What is the difference between createElement and cloneElement?
# What is Lifting State Up in React?
# What are Higher-Order Components?
# What is the children prop?
# How do you write comments in React?
# What is reconciliation?
# Does the lazy function support named exports?
# Why does React use className instead of the class attribute?
# What are Fragments?
# Why are Fragments better than container divs?
# What are portals in React?
# What are stateless components?
# What are stateful components?
# How do you apply validation to props in React?
# What are the advantages of React?
# What are the limitations of React?
# What are the recommended ways for static type checking?
# What is the use of the react-dom package?
# What is ReactDOMServer?
# How do you use innerHTML in React?
# How do you apply styles in React?
# How are events different in React?
# What is the impact of using indexes as keys?
# How do you conditionally render components?
# Why do we need to be careful when spreading props on DOM elements?
# How do you memoize a component?
# How do you implement Server-Side Rendering (SSR)?
# How do you enable production mode in React?
# Do Hooks replace render props and higher-order components?
# What is a switching component?
# What are React Mixins?
# What are the pointer events supported in React?
# Why should component names start with a capital letter?
# Are custom DOM attributes supported in React v16?
# How do you loop inside JSX?
# How do you access props within attribute quotes?
# What is a React PropType array with shape?
# How do you conditionally apply class attributes?
# What is the difference between React and ReactDOM?
# Why is ReactDOM separated from React?
# How do you use the React label element?
# How do you combine multiple inline style objects?
# How do you re-render the view when the browser is resized?
# How do you pretty-print JSON with React?
# Why can’t you update props in React?
# How do you focus an input element on page load?
# How can you find the version of React at runtime in the browser?
# How do you add Google Analytics for React Router?
# How do you apply vendor prefixes to inline styles in React?
# How do you import and export components using React and ES6?
# What are the exceptions to React component naming?
# Is it possible to use async/await in plain React?
# What are common folder structures for React?
# What are popular packages for animation?
# What are the benefits of style modules?
# What are popular React-specific linters?
# React Router
# What is React Router?
# How is React Router different from the history library?
# What are the components of React Router v6?
# What is the purpose of the push and replace methods of history?
# How do you programmatically navigate using React Router v4?
# How do you get query parameters in React Router v4?
# Why do you get a "Router may have only one child element" warning?
# How do you pass params to the history.push method in React Router v4?
# How do you implement a default or NotFound page?
# How do you get history in React Router v4?
# How do you perform an automatic redirect after login?
# React Internationalization
# What is React Intl?
# What are the main features of React Intl?
# What are the two ways of formatting in React Intl?
# How do you use FormattedMessage as a placeholder with React Intl?
# How do you access the current locale with React Intl?
# How do you format a date using React Intl?
# React Testing
# What is the Shallow Renderer in React testing?
# What is the TestRenderer package in React?
# What is the purpose of the ReactTestUtils package?
# What is Jest?
# What are the advantages of Jest over Jasmine?
# Can you give a simple example of a Jest test case?
# React Redux
# What is Flux?
# What is Redux?
# What are the core principles of Redux?
# What are the downsides of Redux compared to Flux?
# What is the difference between mapStateToProps() and mapDispatchToProps()?
# Can you dispatch an action in a reducer?
# How do you access the Redux store outside a component?
# What are the drawbacks of the MVW pattern?
# Are there any similarities between Redux and RxJS?
# How do you reset state in Redux?
# What is the difference between React Context and React Redux?
# Why are Redux state functions called reducers?
# How do you make an AJAX request in Redux?
# Should you keep all component states in the Redux store?
# What is the proper way to access the Redux store?
# What is the difference between a component and a container in React Redux?
# What is the purpose of constants in Redux?
# What are the different ways to write mapDispatchToProps()?
# What is the use of the ownProps parameter in mapStateToProps() and mapDispatchToProps()?
# How do you structure Redux top-level directories?
# What is Redux Saga?
# What is the mental model of Redux Saga?
# What are the differences between call and put in Redux Saga?
# What is Redux Thunk?
# What are the differences between Redux Saga and Redux Thunk?
# What is Redux DevTools?
# What are the features of Redux DevTools?
# What are Redux selectors and why should you use them?
# What is Redux Form?
# What are the main features of Redux Form?
# How do you add multiple middlewares to Redux?
# How do you set the initial state in Redux?
# How is Relay different from Redux?
# What is an action in Redux?
'''React Native'''
# What is the difference between React Native and React?
# How do you test React Native apps?
# How do you log in React Native?
# How do you debug React Native apps?
'''React Supported Libraries and Integration'''
# What is Reselect and how does it work?
# What is Flow?
# What is the difference between Flow and PropTypes?
# How do you use Font Awesome icons in React?
# What is React DevTools?
# Why does DevTools not load in Chrome for local files?
# How do you use Polymer in React?
# What are the advantages of React over Vue.js?
# What is the difference between React and Angular?
# Why is the React tab not showing up in DevTools?
# What are styled-components?
# Can you give an example of styled-components?
# What is Relay?
'''Miscellaneous'''
# What are the main features of the Reselect library?
# Can you give an example of Reselect usage?
# Can Redux only be used with React?
# Do you need a specific build tool to use Redux?
# How do Redux Form initial values get updated from state?
# How do React PropTypes allow different types for one prop?
# Can you import an SVG file as a React component?
# What is render hijacking in React?
# How do you pass numbers to a React component?
# Do you need to keep all state in Redux? Should you ever use React’s internal state?
# What is the purpose of registerServiceWorker in React?
# What is the React.memo function?
# What is the React.lazy function?
# How do you prevent unnecessary updates using setState?
# How do you render arrays, strings, and numbers in React v16?
# What are Hooks?
# What rules must be followed for Hooks?
# How do you ensure Hooks follow the rules in your project?
# What are the differences between Flux and Redux?
# What are the benefits of React Router v4?
# Can you describe the componentDidCatch lifecycle method signature?
# In which scenarios do error boundaries not catch errors?
# What is the behavior of uncaught errors in React v16?
# What is the proper placement for error boundaries?
# What is the benefit of a component stack trace from an error boundary?
# What are default props?
# What is the purpose of the displayName class property?
# What is the browser support for React applications?
# What is code-splitting?
# What are keyed Fragments?
# Does React support all HTML attributes?
# When do component props default to true?
# What is Next.js and what are its major features?
# How do you pass an event handler to a component?
# How do you prevent a function from being called multiple times?
# How does JSX prevent injection attacks?
# How do you update rendered elements?
# How do you indicate that props are read-only?
# What are the conditions for safely using an index as a key?
# Do keys need to be globally unique?
# What is the popular choice for form handling?
# What are the advantages of Formik over the Redux Form library?
# Why are you not required to use inheritance?
# Can you use web components in a React application?
# What is a dynamic import?
# What are loadable components?
# What is a Suspense component?
# What is route-based code splitting?
# What is the purpose of the default value in Context?
# What is the diffing algorithm?
# What rules are covered by the diffing algorithm?
# When do you need to use refs?
# Must a prop be named "render" for render props?
# What are the problems with using render props with Pure Components?
# What is the windowing technique?
# How do you print falsy values in JSX?
# What is the typical use case for portals?
# How do you set a default value for an uncontrolled component?
# What is your favorite React stack?
# What is the difference between the real DOM and the Virtual DOM?
# How do you add Bootstrap to a React application?
# Can you list the top websites or applications using React as a front-end framework?
# Is it recommended to use the CSS-in-JS technique in React?
# Do you need to rewrite all class components with Hooks?
# How do you fetch data with React Hooks?
# Do Hooks cover all use cases for classes?
# What is the stable release for Hooks support?
# Why do we use array destructuring (square bracket notation) in useState?
# What sources were used for introducing Hooks?
# How do you access the imperative API of web components?
# What is Formik?
# What are typical middleware choices for handling asynchronous calls in Redux?
# Do browsers understand JSX code?
# Can you describe data flow in React?
# What is MobX?
# What are the differences between Redux and MobX?
# Should you learn ES6 before learning ReactJS?
# What is concurrent rendering?
# What is the difference between async mode and concurrent mode?
# Can you use JavaScript URLs in React v16.9?
# What is the purpose of the ESLint plugin for Hooks?
# What is the difference between imperative and declarative programming in React?
# What are the benefits of using TypeScript with ReactJS?
# How do you ensure a user remains authenticated on page refresh while using Context API state management?
# What are the benefits of the new JSX transform?
# How is the new JSX transform different from the old transform?
# What are React Server Components?
# What is prop drilling?
# What is the difference between the useState and useRef Hooks?
# What is a wrapper component?
# What are the differences between the useEffect and useLayoutEffect Hooks?
# What are the differences between functional and class components?
# What is Strict Mode in React?
# What is the benefit of Strict Mode?
# Why does Strict Mode render twice in React?
# What are the rules of JSX?
# What is the reason multiple JSX tags must be wrapped?
# How do you prevent mutating array variables?
# What are capture phase events?
# How does React update the screen in an application?
# How does React batch multiple state updates?
# Is it possible to prevent automatic batching?
# What is React hydration?
# How do you update objects inside state?
# How do you update nested objects inside state?
# How do you update arrays inside state?
# How do you use the Immer library for state updates?
# What are the benefits of preventing direct state mutations?
# What are the preferred and non-preferred array operations for updating state?
# What will happen when defining nested function components?
# Can I use keys for non-list items?
# What are the guidelines to follow for writing reducers?
'''Hooks'''
# What is useReducer hook? Can you describe its usage?
# How do you compare useState and useReducer?
# How does Context work with the useContext hook?
# What are the use cases of the useContext hook?
# When should you use client and server components?
# What are the differences between the Page Router and App Router in Next.js?
