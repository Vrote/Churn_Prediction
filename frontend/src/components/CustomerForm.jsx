export default function CustomerForm({ formData, onChange, onSubmit, onReset, loading }) {
  return (
    <form onSubmit={onSubmit} className="card form-card">
      <h2>Customer Details</h2>

      {/* Model Selection Section */}
      <div className="model-selector-container">
        <label className="model-selector-label">Select Machine Learning Model</label>
        <div className="model-options">
          <label className={`model-option-btn ${formData.model_type === 'xgboost' ? 'active' : ''}`}>
            <input
              type="radio"
              name="model_type"
              value="xgboost"
              checked={formData.model_type === 'xgboost'}
              onChange={onChange}
            />
            <span className="model-icon"></span>
            <div className="model-text">
              <span className="model-title">XGBoost Classifier</span>
              <span className="model-subtitle">High Accuracy Boosting</span>
            </div>
          </label>

          <label className={`model-option-btn ${formData.model_type === 'logistic_regression' ? 'active' : ''}`}>
            <input
              type="radio"
              name="model_type"
              value="logistic_regression"
              checked={formData.model_type === 'logistic_regression'}
              onChange={onChange}
            />
            <span className="model-icon"></span>
            <div className="model-text">
              <span className="model-title">Logistic Regression</span>
              <span className="model-subtitle">Probabilistic Classifier</span>
            </div>
          </label>
        </div>
      </div>

      <div className="form-grid">
        <div className="form-group">
          <label htmlFor="gender">Gender</label>
          <select
            id="gender"
            name="gender"
            value={formData.gender}
            onChange={onChange}
            required
          >
            <option value="Female">Female</option>
            <option value="Male">Male</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="country">Country</label>
          <select
            id="country"
            name="country"
            value={formData.country}
            onChange={onChange}
            required
          >
            <option value="France">France</option>
            <option value="Germany">Germany</option>
            <option value="Spain">Spain</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="age">Age (18 - 100)</label>
          <input
            type="number"
            id="age"
            name="age"
            min="18"
            max="100"
            value={formData.age}
            onChange={onChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="tenure">Tenure (Years: 0 - 10)</label>
          <input
            type="number"
            id="tenure"
            name="tenure"
            min="0"
            max="10"
            value={formData.tenure}
            onChange={onChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="balance">Account Balance ($)</label>
          <input
            type="number"
            id="balance"
            name="balance"
            min="0"
            step="100"
            value={formData.balance}
            onChange={onChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="products_number">Number of Products</label>
          <select
            id="products_number"
            name="products_number"
            value={formData.products_number}
            onChange={onChange}
            required
          >
            <option value={1}>1 Product</option>
            <option value={2}>2 Products</option>
            <option value={3}>3 Products</option>
            <option value={4}>4 Products</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="active_member">Active Membership Status</label>
          <select
            id="active_member"
            name="active_member"
            value={formData.active_member}
            onChange={onChange}
            required
          >
            <option value={1}>Active Member</option>
            <option value={0}>Inactive Member</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="estimated_salary">Estimated Salary ($)</label>
          <input
            type="number"
            id="estimated_salary"
            name="estimated_salary"
            min="0"
            step="500"
            value={formData.estimated_salary}
            onChange={onChange}
            required
          />
        </div>
      </div>

      <div className="button-group">
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? 'Predicting...' : 'Predict Churn'}
        </button>
        <button type="button" className="btn btn-secondary" onClick={onReset}>
          Reset Values
        </button>
      </div>
    </form>
  )
}
