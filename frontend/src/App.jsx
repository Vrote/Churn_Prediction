import { useState } from 'react'
import Header from './components/Header'
import CustomerForm from './components/CustomerForm'
import PredictionResult from './components/PredictionResult'
import { predictChurn } from './services/api'
import { DEFAULT_FORM } from './constants/defaults'

export default function App() {
  // 1. State management
  const [formData, setFormData] = useState(DEFAULT_FORM) // Stores input form values
  const [loading, setLoading] = useState(false)            // Shows loading state while calling backend API
  const [result, setResult] = useState(null)               // Stores prediction response from backend
  const [error, setError] = useState(null)                 // Stores error message if API fails

  // 2. Handle input changes dynamically
  const handleChange = (e) => {
    const { name, value, type } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: type === 'number' ? Number(value) : value
    }))
  }

  // 3. Handle form submission (API Call)
  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const data = await predictChurn(formData)
      setResult(data)
    } catch (err) {
      setError('Backend server disconnected. Please start FastAPI on http://localhost:8000')
    } finally {
      setLoading(false)
    }
  }

  // 4. Reset form back to default values
  const handleReset = () => {
    setFormData(DEFAULT_FORM)
    setResult(null)
    setError(null)
  }

  return (
    <div className="container">
      <Header />
      <main className="main-content">
        {/* Input Form Section */}
        <CustomerForm
          formData={formData}
          onChange={handleChange}
          onSubmit={handleSubmit}
          onReset={handleReset}
          loading={loading}
        />
        {/* Prediction Results Section */}
        <section className="results-section">
          <PredictionResult
            result={result}
            error={error}
            loading={loading}
          />
        </section>
      </main>
    </div>
  )
}
