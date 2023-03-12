import HomeCSS from "./Home.module.css"

// components
import Navbar from './Navbar';

// hooks
import useFetchFromDB from '../../hooks/fetchApi/useFetchFromDB'

function Home() {
  // hook to retrieve data from api
  //    -> data will be populated on mount of the Home component
  //    -> if [data, loading, error] states change, the Home component will rerender
  // how to use: 
  const [data, loading, error] = useFetchFromDB();

  return (
    <div className="Home">
        <Navbar />
      <header className={HomeCSS.header}>
      </header>
      {loading ? "loading..." : <></>}
      {data ?
        data.map(function(course) {
          return <p key={course['DEPTCODE'] + course['COURSENUM'] + course['COURSELETTER']}>{course['DEPTCODE']} {course['COURSENUM']} {course['COURSELETTER']}</p>
        }) : <></>
      }
    </div>
  );
}

export default Home;
