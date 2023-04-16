import React, { useState } from 'react';
import CSS from './SearchButton.module.css';


function SearchButton(props){
  const handleSearch = (event) => {
      console.log('clicked button')
  };

    return(
        <div className={CSS.searchButton}>
            <button onClick={handleSearch}> Search </button>
        </div>
    );
};

export default SearchButton;
