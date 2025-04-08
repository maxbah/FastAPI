from fastapi import APIRouter, Depends

from app.redis_tools.tools import RedisTool

router = APIRouter(prefix='/concur', tags=['Криптопары'])


@router.get("/{pair}")
def get_pair_currency(pair: str):
    if pair not in [s for s in RedisTool.get_keys()]:
        return {
            'error': "This pair does not exist"
        }
    return {
        'pair': pair,
        'price': RedisTool.get_pair(pair)
    }
