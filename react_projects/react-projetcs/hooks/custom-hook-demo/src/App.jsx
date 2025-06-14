import React from 'react';
import useFetch from './hooks/useFetch';

const App = () => {
  const { data, loading, error } = useFetch('https://jsonplaceholder.typicode.com/posts/1');

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: 20 }}>
      <h1>{data.title}</h1>
      <p>{data.body}</p>
    </div>
  );
};

export default App;
