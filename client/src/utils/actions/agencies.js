import axios from 'axios'
import { formToObj, getToken } from '../helpers/common'









export async function createAgency(request){

  const data = await formToObj(request)
  return await axios.post('/api/Agencies/', data, {
    validateStatus : () => true,
    headers: {
      Authorization: `Bearer ${getToken()}`,
      
    }
  })
}

export async function editAgency(request, id){

  const data = await formToObj(request)
  return await axios.patch(`/api/agencies/${id}/`, data, {
    validateStatus : () => true,
    headers: {
      Authorization: `Bearer ${getToken()}`

    }
  })
}