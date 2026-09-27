async function request(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json();
}

export const api = {
  health: () => request("/health"),
  signup: (body) => request("/api/auth/signup", { method: "POST", body: JSON.stringify(body) }),
  login: (body) => request("/api/auth/login", { method: "POST", body: JSON.stringify(body) }),
  resetPassword: (body) =>
    request("/api/auth/reset-password", { method: "POST", body: JSON.stringify(body) }),
  wells: () => request("/api/wells"),
  startAnalysis: (wellId) => request(`/api/analysis/${wellId}/start`, { method: "POST" }),
  fractures: (wellId) => request(`/api/fractures/${wellId}`),
  facies: (wellId) => request(`/api/facies/${wellId}`),
  logs: (wellId) => request(`/api/logs/${wellId}`),
  reports: () => request("/api/reports"),
  chat: (body) => request("/api/agent/chat", { method: "POST", body: JSON.stringify(body) }),
};
