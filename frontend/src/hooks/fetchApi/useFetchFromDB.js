import {useState, useEffect} from 'react'

function useFetchFromDB() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                const response = await fetch('http://127.0.0.1:5000/fetchall-courses');
                const response_json = await response.json();
                setData(response_json);
            } catch(err) {
                console.log('error: ' + err)
                setError(err);
            } finally {
                setLoading(false);
            }
        }

        fetchData();
    }, []);

    return [data, loading, error]
}

export default useFetchFromDB