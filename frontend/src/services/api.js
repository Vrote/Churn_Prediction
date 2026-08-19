const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:8000'

/**
 * Sends customer data to the FastAPI backend and gets the prediction result.
 */
export async function predictChurn(formData) {
  const response = await fetch(`${API_BASE_URL}/predict`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      gender: formData.gender,
      country: formData.country,
      age: Number(formData.age),
      tenure: Number(formData.tenure),
      balance: Number(formData.balance),
      products_number: Number(formData.products_number),
      active_member: Number(formData.active_member),
      estimated_salary: Number(formData.estimated_salary),
    }),
  })

  if (!response.ok) {
    throw new Error(`Server Error (${response.status}): Could not get prediction`)
  }

  return await response.json()
}
