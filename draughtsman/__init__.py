from typing import Optional

from refract.json import JSONDeserialiser
from refract.contrib.apielements import registry, ParseResult
from refract.registry import Registry
from draughtsman.drafter import drafter_parse_blueprint_to


__all__ = ('parse',)


def parse(
    blueprint: str,
    generate_source_map: bool = False,
    deserialiser_cls: JSONDeserialiser = JSONDeserialiser,
    custom_registry: Optional[Registry] = None
) -> ParseResult:
    result = drafter_parse_blueprint_to(
        blueprint,
        generate_source_map=generate_source_map
    )

    deserialiser = deserialiser_cls(registry=custom_registry or registry)
    return deserialiser.deserialise(result)
