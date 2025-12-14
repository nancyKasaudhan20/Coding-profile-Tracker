import { useState , useEffect} from 'react'
import './App.css'

function App({ username="nancy20" }) {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/profile/${username}`)
      .then(res => res.json())
      .then(data => setProfile(data));
  }, [username]);
console.log("profile", profile)
  if (!profile) return <p>Loadregrgeing...</p>;

  return (
    <div>
      <h2>{profile.username}</h2>
      <p>Platform: {profile.platform}</p>
      <p>Total Solved: {profile.total_solved}</p>
      <p>Last Solved: {profile.last_solved_at}</p>
    </div>
  );
}



export default App
