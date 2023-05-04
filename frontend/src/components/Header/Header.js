// CSS IMPORTS
import HeaderCss from "./Header.module.css"

// COMPONENTS IMPORTS
import Navbar from "./Navbar/Navbar";

const Header = () => {
  return (
    <header className={HeaderCss.header}>
      <Navbar />
    </header>
  )
}

export default Header