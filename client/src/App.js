// useState -> used to create the state variable containing the data retrieved from the backend. The state variable is used to render data on the page. 
// useEffect -> used to fetch the backend API on the first render 
import React, { useState, useEffect } from 'react'

function App() {
  // data -> state variable
  // setData -> function to modify the data variable
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch('/api/users')
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      });
  }, []);





  return (
    <div>
      {(typeof data.users === 'undefined') ?
        (
          <p>Loading...</p>
        ) : (
          data.users.map((member, i) => (
            <p key={i}>{member}</p>
          ))
        )}
    </div>
  )
}

export default App