import React, { useState } from 'react';
import CSS from './SearchBar.module.css';

import ClassVisualization from '../../ClassVisualization/ClassVisualization.js'

// DJB - Pull all classes from DB
//
const classes = [
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


function SearchBar(props) {
    const {possibleCourses, onPossibleCoursesChange, courses} = props;
    const [searchTerm, setSearchTerm] = useState('');

  const handleInputChange = (event) => {

    const searchTerm = event.target.value;
    setSearchTerm(searchTerm);
    console.log('User typed:', searchTerm);

    const possibleClassesArray = courses.filter((className) => {
      return className.toLowerCase().includes(searchTerm.toLowerCase());
    });

    if (possibleClassesArray.length && searchTerm.length > 0){
        onPossibleCoursesChange(possibleClassesArray);
    }
      else{
        onPossibleCoursesChange([]);
      }

  };

  // DJB classes are fake for now
  return (
      <div className={CSS.searchBar}>
        <input
          type="text"
          placeholder="Search for a class..."
          value={searchTerm}
          onChange={handleInputChange}
        />
      </div>
  );
};

export default SearchBar;


