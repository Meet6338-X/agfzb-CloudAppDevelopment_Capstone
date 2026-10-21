import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import './Register.css'

/**
 * Register - the "Sign-up" page of the Best Cars Dealership application.
 *
 * It presents the five sign-up input fields required by the capstone
 * (Username, First Name, Last Name, Email and Password) together with the
 * Register button that submits the new account to the Django backend.
 */
function Register() {
  const [form, setForm] = useState({
    username: '',
    firstname: '',
    lastname: '',
    email: '',
    psw: '',
  })
  const [message, setMessage] = useState('')

  const handleChange = (event) => {
    const { name, value } = event.target
    setForm({ ...form, [name]: value })
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    try {
      const response = await fetch('/djangoapp/registration', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })
      if (response.ok) {
        setMessage('Account created successfully. Redirecting to the home page...')
        setTimeout(() => {
          window.location.href = '/'
        }, 1500)
      } else {
        setMessage('Unable to create the account. Please try again.')
      }
    } catch (error) {
      setMessage('Unable to reach the server. Please try again.')
    }
  }

  return (
    <div className="register-page">
      <h1>Sign Up</h1>
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
            id="username"
            name="username"
            placeholder="Enter User Name: "
            value={form.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="firstname">
            <b>First Name</b>
          </label>
          <br />
          <input
            className="form-control"
            type="text"
            id="firstname"
            name="firstname"
            placeholder="Enter First Name: "
            value={form.firstname}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="lastname">
            <b>Last Name</b>
          </label>
          <br />
          <input
            className="form-control"
            type="text"
            id="lastname"
            name="lastname"
            placeholder="Enter Last Name: "
            value={form.lastname}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">
            <b>Email</b>
          </label>
          <br />
          <input
            className="form-control"
            type="email"
            id="email"
            name="email"
            placeholder="Enter Email: "
            value={form.email}
            onChange={handleChange}
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
            id="psw"
            name="psw"
            placeholder="Enter Password: "
            value={form.psw}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <button className="btn btn-primary" type="submit">
            Register
          </button>
        </div>
        {message ? <p className="register-message">{message}</p> : null}
        <p>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </form>
    </div>
  )
}

export default Register
