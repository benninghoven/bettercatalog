import React, { useState } from 'react';
import CSS from './SearchBar.module.css';


const SearchBar = ({ classes, onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleInputChange = (event) => {
    const searchTerm = event.target.value;
    setSearchTerm(searchTerm);
    console.log('User typed:', searchTerm);

    const possibleClassesArray = classes.filter((className) => {
      return className.toLowerCase().includes(searchTerm.toLowerCase());
    });

    if (possibleClassesArray.length){
        console.log('PossibleClasses:', possibleClassesArray);
    }
    else{
        console.log('No PossibleClasses:');
    }
  };


  const handleSearch = () => {
    onSearch(searchTerm);
    console.log('HandleSearch:', searchTerm);
    console.log('User Clicked Search');
 
  };
    const Dropdown = ({ options }) => {
      return (
        <select>
          {options.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      );
    };

    // DJB FIXME: classes are fake for now
  return (
    <div>
        <div className={CSS.searchBar}>
            <input
              type="text"
              placeholder="Search for a class..."
              value={searchTerm}
              onChange={handleInputChange}
            />
          <button onClick={handleSearch}>Search</button>
        </div>
        {classes.length > 0 && (
        <Dropdown options={classes} />
      )}
    </div>
  );
};

export default SearchBar;
