# Flask Buildpacks Demo

This is s simple Flask application demonstrating how to use Cloud Native Buildpacks.

## Running with Buildpacks
1. Install pack CLI
2. Build the application
```
pack build flask-buildpacks-demo --builder paketobuildpacks/builder-jammy-base
```
3. Run the image
```
docker run -p 5001:5001 flask-buildpacks-demo
```

## Endpoints
- `/`: Return a hello world message
- `/env`: Shows environment variables