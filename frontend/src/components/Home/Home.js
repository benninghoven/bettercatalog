import HomeCSS from "./Home.module.css"

// components
import Navbar from './Navbar';
import ClassTree from './ClassTree.js';
import ClassSearch from './ClassSearch';


// hooks
import useFetchFromDB from '../../hooks/fetchApi/useFetchFromDB'

function Home() {
  // hook to retrieve data from api
  //    -> data will be populated on mount of the Home component
  //    -> if [data, loading, error] states change, the Home component will rerender
  // how to use: 
  const [data, loading, error] = useFetchFromDB();
    const handleSearch = (searchTerm) => {
    // Do something with the search term, like filter your class data
  };

  return (
    <div className="Home">
        <Navbar />
      <header className={HomeCSS.header}>
             <div className={HomeCSS.logo}>
                <img src={process.env.PUBLIC_URL + '/logo.png'} alt="better catalog" />
            </div>
        <ClassSearch onSearch={handleSearch} />
        <ClassTree />

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
