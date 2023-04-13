import React from 'react';
import CSS from "./Home.module.css"

const ClassTree = () => {
  return (
    <div className={CSS.classTree}>
      <ul>
        <li>
          Class A
          <ul>
            <li>Class B</li>
            <li>
              Class C
              <ul>
                <li>Class D</li>
                <li>Class E</li>
              </ul>
            </li>
          </ul>
        </li>
        <li>Class F</li>
        <li>
          Class G
          <ul>
            <li>Class H</li>
            <li>
              Class I
              <ul>
                <li>Class J</li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  );
};

export default ClassTree;
