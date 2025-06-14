# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.



### Explanation:

* Both boxes have fixed width (200px).
* The first box measures width using `useEffect` (runs  **after paint** ).
* The second box measures width using `useLayoutEffect` (runs  **before paint** ).
* In this simple case, widths will be the same, but `useLayoutEffect` is better when you want to avoid flickering when reading and updating DOM.

---

### When to use?

* Use `useEffect` for most side effects.
* Use `useLayoutEffect` if you need to **measure or modify the DOM immediately after render** to prevent flicker.
