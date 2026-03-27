from src.adapters.output import NGGOutputAdapter
from src.application.use_cases import NGGUseCases
from src.adapters.input import NGGInputAdapter

output_adapter = NGGOutputAdapter("score.json")
use_cases = NGGUseCases(output_adapter)
input_adapter = NGGInputAdapter(use_cases)

input_adapter.main()
