import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

function DealerDetails() {
  const { dealerId } = useParams()
  const [dealer, setDealer] = useState(null)
  const [reviews, setReviews] = useState([])

  useEffect(() => {
    fetch(`/djangoapp/dealers/${dealerId}`, { credentials: 'include' })
      .then((response) => response.json())
      .then((data) => {
        setDealer(data.dealer || data)
        setReviews(data.reviews || [])
      })
  }, [dealerId])

  if (!dealer) {
    return <p>Loading dealer details...</p>
  }

  return (
    <div className="dealer-details">
      <h1>{dealer.name}</h1>
      <p className="dealer-address">
        {dealer.street}, {dealer.city}, {dealer.state}, {dealer.zip}
      </p>
      <a className="btn btn-primary" href={`/dealers/${dealerId}/add_review`}>
        Post Review
      </a>

      <h2>Reviews</h2>
      {reviews.length === 0 ? <p>No reviews yet for this dealer.</p> : null}
      {reviews.map((review, index) => (
        <div className="review-card" key={index}>
          <h3>{review.title}</h3>
          <p className="review-meta">
            {review.name} &mdash; {review.reviewedate ? String(review.reviewedate).slice(0, 10) : ''}
          </p>
          <p className="review-text">{review.review}</p>
          <p className="review-sentiment">Sentiment: {review.sentiment}</p>
        </div>
      ))}
    </div>
  )
}

export default DealerDetails
