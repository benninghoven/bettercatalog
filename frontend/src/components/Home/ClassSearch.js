import React, { useState } from 'react';
import CSS from './ClassSearch.module.css';

const ClassSearch = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearch = () => {
    onSearch(searchTerm);
  };

  return (
    <div className={CSS.classSearch}>
      <input
        type="text"
        placeholder="Search for a class..."
        value={searchTerm}
        onChange={handleInputChange}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default ClassSearch;

