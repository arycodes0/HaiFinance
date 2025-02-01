import React, { useState } from 'react';
import axios from 'axios';
import './Dashboard.css';

const Dashboard = () => {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const predictLoan = async () => {
    setLoading(true);
    setError(null); // Reset error before making a new request

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/loan-predict/', {
        income: 6000,
        credit_score: 750,
        loan_amount: 20000
      });

      setPrediction(response.data.prediction);
    } catch (error) {
      console.error("Error fetching prediction:", error.response ? error.response.data : error.message);
      setError("Failed to fetch loan prediction. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container">
      <h1 className="dashboard-title">Dashboard</h1>

      <div className="dashboard-content">
        {/* Credit Card Details */}
        <div className="credit-card">
          <h2 className="credit-card-title">💳 Credit Card Details</h2>
          <div className="credit-card-info">
            <p><strong>Card Number:</strong> **** **** **** 1234</p>
            <p><strong>Expiry:</strong> 12/25</p>
            <p><strong>Balance:</strong> $5,300.00</p>
          </div>
        </div>

        {/* Loan Approval Section (Button Centered Below) */}
        <div className="loan-approval">
          <button 
            className="btn btn-primary"
            onClick={predictLoan}
            disabled={loading} // Prevent multiple requests
          >
            {loading ? "Checking..." : "Check Loan Approval"}
          </button>

          {error && <p className="error-message">{error}</p>}
          {prediction && <p className="prediction-result">Prediction: {prediction}</p>}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
