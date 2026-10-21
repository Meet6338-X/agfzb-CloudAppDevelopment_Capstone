import React, { useState } from 'react'
import { useParams } from 'react-router-dom'

function AddReview() {
  const { dealerId } = useParams()
  const [review, setReview] = useState({
    name: '',
    title: '',
    review: '',
    purchased: 'yes',
  })
  const [message, setMessage] = useState('')

  const handleChange = (event) => {
    const { name, value } = event.target
    setReview({ ...review, [name]: value })
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    const response = await fetch(`/djangoapp/dealers/${dealerId}/add_review`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(review).toString(),
      credentials: 'include',
    })
    if (response.ok) {
      setMessage('Review submitted successfully.')
      setTimeout(() => {
        window.location.href = `/dealers/${dealerId}`
      }, 1500)
    } else {
      setMessage('Unable to submit the review.')
    }
  }

  return (
    <div className="add-review">
      <h1>Post Review</h1>
      <hr />
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">
            <b>Name</b>
          </label>
          <br />
          <input
            className="form-control"
            type="text"
            id="name"
            name="name"
            placeholder="Enter your name"
            value={review.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="title">
            <b>Title</b>
          </label>
          <br />
          <input
            className="form-control"
            type="text"
            id="title"
            name="title"
            placeholder="Enter the review title"
            value={review.title}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="review">
            <b>Your review</b>
          </label>
          <br />
          <textarea
            className="form-control"
            id="review"
            name="review"
            rows="5"
            placeholder="Enter your review"
            value={review.review}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="purchased">
            <b>Did you purchase the car here?</b>
          </label>
          <br />
          <select id="purchased" name="purchased" value={review.purchased} onChange={handleChange}>
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </div>
        <button className="btn btn-primary" type="submit">
          Submit Review
        </button>
        {message ? <p className="review-message">{message}</p> : null}
      </form>
    </div>
  )
}

export default AddReview
