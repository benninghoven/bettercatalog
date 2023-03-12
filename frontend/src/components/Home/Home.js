import HomeCSS from "./Home.module.css"

// components
import Navbar from './Navbar';

// hooks
import useFetchFromDB from '../../hooks/fetchApi/useFetchFromDB'

function Home() {
  // fetch data from
  const [data, loading, error] = useFetchFromDB();

  return (
    <div className="Home">
        <Navbar />
      <header className={HomeCSS.header}>
      {data ?
        data.map(function(course) {
          return <p key={course['DEPTCODE'] + course['COURSENUM'] + course['COURSELETTER']}>{course['DEPTCODE']} {course['COURSENUM']} {course['COURSELETTER']}</p>
        }) : <p>err</p>
      }
      </header>
    </div>
  );
}

export default Home;
