import React from 'react';
import CSS from "./Home.module.css"

const Navbar = () => {
  return (
    <nav className={CSS.navbar}>
      <ul>
        <li>Home</li>
        <li>Courses</li>
        <li>Events</li>
        <li>About</li>
      </ul>
    </nav>
  );
};

export default Navbar;

