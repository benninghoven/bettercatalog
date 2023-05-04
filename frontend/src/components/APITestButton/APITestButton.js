import React from 'react'

import useFetchAllTest from '../../hooks/fetchApi/useFetchAllTest';

import ApiCss from "./APITestButton.module.css";

const APITestButton = ({btnClicked, setBtn}) => {
    const [data, loading, error] = useFetchAllTest();

  return (
    <>
        <button onClick={() => setBtn(!btnClicked)}>get courses</button>
        {loading && <div>loading...</div>}
        {error && <div>error: {error.message}, error type: {error.type}</div>}
        { btnClicked && data && 
            data.map(x => <div key={x} className={ApiCss.APITestResult}>{x}</div>)    
        }
    </>
  )
}

export default APITestButton