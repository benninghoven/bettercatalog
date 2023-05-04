// YE - NODE MODULES
import React, { useState, useEffect } from 'react';

// YE - COMPONENETS IMPORTS
import Header from "./components/Header/Header"
import CoursesView from './components/CoursesView/CoursesView';
import ClassVisualization from './components/CoursesView/ClassVisualization/ClassVisualization.js';

// YE - CSS IMPORTS
import MainCss from './App.module.css';

// YE - HOOKS IMPORTS
import APITestButton from './components/APITestButton/APITestButton';

function App() {
    const [btnClicked, setBtnClicked] = useState(false);

    /* YE - arranged components as follows:
        HEADER COMPONENT
            includes:
                Navbar
                SearchBar
                SearchButton
                DropDown
        COURSESVIEW COMPONENT
            includes:
                ClassVisualization - legacy (removed for new frontend)
    */
        
    return (
        <div className={MainCss.body}>
            <Header></Header>
            <CoursesView></CoursesView>
            {/* <ClassVisualization /> */}
            {/* <APITestButton btnClicked={btnClicked} setBtn={setBtnClicked}></APITestButton> */}
        </div>
  );
}

export default App;
