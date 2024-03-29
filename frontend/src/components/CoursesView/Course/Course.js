import {useState} from 'react'

import CourseCss from "./Course.module.css"
import useFetchPrereqs from '../../../hooks/fetchApi/useFetchPrereqs';

const Course = ({courseData}) => {
  const [prereqs, loading, error] = useFetchPrereqs(courseData.DEPTCODE, courseData.COURSENUM, courseData.COURSELETTER)
  const [showDetails, setShowDetails] = useState(false);
  const [showPrereqs, setShowPrereqs] = useState(false);

  return (
    <>
      <div className={CourseCss.course}>
        <div className={CourseCss.course_name}>{courseData.DEPTCODE} {courseData.COURSENUM}{courseData.COURSELETTER} - {courseData.COURSENAME}
        <button className={CourseCss.detailbtn} onClick={() => setShowDetails(!showDetails)}>show details</button>
      </div>
        {showDetails &&
          <div className={CourseCss.course_details}>
            {courseData.COURSEDESCRIPTION}
          </div>
        }
        <button className={CourseCss.prereqbtn} onClick={() => setShowPrereqs(!showPrereqs)}>show prereqs</button>
        {showPrereqs && prereqs &&
          prereqs.map(prereq =>
          <div className={CourseCss.course_prereqs}>
            <div key={prereq.PREREQDEPT + prereq.PREREQNUM + prereq.PREREQCOURSELETTER} style={{"paddingLeft":`${prereq.PREREQLEVEL * 2}rem`}}>{prereq.PREREQDEPT} {prereq.PREREQNUM} {prereq.PREREQCOURSELETTER} {prereq.PREREQLEVEL}</div>
          </div>
          )
        }
        {loading &&
          <div>loading...</div>
        }
        {error && 
          <div>ran into error...</div>
        }
      </div>
    
    </>
  )
}

export default Course
