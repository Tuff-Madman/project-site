# GitHub Repository Creation Helper
# Run this after creating the repository on GitHub

Write-Host "📋 GitHub Repository Setup Helper" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📌 Step 1: Create Repository on GitHub" -ForegroundColor Yellow
Write-Host "   1. Open: https://github.com/new" -ForegroundColor White
Write-Host "   2. Repository name: project-site" -ForegroundColor Green
Write-Host "   3. Keep it PUBLIC (required for GitHub Pages)" -ForegroundColor Red
Write-Host "   4. DO NOT initialize with README" -ForegroundColor Red
Write-Host ""
Write-Host "Press Enter when repository is created..." -ForegroundColor Yellow
Read-Host

Write-Host ""
Write-Host "📌 Step 2: Push your code" -ForegroundColor Yellow
Write-Host "Running git commands..." -ForegroundColor White

# Set remote and push
git remote set-url origin https://github.com/Tuff-Madman/project-site.git
git push -u origin main

Write-Host ""
Write-Host "✅ Code pushed to GitHub!" -ForegroundColor Green
Write-Host ""
Write-Host "📌 Step 3: Enable GitHub Pages" -ForegroundColor Yellow
Write-Host "   1. Go to: https://github.com/Tuff-Madman/project-site/settings/pages" -ForegroundColor White
Write-Host "   2. Source: Deploy from a branch" -ForegroundColor White
Write-Host "   3. Branch: main, Folder: / (root)" -ForegroundColor White
Write-Host "   4. Click Save" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Your site will be available at:" -ForegroundColor Cyan
Write-Host "   https://Tuff-Madman.github.io/project-site/" -ForegroundColor Green
Write-Host ""
Write-Host "⏳ Note: First deployment takes 5-10 minutes" -ForegroundColor Yellow 