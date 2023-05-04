// YE - SEARCH COURSE WORKFLOW
//      user inputs into input box
//      search result dropdown is populated and updated on every character input
//      user selects dropdown option(s)
//      courseview is updated
//      if user clears the input field, the original course list is viewed

import { useState, useEffect } from 'react'
import Select from 'react-select';

import SearchCSS from "./Search.module.css"

const Search = ({courses, showSearch, setResult}) => {
    const [dropDownSelections, setDropDownSelections] = useState([]); 

    useEffect(() => {
        parseCourses(courses);
    }, [])

    // parses courses to drop down objects
    const parseCourses = () => {
        let selections = []
        for (let course of courses){
            let selection = {}
            selection.label = `${course["DEPTCODE"]} ${course["COURSENUM"]}${course["COURSELETTER"]}`;
            selection.value = course;
            selections.push(selection);
        }
        setDropDownSelections(selections);
    }

    const handleSearch = (opt) => {
        // if an option is selected
        if (opt.length != 0) {
            let search_result = opt.map(x => x.value);
            showSearch(true);
            setResult(search_result);
        } else {
            // don't show the search result and show the og course list
            showSearch(false);
        }
    }

    return (
        <div className={SearchCSS.container}>
            <Select className={SearchCSS.select}
                placeholder="Search Courses..."
                options={dropDownSelections && dropDownSelections}
                onChange={opt => handleSearch(opt)}
                isClearable
                isSearchable
                isMulti
            />
        </div>
    )
}

export default Search