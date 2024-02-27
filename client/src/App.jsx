

import './App.css'
import NavBar from './components/Nav'
import { Outlet } from 'react-router-dom'

function App() {
  

  return (
    <>
      <NavBar/>
      <main>

        <Outlet />
      </main>
    </>
  )
}

export default App
