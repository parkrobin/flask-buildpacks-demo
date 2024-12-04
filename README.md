# Flask Buildpacks Demo

This is s simple Flask application demonstrating how to use Cloud Native Buildpacks.

## Running with Buildpacks
1. Install pack CLI
```
https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/
```
2. Build the application
```
pack build flask-buildpacks-demo --builder paketobuildpacks/builder-jammy-base
```
3. Run the image
```
docker run -p 5001:5001 flask-buildpacks-demo
```

## Endpoints
- `http://localhost:5001/`: Return a hello world message
- `http://localhost:5001/env`: Shows environment variables