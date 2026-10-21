import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async (event) => {
    event.preventDefault()
    const body = new URLSearchParams()
    body.append('username', username)
    body.append('psw', password)
    const response = await fetch('/djangoapp/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: body.toString(),
      credentials: 'include',
      redirect: 'follow',
    })
    if (response.ok) {
      setError('')
      navigate('/')
    } else {
      setError('Invalid username or password.')
    }
  }

  return (
    <div className="login-page">
      <h1>Login</h1>
      <hr />
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">
            <b>User Name</b>
          </label>
          <br />
          <input
            className="form-control"
            type="text"
            name="username"
            id="username"
            placeholder="Enter User Name: "
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="psw">
            <b>Password</b>
          </label>
          <br />
          <input
            className="form-control"
            type="password"
            name="psw"
            id="psw"
            placeholder="Enter Password: "
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error ? <p className="login-error">{error}</p> : null}
        <button className="btn btn-primary" type="submit">
          Login
        </button>
      </form>
    </div>
  )
}

export default Login
