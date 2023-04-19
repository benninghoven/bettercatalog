import { useEffect, useState } from 'react'

const useFetchPrereqs = (course_dept_code, course_num, course_letter) => {
    const [prereqs, setPrereqs] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        // let controller = new AbortController();

        const fetchPrereqs = async () => {
            try {
                setLoading(true);
                let query_param = "?" +
                "dept_code=" + course_dept_code + '&' +
                "course_num=" + course_num + '&' +
                "course_letter=" + course_letter
                const response = await fetch(process.env.REACT_APP_API_URL_PREREQS + query_param, {timeout: 10000});
                const data = await response.json();
                setPrereqs(data);
                // controller = null;
            } catch(err) {
                if (err.code === 20) return;
                if (err instanceof TypeError) setError({message: err.message, type: "type error"})
                setError({message: err.message, type: "not specified"});
            } finally {
                setLoading(false);
            }

        }
        fetchPrereqs();

        // clean up
        return () => {
            // controller?.abort();
        }
    }, [])


  return [prereqs, loading, error]
}

export default useFetchPrereqs