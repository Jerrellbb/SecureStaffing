import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
// import { useNavigate } from 'react-router-dom'

export default function NavBar(){



  return(

    <>
    <Navbar>
      <div className="navlinks">
    
    <Nav.Link> <button type='button' id='/'>Home</button> </Nav.Link>
    <Nav.Link> <button type='button' id='/agencies/'>agencyname</button> </Nav.Link>
    <Nav.Link> <button type='button' id='/security/:id'>My profile</button> </Nav.Link>
    <Nav.Link> <button type='button' id='/shifts/'>Avalable Shifts</button> </Nav.Link>
    </div>

    
    </Navbar>
    </>
  )
}