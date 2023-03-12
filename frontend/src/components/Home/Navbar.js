import React from 'react';
import CSS from "./Home.module.css"

const Navbar = () => {
  return (
    <nav className={CSS.navbar}>
      <ul>
        <li>Home</li>
        <li>Contact</li>
        <li>Fullerton</li>
      </ul>
    </nav>
  );
};

export default Navbar;

