import './App.css'
import { useState, useEffect } from 'react'

function App() {
  const [videoList, setVideoList] = useState([])

  useEffect(() => {
    fetch("/api/video").then(
      res => res.json()
    ).then(
      data => {
        setVideoList(data)
        console.log(data)
      }
    )
  }, [])

  // Define state variables for form fields
  const [videoName, setVideoName] = useState('');
  const [timeUpdated, setTimeUpdated] = useState('');
  const [isInputValid, setIsInputValid] = useState(false);

  // Event handler for input changes
  const handleInputChange = (event) => {
    const { name, value } = event.target;

    // Update state based on input changes
    if (name === 'videoName') {
      setVideoName(value);
    } else if (name === 'timeUpdated') {
      setTimeUpdated(value);
    }

    if(videoName != "" && timeUpdated != "")setIsInputValid(true)
    else setIsInputValid(false)
  };

  // Event handler for form submission
  const handleSubmit = (event) => {
    event.preventDefault(); // Prevents the default form submission behavior

    fetch('/api/create-video/?name=' + videoName + '&time=' + timeUpdated, {
      method: 'POST',
    })
    .then(res => {
      if (!res.ok) {
        throw new Error(`HTTP error! Status: ${res.status}`);
      }
      // response.json() returns a Promise
      return res.json();
    })
    .then(data => {
      console.log("Record created with id: " + data.createdId);
      const newItem = [data.createdId, videoName, timeUpdated];
      setVideoList([...videoList, newItem]);
    })
  };

  const handleDelete = (id) => {
    fetch('/api/delete-video/?id=' + id, {
      method: 'DELETE',
    })
    .then(res => {
      console.log("Successful: "+res);
      setVideoList(videoList.filter(rec => rec[0]!=id))
    })
  }

  return <>
    <form id="createVideo" onSubmit={handleSubmit}>
        <label for="videoName">Name of the Video:</label>
        <input type="text" name="videoName" value={videoName} onChange={handleInputChange} ></input>

        <label for="timeUpdated">Time Updated:</label>
        <input type="text" name="timeUpdated" value={timeUpdated} onChange={handleInputChange} ></input>

        <button type="submit" className={isInputValid ? '' : 'disabled'} disabled={!isInputValid}>Create Video</button>
    </form>
    <br></br>
    <table>
    <tr>
    <th>Video Name</th>
    <th>Time Updated</th>
    <th>Actions</th>
    </tr>
      {
        videoList.map(item => (
          <tr>
          <td>{item[1]}</td>
          <td>{item[2]}</td>
          <td>
            <button className="delete" onClick={() => handleDelete(item[0])}>Delete</button>
            <button>Update</button>
          </td>
          </tr>))
      }
    </table>
  </>
}

export default App
