import axios from 'axios'
import { formToObj, getToken } from '../helpers/common'
// import { redirect,  } from 'react-router-dom'




export async function editshift(request, id){

  const data = await formToObj(request)
  return await axios.patch(`/api/shifts/${id}/`, data, {
    validateStatus : () => true,
    headers: {
      Authorization: `Bearer ${getToken()}`

    }
  })
}

export async function createShift(request){

  const data = await formToObj(request)
  return await axios.post('/api/shifts/', data, {
    validateStatus : () => true,
    headers: {
      Authorization: `Bearer ${getToken()}`,
      
    }
  })
}