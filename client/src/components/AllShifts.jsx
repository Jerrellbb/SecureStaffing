
import { useLoaderData } from "react-router-dom"

export default function AllShifts() {
  const allShifts = useLoaderData()


    
  return (
    <>
      <div>
        <h1 className="text-center bold display-3 mb-4">Avalable Shifts</h1>
      </div>
      <div className="container-grid">
        <ul className="shifts-list">
          {allShifts.map((shift) => {
            const { id, agency_name, start_time, end_time, available_slots, shift_location } = shift
            return (

              <li key={id}>
                <p>{agency_name}</p>
                <p>shift start:{start_time}</p>
                <p>shift end:{end_time}</p>
                <p>available slots: {available_slots}</p>
                <p>{shift_location}</p>
                

              </li>
            )
          })}
        </ul>

      </div>

    </>
  )
}