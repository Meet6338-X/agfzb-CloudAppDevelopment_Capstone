import React, { useEffect, useState } from 'react'

function Home() {
  const [dealers, setDealers] = useState([])
  const [state, setState] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const url = state
      ? `/djangoapp/dealers?state=${encodeURIComponent(state)}`
      : '/djangoapp/dealers'
    fetch(url, { credentials: 'include' })
      .then((response) => response.json())
      .then((data) => {
        setDealers(data.dealerships || data || [])
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [state])

  return (
    <div className="home">
      <h1>Best Cars Dealership</h1>
      <p>Welcome to Best Cars dealership, home to the best cars in North America.</p>

      <div className="state-filter">
        <label htmlFor="state">Filter by state:</label>
        <input
          type="text"
          id="state"
          name="state"
          placeholder="e.g. Kansas"
          value={state}
          onChange={(e) => setState(e.target.value)}
        />
      </div>

      {loading ? <p>Loading dealerships...</p> : null}

      <table className="dealer-table">
        <thead>
          <tr>
            <th>Id</th>
            <th>Dealership</th>
            <th>State</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {dealers.map((dealer) => (
            <tr key={dealer.id}>
              <td>{dealer.id}</td>
              <td>{dealer.name}</td>
              <td>{dealer.state}</td>
              <td>
                <a href={`/dealers/${dealer.id}`}>Review Dealer</a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Home
