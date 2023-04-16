import React, { useState } from 'react';
import CSS from './DropDown.module.css';

const DropDown = ({possibleCourses}) => {
  const [selectedOption, setSelectedOption] = useState('');

  const handleOptionSelect = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div className={CSS.dropdown}>
      <select value={selectedOption} onChange={handleOptionSelect}>
        {possibleCourses.map((course, index) => (
          <option key={index} value={course}>
            {course}
          </option>
        ))}
      </select>
    </div>
  );
};

export default DropDown;
