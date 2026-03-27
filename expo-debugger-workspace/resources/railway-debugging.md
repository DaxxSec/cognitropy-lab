# Railway Backend Debugging Reference

Quick reference for diagnosing and fixing Railway-specific issues.

---

## Railway Architecture Basics

- Railway assigns a random PORT via `process.env.PORT` — never hardcode a port
- Public URL format: `https://[service-name].up.railway.app`
- Railway uses Nixpacks for auto-detection of build/start commands
- Services auto-restart on crash, but check logs for restart loops
- Free tier limits: 500 hours/month, 512 MB RAM, limited egress

## Common Railway Issues

### Service Won't Start

**Check in this order:**
1. Does `package.json` have a valid `start` script?
2. Does the app bind to `process.env.PORT`? (not 3000, not 8080)
3. Does the app start successfully locally?
4. Are all required environment variables set in Railway?
5. Is the build step succeeding? (check build logs separately from runtime logs)

### Deployment Fails

**Common causes:**
- TypeScript errors not caught locally (Railway runs `tsc` as part of build)
- Missing `build` script in package.json
- Node version mismatch (set `engines.node` in package.json)
- Memory exceeded during build (optimize build, or upgrade plan)

### Database Connection

**PostgreSQL on Railway:**
```
DATABASE_URL=postgresql://user:pass@host:port/dbname?sslmode=require
```
- Always use `?sslmode=require` — Railway enforces SSL
- Connection pooling: use PgBouncer or limit pool size in your ORM
- Internal URL (for services in same project): use `DATABASE_PRIVATE_URL`
- External URL (for local dev): use `DATABASE_URL`

### Environment Variables

**Best practices:**
- Set in Railway dashboard, not in code
- Use separate variables for dev vs production
- Common vars needed: `DATABASE_URL`, `PORT`, `NODE_ENV`, `JWT_SECRET`, `CORS_ORIGINS`
- Railway auto-provides `PORT` — don't set it manually
- Check for typos: Railway doesn't warn about unused variables

### Logs & Monitoring

**How to read Railway logs:**
- Dashboard → Service → Deployments → Latest → View Logs
- Filter by: Build logs (compilation) vs Deploy logs (runtime)
- Look for: startup errors, unhandled rejections, connection failures
- Logs rotate — if you need history, add an external logging service

### CORS Configuration

**For Express backend:**
```javascript
const cors = require('cors');
app.use(cors({
  origin: process.env.CORS_ORIGINS?.split(',') || ['http://localhost:19006'],
  credentials: true
}));
```
Set `CORS_ORIGINS` in Railway to include your Expo app's origin.

### Health Check Endpoint

**Always have one:**
```javascript
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});
```
Use this to verify your service is reachable before debugging app-side issues.

## Railway CLI Quick Reference

```bash
# Install
npm install -g @railway/cli

# Login
railway login

# Link to project
railway link

# Deploy
railway up

# View logs
railway logs

# Open dashboard
railway open

# Run local with Railway env vars
railway run npm start

# List environment variables
railway variables
```
