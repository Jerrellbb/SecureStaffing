import axios from 'axios'

export async function getAllShifts(){
  const res = await axios.get('/api/shifts/')
  return res.data
}

export async function agencyProfile(id){
  const res = await axios.get(`/api/agencies/${id}`)
  return res.data
}
export async function securityProfile(id){
  const res = await axios.get(`/api/security/${id}`)
  return res.data
}

export async function getProfile(id){
  const res = await axios.get(`/api/auth/${id}/`)
  return res.data
}

export async function getAllProfiles(){
  const res = await axios.get('/api/auth/users/')
  console.log(res)
  return res.data
}
