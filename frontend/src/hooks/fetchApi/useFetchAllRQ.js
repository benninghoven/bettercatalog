import  { useQuery  } from 'react-query';

const fetchAll = async () => {
    return fetch('http://localhost:5000/fetchall-courses').then((response) => {return response.json();});
}

export const useFetchAllRQ = () => {
    return useQuery('fetchAll', fetchAll);
}