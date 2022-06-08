from src.adapters.errors.http_exception import HttpException
from src.adapters.helpers.http_models import HttpRequest, HttpResponse, BadRequest, Ok, NoContent, InternalServerError
from src.adapters.viewmodels.get_user_model import GetUserModel
from src.domain.entities.user import User
from src.domain.errors.errors import UnexpectedError, NoItemsFound, NonExistentUser
from src.domain.usecases.get_user_by_id_usecase import GetUserByIdUsecase
from src.domain.repositories.user_repository_interface import IUserRepository


class GetUserByIdController:

    def __init__(self, userRepository: IUserRepository) -> None:
        self._getAllUserByIdUseCase = GetUserByIdUsecase(userRepository)

    async def __call__(self, req: HttpRequest) -> HttpResponse:

        if req.query is None:
            return BadRequest('Missing parameter.')

        try:
            if  type(req.query['id']) != int:
                return BadRequest('Invalid parameter. (id value should be Int) ')

            user = await self._getAllUserByIdUseCase(int(req.query['id']))
            response = GetUserModel.parse_obj(user)

            if user is None:
                raise NonExistentUser('')
            return Ok(response)

        except (NoItemsFound, NonExistentUser):
            return NoContent()

        except (UnexpectedError) as e:
            err = InternalServerError(e.message)
            return err

        except Exception as e:
            err = InternalServerError(e.args[0])
            return err



