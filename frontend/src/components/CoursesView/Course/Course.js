import {useState} from 'react'

import CourseCss from "./Course.module.css"
import useFetchPrereqs from '../../../hooks/fetchApi/useFetchPrereqs';

const Course = ({courseData}) => {
  const [prereqs, setPrereqs] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [showDetails, setShowDetails] = useState(false);

  const fetchPrereqs = async () => {
    try {
        setLoading(true);
        let query_param = "?" +
        "dept_code=" + courseData.DEPTCODE + '&' +
        "course_num=" + courseData.COURSENUM + '&' +
        "course_letter=" + courseData.COURSELETTER
        const response = await fetch(process.env.REACT_APP_API_URL_PREREQS + query_param, {timeout: 10000});
        const data = await response.json();
        if (data == false) setPrereqs("")
        else setPrereqs(data);
        // controller = null;
    } catch(err) {
        if (err.code === 20) return;
        if (err instanceof TypeError) setError({message: err.message, type: "type error"})
        setError({message: err.message, type: "not specified"});
    } finally {
        setLoading(false);
    }
  }

  return (
    <>
      <div className={CourseCss.course}>
        <div className={CourseCss.course_name}>{courseData.DEPTCODE} {courseData.COURSENUM}{courseData.COURSELETTER} - {courseData.COURSENAME}</div>
        <button onClick={() => setShowDetails(!showDetails)}>show details</button>
        <button onClick={fetchPrereqs}>show prereqs</button>
        {showDetails &&
          <div className={CourseCss.course_details}>
            {courseData.COURSEDESCRIPTION}
          </div>
        }
        {prereqs &&
          <div>prereqs are loaded</div>
        }
      </div>
    
    </>
  )
}

export default Course