import logo from './logo.svg';
import CSS from './App.module.css';
import React, { useState, useEffect } from 'react';

import Navbar from './components/Navbar/Navbar.js';
import SearchBar from './components/SearchBar/SearchBar.js';
import DropDown from './components/DropDown/DropDown.js';
import SearchButton from './components/SearchButton/SearchButton.js';
import ClassVisualization from './components/ClassVisualization/ClassVisualization.js';

import useFetchFromDB from './hooks/fetchApi/useFetchFromDB'
// <img src={process.env.PUBLIC_URL + '/logo.png'} alt="better catalog" />
    
// DJB - Moved these around, don't know where they go
//{loading ? "loading..." : <></>}
//{data ?
//data.map(function(course) {
//return <p key={course['DEPTCODE'] + course['COURSENUM'] + course['COURSELETTER']}>{course['DEPTCODE']} {course['COURSENUM']} {course['COURSELETTER']}</p>
//}) : <></>
//}
// hook to retrieve data from api
//    -> data will be populated on mount of the Home component
//    -> if [data, loading, error] states change, the Home component will rerender
// how to use: 
//const [data, loading, error] = useFetchFromDB();
//

function App() {
    const [courseNames, setCourseNames] = useState([]);

    const getCourseNames = async () => {
        const response = await fetch("http://127.0.0.1:5000/fetchall-courses");
        const data = await response.json();
        setCourseNames(data)
    }
    getCourseNames();

    const [possibleCourses, setPossibleCourses] = useState([]);

    const handlePossibleCoursesChange = (newData) => {
        setPossibleCourses(newData);
    }

    return (
        <div>
            <header className ={CSS.header}>
                <Navbar />
                <div className = {CSS.inputarea}>
                    <div className = {CSS.searcharea}>
                        <SearchBar possibleCourses={possibleCourses} onPossibleCoursesChange={handlePossibleCoursesChange} courses={courseNames}/>
                        <DropDown possibleCourses={possibleCourses} />
                    </div>
                <SearchButton />
                </div>
                <ClassVisualization />
            </header>
        </div>
  );
}

export default App;
