// App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [num1, setNum1] = useState('');
    const [num2, setNum2] = useState('');
    const [result, setResult] = useState(null);

    const addNumbers = async () => {
        const response = await axios.post('http://localhost:3000/', { num1, num2 });
        setResult(response.data.result);
    };

    return (
        <div>
            <input type="number" value={num1} onChange={e => setNum1(e.target.value)} />
            <input type="number" value={num2} onChange={e => setNum2(e.target.value)} />
            <button onClick={addNumbers}>Add</button>
            {result && <p>Result: {result}</p>}
        </div>
    );
}

export default App;