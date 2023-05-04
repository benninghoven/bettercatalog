import React from 'react';
import CSS from './ClassVisualization.module.css'

const ClassVisualization= () => {
  return (
    <div className = {CSS.classVisualization}>
<ul>
  <li>Class A
    <ul>
      <li>Subclass A1
        <ul>
            <li>Another One</li>
            <li>Another One</li>
            <li>Another One</li>
        </ul>
      </li>
      <li>Subclass A2</li>
      <li>Subclass A3</li>
      <li>Subclass A4</li>
        <ul>
            <li>Another One</li>
        <ul>
            <li>Another One</li>
        <ul>
            <li>Another One</li>
            <li>Another One</li>
        <ul>
        <ul>
        <ul>
            <li>Another One</li>
            <li>Another One</li>
        </ul>
            <li>Another One</li>
            <li>Another One</li>
        </ul>
            <li>Another One</li>
            <li>Another One</li>
        </ul>
        </ul>
            <li>Another One</li>
        </ul>
            <li>Another One</li>
        </ul>
      <li>Subclass A5</li>
      <li>Subclass A6</li>
      <li>Subclass A7</li>
        <ul>
            <li>Another One</li>
        </ul>
      <li>Subclass A8</li>
      <li>Subclass A9</li>
    </ul>
  </li>
</ul>
    </div>
  );
};

export default ClassVisualization;
