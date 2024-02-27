
import ImageUploadField from "./ImageUpload"
import { useState } from 'react'
import { useNavigate } from "react-router-dom"

export default function CreateAgency() {

  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phonenumber: "",

    image: ""
  })

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }
  return (
    <>
    <div className="form-container">
      <h1 className="text-center bold display-3 mb-4">Create Agency</h1>
      <form className='form' method="POST">
        <input type="text" name="name" placeholder='Agency Name' autoComplete='name' onChange={handleChange} />
        <input type="text" name="email" placeholder='Email' autoComplete='email' onChange={handleChange} />
        <input type="text" name="phonenumber" placeholder='Phone Number e.g. +440796033434' autoComplete='phonenumber' onChange={handleChange} />
        <ImageUploadField formData={formData} setFormData={setFormData} />
        <button type="submit">Create Agency</button>
      </form>
    </div>
    </>
  )
}