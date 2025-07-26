# 🚀 Railway Deployment Guide

Deploy your Dog Identifier app to Railway for instant cloud hosting.

## 🏗️ What's Included

- **Mobile-friendly web frontend** (`frontend/index.html`)
- **Cloud-ready FastAPI backend** with health checks
- **Railway configuration** (`railway.toml`) for seamless deployment

## ⚡ Deploy to Railway

Railway automatically detects Python projects and handles everything for you.

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and deploy:**
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Your app will be live!** Railway provides a URL like: `https://your-app.railway.app`

## 🔧 Configuration

### Update Frontend URL
After deployment, update the API URL in `frontend/index.html`:

```javascript
const API_BASE_URL = 'https://your-app-name.railway.app';
```

Replace `your-app-name` with your actual Railway app URL.

### No Environment Variables Needed
The app uses the local CLIP model, so no external API keys are required.

## 📱 Using Your App

1. **Access your app** at your Railway URL
2. **Take/upload photos** to identify dogs  
3. **Add new dogs** to expand the database
4. **Works on any mobile device** - fully responsive!

## 🛠️ Local Development

```bash
# Run backend locally
./run.sh

# Test frontend locally  
python -m http.server 8080 -d frontend
# Visit: http://localhost:8080
```

## 📊 Monitoring

- **Health check:** `/health` endpoint
- **Railway dashboard:** Monitor logs and performance
- **Automatic restarts:** Configured in `railway.toml`

## 🔄 Updates

Railway automatically redeploys when you push to GitHub:

```bash
git add .
git commit -m "Update app"  
git push
```

Your changes will be live in minutes!