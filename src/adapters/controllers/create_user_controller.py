from pydantic import ValidationError

from src.adapters.errors.http_exception import HttpException
from src.domain.entities.user import User
from src.domain.errors.errors import UnexpectedError, NoItemsFound, EntityError
from src.domain.repositories.user_repository_interface import IUserRepository
from src.domain.usecases.create_user_usecase import CreateUserUsecase
from src.adapters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok, NoContent


class CreateUserController:
    def __init__(self, userRepository: IUserRepository) -> None:
        self._createUserUsecase = CreateUserUsecase(userRepository)

    async def __call__(self, req: HttpRequest) -> HttpResponse:

        if req.query is not None:
            return BadRequest('No parameters allowed.')
        if req.body is None:
            return BadRequest('Missing body.')

        try:
            user = User.parse_obj(req.body)
            await self._createUserUsecase(user)
            response = {f"User {user.name} created."}
            return Ok(response)

        except EntityError as e:
            return BadRequest(e.message)

        except ValidationError:
            return BadRequest("Invalid parameters.")

        except (UnexpectedError, Exception) as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)