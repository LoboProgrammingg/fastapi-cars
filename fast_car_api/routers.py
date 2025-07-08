from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/cars', tags=['cars'])


@router.get('/')
def list_cars():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Marea 20v'},
            {'id': 2, 'modelo': 'Opala'},
            {'id': 3, 'modelo': 'Corsa Wind'},
        ]
    }
