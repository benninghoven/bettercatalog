import HomeCSS from "./Home.module.css"

import Navbar from './Navbar';

function Home() {
  return (
    <div className="Home">
        <Navbar />
      <header className={HomeCSS.header}>
      <p> YOYOYO </p>
      </header>
    </div>
  );
}

export default Home;
