import { useLoaderData } from "react-router-dom"

export default function AgencyProfile() {
  const agency = useLoaderData()

  const { name, email, phone_number, image,  owner } = agency

  return (
    <>
      <div>
        <h1 className="text-center bold display-3 mb-4">{name}</h1>
      </div>
      <div className="container-profile">


        <div className="profile-info">
          <img src={image} alt={name} />
          <p>Email: {email}</p>
          <p>Primary Contact:{owner.username}</p>
          <p>Contact Number:{phone_number}</p>
        </div>
      <button>edit</button>
      </div>
    </>
  )
}