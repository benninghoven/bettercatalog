const SearchBar = ({ classes, onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedClass, setSelectedClass] = useState(null);

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearch = () => {
    onSearch(searchTerm);
  };

  const handleDropdownChange = (event) => {
    setSelectedClass(event.target.value);
  };

  const filteredClasses = classes.filter((className) => {
    return className.toLowerCase().includes(searchTerm.toLowerCase());
  });

  return (
    <div className={CSS.searchBar}>
      <div className={CSS.searchContainer}>
        <input
          type="text"
          placeholder="Search for a class..."
          value={searchTerm}
          onChange={handleInputChange}
        />
        {filteredClasses.length > 0 && (
          <select
            className={CSS.dropdown}
            value={selectedClass}
            onChange={handleDropdownChange}
            style={{ top: 'calc(100% + 4px)', left: 0 }}
          >
            <option value="">Select a class</option>
            {filteredClasses.map((className) => (
              <option key={className} value={className}>
                {className}
              </option>
            ))}
          </select>
        )}
      </div>
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

