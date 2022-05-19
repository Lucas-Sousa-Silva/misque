from fastapi import Request
async def get_pool(request: Request):
    return getattr(request.app.state, "pool")
