import logo from './logo.svg';
import CSS from './App.module.css';
import React, { useState } from 'react';

import Navbar from './components/Navbar/Navbar.js';
import SearchBar from './components/SearchBar/SearchBar.js';
import SearchButton from './components/SearchButton/SearchButton.js';
import DropDown from './components/DropDown/DropDown.js';

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
const courses = [
  'CPSC 456',
  'CPSC 789',
  'CPSC 234',
  'CPSC 567',
  'CPSC 890',
  'CPSC 321',
  'CPSC 654',
  'CPSC 987',
  'CPSC 432'
];

function App() {

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
                        <SearchBar possibleCourses={possibleCourses} onPossibleCoursesChange={handlePossibleCoursesChange} />
                        <DropDown possibleCourses={possibleCourses} />
                    </div>
                <SearchButton />
                </div>
            </header>
        </div>
  );
}

export default App;
