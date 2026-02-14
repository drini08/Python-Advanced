from typing import Optional, Any, List, Union

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())


def get_value(value: Union[str, int]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(get_value(74))

def get_vlera(vlera: Any) -> str:
    return vlera

print(get_vlera("nigka"))

def get_lista(lista: List[int]) -> int:
    return sum(lista)

print (get_lista([1, 3, 5]))