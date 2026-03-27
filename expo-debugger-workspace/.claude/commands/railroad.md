# /railroad — Railway Backend Debugging

Specialized debugging for Railway-hosted backend issues: deployment failures, API errors, database problems, and environment configuration.

## Instructions

Ask the user:
1. What's going wrong? (deploy failure, API error, database issue, performance)
2. When did it start? (after a deploy, code change, or spontaneously)
3. Can you share the Railway logs? (from the Railway dashboard → Deployments → View Logs)

## Debugging Flows

### Deploy Failure

1. Ask for the build/deploy log output
2. Read from the BOTTOM UP — the actual error is at the end
3. Common causes:
   - Missing `start` script in package.json → add `"start": "node dist/index.js"` or equivalent
   - TypeScript compilation error → fix the type error shown in logs
   - Missing environment variable → check Railway dashboard env vars
   - Port binding → ensure the server reads `process.env.PORT`, not a hardcoded port
   - Memory exceeded → check if build step is too memory-intensive
4. Provide the exact fix and how to redeploy

### API Not Responding

1. Check if the Railway service is running (green status in dashboard)
2. Verify the URL being called:
   - Should be `https://[project].up.railway.app/[endpoint]`
   - NOT `localhost:3000`
   - NOT `http://` (must be https)
3. Test independently: `curl https://[project].up.railway.app/health`
4. If the server starts but crashes:
   - Check for unhandled promise rejections
   - Check database connection on startup
   - Check for missing env vars that cause runtime errors

### CORS Issues

1. Is the backend CORS configuration including the Expo app's origin?
2. For development with Expo Go, allow all origins or specific Expo URLs
3. For production, whitelist the specific bundle identifier
4. Example Express CORS fix:
```javascript
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || '*',
  credentials: true
}));
```

### Database Issues

1. Verify DATABASE_URL is set in Railway environment
2. Check SSL: Railway PostgreSQL requires `?sslmode=require`
3. Run migrations: has the schema been applied?
4. Connection pooling: too many connections can exhaust the pool
5. Ask to see the database connection code and ORM configuration

### Environment Variable Problems

1. List all expected env vars (names only) from the codebase
2. Cross-reference with Railway dashboard
3. Common gotchas:
   - Variable set in Railway but code reads a different name
   - Variable has trailing whitespace or quotes
   - Variable only set in one environment (dev vs production)

## Output

Provide the fix with:
1. What to change in the code
2. What to change in Railway dashboard (if any)
3. How to redeploy: `railway up` or push to trigger GitHub auto-deploy
4. How to verify: check logs, curl the endpoint, test from the app

Log to `work-log/`.
