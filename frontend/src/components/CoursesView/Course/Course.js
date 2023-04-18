import {useState} from 'react'

import CourseCss from "./Course.module.css"

const Course = ({courseData}) => {
  const [showDetails, setShowDetails] = useState(false);

  return (
    <>
      <div className={CourseCss.course}>
        <div className={CourseCss.course_name}>{courseData.DEPTCODE} {courseData.COURSENUM}{courseData.COURSELETTER} - {courseData.COURSENAME}</div>
        <button onClick={() => setShowDetails(!showDetails)}>show details</button>
        {showDetails &&
          <div className={CourseCss.course_details}>
            {courseData.COURSEDESCRIPTION}
          </div>
        }
      </div>
    
    </>
  )
}

export default Course