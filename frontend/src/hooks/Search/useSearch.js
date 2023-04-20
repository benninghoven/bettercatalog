import {useState, useEffect} from 'react'

function useSearch( courses ) {
    const [searchResult, setSearchResult] = useState(null);

    useEffect(() => {
      let controller = new AbortController();

      // clean up
      return () => {
          controller?.abort();
      }

    // run effect once and clean up once on mount
    }, []);

    return searchResult
}

export default useSearch
