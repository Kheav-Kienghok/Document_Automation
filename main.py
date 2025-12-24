from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any

from sheerid_verifier import SheerIDVerifier

app = FastAPI(
    title="SheerID 教师验证 API",
    description="FastAPI wrapper for SheerID 教师身份验证流程",
    version="1.0.0",
)


class VerifyRequest(BaseModel):
    install_page_url: HttpUrl
    verification_id: Optional[str] = None

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    birth_date: Optional[str] = None
    school_id: Optional[str] = None


class VerifyResponse(BaseModel):
    success: bool
    message: str
    verification_id: Optional[str] = None
    pending: Optional[bool] = None
    redirect_url: Optional[str] = None
    reward_code: Optional[str] = None
    status: Optional[Dict[str, Any]] = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/verify", response_model=VerifyResponse)
def verify_teacher(payload: VerifyRequest):
    """
    执行 SheerID 教师身份验证
    """
    try:
        verifier = SheerIDVerifier(
            install_page_url=str(payload.install_page_url),
            verification_id=payload.verification_id,
        )

        result = verifier.verify(
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            birth_date=payload.birth_date,
            school_id=payload.school_id,
        )

        if not result.get("success"):
            raise HTTPException(status_code=400, detail=result)

        return result

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

