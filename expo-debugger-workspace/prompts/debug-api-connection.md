# Prompt Template: Debug API Connection

Use this when your app can't connect to or get correct responses from your Railway backend.

---

## Prompt

```
My Expo app isn't communicating correctly with my Railway backend.

**Problem:**
[describe what's failing — e.g., login returns 500, data doesn't load, request times out]

**API URL being called:**
[the full URL, e.g., https://myapp.up.railway.app/api/users]

**Request code (frontend):**
[paste the fetch/axios call]

**Endpoint code (backend):**
[paste the route handler]

**What I see:**
- HTTP status code: [e.g., 500, 403, timeout]
- Response body: [paste if available]
- Railway logs: [paste relevant log lines]

**Environment:**
- Railway service status: [running / deploying / crashed]
- Testing from: [Expo Go / Simulator / Physical device]
- Network: [WiFi / cellular / localhost]

Please:
1. Determine if the issue is frontend, backend, or network
2. Identify the root cause
3. Provide fixes for both frontend and backend code if needed
4. Include the curl command I can use to test the endpoint independently
5. Tell me how to verify the connection is working end-to-end
```
