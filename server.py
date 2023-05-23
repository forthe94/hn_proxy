from fastapi import FastAPI, Request, Response
import httpx
import config
import uvicorn

from html_parser import process_hn_page

app = FastAPI()


@app.api_route(
    "/{full_path:path}",
    methods=["GET", "POST", "DELETE", "PATCH", "PUT", "OPTIONS", "HEAD", "TRACE"],
)
async def hacker_news_proxy(
    request: Request, full_path: str, response: Response
) -> Response:
    async with httpx.AsyncClient() as client:
        proxy = await client.request(
            request.method,
            f"{config.HACKERNEWS_URL}/{full_path}",
            params=request.query_params,
        )
        response.body = process_hn_page(proxy.content)
        response.status_code = proxy.status_code
        response.headers['content-type'] = proxy.headers['content-type']
        return response


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
