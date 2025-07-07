

sync vs async pipes
why * in *ngFor 
template expression vs template statement
pure vs impure pipes 


RxJs
observable
Observables
Observer
promise vs Observables ❌
Subject
SubjectBehaviour

Angular elements vs Custom Elements 
dynamic components
Directives

Angular Router
router-outlet
routerLink
routerLinkActive
RouterState 
router events
activated route 
wildcard route
RouteParameters - path parameters, query parameters, optional parameters

Angular Compiler
JIT vs AOT
folding
type narrowing
webpack vs bazel
differential loading
safe navigation operator or Elvis Operator 
NgNodule vs javascript module 


Angular Animation
State function
Style function
animate function
transition function
trigger function

Angular language services
DI Token
Angular DSL

zone.js - NgZone, Noop Zone, zone context, lifecycle hooks of zone, run() vs runOutsideAngular(), 

Forms - ReactiveFormModule, FormsModule, FormControl, FormGroup, FormArray, FormBuilder, Reactive Form, Template Driven Form, Dynamic Form, patchValue() vs setValue(),  visited - ng-touched, ng-untouched, Value has changed - ng-dirty, ng-pristine, Value is valid - ng-valid, ng-invalid, sync validator, async validator, custom validator, custom async validator, ngModel vs ngModelOptions, 

Signals - 

'''
✅ - okay need to read onece
❌ - need to understand
⭐ - asked in interview 
👉 - important may be
'''




# ✅👉 Angular Framework
'''Angular is a TypeScript-based open-source front-end platform that makes it easy to build web, mobile and desktop applications. It is developed and maintained by Google and provides features like declarative templates, dependency injection, end to end tooling which ease application development etc.'''
# ✅ AngularJS vs Angular
# ✅ TypeScript
# ✅ What are the key components of Angular - Components, Modules, Templates, Services, Directives
# ✅👉  What are directives - 
'''classes that add behaviour to an existing DOM element or an existing component instance. types - Components, Structural Directives, and Attribute Directives'''
# ✅ components
# ✅ Component vs Directive
# ✅ template 
# ✅ template property - HTML view is defined inline
# ✅ templateUrl property - HTML view is defined in a separate file
# ✅ module
'''module is a set of angular basic building blocks like components, directives, services etc. An application is divided into logical pieces and each piece of code is called as "module" which perform a single task.
- @NgModule - used to define a module
- imports - used to import other dependent modules. 
- BrowserModule - required by default for any web based angular application.
- declarations - used to define components in the respective module.
- bootstrap -  tells Angular which Component to bootstrap in the application.
- providers -  used to configure a set of injectable objects that are available in the injector of this module.
- entryComponents -  set of components dynamically loaded into the view. '''
# ❌👉lifecycle hooks - 
'''Angular application goes through an entire set of processes or has a lifecycle right from its initiation to the end of the application.
- ngOnChanges: When the value of a data bound property changes, then this method is called.
- ngOnInit: Called once after the first ngOnChanges(). Used for initialization.
- ngDoCheck: Called during every change detection run. Used for custom change detection.
- ngAfterContentInit: This is called in response after Angular projects external content like ng-content into the component's view.
- ngAfterContentChecked: This is called in response after Angular checks the content projected into the component.
- ngAfterViewInit: This is called in response after Angular initializes the component's views and child views.
- ngAfterViewChecked: This is called in response after Angular checks the component's views and child views.
- afterRender() - Runs after each render cycle of the component's view.
- afterNextRender() - Runs only after the next render and then unsubscribes.
- ngOnDestroy: This is the cleanup phase just before Angular destroys the directive/component.
'''
# ✅ data binding
'''allows to define communication between a component and the DOM
From the Component to the DOM: interpolation {{ value }}, property binding  [property]=”value”
From the DOM to the Component: event binding,  (event)=”function”
Two-way binding: [(ngModel)]=”value”'''
# ✅ What is metadata 
'''used to decorate a class so that it can configure the expected behavior of the class.
- Class decorators, e.g. @Component and @NgModule
- Property decorators Used for properties inside classes, e.g. @Input and @Output
- Method decorators Used for methods inside classes, e.g. @HostListener
- Parameter decorators Used for parameters inside class constructors, e.g. @Inject, @Optiona'''
# ✅ What is Angular CLI
'''command line interface to scaffold and build angular apps using nodejs style (commonJs) modules.'''
# ❌ constructor and ngOnInit
'''Constructor is a special method that is called when an instance of the class is created. It is used for initializing class members and dependencies. ngOnInit is a lifecycle hook that is called after the component's constructor and after Angular has initialized all data-bound properties and depencies.'''
# ✅ What is a service
'''service is used when a common functionality needs to be provided to various modules. Services allow for greater separation of concerns for your application and better modularity by allowing you to extract common functionality out of components'''
# ✅⭐ What is dependency injection in Angular
'''Dependency Injection (DI) is a design pattern allowing a class to receive its dependencies from an external source rather than creating them itself. In Angular, DI is used to provide instances of services to components and other services.'''
# ❌👉🤔 How is Dependency Hierarchy formed
# ✅ Module injector -
'''Module injector is created for each module and it is used to provide services to the components declared in that module. It is created when the module is loaded and destroyed when the module is unloaded.'''
# ✅ Platform Module
'''During application bootstrapping angular creates a few more injectors, above the root injector goes the platform injector, this one is created by the platform browser dynamic function inside the main.ts file, and it provides some platform-specific features like DomSanitizer.'''
# ✅ NullInjector 
''' responsibility of this injector is to throw the error if something tries to find dependencies there, unless you've used @Optional() because ultimately, everything ends at the NullInjector() and it returns an error or, in the case of @Optional(), null.'''
# ✅ ElementInjector
'''Angular creates ElementInjector hierarchies implicitly for each DOM element. ElementInjector injector is being created for any tag that matches the angular component, or any tag on which directive is applied, and you can configure it in component and directive annotations inside the provider's property, thus, it creates its own hierarchy likewise the upper one.'''
# ✅ purpose of async pipe
''' AsyncPipe subscribes to an observable or promise and returns the latest value it has emitted. '''
# ✅ What is the option to choose between inline and external template file -  depends on requirement
# ✅ purpose of *ngFor directive - used to display each item in the list
# ✅ purpose of ngIf directive - inserts or removes an element based on a truthy/falsy condition.
# ✅ What happens if you use script tag inside template 
'''Angular recognizes the value as unsafe and automatically sanitizes it, which removes the script tag but keeps safe content such as the text content of the script tag.'''
# ✅ interpolation
'''way to bind data from the component to the template by using double curly braces {{ }}. It allows you to display dynamic values in the template.'''
# template expressions
'''A template expression produces a value similar to any Javascript expression. Angular executes the expression and assigns it to a property of a binding target; the target might be an HTML element, a component, or a directive. '''
# What are template statements
'''template statement responds to an event raised by a binding target such as an element, component, or directive. The template statements appear in quotes to the right of the = symbol like (event)="statement"'''
# How do you categorize data binding types
'''
From the Component to the DOM: interpolation {{ value }}, property binding  [property]=”value”, attribute binding [attr.attributeName]="value", class binding [class.className]="value", style binding [style.styleName]="value"
From the DOM to the Component: event binding,  (event)=”function”, on-target="function"
Two-way binding: [(ngModel)]=”value”'''
# What are pipes -  
'''functions that use template expressions to accept data as input and transform it into a desired output. {{ birthday | date }}'''
# What is a parameterized pipe
'''parameterized pipe can be created by declaring the pipe name with a colon ( : ) and then the parameter value. If the pipe accepts multiple parameters, separate the values with colons, {{ birthday | date:'dd/MM/yyyy'}}'''
# How do you chain pipes - {{  birthday | date:'fullDate' | uppercase}}
# What is a custom pipe
'''A custom pipe is a user-defined pipe that allows you to create your own transformation logic for data. You can create a custom pipe by implementing the PipeTransform interface and using the @Pipe decorator.'''
# @Pipe({name: 'myCustomPipe'})
# PipeTransform interface
'''interface PipeTransform {
  transform(value: any, ...args: any[]): any
}''' 
# Give an example of custom pipe
# What is the difference between pure and impure pipe
'''Pure pipes are only executed when the input data changes, while impure pipes are executed on every change detection cycle. Pure pipes are more efficient as they do not require constant re-evaluation.'''
# What is a bootstrapping module
'''The bootstrapping module is the root module of an Angular application that is responsible for launching the application. It is typically defined in the main.ts file and uses the platformBrowserDynamic().bootstrapModule() method to bootstrap the root module.'''
# What are observables
'''Observables are a way to handle asynchronous data streams in Angular. They allow you to subscribe to data changes and react to them in real-time. Observables are part of the RxJS library and provide powerful operators for transforming, filtering, and combining data streams.'''
# What is HttpClient and its benefits
'''HttpClient is a built-in Angular service that provides a simplified API for making HTTP requests. It is part of the @angular/common/http package and offers features like request and response interception, automatic JSON parsing, and support for typed responses. Benefits include better error handling, easier testing, and improved performance compared to the older Http service.'''
# Explain on how to use HttpClient with an example
# How can you read full response
''' use observe option from HttpClient
getUserResponse(): Observable<HttpResponse<User>> {
  return this.http.get<User>(
    this.userUrl, { observe: 'response' });
}
'''
# How do you perform Error handling - need to handle in the component by passing error object as a second callback to subscribe() method.
# What is RxJS
'''RxJS (Reactive Extensions for JavaScript) is a library for composing asynchronous and event-based programs using observable sequences. It provides a powerful set of operators for working with asynchronous data streams, making it easier to handle complex data flows in Angular applications.'''
# What is subscribing
'''Subscribing is the process of registering an observer to an observable. When you subscribe to an observable, you provide a callback function that will be executed whenever the observable emits a new value. This allows you to react to changes in the data stream and perform actions based on those changes.'''
# What is an observable
'''An observable is a data structure that represents a stream of values over time. It can emit multiple values, complete, or error out. Observables are lazy, meaning they do not execute until there is a subscription. They are used to handle asynchronous data streams in Angular applications.'''
# What is an observer
'''An observer is an object that defines how to handle the values emitted by an observable. It typically has three methods: next() for handling emitted values, error() for handling errors, and complete() for handling completion of the observable. When you subscribe to an observable, you provide an observer to receive notifications about the data stream.'''
# ❌ What is the difference between promise and observable
'''
Promises are used for single asynchronous operations and can only emit a single value, while observables can emit multiple values over time and support cancellation. Observables are lazy, meaning they do not execute until there is a subscription, while promises execute immediately upon creation. Observables also provide powerful operators for transforming and combining data streams, making them more flexible for complex data flows.'''
# What is multicasting - 
'''Multicasting is a technique in RxJS that allows multiple observers to share a single observable execution. It enables the observable to emit values to multiple subscribers without creating separate instances for each subscriber. This is achieved using operators like share(), publish(), or multicast(). Multicasting can improve performance and reduce resource consumption in scenarios where multiple subscribers need to listen to the same data stream.'''
# How do you perform error handling in observables
'''const myObserver = {
  next: x => console.log('Observer got a next value: ' + x),
  error: err => console.error('Observer got an error: ' + err),
  complete: () => console.log('Observer got a complete notification'),
};'''
# What is the shorthand notation for subscribe method
'''myObservable.subscribe(
  x => console.log('Observer got a next value: ' + x),
  err => console.error('Observer got an error: ' + err),
  () => console.log('Observer got a complete notification')
);'''
# What are the utility functions provided by RxJS
'''
- Converting existing code for async operations into observables
- Iterating through the values in a stream
- Mapping values to different types
- Filtering streams
- Composing multiple streams'''
# What are observable creation functions - from(fetch('/api/endpoint'));, ajax('/api/data');, interval(1000);, fromEvent(el, 'mousemove');
# What will happen if you do not supply handler for the observer - observer just ignores notifications
# 👉 What are Angular elements
'''Angular elements are Angular components packaged as custom elements (a web standard for defining new HTML elements in a framework-agnostic way). Angular Elements host an Angular component, providing a bridge between the data and the logic defined in the component and the standard DOM APIs, thus, providing a way to use Angular components in non-Angular environments.'''
# What is the browser support of Angular Elements
# 👉 What are custom elements
'''Custom elements (or Web Components) are a Web Platform feature which extends HTML by allowing you to define a tag whose content is created and controlled by JavaScript code. The browser maintains a CustomElementRegistry of defined custom elements, which maps an instantiable JavaScript class to an HTML tag.'''
# Do I need to bootstrap custom elements - 
'''No, custom elements bootstrap (or start) automatically when they are added to the DOM, and are automatically destroyed when removed from the DOM.'''
# ❌🤔Explain how custom elements works internally
# ❌🤔How to transfer components to custom elements
# ❌🤔What are the mapping rules between Angular component and custom element
# ❌🤔How do you define typings for custom elements
# ❌ What are dynamic components - 
'''Dynamic components are components that are inserted into the DOM at runtime, rather than being defined statically in the template.'''
# ✅ What are the various kinds of directives - structural, attribute, and component directives.
# ✅ How do you create directives using CLI - ng generate directive my-directive
# ❌ Give an example for attribute directives
# ✅ What is Angular Router
'''Angular Router is a mechanism that allows you to define navigation paths in your Angular application. It enables you to create single-page applications (SPAs) by managing the navigation between different views or components without reloading the entire page.'''
# ✅ What is the purpose of base href tag
'''The base href tag is used to specify the base URL for all relative URLs in the application. It helps the Angular Router to resolve the correct paths for navigation and resource loading. It is typically defined in the index.html file as <base href="/">.'''
# ✅ What are the router imports
'''@angular/router provides the necessary modules and services for routing in Angular applications. The main imports include RouterModule, Routes, and RouterOutlet. RouterModule is used to configure the router, Routes is an array of route definitions, and RouterOutlet is a directive that acts as a placeholder for the routed components.'''
# ✅ What is router-outlet
'''RouterOutlet is a directive that acts as a placeholder in the template where the routed component will be displayed. It is used to render the component associated with the current route. You can have multiple RouterOutlet directives in your application to support nested routing.'''
# ✅ What are router links
'''Router links are directives that allow you to navigate to different routes in your Angular application. They are typically used in anchor tags (<a>) or button elements to create clickable links that trigger navigation. The routerLink directive is used to bind the route path to the element, e.g., <a [routerLink]="['/path']">Link</a>.'''
# ✅ What are active router links
'''RouterLinkActive is a directive that toggles css classes for active RouterLink bindings based on the current RouterState. i.e, The Router will add CSS classes when this link is active and remove when the link is inactive. The routerLinkActive directive is used for this purpose, e.g., <a [routerLink]="['/path']" routerLinkActive="active">Link</a>.'''
# ✅ What is router state
'''RouterState is an object that represents the current state of the router, including the active route, parameters, query parameters, and data associated with the route. It provides information about the current navigation and allows you to access route-specific data. You can access the RouterState using the ActivatedRoute service or by injecting the Router service.'''
# ✅ What are router events
'''Router events are events emitted by the Angular Router during navigation. They provide information about the navigation process, such as when a route is activated, deactivated, or when navigation starts or ends. You can subscribe to router events using the Router service's events property, e.g., this.router.events.subscribe(event => { ... }).
- NavigationStart,
- RouteConfigLoadStart,
- RouteConfigLoadEnd,
- RoutesRecognized,
- GuardsCheckStart,
- ChildActivationStart,
- ActivationStart,
- GuardsCheckEnd,
- ResolveStart,
- ResolveEnd,
- ActivationEnd
- ChildActivationEnd
- NavigationEnd,
- NavigationCancel,
- NavigationError
- Scroll
'''
# ✅ What is activated route
'''ActivatedRoute is a service that provides access to the information about the currently active route. It contains properties such as params, queryParams, data, and snapshot, which allow you to access route parameters, query parameters, and data associated with the route. You can inject ActivatedRoute into your component or service to access this information.'''
# ✅ How do you define routes
'''Routes are defined as an array of route objects, where each object represents a route configuration. Each route object can have properties such as path, component, redirectTo, children, and data. The path property defines the URL path for the route, and the component property specifies the component to be rendered for that route. You can define routes in the AppRoutingModule or any feature module's routing module.'''
# ✅ What is the purpose of Wildcard route
'''Wildcard route is a special route that matches any URL that does not match any of the defined routes. It is typically used to handle 404 Not Found scenarios or to redirect users to a specific page when they navigate to an undefined route. You can define a wildcard route using the path '**' and redirect it to a specific component or page.'''
# ✅ Do I need a Routing Module always - No, the Routing Module is a design choice. 
# ✅ What is Angular Universal
'''@angular/platform-server package module allows you to render Angular applications on the server side. It enables server-side rendering (SSR) of Angular applications, improving performance, SEO, and initial load time. Angular Universal generates static HTML content on the server, which can be sent to the client for faster rendering.'''
# ✅ What are different types of compilation in Angular - Just-in-Time (JIT) and Ahead-of-Time (AOT).
# ✅ What is JIT
'''type of compilation that compiles your app in the browser at runtime. JIT compilation was the default until Angular 8, now default is AOT. in angular.json. By default, aot is set to true.'''
# ✅ What is AOT
'''type of compilation that compiles your app at build time, before it is served to the browser. AOT compilation converts your Angular HTML and TypeScript code into efficient JavaScript code during the build process, resulting in faster rendering and smaller bundle sizes.'''
# ✅ Why do we need compilation process
'''compiler converts both Angular HTML and TypeScript code converted into efficient JavaScript code during the build phase before browser runs it.'''
# ✅ What are the advantages with AOT
'''AOT compilation offers several advantages, including:
- Faster rendering: AOT compiles the templates and components at build time, resulting in faster rendering in the browser.
- Smaller bundle sizes: AOT generates optimized JavaScript code, reducing the size of the final bundle.
- Early error detection: AOT catches template errors during the build process, allowing developers to fix them before deployment.
- Improved security: AOT compiles templates into JavaScript code, making it harder for attackers to inject malicious code into the application.'''
# ✅ What are the ways to control AOT compilation - template compiler options in tsconfig.json, using the --aot flag with the Angular CLI commands, or by setting the aot property to true in angular.json.
# ❌ What are the restrictions of metadata
# ✅ What are the three phases of AOT - code analysis, code generation, and code validation.
# ✅ Can I use arrow functions in AOT - No, Arrow functions or lambda functions can’t be used to assign values to the decorator properties.
# ✅ What is the purpose of metadata json files
'''metadata.json files are generated during the AOT compilation process and contain information about the components, directives, pipes, and modules in your Angular application. They provide metadata about the structure and dependencies of the application, allowing the Angular compiler to optimize the code and perform static analysis.'''
# ✅ Can I use any javascript feature for expression syntax in AOT - No, the AOT collector understands a subset of (or limited) JavaScript features. If an expression uses unsupported syntax, the collector writes an error node to the .metadata.json file.
# ✅ What is folding
'''Folding is an optimization technique used in AOT compilation to reduce the size of the generated code. It involves removing unnecessary code and simplifying expressions by evaluating them at compile time.'''
# ❌ What are macros
'''The AOT compiler supports macros in the form of functions or static methods that return an expression in a single return expression.'''
# ✅ Give an example of few metadata errors - Expression form not supported, Reference to a local (non-exported) symbol, Function calls are not supported, Destructured variable or constant not supported
# ❌ What is metadata rewriting
'''process in which the compiler converts the expression initializing the fields such as useClass, useValue, useFactory, and data into an exported variable, which replaces the expression. Remember that the compiler does this rewriting during the emit of the .js file but not in definition files( .d.ts file).'''
# ✅ How do you provide configuration inheritance - tsconfig.json on angularCompilerOptions
# ✅ How do you specify angular template compiler options - tsconfig.json on angularCompilerOptions
# ✅ How do you enable binding expression validation - adding the compiler option fullTemplateTypeCheck in the "angularCompilerOptions" of the project's tsconfig.json
# ✅ What is the purpose of $any() type cast function - disable binding expression type checking using $any() type cast function, '{{ $any(user).contacts.email }}', '{{ $any(this).contacts.email }}'
# ✅ What is Non null type assertion (!) operator - suppress the Object is possibly 'undefined' error
# ❌ What is type narrowing
'''expression used in an ngIf directive is used to narrow type unions in the Angular template compiler similar to if expression in typescript.'''
# ✅ How do you describe various dependencies in angular application - angular packages, support packages, polyfill packages 


# What is zone
# What is the purpose of common module
# What is codelyzer
# What is angular animation
# What are the steps to use animation module
# What is State function
# What is Style function
# What is the purpose of animate function
# What is transition function
# How to inject the dynamic script in angular
# What is a service worker and its role in Angular
# What are the design goals of service workers
# What are the differences between AngularJS and Angular with respect to dependency injection
# What is Angular Ivy
# What are the features included in ivy preview
# Can I use AOT compilation with Ivy
# What is Angular Language Service
# How do you install angular language service in the project
# Is there any editor support for Angular Language Service
# Explain the features provided by Angular Language Service
# How do you add web workers in your application
# What are the limitations with web workers
# What is Angular CLI Builder
# What is a builder
# How do you invoke a builder
# How do you create app shell in Angular
# What are the case types in Angular
# What are the class decorators in Angular
# What are class field decorators
# What is declarable in Angular
# What are the restrictions on declarable classes
# What is a DI token
# What is Angular DSL
# What is an rxjs Subject
# What is Bazel tool
# What are the advantages of Bazel tool
# How do you use Bazel with Angular CLI
# How do you run Bazel directly
# What is platform in Angular
# What happens if I import the same module twice
# How do you select an element with in a component template
# How do you detect route change in Angular
# How do you pass headers for HTTP client
# What is the purpose of differential loading in CLI
# Does Angular support dynamic imports
# What is lazy loading
# What are workspace APIs
# How do you upgrade angular version
# What is Angular Material
# How do you upgrade location service of angularjs
# What is NgUpgrade
# How do you test Angular application using CLI
# How to use polyfills in Angular application
# What are the ways to trigger change detection in Angular
# What are the differences of various versions of Angular
# What are the security principles in angular
# What is the reason to deprecate Web Tracing Framework
# What is the reason to deprecate web worker packages
# How do you find angular CLI version
# What is the browser support for Angular
# What is schematic
# What is rule in Schematics
# What is Schematics CLI
# What are the best practices for security in angular
# What is Angular security model for preventing XSS attacks
# What is the role of template compiler for prevention of XSS attacks
# What are the various security contexts in Angular
# What is Sanitization Does Angular support it
# What is the purpose of innerHTML
# What is the difference between interpolated content and innerHTML
# How do you prevent automatic sanitization
# Is it safe to use direct DOM API methods in terms of security
# What is DOM sanitizer
# How do you support server side XSS protection in Angular application
# Does Angular prevent HTTP level vulnerabilities
# What are Http Interceptors
# What are the applications of HTTP interceptors
# Are multiple interceptors supported in Angular
# How can I use interceptor for an entire application
# How does Angular simplify Internationalization
# How do you manually register locale data
# What are the four phases of template translation
# What is the purpose of i18n attribute
# What is the purpose of custom id
# What happens if the custom id is not unique
# Can I translate text without creating an element
# How can I translate attribute
# List down the pluralization categories
# What is select ICU expression
# How do you report missing translations
# How do you provide build configuration for multiple locales
# What is an angular library
# What is AOT compiler
# How do you select an element in component template
# What is TestBed
# What is protractor
# What is collection
# How do you create schematics for libraries
# How do you use jquery in Angular
# What is the reason for No provider for HTTP exception
# What is router state
# How can I use SASS in angular project
# What is the purpose of hidden property
# What is the difference between ngIf and hidden property
# What is slice pipe
# What is index property in ngFor directive
# What is the purpose of ngFor trackBy
# What is the purpose of ngSwitch directive
# Is it possible to do aliasing for inputs and outputs
# What is safe navigation operator
# Is any special configuration required for Angular9
# What are type safe TestBed API changes in Angular9
# Is mandatory to pass static flag for ViewChild
# What are the list of template expression operators
# What is the precedence between pipe and ternary operators
# What is an entry component
# What is a bootstrapped component
# How do you manually bootstrap an application
# Is it necessary for bootstrapped component to be entry component
# What is a routed entry component
# Why is not necessary to use entryComponents array every time
# Do I still need to use entryComponents array in Angular9
# Is it all components generated in production build
# What is Angular compiler
# What is the role of ngModule metadata in compilation process
# How does angular finds components, directives and pipes
# Give few examples for NgModules
# What are feature modules
# What are the imported modules in CLI generated feature modules
# What are the differences between ngmodule and javascript module
# What are the possible errors with declarations
# What are the steps to use declaration elements
# What happens if browserModule used in feature module
# What are the types of feature modules
# What is a provider
# What is the recommendation for provider scope
# How do you restrict provider scope to a module
# How do you provide a singleton service
# What are the different ways to remove duplicate service registration
# How does forRoot method helpful to avoid duplicate router instances
# What is a shared module
# Can I share services using modules
# How do you get current direction for locales
# What is ngcc
# What classes should not be added to declarations
# What is ngzone
# What is NoopZone
# How do you create displayBlock components
# What are the possible data change scenarios for change detection
# What is a zone context
# What are the lifecycle hooks of a zone
# Which are the methods of NgZone used to control change detection
# How do you change the settings of zonejs
# How do you trigger an animation
# How do you configure injectors with providers at different levels
# Is it mandatory to use injectable on every service class
# What is an optional dependency
# What are the types of injector hierarchies
# What are reactive forms
# What are dynamic forms
# What are template driven forms
# What are the differences between reactive forms and template driven forms
# What are the different ways to group form controls
# How do you update specific properties of a form model
# What is the purpose of FormBuilder
# How do you verify the model changes in forms
# What are the state CSS classes provided by ngModel
# How do you reset the form
# What are the types of validator functions
# Can you give an example of built-in validators
# How do you optimize the performance of async validators
# How to set ngFor and ngIf on the same element
# What is host property in css
# How do you get the current route
# What is Component Test Harnesses
# What is the benefit of Automatic Inlining of Fonts
# What is content projection
# What is ng-content and its purpose
# What is standalone component
# How to create a standalone component uing CLI command
# How to create a standalone component manually
# What is hydration 
# What are Angular Signals
# Explain Angular Signals with an example
# What are the Route Parameters Could you explain each of them




