

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
''' an execution context that persists across async tasks. Angular relies on zone.js to run Angular's change detection processes when native JavaScript operations raise events'''
# What is the purpose of common module
'''commonly-needed services, pipes, and directives provided by @angular/common module.'''
# What is codelyzer
'''a set of tslint rules for static code analysis of Angular TypeScript projects.'''

# What is angular animation
'''Angular animations enable you to use CSS transitions, animations, and styles to make your application more dynamic and engaging. @angular/animations '''
# What are the steps to use animation module - Enabling the animations module:, Importing animation functions into component files, Adding the animation metadata property
# What is State function
''' state() function is used to define different states to call at the end of each transition. This function takes two arguments: a unique name like open or closed and a style() function.
state('open', style({
  height: '300px',
  opacity: 0.5,
  backgroundColor: 'blue'
})),'''
# What is Style function
'''style() function is used to define the styles for the different states. This function takes an object as an argument that contains the styles for the different states.'''
# What is the purpose of animate function
'''way to implement sophisticated and compelling animations for your Angular single page web application
animations: [
    trigger('changeState', [
    state('state1', style({
        backgroundColor: 'green',
        transform: 'scale(1)'
    })),
    state('state2', style({
        backgroundColor: 'red',
        transform: 'scale(1.5)'
    })),
    transition('*=>state1', animate('300ms')),
    transition('*=>state2', animate('2000ms'))
    ])
]'''
# What is transition function
'''transition function is used to specify the changes that occur between one state and another over a period of time. It accepts two arguments: the first argument accepts an expression that defines the direction between two transition states, and the second argument accepts an animate() function.'''
# How to inject the dynamic script in angular - 
'''Using DomSanitizer, 
export class App {
       constructor(protected sanitizer: DomSanitizer) {}
       htmlSnippet: string = this.sanitizer.bypassSecurityTrustScript("<script>safeCode()</script>");
   }'''
# What is a service worker and its role in Angular
'''A service worker is a script that your browser runs in the background, separate from a web page, opening the door to features that don't need a web page or user interaction like caching resources, syncing resources, push notifications, and background sync.'''
# What are the design goals of service workers
'''
- It caches an application just like installing a native application
- A running application continues to run with the same version of all files without any incompatible files
- When you refresh the application, it loads the latest fully cached version
- When changes are published then it immediately updates in the background
- Service workers saves the bandwidth by downloading the resources only when they changed.'''
# What are the differences between AngularJS and Angular with respect to dependency injection
'''
- Token: AngularJs dependency injection tokens are always strings but in angular tokens can have different types. They are often classes and sometimes can be strings.
- Quantity - In AngularJs there is exactly one injector even though it is a multi-module applications, where as in angular there is a tree hierarchy of injectors, with a root injector and an additional injector for each component.'''
# What is Angular Ivy
'''rendering engine for Angular, 
- ng new ivy-demo-app --enable-ivy
- tsconfig.app.json
{
  "compilerOptions": { ... },
  "angularCompilerOptions": {
    "enableIvy": true
  }
}'''
# What are the features included in ivy preview - Generated code that is easier to read and debug at runtime, Faster re-build time, Improved payload size, Improved template type checking
# Can I use AOT compilation with Ivy
'''
in angular.json
{
  "projects": {
    "my-project": {
      "architect": {
        "build": {
          "options": {
            ...
            "aot": true,
          }
        }
      }
    }
  }
}
'''
# What is Angular Language Service
'''way to get completions, errors, hints, and navigation inside your Angular templates whether they are external in an HTML file or embedded in annotations/decorators in a string. It has the ability to autodetect that you are opening an Angular file, reads your tsconfig.json file, finds all the templates you have in your application, and then provides all the language services.'''
# How do you install angular language service in the project
'''
- npm install --save-dev @angular/language-service
- "compilerOptions" section of your project's tsconfig.json
"plugins": [
    {"name": "@angular/language-service"}
]'''
# What are the benefits of Angular Language Service - 
# Is there any editor support for Angular Language Service - available for Visual Studio Code and WebStorm IDE
# Explain the features provided by Angular Language Service - Autocompletion, Error checking, Navigation
# How do you add web workers in your application - ng generate web-worker <name>
# What are the limitations with web workers
'''
- Some environments or platforms(like @angular/platform-server) used in Server-side Rendering, don't support Web Workers. In this case you need to provide a fallback mechanism to perform the computations to work in this environments.
- Running Angular in web worker using @angular/platform-webworker is not yet supported in Angular CLI.'''
# What is Angular CLI Builder
'''Angular CLI Builder is a library that allows you to create custom builders for Angular CLI. It provides a set of tools and utilities to create custom builders that can be used with Angular CLI.'''
# ❌ What is a builder
'''A builder is a TypeScript class that implements the Builder interface. Builders are used to perform a specific task, such as building a project, running tests, or deploying an application.'''
# How do you invoke a builder - ng run is used to invoke a builder with a specific target configuration.
# How do you create app shell in Angular
'''way to render a portion of your application via a route at build time. This is useful to first paint of your application that appears quickly because the browser can render static HTML and CSS without the need to initialize JavaScript. ng generate appShell [options] '''
# What are the case types in Angular - camelCase, UpperCamelCase, dash-case (or "kebab-case"), UPPER_UNDERSCORE_CASE
# What are the class decorators in Angular
'''decorator that appears immediately before a class definition, which declares the class to be of the given type, and provides metadata suitable to the type. like @Component(), @Directive(), @Pipe(), @Injectable(), @NgModule()'''
# What are class field decorators
'''decorator that appears immediately before a class field declaration, which declares the field to be of the given type, and provides metadata suitable to the type. like @Input(), @Output(), @ViewChild(), @ViewChildren(), @ContentChild(), @ContentChildren()'''
# What is declarable in Angular
'''class type that you can add to the declarations list of an NgModule. The class types such as components, directives, and pipes comes can be declared in the module.'''
# What are the restrictions on declarable classes - A class that's already declared in another NgModule, Ngmodule classes, Service classes, Helper classes
# ❌ What is a DI token
'''a value that can be used to identify or select a service. A DI token can be a string, a token class, or a token factory function.
const BASE_URL = new InjectionToken<string>('BaseUrl');
const injector =
   Injector.create({providers: [{provide: BASE_URL, useValue: 'http://some-domain.com'}]});
const url = injector.get(BASE_URL);'''
# What is Angular DSL
'''(DSL) is a computer language specialized to a particular application domain. Angular has its own Domain Specific Language (DSL) which allows us to write Angular specific html-like syntax on top of normal html. It has its own compiler that compiles this syntax to html that the browser can understand. This DSL is defined in NgModules such as animations, forms, and routing and navigation.'''
# What is an rxjs Subject
'''special type of Observable that allows values to be multicasted to many Observers. While plain Observables are unicast (each subscribed Observer owns an independent execution of the Observable), Subjects are multicast.'''
# What is Bazel tool
'''a build and test tool from Google that builds code quickly and reliably.'''
# What are the advantages of Bazel tool - creates the possibility of building your back-ends and front-ends with the same tool, incremental build and tests, creates the possibility to have remote builds and cache on a build farm.
# How do you use Bazel with Angular CLI - npm install -g @angular/bazel
# How do you run Bazel directly - @bazel/bazel npm package
# What is platform in Angular
'''A platform is the context in which an Angular application runs. The most common platform for Angular applications is a web browser, but it can also be an operating system for a mobile device, or a web server. The runtime-platform is provided by the @angular/platform-* packages and these packages allow applications that make use of @angular/core and @angular/common to execute in different environments. '''
# What happens if I import the same module twice -  angular evaluates it only once
# How do you select an element with in a component template
'''
<input #uname>
------
@ViewChild('uname') input;

ngAfterViewInit() {
  console.log(this.input.nativeElement.value);
}'''
# How do you detect route change in Angular - this.router.events.subscribe((event: Event) => {})
# How do you pass headers for HTTP client
'''
constructor(private _http: HttpClient) {}
this._http.get('someUrl',{
   headers: {'header1':'value1','header2':'value2'}
});'''
# What is the purpose of differential loading in CLI
'''Angular CLI provides a way to build your application with different sets of application code based on the browser that the user is using. This is called differential loading.'''
# Does Angular support dynamic imports - {path: ‘user’, loadChildren: () => import(‘./users/user.module’).then(m => m.UserModule)};
# What is lazy loading
'''download the web pages in chunks instead of downloading everything in a big bundle. It is used for lazy loading by asynchronously loading the feature module for routing whenever required using the property loadChildren.'''
# What are workspace APIs
'''Workspace APIs to make it easier for developers to read and modify the angular.json file instead of manually modifying it. Currently, the only supported storage3 format is the JSON-based format used by the Angular CLI.'''
# How do you upgrade angular version - ng update @angular/cli @angular/core
# What is Angular Material
'''Angular Material is a UI component library that implements Google's Material Design specification for Angular. It provides a set of reusable, well-tested, and accessible UI components based on Google's Material Design system. npm install --save @angular/material @angular/cdk @angular/animations'''
# How do you upgrade location service of angularjs
'''
import { LocationUpgradeModule } from '@angular/common/upgrade';
@NgModule({
  imports: [
    // Other NgModule imports...
    LocationUpgradeModule.config()
  ]
})
export class AppModule {}'''
# What is NgUpgrade
'''library put together by the Angular team, which you can use in your applications to mix and match AngularJS and Angular components and bridge the AngularJS and Angular dependency injection systems.'''
# How do you test Angular application using CLI
'''Angular CLI downloads and install everything needed with the Jasmine Test framework. You just need to run ng test to see the test results. By default this command builds the app in watch mode, and launches the Karma test runner. '''
# How to use polyfills in Angular application
''' When you create a new project with the ng new command, a src/polyfills.ts configuration file is created as part of your project folder. This file includes the mandatory and many of the optional polyfills as JavaScript import statements. Let's categorize the polyfills,
- Mandatory polyfills: These are installed automatically when you create your project with ng new command and the respective import statements enabled in 'src/polyfills.ts' file.
- Optional polyfills: You need to install its npm package and then create import statement in 'src/polyfills.ts' file. For example, first you need to install below npm package for adding web animations (optional) polyfill. bash npm install --save web-animations-js  and create import statement in polyfill file. javascript import 'web-animations-js'; '''
# What are the ways to trigger change detection in Angular
'''
- ApplicationRef.tick(): Invoke this method to explicitly process change detection and its side-effects. It check the full component tree.
- NgZone.run(callback): It evaluate the callback function inside the Angular zone.
- ChangeDetectorRef.detectChanges(): It detects only the components and it's children.'''
# ❌ What are the differences of various versions of Angular
# What are the security principles in angular
'''
- avoid direct use of the DOM APIs.
- enable Content Security Policy (CSP) and configure your web server to return appropriate CSP HTTP headers.
- Use the offline template compiler.
- Use Server Side XSS protection.
- Use DOM Sanitizer.
- Preventing CSRF or XSRF attacks.'''
# What is the reason to deprecate Web Tracing Framework - for the purpose of performance testing. Since it is not well maintained and failed in majority of the applications, the support is deprecated in latest releases.
# What is the reason to deprecate web worker packages - Both @angular/platform-webworker and @angular/platform-webworker-dynamic are officially deprecated, the Angular team realized it's not good practice to run the Angular application on Web worker
# How do you find angular CLI version - ng --version
# What is the browser support for Angular

# What is schematic
'''It's a scaffolding library that defines how to generate or transform a programming project by creating, modifying, refactoring, or moving files and code. It defines rules that operate on a virtual file system called a tree.'''
# What is rule in Schematics
'''A rule is a function that takes a tree and returns a tree. It is a pure function that takes a tree and returns a tree. It is a pure function that takes a tree and returns a tree.'''
# What is Schematics CLI
'''The schematics CLI is a command-line interface for working with schematics. It provides a set of commands for creating, running, and testing schematics. npm install -g @angular-devkit/schematics-cli'''
# What are the best practices for security in angular - Use the latest Angular library releases, Don't modify your copy of Angular, Avoid Angular APIs marked in the documentation as “Security Risk.”
# What is Angular security model for preventing XSS attacks - 
'''Angular treats all values as untrusted by default. i.e, Angular sanitizes and escapes untrusted values When a value is inserted into the DOM from a template, via property, attribute, style, class binding, or interpolation.'''
# What is the role of template compiler for prevention of XSS attacks - it is recommended to use offline template compiler in production deployments without dynamically generating any template.
# What are the various security contexts in Angular - HTML, Style, URL, Resource URL
# What is Sanitization Does Angular support it- 
'''Sanitization is the inspection of an untrusted value, turning it into a value that's safe to insert into the DOM. '''
# What is the purpose of innerHTML - innerHtml is a property of HTML-Elements, which allows you to set it's html-content programmatically.
# What is the difference between interpolated content and innerHTML
'''Interpolated content is a value or strings with < > that is inserted into the DOM by Angular. InnerHTML is a property of HTML-Elements, which allows you to set it's html-content programmatically.'''
# How do you prevent automatic sanitization
'''
- Inject DomSanitizer
- Mark the trusted value by calling some of the below methods - bypassSecurityTrustHtml, bypassSecurityTrustScript, bypassSecurityTrustStyle, bypassSecurityTrustUrl, bypassSecurityTrustResourceUrl
Example:
constructor(private sanitizer: DomSanitizer) {
  this.dangerousUrl = 'javascript:alert("XSS attack")';
  this.trustedUrl = sanitizer.bypassSecurityTrustUrl(this.dangerousUrl);
'''
# Is it safe to use direct DOM API methods in terms of security - No, security issues
# What is DOM sanitizer 
'''used to help preventing Cross Site Scripting Security bugs (XSS) by sanitizing values to be safe to use in the different DOM contexts.'''
# How do you support server side XSS protection in Angular application - by using a templating language that automatically escapes values to prevent XSS vulnerabilities on the server
# Does Angular prevent HTTP level vulnerabilities
'''
- HttpClient supports a token mechanism used to prevent XSRF attacks
- HttpClient library recognizes the convention of prefixed JSON responses(which non-executable js code with ")]}',\n" characters) and automatically strips the string ")]}',\n" from all responses before further parsing'''
# What are Http Interceptors
'''part of @angular/common/http, which inspect and transform HTTP requests from your application to the server and vice-versa on HTTP responses. These interceptors can perform a variety of implicit tasks, from authentication to logging.'''
# What are the applications of HTTP interceptors - Authentication, Logging, Caching, Fake backend, URL transformation, Modifying headers
# Are multiple interceptors supported in Angular - Yes, define multiple interceptors in providers property  
# How can I use interceptor for an entire application
'''You can use same instance of HttpInterceptors for the entire app by importing the HttpClientModule only in your AppModule, and add the interceptors to the root application injector. '''


# How does Angular simplify Internationalization
'''
- Displaying dates, number, percentages, and currencies in a local format.
- Preparing text in component templates for translation.
- Handling plural forms of words.
- Handling alternative text.'''
# How do you manually register locale data
'''
import { registerLocaleData } from '@angular/common';
import localeDe from '@angular/common/locales/de';

registerLocaleData(localeDe, 'de');'''
# What are the four phases of template translation
'''
- Mark static text messages in your component templates for translation
- Create a translation file
- Edit the generated translation file
- Merge the completed translation file into the app'''
# What is the purpose of i18n attribute - marks translatable content. It is a custom attribute, recognized by Angular tools and compilers. The compiler removes it after translation.
# ❌ What is the purpose of custom id
'''
When you change the translatable text, the Angular extractor tool generates a new id for that translation unit. Because of this behavior, you must then update the translation file with the new id every time.'''
# What happens if the custom id is not unique
'''If you use the same id for two different text messages then only the first one is extracted. But its translation is used in place of both original text messages.'''
# Can I translate text without creating an element - <ng-container i18n>I'm not using any DOM element for translation</ng-container>
# How can I translate attribute - <img [src]="example" i18n-title title="Internationlization" />
# List down the pluralization categories - =0 (or any other number), zero, one, two, few, many, other
# What is select ICU expression
'''ICU expression is is similar to the plural expressions except that you choose among alternative translations based on a string value instead of a number. Here you define those string values.
Example:
<span i18n>The person is {residenceStatus, select, citizen {citizen} permanent resident {permanentResident} foreigner {foreigner}}</span>'''
# How do you report missing translations - By default, When translation is missing, it generates a warning message such as "Missing translation for message 'somekey'"
# How do you provide build configuration for multiple locales
'''
in angular.json file
"configurations": {
  "de": {
    "aot": true,
    "outputPath": "dist/my-project-de/",
    "baseHref": "/fr/",
    "i18nFile": "src/locale/messages.de.xlf",
    "i18nFormat": "xlf",
    "i18nLocale": "de",
    "i18nMissingTranslation": "error",
  }'''
# What is an angular library
'''Angular library is an Angular project that differs from an app in that it cannot run on its own. It must be imported and used in an app.'''
# What is AOT compiler
'''AOT compiler is part of a build process that produces a small, fast, ready-to-run application package, typically for production. It converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.'''
# How do you select an element in component template - via ElementRef by injecting it into your component's constructor
# What is TestBed
'''api for writing unit tests for Angular applications and it's libraries. Even though We still write our tests in Jasmine and run using Karma, this API provides an easier way to create components, handle injection, test asynchronous behaviour and interact with our application.'''
# What is protractor
'''end-to-end test framework for Angular and AngularJS applications. It runs tests against your application running in a real browser, interacting with it as a user would, npm install -g protractor'''
# What is collection - set of related schematics collected in an npm package
# How do you create schematics for libraries - Add schematics, Generate schematics, Update schematics
# How do you use jquery in Angular
'''
=    npm install --save jquery
- "scripts": [
   "node_modules/jquery/dist/jquery.min.js"
]
- declare var $: any;'''
# What is the reason for No provider for HTTP exception - missing HttpClientModule in your module
# What is router state -  interface which represents the state of the router as a tree of activated routes.
# How can I use SASS in angular project - ng new My_New_Project --style=sass
# What is the purpose of hidden property - used to show or hide the associated DOM element, based on an expression.
# What is the difference between ngIf and hidden property - *ngIf will remove the element from the DOM, while [hidden] actually plays with the CSS style by setting display:none
# What is slice pipe - create a new Array or String containing a subset (slice) of the elements. {{ value_expression | slice : start [ : end ] }}
# What is index property in ngFor directive - used to return the zero-based index of the item in each iteration.
# What is the purpose of ngFor trackBy
# What is the purpose of ngSwitch directive - displays one element from among several possible elements, based on a switch condition. It has been used along with NgSwitch, NgSwitchCase and NgSwitchDefault directives.
# Is it possible to do aliasing for inputs and outputs
'''
- Aliasing in metadata
inputs: ['input1: buyItem'],
outputs: ['outputEvent1: completedEvent']
- Aliasing with @Input()/@Output() decorator
@Input('buyItem') input1: string;
@Output('completedEvent') outputEvent1 = new EventEmitter<string>();
'''
# What is safe navigation operator
'''safe navigation operator(?)(or known as Elvis Operator) is used to guard against null and undefined values in property paths when you are not aware whether a path exists or not. i.e. It returns value of the object path if it exists, else it returns the null value.'''
# Is any special configuration required for Angular9 - "angularCompilerOptions": {    "enableIvy": true  }
# What are type safe TestBed API changes in Angular9
'''
TestBed.get(ChangeDetectorRef) // returns any. It is deprecated now.
TestBed.inject(ChangeDetectorRef) // returns ChangeDetectorRef'''
# Is mandatory to pass static flag for ViewChild
'''
@ViewChild(ChildDirective) child: ChildDirective; // Angular9 usage
@ViewChild(ChildDirective, { static: false }) child: ChildDirective; //Angular8 usage'''
# What are the list of template expression operators - Pipe operator, Safe navigation operator, Non-null assertion operator
# What is the precedence between pipe and ternary operators - pipe operator has a higher precedence than the ternary operator 
# What is an entry component
'''component that Angular loads imperatively(i.e, not referencing it in the template) by type. Due to this behavior, they can’t be found by the Angular compiler during compilation.'''
# What is a bootstrapped component
'''entry component that Angular loads into the DOM during the bootstrap process or application launch time. Generally, this bootstrapped or root component is named as AppComponent in your root module using bootstrap property'''
# How do you manually bootstrap an application
'''
class AppModule implements DoBootstrap {
  ngDoBootstrap(appRef: ApplicationRef) {
    appRef.bootstrap(AppComponent); // bootstrapped entry component need to be passed
  }
}'''
# Is it necessary for bootstrapped component to be entry component - Yes
# What is a routed entry component - The components referenced in router configuration are called as routed entry components. 
# Why is not necessary to use entryComponents array every time - Because angular adds components from both @NgModule.bootstrap and route definitions to entry components automatically.
# Do I still need to use entryComponents array in Angular9 - No
# Is it all components generated in production build - No, only the entry components and template components appears in production builds.
# What is Angular compiler
''' used to convert the application code into JavaScript code. It reads the template markup, combines it with the corresponding component class code, and emits component factories which creates JavaScript representation of the component along with elements of @Component metadata.'''
# What is the role of ngModule metadata in compilation process
''' used to tell the Angular compiler what components to be compiled for this module and how to link this module with other modules.'''
# How does angular finds components, directives and pipes
'''Angular compiler finds a component or directive in a template when it can match the selector of that component or directive in that template. Whereas it finds a pipe if the pipe's name appears within the pipe syntax of the template HTML.'''
# Give few examples for NgModules
'''
- Angular libraries such as FormsModule, HttpClientModule, and RouterModule are NgModules.
- Many third-party libraries such as Material Design, Ionic, and AngularFire2 are NgModules.'''
# What are feature modules
'''NgModules, which are used for the purpose of organizing code.'''
# What are the imported modules in CLI generated feature modules - NgModule, CommonModule
# What are the differences between ngmodule and javascript module
# | Angular NgModule                                                   | JavaScript Module                                  |
# |--------------------------------------------------------------------|----------------------------------------------------|
# | NgModule                                                           | JavaScript module                                  |
# | NgModule bounds declarable classes only                            | There is no restriction on classes                 |
# | List the module's classes in declarations array only               | Can define all member classes in one giant file    |
# | It only exports the declarable classes it owns or imports          | It can export any classes                          |
# | Extend the entire application with services via providers array    | Can't extend the application with services         |

# What are the possible errors with declarations - If you use a component without declaring it and If you try to declare the same class in more than one module
# What are the steps to use declaration elements - Create the element, Import it into the appropriate module., Declare it in the @NgModule declarations array.
# What happens if browserModule used in feature module - error telling you to use CommonModule
# What are the types of feature modules - Domain, Routed, Routing, Service, Widget
# What is a provider
'''an instruction to the Dependency Injection system on how to obtain a value for a dependency(aka services created)'''
# What is the recommendation for provider scope
'''You should always provide your service in the root injector unless there is a case where you want the service to be available only if you import a particular @NgModule.'''
# How do you restrict provider scope to a module - Using providedIn in service, Declare provider for the service in module
# How do you provide a singleton service - Set the providedIn property of the @Injectable() to "root", Include the service in root module or in a module that is only imported by root module. 
# What are the different ways to remove duplicate service registration
'''
- Use the providedIn syntax instead of registering the service in the module.
- Separate your services into their own module.
- Define forRoot() and forChild() methods in the module.'''
# How does forRoot method helpful to avoid duplicate router instances - If the RouterModule module didn’t have forRoot() static method then each feature module would instantiate a new Router instance, which leads to broken application due to duplicate instances. 
# What is a shared module - module in which you put commonly used directives, pipes, and components into one module that is shared(import it) throughout the application.
# Can I share services using modules - No, it is not recommended to share services by importing module.
# How do you get current direction for locales - getLocaleDirection can be used to get the current direction in your app. This method is useful to support Right to Left locales for your Internationalization based applications.
# What is ngcc 
''' ngcc(Angular Compatibility Compiler) is a tool which upgrades node_module compiled with non-ivy ngc into ivy compliant format. The postinstall script from package.json will make sure your node_modules will be compatible with the Ivy renderer'''
# What classes should not be added to declarations
'''
- A class which is already declared in any another module.
- Directives imported from another module.
- Module classes.
- Service classes.
- Non-Angular classes and objects, such as strings, numbers, functions, entity models, configurations, business logic, and helper classes.'''
# What is ngzone
''' which creates a zone named angular to automatically trigger change detection when the following conditions are satisfied.
- When a sync or async function is executed.
- When there is no microTask scheduled.'''
# ❌ What is NoopZone
'''You can also use Angular without Zone but the change detection need to be implemented on your own and noop zone need to be configured in bootstrap process. '''
# How do you create displayBlock components
'''By default, Angular CLI creates components in an inline displayed mode(i.e, display:inline). But it is possible to create components with display: block style using displayBlock option,
ng generate component my-component --displayBlock'''
# What are the possible data update scenarios for change detection - Component initialization, Event listener, HTTP Data Request, Macro tasks setTimeout() or setInterval(), Micro tasks Promises, Async operations like Web sockets and Canvas
# What is a zone context
'''Execution Context is an abstract concept that holds information about the environment within the current code being executed. A zone provides an execution context that persists across asynchronous operations is called as zone context. '''
# What are the lifecycle hooks of a zone - onScheduleTask, onInvokeTask, onHasTask, onInvoke
# Which are the methods of NgZone used to control change detection
'''run() method that allows you to execute a function inside the angular zone. This function is used to execute third party APIs which are not handled by Zone and trigger change detection automatically at the correct time Whereas runOutsideAngular() method is used when you don't want to trigger change detection.'''
# How do you change the settings of zonejs
'''You can change the settings of zone by configuring them in a separate file and import it just after zonejs import.'''
# How do you trigger an animation - trigger() function for animation 
# How do you configure injectors with providers at different levels
'''
- In the @Injectable() decorator for the service itself
- In the @NgModule() decorator for an NgModule
- In the @Component() decorator for a component'''
#  ❌Is it mandatory to use injectable on every service class - No
# What is an optional dependency
'''optional dependency is a parameter decorator to be used on constructor parameters, which marks the parameter as being an optional dependency. Due to this, the DI framework provides null if the dependency is not found. '''
# What are the types of injector hierarchies - ModuleInjector hierarchy and ElementInjector` hierarchy
# What are reactive forms
'''model-driven approach for creating forms in a reactive style(form inputs changes over time). These are built around observable streams, where form inputs and values are provided as streams of input values.'''
# What are dynamic forms
'''pattern in which we build a form dynamically based on metadata that describes a business object model.'''
# What are template driven forms
'''model-driven forms where you write the logic, validations, controls etc, in the template part of the code using directives. They are suitable for simple scenarios and uses two-way binding with [(ngModel)] syntax.'''
# What are the differences between reactive forms and template driven forms
'''
Form model setup: In reactive, Created(FormControl instance) in component explicitly where in TDF Created by directives
Data updates: RF are async and TDF are sync
Form custom validation: RF Defined as Functions while in TDF Defined as Directives
Testing: RF No interaction with change detection cycle while in TDF Need knowledge of the change detection process
Mutability: RF are immutable while in TDF are mutable
Scalability: RF are more scalable than TDF'''
# What are the different ways to group form controls - FormGroup, FormArray, FormControl
# How do you update specific properties of a form model - patchValue() method to update specific properties defined in the form model.
# What is the purpose of FormBuilder
'''syntactic sugar for easily creating instances of a FormControl, FormGroup, or FormArray. This is helpful to reduce the amount of boilerplate needed to build complex reactive forms. It is available as an injectable helper class of the @angular/forms package.'''
# How do you verify the model changes in forms - add a getter property(let's say, diagnostic) inside component to return a JSON representation of the model during the development. 
# What are the state CSS classes provided by ngModel
'''
| Form Control State   | If True     | If False      |
|----------------------|-------------|----------------|
| Visited              | ng-touched  | ng-untouched   |
| Value has changed    | ng-dirty    | ng-pristine    |
| Value is valid       | ng-valid    | ng-invalid     |'''
# How do you reset the form - this.myform.reset();
# What are the types of validator functions
'''
- Sync validators: These are the synchronous functions which take a control instance and immediately return either a set of validation errors or null.
- Async validators: These are the asynchronous functions which take a control instance and return a Promise or Observable that later emits a set of validation errors or null.'''
# Can you give an example of built-in validators - required and minlength
# How do you optimize the performance of async validators
'''
TDF - <input [(ngModel)]="name" [ngModelOptions]="{updateOn: 'blur'}">
RF - name = new FormControl('', {updateOn: 'blur'});'''
# How to set ngFor and ngIf on the same element - either ng-container or ng-template
# What is host property in css
''':host pseudo-class selector is used to target styles in the element that hosts the component. Since the host element is in a parent component's template, you can't reach the host element from inside the component by other means. '''
# How do you get the current route - this.router.url
# ❌ What is Component Test Harnesses
'''component harness is a testing API around an Angular directive or component to make tests simpler by hiding implementation details from test suites. This can be shared between unit tests, integration tests, and end-to-end tests. The idea for component harnesses comes from the PageObject pattern commonly used for integration testing.'''
# What is the benefit of Automatic Inlining of Fonts
'''During compile time, Angular CLI will download and inline the fonts that your application is using. This performance update speed up the first contentful paint(FCP) and this feature is enabled by default in apps built with version 11.'''
# What is content projection -  pattern in which you insert, or project, the content you want to use inside another component.
# What is ng-content and its purpose - used to insert the content dynamically inside the component that helps to increase component reusability.
# What is standalone component
'''''A standalone component is a component that doesn't require a module to be imported. It is a standalone component if it has no dependencies on other components, directives, or pipes.'''
# How to create a standalone component uing CLI command - ng generate component component-name --standalone
# How to create a standalone component manually
'''
@Component({
  standalone: true,
  ...
})'''
# What is hydration 
''' process that restores the server side rendered application on the client. This includes things like reusing the server rendered DOM structures, persisting the application state, transferring application data that was retrieved already by the server, and other processes.'''
# What are Angular Signals
'''wrapper around a value that can notify interested consumers when that value changes. Signals can contain any value, from simple primitives to complex data structures.'''
# Explain Angular Signals with an example
# What are the Route Parameters Could you explain each of them
'''Route parameters are used to pass dynamic values in the URL of a route. They allow you to define variable segments in the route path, which can be accessed and used by components and services. Path parameters are represented by a colon (":") followed by the parameter name.
Path parameters - { path: 'users/:id', component: UserComponent }
Query parameters - { path: 'search', component: SearchComponent }
Optional parameters - { path: 'products/:id/:category?', component: ProductComponent }'''




