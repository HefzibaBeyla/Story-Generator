import React, {useState, useEffect} from 'react'
import axios from 'axios';

export default function Story() {

    const [result, setResult] = useState(null);

    const story = async () => {
        try {
            let response = await axios.get('http://localhost:8000/');
            let result = response.data;
            setResult(result);
        } catch(e) {
            console.log(e)
        }
    };

    useEffect (() => {
        story()
    }, [])

    return (
        <div>
            {result}
        </div>
    )
}
