import {useState, useEffect} from 'react'

function useFetchFromDB() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        let controller = new AbortController();

        const fetchData = async () => {
            try {
                setLoading(true);
                // connect controller with fetch request
                const response = await fetch('http://127.0.0.1:5000/fetchall-courses', {mode: "cors", signal: controller.signal});
                const response_json = await response.json();
                setData(response_json);
                controller = null;
            } catch(err) {
                console.log(err)
                setError(err);
            } finally {
                setLoading(false);
            }
        }
        fetchData();

        // clean up
        return () => {
            controller?.abort();
        }

    // run effect once and clean up oce on mount
    }, []);

    return [data, loading, error]
}

export default useFetchFromDB