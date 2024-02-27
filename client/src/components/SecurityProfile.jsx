import { useLoaderData } from "react-router-dom"

export default function SecProfile() {
  const security = useLoaderData()
  const { name, phone_number, image, user, qualifications } = security
  const qualificationNames = {
    1: "Close Protection",
    2: "SIA Door Supervisor",
    3: "Security Guard",
    4: "Cash & Valuables in Transit",
    5: "Key Holding",
    6: "CCTV Operator",
    7: "First Aid Level 1",
    8: "First Aid Level 2",
    9: "First Aid Level 3",

  }
  const qualificationNamesList = qualifications.map(q => qualificationNames[q])
  return (
    <>
      <div className="security-profile">
        <h1>{name}&apos;s profile</h1>
        <img src={image} alt='users image' />
        <p><strong>Email:</strong> {user.email}</p>
        <p><strong>Contact Number:</strong> {phone_number}</p>
        <p><strong>Qualification:</strong> {qualificationNamesList.join(', ')}</p>
      </div>
    </>
  )
}