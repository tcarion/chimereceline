from dataclasses import dataclass
from typing import Any, Dict, List

from chimereceline.utils import read_phenomena


@dataclass(frozen=True)
class Phenomenon:
    id: int
    label: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Phenomenon":
        return cls(id=int(data["id"]), label=data["label"])


def generate_phenomena() -> List[Phenomenon]:
    return [Phenomenon.from_dict(pheno) for pheno in read_phenomena()]
