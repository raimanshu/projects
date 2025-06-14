# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.




### folder structure 

src/
├── i18n/
│   ├── index.js          # i18n initialization
│   ├── locales/
│   │   ├── en.json
│   │   ├── fr.json
│   │   └── es.json
├── components/
│   └── LanguageSwitcher.jsx
├── utils/
│   └── localization.js  # date and currency format helpers
├── App.jsx
└── index.js



### packages

npm install react-i18next i18next date-fns
