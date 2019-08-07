import { useState, useEffect } from 'react';

function useFetch(url, callback) {
  // Custom hook to fetch data from a given url
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUrl = () =>
      fetch(url)
        .then(res => res.json())
        .then(jsonData => setData(jsonData))
        .then(() => setLoading(false))
        .catch(err => console.log(err));
    fetchUrl();
  }, [url]);

  useEffect(() => {
    // Run callback when data arrives, if a callback is given
    if (callback && !loading) {
      callback(data);
    }
  }, [callback, data, loading]);

  return [data, loading];
}

export default useFetch;
