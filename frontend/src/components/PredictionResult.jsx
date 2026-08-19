export default function PredictionResult({ result, error, loading }) {
  if (error) {
    return (
      <div className="card alert alert-error">
        <strong>Error:</strong> {error}
      </div>
    )
  }

  if (result) {
    const isHighRisk = result.churn_prediction === 1
    const percentage = (result.churn_probability * 100).toFixed(1)

    return (
      <div className="card result-card">
        <h2>Prediction Result</h2>

        <div className="result-header">
          <div className={`risk-badge ${isHighRisk ? 'high-risk' : 'low-risk'}`}>
            {result.risk_label || (isHighRisk ? 'High Churn Risk' : 'Low Churn Risk')}
          </div>
          <div className="probability-value">{percentage}%</div>
        </div>

        <div className="probability-bar-container">
          <div
            className={`probability-bar ${isHighRisk ? 'bar-high' : 'bar-low'}`}
            style={{ width: `${percentage}%` }}
          ></div>
        </div>

        <div className="result-details">
          <p>
            <strong>Predicted Action:</strong>{' '}
            {isHighRisk ? 'Customer is likely to churn (leave).' : 'Customer is likely to stay.'}
          </p>
          <p>
            <strong>Probability Score:</strong> {(result.churn_probability * 100).toFixed(2)}% chance of churn.
          </p>
        </div>
      </div>
    )
  }

  if (!loading) {
    return (
      <div className="card placeholder-card">
        <p>💡 Fill in the form and click <strong>Predict Churn</strong> to see results here.</p>
      </div>
    )
  }

  return null
}
