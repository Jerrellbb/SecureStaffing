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
import { loginUser } from "../utils/actions/auth.js"
import { getAllShifts, agencyProfile, securityProfile, getProfile } from "../utils/loaders.js"
import { createShift } from "../utils/actions/shifts.js"
import { getUserId } from "../utils/helpers/common.js"
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
        path: "/agencies/:id/",
        element: <AgencyProfile />,
        loader: async ({ params }) => agencyProfile(params.id)
      },
      {
        path: "/agencies/create/",
        element: <CreateAgency />,
        //   loader: async ({ params }) => getProfile(params.id)
      },
      {
        path: "/security/:id/",
        element: <SecurityProfile />,
        loader: async ({ params }) => securityProfile(params.id)
      },
      {
        path: "/auth/login/",
        element: <Login />,
        action: async ({ request }) => loginUser(request)
      },
      {
        path: "/auth/register/",
        element: <Register />,
        //   action: async ({ request }) => registerUser(request)
      },
      {
        path: "/shifts/create/",
        element: <CreateShift />,
        loader: async () => getProfile(getUserId()),
        action: async ({ request }) => createShift(request)

      },
      {
        path: "/shifts/",
        element: <AllShifts />,
        loader: async ({ params }) => getAllShifts(params)
      },

    ]
  },
]);
ReactDOM.createRoot(document.getElementById('root')).render(

  <RouterProvider router={router} />

)

