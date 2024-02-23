import { createBrowserRouter, RouterProvider, } from "react-router-dom"
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
// import './index.css'
import './styles/main.scss'
import AllShifts from './components/AllShifts.jsx'
import Login from './components/Login.jsx'
import Register from './components/Register.jsx'
import AgencyProfile from './components/AgencyProfile.jsx'
import CreateShift from './components/CreateShift.jsx'
import SecurityProfile from './components/SecurityProfile.jsx'
import CreateAgency from './components/CreateAgency.jsx'
import Home from './components/Home.jsx'


const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,


    children: [
      {
        path: "/",
        element: <Home />
      },
      {
        path: "/shifts/",
        element: <AllShifts/>,
        // loader: getAllProjects
      },
      {
        path: "/angencies/:id/",
        element: <AgencyProfile/>,
      //   loader: async ({ params }) => getProfile(params.id)
      },
      {
        path: "/angencies/create/",
        element: <CreateAgency/>,
      //   loader: async ({ params }) => getProfile(params.id)
      },
      {
        path: "/security/:id/",
        element: <SecurityProfile/>,
      //   loader: async ({ params }) => getProfile(params.id)
      },
      {
        path:"/auth/login/",
        element: <Login/>,
        // action: async ({ request }) => loginUser(request)
      },
      {
        path:"/auth/register/",
        element: <Register/>,
      //   action: async ({ request }) => registerUser(request)
      },
      {
      path:"/shifts/create/",
      element: <CreateShift/>,
      
      },
      {
        path:"/shifts/",
        element: <AllShifts/>,
      //   loader: async ({ params }) => getAllProfiles(params)
      },
    
    ]
  },
]);
ReactDOM.createRoot(document.getElementById('root')).render(

  <RouterProvider router={router} />

)

