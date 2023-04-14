import logo from './logo.svg';
import CSS from './App.module.css';

import Navbar from './components/Navbar/Navbar.js';
import SearchBar from './components/SearchBar/SearchBar.js';

import useFetchFromDB from './hooks/fetchApi/useFetchFromDB'

// <img src={process.env.PUBLIC_URL + '/logo.png'} alt="better catalog" />
    
// DJB - Moved these around, don't know where they go

//{loading ? "loading..." : <></>}
//{data ?
//data.map(function(course) {
//return <p key={course['DEPTCODE'] + course['COURSENUM'] + course['COURSELETTER']}>{course['DEPTCODE']} {course['COURSENUM']} {course['COURSELETTER']}</p>
//}) : <></>
//}
//
const classes = [
  'CPSC 123',
  'CPSC 456',
  'CPSC 789',
  'CPSC 234',
  'CPSC 567',
  'CPSC 890',
  'CPSC 321',
  'CPSC 654',
  'CPSC 987',
  'CPSC 432'
];

function App() {
  // hook to retrieve data from api
  //    -> data will be populated on mount of the Home component
  //    -> if [data, loading, error] states change, the Home component will rerender
  // how to use: 
  const [data, loading, error] = useFetchFromDB();
  const handleSearch = (searchTerm) => {
    // Do something with the search term, like filter your class data
  };
  return (
    <div>
      <header className ={CSS.header}>
      <Navbar />
      <SearchBar classes ={classes} onSearch={handleSearch} />
      </header>
    </div>
  );
}

export default App;
