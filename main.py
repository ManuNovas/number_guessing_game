from src.application.use_cases import NGGUseCases
from src.adapters.input import NGGInputAdapter

use_cases = NGGUseCases()
adapter = NGGInputAdapter(use_cases)

adapter.main()
