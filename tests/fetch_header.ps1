param ([string]$url = 'localhost')

if (-not $url) {
    Write-Host 'Provide a url' exit 1
}
if (-not (Get-Command curl -ErrorAction SilentlyContinue)) {
    Write-Host 'curl is NOT installed OR u must try out with `Invoke-WebRequest -Uri "https://example.com" -Method HEAD`'   exit 1
}

curl -I $url