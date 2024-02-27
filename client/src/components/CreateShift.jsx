import { useState, useEffect} from "react"
import { useLoaderData, useActionData, useNavigate, Form } from "react-router-dom"


export default function CreateShift() {
  const agency = useLoaderData()
  const navigate = useNavigate()
  const res = useActionData()
  const { owned_agency } = agency
  console.log(owned_agency[0].id)



  const [formData, setFormData] = useState({
    start_time: "",
    end_time: "",
    shift_location: "",

    agency: `${owned_agency[0].id}`,
  })

  useEffect(() => {
    console.log(res)
    if (res?.status === 200) {
      navigate(`/`)
    }
  }, [res, navigate,])

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }


  return (
    <>
      <div className="form-container">
        <h1 className="text-center bold display-3 mb-4">Create Shift</h1>
        <Form className='form' method="POST"  >
          <input type="datetime-local" name="start_time" placeholder='shift start time'  onChange={handleChange} />
          <input type="datetime-local" name="end_time" placeholder='shift finish time'  onChange={handleChange} />
          <input type="text" name="shift_location" placeholder='location of shift'  onChange={handleChange} />
          <input type="hidden" name="agency" value={formData.agency} />

          <button type="submit">Create Shift</button>
        </Form>
      </div>
    </>
  )
}