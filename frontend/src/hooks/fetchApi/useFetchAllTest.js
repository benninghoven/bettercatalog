import {useState, useEffect} from 'react'

function useFetchAllTest() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        let controller = new AbortController();

        const fetchData = async () => {
            try {
                setLoading(true);
                // connect controller with fetch request
                const response = await fetch('http://127.0.0.1:5000/fetchall-test', {mode: "cors", signal: controller.signal});
                const response_json = await response.json();
                setData(response_json);
                controller = null;
            } catch(err) {
                console.log(err)
                // ignore error code 20
                if (err.code === 20) return;
                if (err instanceof TypeError) setError({message: err.message, type: "type error"})
                setError({message: err.message, type: "not specified"});
            } finally {
                setLoading(false);
            }
        }
        fetchData();

        // clean up
        return () => {
            controller?.abort();
        }

    // run effect once and clean up once on mount
    }, []);

    return [data, loading, error]
}

export default useFetchAllTest