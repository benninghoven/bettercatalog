import { useState } from "react";

import HeaderCss from "./Header.module.css"

import Navbar from "./Navbar/Navbar";
import SearchBar from "./SearchBar/SearchBar";
import SearchButton from "./SearchButton/SearchButton";
import DropDown from "./DropDown/DropDown";

const Header = () => {
  const [courseNames, setCourseNames] = useState();
  const [possibleCourses, setPossibleCourses] = useState([]);

  const handlePossibleCoursesChange = (newData) => {
      setPossibleCourses(newData);
  }
  return (
    <header className={HeaderCss.header}>
      <Navbar />
      <div className = {HeaderCss.inputarea}>
          <div className = {HeaderCss.searcharea}>
              <SearchBar possibleCourses={possibleCourses} onPossibleCoursesChange={handlePossibleCoursesChange} courses={courseNames}/>
              {/* <DropDown possibleCourses={possibleCourses} /> */}
          </div>
      <SearchButton />
      </div>
    </header>
  )
}

export default Header