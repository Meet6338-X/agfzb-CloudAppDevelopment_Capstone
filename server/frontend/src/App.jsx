import React from 'react'
import { Routes, Route } from 'react-router-dom'
import NavBar from './components/NavBar/NavBar'
import Home from './components/Home/Home'
import Login from './components/Login/Login'
import Register from './components/Register/Register'
import DealerDetails from './components/DealerDetails/DealerDetails'
import AddReview from './components/AddReview/AddReview'

function App() {
  return (
    <div className="app">
      <NavBar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/dealers/:dealerId" element={<DealerDetails />} />
          <Route path="/dealers/:dealerId/add_review" element={<AddReview />} />
        </Routes>
      </div>
      <footer className="footer">
        <p>Best Cars Dealership &mdash; 1000 Auto Mall Drive, North America | Phone: 123456789</p>
      </footer>
    </div>
  )
}

export default App
