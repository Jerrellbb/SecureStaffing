import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
import { useNavigate } from 'react-router-dom'

export default function NavBar() {

  const navigate = useNavigate()

  const handleClick = (e) => {
    navigate(`${e.target.id}`)
  }

  return (

    <>
      <Navbar>
        <div className="navlinks">

          <Nav.Link onClick={handleClick}> <button type='button' id='/'>Home</button> </Nav.Link>
          <Nav.Link onClick={handleClick}> <button type='button' id='/agencies/'>agencyname</button> </Nav.Link>
          <Nav.Link onClick={handleClick}> <button type='button' id='/security/:id'>My profile</button> </Nav.Link>
          <Nav.Link onClick={handleClick}> <button type='button' id='/shifts/'>Avalable Shifts</button> </Nav.Link>
          <Nav.Link onClick={handleClick}> <button type='button' id='/auth/login/'>Login</button> </Nav.Link>
          <Nav.Link onClick={handleClick}> <button type='button' id='/auth/register/'>Register</button> </Nav.Link>
        </div>


      </Navbar>
    </>
  )
}