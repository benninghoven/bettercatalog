/* YE
    this component will:
        2. render courses in in a list of Course component format

    TODO: 
        1. implement CourseView
            a. CSS for CourseView - how to view courses?
        2. implement Courses
            a. fetch all courses
        3. implement Course
            a. fetch all Course prerequisites
            b. fetch all Course postrequisites

    TO CONSIDER:
        1. when and where should we do the fetching from the DB?
            a. think efficiency. is it better to have it intialized
               all at the same time? or per component
*/

// NODE MODULE IMPORTS
import {useState} from 'react'

// CUSTOM COMPONENTS IMPORTS:
import Course from "./Course/Course"

// CUSTOM HOOK IMPORT
import useFetchAll from '../../hooks/fetchApi/useFetchAllCourses'
import { useFetchAllRQ } from '../../hooks/fetchApi/useFetchAllRQ'

// CSS IMPORTS
import CoursesViewCss from "./CoursesView.module.css"
import Search from './Search/Search'

const CoursesView = () => {
    // const [data, loading, error] = useFetchAll();
    const {data, isLoading, isError} = useFetchAllRQ();
    const [searchResult, setSearchResult] = useState(false);
    const [showSearchResult, setShowSearchResult] = useState(false);

    if (data) console.log(data);

    return (
        <>
            {data && <Search courses={data} showSearch={setShowSearchResult} searchResult={searchResult} setResult={setSearchResult}/>}
            <div className={CoursesViewCss.body}>
                {/* if not searching and the course list is ready, show original course list */}
                    {data && !showSearchResult && data.map(course => <Course key={course.DEPTCODE + course.COURSENUM + course.COURSELETTER} courseData={course}></Course>)}
                    {isLoading && !showSearchResult && <p>loading...</p>}
                    {isError && !showSearchResult && <p>an error occured...</p>}
                {/* if searching, show search result */}
                    {showSearchResult && searchResult.map(course => <Course key={course.DEPTCODE + course.COURSENUM + course.COURSELETTER} courseData={course}></Course>)}
            </div>
        </>
    )
}

export default CoursesView