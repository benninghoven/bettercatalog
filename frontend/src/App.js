import CSS from './App.module.css';
import React, { useState, useEffect } from 'react';

import Navbar from './components/Navbar/Navbar.js';
import SearchBar from './components/SearchBar/SearchBar.js';
import DropDown from './components/DropDown/DropDown.js';
import SearchButton from './components/SearchButton/SearchButton.js';
import ClassVisualization from './components/ClassVisualization/ClassVisualization.js';

import useFetchAll from './hooks/fetchApi/useFetchFromDB'

function App() {
    const [data, loading, error] = useFetchAll();
    const [btnClicked, setBtnClicked] = useState(false);
    
    const [courseNames, setCourseNames] = useState();
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
                <button onClick={() => setBtnClicked(!btnClicked)}>get courses</button>
                {loading && <div>loading...</div>}
                {error && <div>error: {error}</div>}
                { btnClicked && data && 
                    data.map(x => <div key={x} className={CSS.courses}>{x}</div>)    
                }
            </header>
        </div>
  );
}

export default App;
