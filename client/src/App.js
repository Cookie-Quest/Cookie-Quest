import React, { useState, useEffect } from 'react';


function App() {
  const [data, setData] = useState([]); // Update initial state to an empty array

  useEffect(() => {
    fetch("/scan_cookies")
      .then(res => res.json())
      .then(data => {
        setData(data.cookies); // Update the state with the scanned cookies
      });
  }, []);

  return (
    <div>
      <h1>Scanned Cookies</h1>
      <ul>
        {data.map((cookie, index) => (
          <li key={index}>
            <strong>Name:</strong> {cookie.name}<br />
            <strong>Value:</strong> {cookie.value}<br />
            <strong>Domain:</strong> {cookie.domain}<br />
            <strong>Path:</strong> {cookie.path}<br />
            <strong>Expiry:</strong> {cookie.expiry}<br />
            <strong>Secure:</strong> {cookie.secure ? "Yes" : "No"}<br />
            <br />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
