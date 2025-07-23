# 🚀 Deployment Guide

This guide shows how to deploy your Dog Identifier app to the cloud with multiple hosting options.

## 🏗️ What's Included

- **Mobile-friendly web frontend** (`frontend/index.html`)
- **Cloud-ready FastAPI backend** with health checks
- **Multiple deployment configs** (Railway, Heroku, Docker)

## ⚡ Quick Deploy Options

### Option 1: Railway (Recommended)
Railway is the easiest way to deploy Python apps.

1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login and deploy:
   ```bash
   railway login
   railway init
   railway up
   ```

3. Your app will be available at: `https://your-app.railway.app`

### Option 2: Heroku
1. Install Heroku CLI and login
2. Create and deploy:
   ```bash
   heroku create your-dog-identifier
   heroku stack:set container
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### Option 3: Any Docker Platform
Use the provided `Dockerfile` with any platform that supports Docker (Render, Fly.io, etc.)

## 🔧 Configuration

### Update Frontend URL
After deployment, update the API URL in `frontend/index.html`:

```javascript
const API_BASE_URL = 'https://your-deployed-backend-url.com';
```

### Environment Variables
No environment variables required - the app uses the local CLIP model.

## 📱 Using Your App

1. **Access your app** at your deployed URL
2. **Take/upload photos** to identify dogs
3. **Add new dogs** to expand the database
4. **Share the URL** - it works on any mobile device!

## 🛠️ Local Development

```bash
# Backend only
./run.sh

# Test frontend locally
python -m http.server 8080 -d frontend
# Then visit: http://localhost:8080
```

## 📊 Monitoring

- Health check endpoint: `/health`
- Check deployment logs via your platform's dashboard
- Monitor response times and errors

## 🔄 Updates

To update your deployed app:
```bash
git add .
git commit -m "Update app"
git push
```

Your platform will automatically redeploy!