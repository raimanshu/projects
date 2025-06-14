- useState

  - const[state, setState] = useState(initialState)
  - setState(newState)
  - useEffect

    - useEffect(callbackFunction, [dependencies])
    - Runs on every render, useEffect(() => {...})
    - Runs only on first render, useEffect(() => {...}, [])
    - Runs any of the passed dependency changed, useEffect(() => {...}, [state1, state2])
    - Cleanup Function (return function)
  - useRef

    - const refContainer = useRef(initialValue)
    - refContainer.current
  - useContext

    - Prop Drilling
    - React.createContext()

    -<contextName.Provider>...</contextName.Provider>

    - useContext()
  - useReducer

    - const[state, dispatchFunction] = useReducer(reducerFunction, initialState)
    - Dispatch Function (dispatch({actionType, payload}))
    - Reducer Function (handle the logic related to state, takes state and {actionType, payload} as parameters)

      - Reducer
      - Action
      - Dispatch
      - Store
    - useReducer() vs useState()
  - useLayoutEffect

    - useLayoutEffect(() => {...}, [])
    - useLayoutEffect() vs useEffect()
  - useMemo

    - const variable = useMemo(() => {return variable}, [state1, state2])
    - useMemo() vs useState()
  - useCallback

    - const variable = useCallback(() => {return `<Component />`}, [state1, state2])
    - useCallback() vs useMemo()
  - useTransition
  - useId
  - CustomHook [ useFetch ]

    import { useState, useEffect } from 'react';

    function useWindowWidth() {
      const [width, setWidth] = useState(window.innerWidth);

      useEffect(() => {
        const handleResize = () => setWidth(window.innerWidth);

        window.addEventListener('resize', handleResize);

        // Cleanup on unmount
        return () => window.removeEventListener('resize', handleResize);
      }, []);

      return width;
    }

    export default useWindowWidth;
