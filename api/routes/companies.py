from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from common.database import get_session
from common.models import Company, CompanyCreate
from sqlalchemy import select

router = APIRouter(prefix="/companies")

@router.get('/')
async def get_companies(session: AsyncSession = Depends(get_session)):
    statement = select(Company)
    results = await session.execute(statement)
    return results.scalars().all()

@router.post('/', response_model=Company)
async def post_company(company_create: CompanyCreate, session: AsyncSession = Depends(get_session)):
    company = Company(**company_create.model_dump())
    session.add(company)
    await session.commit()
    await session.refresh(company)
    return company