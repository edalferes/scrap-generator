# src/scrap_generator/routes/metrics.py

from fastapi import APIRouter, Response, Request

router = APIRouter()


@router.get("/metrics")
def metrics_route(request: Request):
    generator = request.app.state.generator
    data = generator.get_metrics()
    return Response(content=data, media_type="text/plain")
