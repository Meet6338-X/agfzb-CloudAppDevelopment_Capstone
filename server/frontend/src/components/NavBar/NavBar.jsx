import React, { useState } from 'react'
import { Link } from 'react-router-dom'

function NavBar() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleLogin = async (event) => {
    event.preventDefault()
    const body = new URLSearchParams()
    body.append('username', username)
    body.append('psw', password)
    await fetch('/djangoapp/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: body.toString(),
      credentials: 'include',
    })
    window.location.reload()
  }

  return (
    <nav className="navbar">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">
          Best Cars Dealership
        </a>
        <ul className="nav navbar-nav navbar-right">
          <li>
            <a className="btn btn-link" href="/About.html">
              About Us
            </a>
            <a className="btn btn-link" href="/Contact.html">
              Contact Us
            </a>
          </li>
          <li>
            <form className="form-inline" onSubmit={handleLogin}>
              <input
                type="text"
                name="username"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              <input
                type="password"
                name="psw"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <button className="btn btn-primary" type="submit">
                Login
              </button>
              <Link className="btn btn-link" to="/register">
                Sign Up
              </Link>
            </form>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default NavBar
